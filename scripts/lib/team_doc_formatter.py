"""Apply WM team document visual format (Google Docs API)."""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import date
from typing import Any

# Docs API: 60 write requests/min/user — pace batchUpdate calls on large publishes.
_BATCH_MIN_INTERVAL_SEC = 1.05

from .team_doc_translator import Block

FORMAT_REFERENCE_DOC_ID = "19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y"
FORMAT_REFERENCE_URL = (
    "https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit"
)

# WM brand palette (0.0–1.0 rgbColor)
WM_NAVY = {"red": 0.10, "green": 0.21, "blue": 0.36}
WM_BLUE = {"red": 0.17, "green": 0.48, "blue": 0.72}
WM_GRAY = {"red": 0.45, "green": 0.45, "blue": 0.45}
WM_CALLOUT_BG = {"red": 0.91, "green": 0.96, "blue": 1.0}
WM_TEMPLATE_BG = {"red": 0.95, "green": 0.97, "blue": 0.99}
WM_CALLOUT_BORDER = {"red": 0.17, "green": 0.48, "blue": 0.72}
WM_WHITE = {"red": 1.0, "green": 1.0, "blue": 1.0}
TEMPLATE_LABEL = "✉️ COPY & PASTE"

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

MAX_NORTH_STAR_LEN = 220


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
    north_star_line: str = ""
    overview_meta: list[str] = field(default_factory=list)


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

        if b.kind == "north_star":
            fd.north_star_line = _trim_north_star(b.text)
            continue

        if b.kind == "meta_bullet":
            fd.overview_meta.append(b.text)
            continue

        if b.kind in ("heading1", "h1") and _normalize_text(b.text) == _normalize_text(title):
            continue

        if b.kind in ("heading1", "h1"):
            fd.blocks.append(Block("h1", b.text))
            continue

        if b.kind == "heading2" and b.text == "At a glance":
            while i < len(blocks) and blocks[i].kind in ("bullet", "meta_bullet"):
                bullet = blocks[i]
                i += 1
                text = bullet.text
                if text.lower().startswith("outcome:"):
                    fd.north_star_line = _trim_north_star(text.split(":", 1)[-1].strip())
                elif text.lower().startswith(("who:", "when:")):
                    fd.overview_meta.append(text)
                elif text.lower().startswith("questions:"):
                    pass
            continue

        if b.kind in ("heading2", "h2"):
            h = b.text
            low = h.lower()
            if low in ("what this is for", "what this is for "):
                if not overview_started:
                    fd.blocks.append(Block("h1", "Overview"))
                    overview_started = True
                continue
            if low == "before you start":
                fd.blocks.append(Block("label", "Before You Start"))
                continue
            if low in ("how to do it", "how to do it "):
                fd.blocks.append(Block("h1", "How To Do It"))
                continue
            if low == "done right looks like":
                fd.blocks.append(Block("h2", "Done Right Looks Like"))
                continue
            if low == "when to get help":
                fd.blocks.append(Block("h2", "When To Get Help"))
                continue
            if low == "related procedures":
                fd.blocks.append(Block("h2", "Related Procedures"))
                continue
            fd.blocks.append(Block("h2", h))
            continue

        if b.kind == "heading3":
            fd.blocks.append(Block("label", b.text.split(" — ", 1)[-1] if " — " in b.text else b.text))
            continue

        if b.kind in ("table", "template"):
            fd.blocks.append(b)
            continue

        if b.kind == "callout":
            ctype = b.callout_type or _infer_callout(b.text)
            fd.blocks.append(Block("callout", b.text, callout_type=ctype))
            continue

        if not overview_started and b.kind == "paragraph" and b.text:
            fd.blocks.append(Block("h1", "Overview"))
            overview_started = True

        fd.blocks.append(b)

    _inject_overview_extras(fd)

    fd.blocks.append(
        Block(
            "callout",
            "If this doc conflicts with what you heard elsewhere, follow this doc and tell Gabriel.",
            callout_type="remember",
        )
    )
    return fd


def _trim_north_star(text: str) -> str:
    text = " ".join(text.split())
    if len(text) > MAX_NORTH_STAR_LEN:
        return text[: MAX_NORTH_STAR_LEN - 1].rstrip() + "…"
    return text


def _overview_extra_blocks(
    fd: FormattedDoc, *, skip_duplicate_north_star: bool = False
) -> list[Block]:
    extras: list[Block] = []
    show_north_star = bool(fd.north_star_line)
    if show_north_star and skip_duplicate_north_star:
        first_para = next(
            (b.text for b in fd.blocks if b.kind == "paragraph" and b.text), ""
        )
        if _normalize_text(fd.north_star_line) == _normalize_text(first_para):
            show_north_star = False
    if show_north_star:
        extras.append(Block("callout", fd.north_star_line, callout_type="north_star"))
    for line in fd.overview_meta:
        extras.append(Block("bullet", line))
    return extras


def _normalize_text(text: str) -> str:
    return " ".join(text.split()).lower()


def _overview_insert_index(blocks: list[Block]) -> int:
    """Insert after first Overview paragraph(s), before next h1/h2."""
    idx = 0
    for i, b in enumerate(blocks):
        if b.kind == "h1" and b.text == "Overview":
            idx = i + 1
            break
    para_count = 0
    for j in range(idx, len(blocks)):
        if blocks[j].kind == "paragraph":
            para_count += 1
            if para_count >= 1:
                return j + 1
        if blocks[j].kind in ("h1", "h2", "callout"):
            return j
    return idx + 1


def _inject_overview_extras(fd: FormattedDoc) -> None:
    if not fd.north_star_line and not fd.overview_meta:
        return
    if not any(bl.kind == "h1" and bl.text == "Overview" for bl in fd.blocks):
        fd.blocks.insert(0, Block("h1", "Overview"))
    insert_at = _overview_insert_index(fd.blocks)
    extras = _overview_extra_blocks(fd, skip_duplicate_north_star=True)
    for j, extra in enumerate(extras):
        fd.blocks.insert(insert_at + j, extra)
    fd.north_star_line = ""
    fd.overview_meta = []


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
    writer.write_cover(fd.title, fd.owner_line)

    for block in fd.blocks:
        if block.kind == "h1":
            writer.append_heading(block.text, "HEADING_1", colored=True)
        elif block.kind == "h2":
            writer.append_heading(block.text, "HEADING_2", colored=True)
        elif block.kind == "label":
            writer.append_label(block.text)
        elif block.kind == "callout":
            label = CALLOUT_LABELS.get(block.callout_type or "important", "⚠️ IMPORTANT")
            writer.append_callout_box(label, block.text)
        elif block.kind == "template":
            writer.append_template_box(block.text)
        elif block.kind == "table" and block.table_headers and block.table_rows:
            writer.append_data_table(block.table_headers, block.table_rows)
        elif block.kind == "bullet":
            label = block.text
            if block.link_url:
                label = f"{block.text} — {block.link_url}"
            writer.append_bullet(label)
        elif block.kind == "numbered":
            writer.append_bullet(block.text)
        elif block.kind == "paragraph":
            writer.append_body(block.text + "\n")

    if fd.quick_reference:
        writer.append_heading("Quick Reference — At a Glance", "HEADING_2", colored=True)
        writer.append_data_table(fd.quick_reference.headers, fd.quick_reference.rows)

    writer.write_cover_footer()


class _DocWriter:
    def __init__(self, docs, doc_id: str):
        self.docs = docs
        self.doc_id = doc_id
        self.index = 1
        self._last_batch_at: float = 0.0

    def _batch(self, requests: list[dict[str, Any]]) -> None:
        if not requests:
            return
        elapsed = time.monotonic() - self._last_batch_at
        if self._last_batch_at and elapsed < _BATCH_MIN_INTERVAL_SEC:
            time.sleep(_BATCH_MIN_INTERVAL_SEC - elapsed)
        self.docs.documents().batchUpdate(
            documentId=self.doc_id, body={"requests": requests}
        ).execute()
        self._last_batch_at = time.monotonic()
        self._refresh_index()

    def _refresh_index(self) -> None:
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        self.index = doc["body"]["content"][-1]["endIndex"] - 1

    def _insert(self, text: str) -> int:
        start = self.index
        self._batch([{"insertText": {"location": {"index": start}, "text": text}}])
        return start

    def _text_style(
        self,
        start: int,
        end: int,
        *,
        bold: bool | None = None,
        italic: bool | None = None,
        size: float | None = None,
        color: dict | None = None,
    ) -> dict[str, Any]:
        style: dict[str, Any] = {}
        fields: list[str] = []
        if bold is not None:
            style["bold"] = bold
            fields.append("bold")
        if italic is not None:
            style["italic"] = italic
            fields.append("italic")
        if size is not None:
            style["fontSize"] = {"magnitude": size, "unit": "PT"}
            fields.append("fontSize")
        if color is not None:
            style["foregroundColor"] = {"color": {"rgbColor": color}}
            fields.append("foregroundColor")
        return {
            "updateTextStyle": {
                "range": {"startIndex": start, "endIndex": end},
                "textStyle": style,
                "fields": ",".join(fields),
            }
        }

    def write_cover(self, title: str, owner_line: str) -> None:
        """Branded cover: navy WAIZ MEDIA, blue title, gray subtitle, divider."""
        media = "WAIZ MEDIA\n"
        title_line = f"{title}\n"
        meta = f"{owner_line}\n\n"

        start = self.index
        self._batch(
            [
                {
                    "insertText": {
                        "location": {"index": start},
                        "text": media + title_line + meta,
                    }
                }
            ]
        )
        media_start = start
        media_end = start + len(media)
        title_start = media_end
        title_end = title_start + len(title_line)
        meta_start = title_end
        meta_end = meta_start + len(meta)

        self._batch(
            [
                self._para_align(media_start, media_end, "CENTER"),
                self._para_align(title_start, title_end, "CENTER"),
                self._para_align(meta_start, meta_end, "CENTER"),
                self._text_style(media_start, media_end - 1, bold=True, size=26, color=WM_NAVY),
                self._text_style(title_start, title_end - 1, bold=False, size=20, color=WM_BLUE),
                self._text_style(meta_start, meta_end - 1, italic=True, size=11, color=WM_GRAY),
                self._para_border_bottom(meta_start, meta_end),
            ]
        )

    def _para_align(self, start: int, end: int, align: str) -> dict[str, Any]:
        return {
            "updateParagraphStyle": {
                "range": {"startIndex": start, "endIndex": end},
                "paragraphStyle": {"alignment": align},
                "fields": "alignment",
            }
        }

    def _para_border_bottom(self, start: int, end: int) -> dict[str, Any]:
        return {
            "updateParagraphStyle": {
                "range": {"startIndex": start, "endIndex": end},
                "paragraphStyle": {
                    "borderBottom": {
                        "color": {"color": {"rgbColor": WM_BLUE}},
                        "width": {"magnitude": 1, "unit": "PT"},
                        "padding": {"magnitude": 6, "unit": "PT"},
                        "dashStyle": "SOLID",
                    }
                },
                "fields": "borderBottom",
            }
        }

    def append_heading(self, text: str, style: str, *, colored: bool = False) -> None:
        start = self._insert(f"{text}\n")
        end = start + len(text) + 1
        reqs: list[dict[str, Any]] = [
            {
                "updateParagraphStyle": {
                    "range": {"startIndex": start, "endIndex": end},
                    "paragraphStyle": {"namedStyleType": style},
                    "fields": "namedStyleType",
                }
            }
        ]
        if colored:
            reqs.append(self._text_style(start, end - 1, bold=True, color=WM_NAVY))
        self._batch(reqs)

    def append_label(self, text: str) -> None:
        start = self._insert(f"{text}\n")
        end = start + len(text) + 1
        self._batch([self._text_style(start, end - 1, bold=True, size=11, color=WM_NAVY)])

    def append_body(self, text: str) -> None:
        self._insert(text)

    def append_bullet(self, text: str) -> None:
        self._insert(f"• {text}\n")

    def write_cover_footer(self) -> None:
        text = "\nWaiz Media  |  Internal Document  |  Confidential\n"
        start = self.index
        end = start + len(text)
        self._batch(
            [
                {"insertText": {"location": {"index": start}, "text": text}},
                self._para_align(start, end, "CENTER"),
                self._text_style(start, end - 1, size=10, color=WM_GRAY),
            ]
        )

    def append_callout_box(self, label: str, message: str) -> None:
        """Single-cell shaded callout (label + body), matching Objection Handling reference."""
        body = _trim_north_star(message) if "NORTH STAR" in label else message.strip()
        cell_text = f"{label}\n\n{body}\n"
        idx = self.index
        self._batch(
            [{"insertTable": {"rows": 1, "columns": 1, "location": {"index": idx}}}]
        )
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        table_start, cell_start = _table_anchor(doc, -1)
        if cell_start is None or table_start is None:
            self._insert("\n")
            return

        self._batch(
            [{"insertText": {"location": {"index": cell_start}, "text": cell_text}}]
        )
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        _, cell_start = _table_anchor(doc, -1)
        if cell_start is None:
            self._refresh_index()
            return
        c_start = cell_start
        c_end = c_start + len(cell_text)
        label_end = c_start + len(label) + 2

        self._batch(
            [
                self._style_table_cell(
                    table_start,
                    0,
                    0,
                    background=WM_CALLOUT_BG,
                    borders=True,
                ),
                self._text_style(c_start, c_start + len(label), bold=True, color=WM_NAVY),
                self._text_style(label_end, max(label_end, c_end - 1), size=11),
            ]
        )
        self._refresh_index()
        self._insert("\n")

    def append_template_box(self, message: str) -> None:
        """Ready-to-send message — distinct from rules/callouts."""
        body = message.strip()
        if not body:
            return
        cell_text = f"{TEMPLATE_LABEL}\n\n{body}\n"
        idx = self.index
        self._batch(
            [{"insertTable": {"rows": 1, "columns": 1, "location": {"index": idx}}}]
        )
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        table_start, cell_start = _table_anchor(doc, -1)
        if cell_start is None or table_start is None:
            self._insert("\n")
            return

        self._batch(
            [{"insertText": {"location": {"index": cell_start}, "text": cell_text}}]
        )
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        _, cell_start = _table_anchor(doc, -1)
        if cell_start is None:
            self._refresh_index()
            return
        c_start = cell_start
        c_end = c_start + len(cell_text)
        label_end = c_start + len(TEMPLATE_LABEL) + 2
        self._batch(
            [
                self._style_table_cell(
                    table_start,
                    0,
                    0,
                    background=WM_TEMPLATE_BG,
                    borders=True,
                ),
                self._text_style(
                    c_start, c_start + len(TEMPLATE_LABEL), bold=True, color=WM_BLUE
                ),
                self._text_style(label_end, max(label_end, c_end - 1), size=11, italic=True),
            ]
        )
        self._refresh_index()
        self._insert("\n")

    def append_data_table(self, headers: list[str], rows: list[list[str]]) -> None:
        idx = self.index
        nrows = 1 + len(rows)
        ncols = len(headers)
        self._batch(
            [
                {
                    "insertTable": {
                        "rows": nrows,
                        "columns": ncols,
                        "location": {"index": idx},
                    }
                }
            ]
        )
        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        cells = _table_cell_starts(doc, -1)
        data = [headers] + rows
        flat = [c for row in data for c in row]
        pairs = [
            (cell_start, text)
            for cell_start, text in zip(cells, flat)
            if cell_start is not None and text
        ]
        for cell_start, text in sorted(pairs, key=lambda p: p[0], reverse=True):
            self._batch(
                [{"insertText": {"location": {"index": cell_start}, "text": text}}]
            )

        doc = self.docs.documents().get(documentId=self.doc_id).execute()
        table_start, _ = _table_anchor(doc, -1)
        cells = _table_cell_starts(doc, -1)
        style_reqs: list[dict[str, Any]] = []
        if table_start is not None:
            for col in range(ncols):
                style_reqs.append(
                    self._style_table_cell(
                        table_start,
                        0,
                        col,
                        background=WM_NAVY,
                        borders=True,
                    )
                )
        for i, text in enumerate(headers):
            if i < len(cells) and text:
                end = cells[i] + len(text)
                if end > cells[i]:
                    style_reqs.append(
                        self._text_style(
                            cells[i],
                            end,
                            bold=True,
                            color=WM_WHITE,
                        )
                    )
        if style_reqs:
            self._batch(style_reqs)
        self._refresh_index()
        self._insert("\n")

    def _style_table_cell(
        self,
        table_start: int,
        row: int,
        col: int,
        *,
        background: dict | None = None,
        borders: bool = False,
    ) -> dict[str, Any]:
        cell_style: dict[str, Any] = {}
        fields: list[str] = []
        if background:
            cell_style["backgroundColor"] = {"color": {"rgbColor": background}}
            fields.append("backgroundColor")
        if borders:
            border = {
                "color": {"color": {"rgbColor": WM_CALLOUT_BORDER}},
                "width": {"magnitude": 1, "unit": "PT"},
                "dashStyle": "SOLID",
            }
            cell_style["borderTop"] = border
            cell_style["borderBottom"] = border
            cell_style["borderLeft"] = border
            cell_style["borderRight"] = border
            fields.extend(
                ["borderTop", "borderBottom", "borderLeft", "borderRight"]
            )
        return {
            "updateTableCellStyle": {
                "tableRange": {
                    "tableCellLocation": {
                        "tableStartLocation": {"index": table_start},
                        "rowIndex": row,
                        "columnIndex": col,
                    },
                    "rowSpan": 1,
                    "columnSpan": 1,
                },
                "tableCellStyle": cell_style,
                "fields": ",".join(fields),
            }
        }


def _table_anchor(doc: dict, table_offset: int = -1) -> tuple[int | None, int | None]:
    tables = [e for e in doc["body"]["content"] if "table" in e]
    if not tables:
        return None, None
    table = tables[table_offset]
    table_start = table.get("startIndex")
    cells = _table_cell_starts(doc, table_offset)
    cell_start = cells[0] if cells else None
    return table_start, cell_start


def _table_cell_starts(doc: dict, table_offset: int = -1) -> list[int]:
    """Insert indices for each table cell (empty cells included)."""
    tables = [e for e in doc["body"]["content"] if "table" in e]
    if not tables:
        return []
    table = tables[table_offset]
    starts = []
    for row in table["table"]["tableRows"]:
        for cell in row["tableCells"]:
            idx = _cell_insert_index(cell)
            if idx is not None:
                starts.append(idx)
    return starts


def _cell_insert_index(cell: dict) -> int | None:
    for el in cell.get("content", []):
        if "paragraph" not in el:
            continue
        if "startIndex" in el:
            return el["startIndex"]
        for pe in el["paragraph"].get("elements", []):
            if "startIndex" in pe:
                return pe["startIndex"]
    return None
