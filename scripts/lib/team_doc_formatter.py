"""Apply WM team document visual format (Google Docs API)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any

from .team_doc_translator import Block

FORMAT_REFERENCE_DOC_ID = "19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y"
FORMAT_REFERENCE_URL = (
    "https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit"
)

CALLOUT_LABELS = {
    "north_star": "📌 NORTH STAR",
    "important": "⚠️ IMPORTANT",
    "tip": "💡 PRO TIP",
    "critical": "🚨 CRITICAL MISTAKE TO AVOID",
    "watch": "⚠️ WATCH FOR THIS",
    "rule": "📌 RULE",
    "remember": "📌 REMEMBER",
}

ROLE_SUBTITLE = {
    "Setter": "Sales & Setting",
    "Closer": "Sales & Setting",
    "Client Success": "Client Success",
    "Operations": "Operations",
    "Everyone on the team": "Company",
    "Sales leadership": "Sales & Setting",
}


@dataclass
class TableSpec:
    headers: list[str]
    rows: list[list[str]]


@dataclass
class FormattedDoc:
    title: str
    owner_line: str
    blocks: list[Block] = field(default_factory=list)
    quick_reference: TableSpec | None = None


def team_subtitle(owner: str) -> str:
    role = ROLE_SUBTITLE.get(owner, owner)
    return f"{role} Team  |  Internal Use Only  |  {date.today().year}"


def blocks_to_formatted_doc(
    blocks: list[Block],
    *,
    title: str,
    owner: str,
) -> FormattedDoc:
    fd = FormattedDoc(title=title, owner_line=team_subtitle(owner))
    i = 0
    overview_started = False

    while i < len(blocks):
        b = blocks[i]
        i += 1

        if b.kind == "heading1":
            continue

        if b.kind == "heading2" and b.text == "At a glance":
            bullets = []
            while i < len(blocks) and blocks[i].kind == "bullet":
                bullets.append(blocks[i].text)
                i += 1
            if bullets:
                fd.blocks.append(
                    Block(
                        "callout",
                        " ".join(bullets[:4]),
                        callout_type="north_star",
                    )
                )
            continue

        if b.kind == "heading2":
            h = b.text
            if h == "What this is for":
                if not overview_started:
                    fd.blocks.append(Block("h1", "Overview"))
                    overview_started = True
                continue  # body paragraphs follow as normal blocks
            if h == "Before you start":
                fd.blocks.append(Block("label", "Before You Start"))
                continue
            if h == "How to do it":
                fd.blocks.append(Block("h1", "How To Do It"))
                continue
            if h == "Done right looks like":
                fd.blocks.append(Block("h2", "Done Right Looks Like"))
                continue
            if h == "When to get help":
                fd.blocks.append(Block("h2", "When To Get Help"))
                continue
            if h == "Related procedures":
                fd.blocks.append(Block("h2", "Related Procedures"))
                continue
            fd.blocks.append(Block("h2", h))
            continue

        if b.kind == "heading3":
            label = b.text.split(" — ", 1)[-1] if " — " in b.text else b.text
            fd.blocks.append(Block("h2", label))
            continue

        if b.kind == "callout":
            ctype = b.callout_type or _infer_callout(b.text)
            fd.blocks.append(Block("callout", b.text, callout_type=ctype))
            continue

        if not overview_started and b.kind == "paragraph" and b.text:
            fd.blocks.append(Block("h1", "Overview"))
            overview_started = True

        fd.blocks.append(b)

    fd.blocks.append(
        Block(
            "callout",
            "If this doc conflicts with what you heard elsewhere, follow this doc and tell Gabriel.",
            callout_type="remember",
        )
    )
    return fd


def _infer_callout(text: str) -> str:
    low = text.lower()
    if "tip:" in low:
        return "tip"
    if "critical" in low:
        return "critical"
    if "watch" in low:
        return "watch"
    return "important"


def write_formatted_doc(docs, doc_id: str, fd: FormattedDoc) -> None:
    from .google_publish import clear_document_body

    clear_document_body(docs, doc_id)
    writer = _DocWriter(docs, doc_id)
    writer.append_line("WAIZ MEDIA\n", bold=True, size=26, align="CENTER")
    writer.append_line(f"{fd.title}\n", size=20, align="CENTER")
    writer.append_line(f"{fd.owner_line}\n\n", size=11, align="CENTER")

    for block in fd.blocks:
        if block.kind == "h1":
            writer.append_heading(block.text, "HEADING_1")
        elif block.kind == "h2":
            writer.append_heading(block.text, "HEADING_2")
        elif block.kind == "label":
            writer.append_label(block.text)
        elif block.kind == "callout":
            label = CALLOUT_LABELS.get(block.callout_type or "important", "⚠️ IMPORTANT")
            writer.append_callout_table(label, block.text)
        elif block.kind == "bullet":
            writer.append_bullet(block.text, link=block.link_url)
        elif block.kind == "numbered":
            writer.append_bullet(block.text)
        elif block.kind == "paragraph":
            if block.link_url:
                writer.append_linked_line(block.text + "\n", block.link_url)
            else:
                writer.append_body(block.text + "\n")

    if fd.quick_reference:
        writer.append_heading("Quick Reference — At a Glance", "HEADING_2")
        writer.append_data_table(fd.quick_reference.headers, fd.quick_reference.rows)

    writer.append_line("\nWaiz Media  |  Internal Document  |  Confidential\n", size=11, align="CENTER")
    writer.flush()


class _DocWriter:
    def __init__(self, docs, doc_id: str):
        self.docs = docs
        self.doc_id = doc_id
        self.pending: list[dict[str, Any]] = []
        self.index = 1

    def _refresh_index(self) -> None:
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        self.index = doc["body"]["content"][-1]["endIndex"] - 1

    def flush(self) -> None:
        if not self.pending:
            return
        self.docs.documents().batchUpdate(
            documentId=self.doc_id, body={"requests": self.pending}
        ).execute()
        self.pending = []
        self._refresh_index()

    def append_line(
        self,
        text: str,
        *,
        bold: bool = False,
        size: int | None = None,
        align: str | None = None,
        named_style: str | None = None,
    ) -> None:
        start = self.index
        self.pending.append({"insertText": {"location": {"index": self.index}, "text": text}})
        end = start + len(text)
        self.index = end
        pfields = []
        pstyle: dict[str, Any] = {}
        if named_style:
            pstyle["namedStyleType"] = named_style
            pfields.append("namedStyleType")
        if align:
            pstyle["alignment"] = align
            pfields.append("alignment")
        if pfields:
            self.pending.append(
                {
                    "updateParagraphStyle": {
                        "range": {"startIndex": start, "endIndex": end},
                        "paragraphStyle": pstyle,
                        "fields": ",".join(pfields),
                    }
                }
            )
        if bold or size:
            ts: dict[str, Any] = {}
            tf = []
            if bold:
                ts["bold"] = True
                tf.append("bold")
            if size:
                ts["fontSize"] = {"magnitude": size, "unit": "PT"}
                tf.append("fontSize")
            self.pending.append(
                {
                    "updateTextStyle": {
                        "range": {"startIndex": start, "endIndex": max(start + 1, end - 1)},
                        "textStyle": ts,
                        "fields": ",".join(tf),
                    }
                }
            )

    def append_heading(self, text: str, style: str) -> None:
        self.append_line(f"{text}\n", named_style=style)
        self.flush()

    def append_label(self, text: str) -> None:
        self.append_line(f"{text}\n", bold=True, size=11)
        self.flush()

    def append_body(self, text: str) -> None:
        self.append_line(text, size=11)

    def append_bullet(self, text: str, link: str | None = None) -> None:
        self.flush()
        start = self.index
        line = f"• {text}\n"
        self.docs.documents().batchUpdate(
            documentId=self.doc_id,
            body={"requests": [{"insertText": {"location": {"index": start}, "text": line}}]},
        ).execute()
        end = start + len(line)
        reqs = [
            {
                "updateTextStyle": {
                    "range": {"startIndex": start + 2, "endIndex": end - 1},
                    "textStyle": {"fontSize": {"magnitude": 11, "unit": "PT"}},
                    "fields": "fontSize",
                }
            }
        ]
        if link:
            reqs.append(
                {
                    "updateTextStyle": {
                        "range": {"startIndex": start + 2, "endIndex": start + 2 + len(text)},
                        "textStyle": {"link": {"url": link}},
                        "fields": "link",
                    }
                }
            )
        self.docs.documents().batchUpdate(documentId=self.doc_id, body={"requests": reqs}).execute()
        self._refresh_index()

    def append_linked_line(self, text: str, url: str) -> None:
        start = self.index
        self.append_line(text, size=11)
        self.flush()
        self.docs.documents().batchUpdate(
            documentId=self.doc_id,
            body={
                "requests": [
                    {
                        "updateTextStyle": {
                            "range": {"startIndex": start, "endIndex": start + len(text) - 1},
                            "textStyle": {"link": {"url": url}},
                            "fields": "link",
                        }
                    }
                ]
            },
        ).execute()
        self._refresh_index()

    def append_callout_table(self, label: str, message: str) -> None:
        self.flush()
        idx = self.index
        self.docs.documents().batchUpdate(
            documentId=self.doc_id,
            body={"requests": [{"insertTable": {"rows": 1, "columns": 2, "location": {"index": idx}}}]},
        ).execute()
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        cells = _table_cell_starts(doc, -1)
        if len(cells) < 2:
            self._refresh_index()
            return
        reqs = [
            {"insertText": {"location": {"index": cells[0]}, "text": label}},
            {"insertText": {"location": {"index": cells[1]}, "text": message}},
        ]
        self.docs.documents().batchUpdate(documentId=self.doc_id, body={"requests": reqs}).execute()
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        cells = _table_cell_starts(doc, -1)
        style_reqs = []
        if cells:
            style_reqs.append(
                {
                    "updateTextStyle": {
                        "range": {"startIndex": cells[0], "endIndex": cells[0] + len(label)},
                        "textStyle": {"bold": True, "fontSize": {"magnitude": 11, "unit": "PT"}},
                        "fields": "bold,fontSize",
                    }
                }
            )
        if len(cells) > 1:
            style_reqs.append(
                {
                    "updateTextStyle": {
                        "range": {"startIndex": cells[1], "endIndex": cells[1] + len(message)},
                        "textStyle": {"fontSize": {"magnitude": 11, "unit": "PT"}},
                        "fields": "fontSize",
                    }
                }
            )
        if style_reqs:
            self.docs.documents().batchUpdate(documentId=self.doc_id, body={"requests": style_reqs}).execute()
        self._refresh_index()
        self.append_line("\n")

    def append_data_table(self, headers: list[str], rows: list[list[str]]) -> None:
        self.flush()
        idx = self.index
        nrows = 1 + len(rows)
        ncols = len(headers)
        self.docs.documents().batchUpdate(
            documentId=self.doc_id,
            body={"requests": [{"insertTable": {"rows": nrows, "columns": ncols, "location": {"index": idx}}}]},
        ).execute()
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        cells = _table_cell_starts(doc, -1)
        data = [headers] + rows
        flat = [c for row in data for c in row]
        reqs = []
        for cell_start, text in zip(cells, flat):
            reqs.append({"insertText": {"location": {"index": cell_start}, "text": text}})
        if reqs:
            self.docs.documents().batchUpdate(documentId=self.doc_id, body={"requests": reqs}).execute()
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        cells = _table_cell_starts(doc, -1)
        bold_reqs = []
        for i, text in enumerate(headers):
            if i < len(cells):
                bold_reqs.append(
                    {
                        "updateTextStyle": {
                            "range": {"startIndex": cells[i], "endIndex": cells[i] + len(text)},
                            "textStyle": {"bold": True},
                            "fields": "bold",
                        }
                    }
                )
        if bold_reqs:
            self.docs.documents().batchUpdate(documentId=self.doc_id, body={"requests": bold_reqs}).execute()
        self._refresh_index()
        self.append_line("\n")


def _table_cell_starts(doc: dict, table_offset: int = -1) -> list[int]:
    tables = [e for e in doc["body"]["content"] if "table" in e]
    if not tables:
        return []
    table = tables[table_offset]
    starts = []
    for row in table["table"]["tableRows"]:
        for cell in row["tableCells"]:
            for el in cell.get("content", []):
                if "paragraph" in el:
                    for pe in el["paragraph"].get("elements", []):
                        if "startIndex" in pe:
                            starts.append(pe["startIndex"])
                            break
    return starts
