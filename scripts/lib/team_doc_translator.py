"""Translate canonical repo Markdown into team-friendly publish blocks."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .paths import repo_root
from .registry import index_by_repo_path, normalize_repo_path

FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

SKIP_SECTIONS_ACCUMULATE = {
    "open questions",
    "metrics",
}

SECTION_ALIASES = {
    "purpose": "purpose",
    "scope": "scope",
    "trigger": "when",
    "when to use": "when",
    "inputs": "inputs",
    "outputs": "outputs",
    "tools": "tools",
    "process": "process",
    "operating content": "process",
    "quality bar": "quality",
    "escalation": "escalation",
    "owner": "owner",
    "related docs": "related docs",
}

KNOWN_SECTION_HEADINGS = set(SECTION_ALIASES.keys())

INTERNAL_LINK_PREFIXES = (
    "_inventory/",
    "SPINE.md",
    "SOURCE-OF-TRUTH",
    "kpis/README",
    "migration-backlog",
    "google-drive-inventory",
)

PRICING_SENSITIVE = "overview-money-model"

SKIP_LINE_PATTERNS = (
    "objective:",
    "see domain owners",
    "status: active",
    "status: draft",
    "spine approved",
    "assign concrete kpis",
    "complements ",
    "per [identity core]",
    "per money model",
    "following tables outline",
    "the core structure is based on the provided reference",
)

SKIP_PHASE_KEYWORDS = (
    "daily schedules",
    "hunt mode only",
    "time\tactivity",
    "appendix:",
    "detailed breakdown",
    "a guide to",
    "playbook:",
)

MAX_TEAM_PARAGRAPH_LEN = 320


@dataclass
class Block:
    kind: str  # heading1, heading2, heading3, callout, paragraph, bullet, numbered, label
    text: str
    link_url: str | None = None
    callout_type: str | None = None


def translate(
    repo_path: Path,
    *,
    registry_data: dict | None = None,
    team_title: str | None = None,
    team_role: str = "team",
) -> list[Block]:
    raw = repo_path.read_text(encoding="utf-8")
    meta = parse_frontmatter(raw)
    body = strip_frontmatter(raw)
    sections = split_sections(body)

    title = team_title or meta.get("title") or repo_path.stem.replace("-", " ").title()
    owner = format_role(meta.get("owner") or team_role)
    slug = repo_path.stem

    registry_index = index_by_repo_path(registry_data or {"entries": []})
    blocks: list[Block] = []

    blocks.append(Block("heading1", title))
    blocks.extend(build_at_a_glance(owner, sections, purpose_text=sections.get("purpose", "")))

    purpose = sections.get("purpose", "")
    if purpose:
        blocks.append(Block("heading2", "What this is for"))
        blocks.extend(paragraphs_to_blocks(truncate_paragraphs(sanitize_body(purpose, repo_path), max_paras=2)))

    inputs = sections.get("inputs", "") or sections.get("tools", "")
    when = sections.get("when", "")
    before_parts = []
    if when:
        before_parts.append(sanitize_body(when, repo_path))
    if inputs:
        before_parts.append(sanitize_body(inputs, repo_path))
    if before_parts:
        blocks.append(Block("heading2", "Before you start"))
        for part in before_parts:
            blocks.extend(content_to_blocks(part))

    process = sections.get("process", "")
    if process:
        blocks.append(Block("heading2", "How to do it"))
        clean_process = sanitize_body(process, repo_path)
        blocks.extend(hunt_normal_callouts(clean_process))
        blocks.extend(
            content_to_blocks(
                clean_process,
                team_mode=True,
                doc_title=title,
            )
        )

    quality = sections.get("quality", "")
    if quality:
        blocks.append(Block("heading2", "Done right looks like"))
        blocks.extend(quality_to_blocks(sanitize_body(quality, repo_path)))

    escalation = sections.get("escalation", "")
    blocks.append(Block("heading2", "When to get help"))
    if escalation:
        blocks.extend(paragraphs_to_blocks(sanitize_body(escalation, repo_path)))
    blocks.append(Block("paragraph", f"Questions, pricing, or exceptions → escalate to Gabriel ({owner} team)."))

    related_body = sections.get("related docs", "")
    if related_body:
        blocks.append(Block("heading2", "Related procedures"))
        blocks.extend(
            related_to_blocks(related_body, repo_path, registry_index),
        )

    from datetime import date

    blocks.append(Block("paragraph", ""))
    blocks.append(
        Block(
            "paragraph",
            f"Published: {date.today().isoformat()} | Owner: {owner} | Ref: {slug}",
        )
    )

    return blocks


def parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = m.group(0)
    meta: dict[str, str] = {}
    for line in fm.splitlines():
        if ":" in line and not line.strip().startswith("---"):
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()
    return meta


def strip_frontmatter(text: str) -> str:
    return FRONTMATTER_RE.sub("", text, count=1).strip()


def split_sections(body: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    current_key = "_intro"
    current_lines: list[str] = []

    for line in body.splitlines():
        if line.startswith("# ") and not line.startswith("## "):
            flush(sections, current_key, current_lines)
            current_key = "_title"
            current_lines = [line[2:].strip()]
            continue
        if line.startswith("## "):
            heading = line[3:].strip().lower()
            if heading not in KNOWN_SECTION_HEADINGS:
                current_lines.append(line)
                continue
            flush(sections, current_key, current_lines)
            current_key = heading
            current_lines = []
            continue
        if current_key in SKIP_SECTIONS_ACCUMULATE and not line.startswith("##"):
            continue
        current_lines.append(line)

    flush(sections, current_key, current_lines)

    mapped: dict[str, str] = {}
    for key, content in sections.items():
        if key.startswith("_"):
            continue
        canonical = SECTION_ALIASES.get(key, key)
        if canonical in mapped:
            mapped[canonical] += "\n\n" + content
        else:
            mapped[canonical] = content

    return mapped


def flush(sections: dict[str, str], key: str, lines: list[str]) -> None:
    if key == "_intro":
        return
    text = "\n".join(lines).strip()
    if text:
        sections[key] = text


def sanitize_body(text: str, repo_path: Path) -> str:
    lines = []
    for line in text.splitlines():
        if "source_document:" in line or "source-docs/" in line:
            continue
        if any(p in line for p in INTERNAL_LINK_PREFIXES):
            continue
        if "see [" in line.lower() and ".md)" in line:
            continue
        lines.append(line)
    result = "\n".join(lines).strip()
    result = re.sub(r"For offer routing and pricing rules, see [^.]+\.", "", result)
    if PRICING_SENSITIVE in repo_path.name:
        result = re.sub(r"\$[\d,]+", "[pricing — escalate to Gabriel]", result)
        result += "\n\nFor specific pricing and deal structure, escalate to Gabriel."
    return result


def build_at_a_glance(owner: str, sections: dict[str, str], *, purpose_text: str) -> list[Block]:
    when = sections.get("when", "") or sections.get("scope", "")
    when_short = team_when_summary(when, owner)
    outcome = first_sentence(purpose_text) or "Complete the procedure below"
    blocks = [
        Block("heading2", "At a glance"),
        Block("bullet", f"Who: {owner}"),
        Block("bullet", f"When: {when_short}"),
        Block("bullet", f"Outcome: {outcome}"),
        Block("bullet", "Questions: Escalate to Gabriel"),
    ]
    return blocks


def team_when_summary(when: str, owner: str) -> str:
    when = strip_markdown_inline(when.replace("\n", " "))
    lower = when.lower()
    if not when or "source document" in lower or "domain owners" in lower:
        defaults = {
            "Setter": "Every working day (hunt or normal schedule)",
            "Closer": "On scheduled discovery and demo calls",
            "Client Success": "When diagnosing client performance issues",
            "Operations": "During daily ops and prioritization",
        }
        return defaults.get(owner, "When this procedure applies")
    return first_sentence(when)


def first_sentence(text: str) -> str:
    text = strip_markdown_inline(text.replace("\n", " ").strip())
    if not text:
        return ""
    parts = re.split(r"(?<=[.!?])\s+", text, maxsplit=1)
    sentence = parts[0].strip()
    return sentence[:200] + ("…" if len(sentence) > 200 else "")


def truncate_paragraphs(text: str, max_paras: int = 2) -> str:
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    return "\n\n".join(paras[:max_paras])


def hunt_normal_callouts(process_text: str) -> list[Block]:
    low = process_text.lower()
    if "hunt mode" not in low and "normal day" not in low:
        return []
    blocks: list[Block] = []
    if "hunt mode" in low:
        blocks.append(
            Block(
                "callout",
                "Hunt day (no close calls): focus on the priority list and outbound — every block is prospecting.",
                callout_type="important",
            )
        )
    if "normal day" in low or "hunt & kill" in low:
        blocks.append(
            Block(
                "callout",
                "Normal day: take scheduled close calls first, then return to the priority list between calls.",
                callout_type="tip",
            )
        )
    return blocks


def should_skip_line(line: str) -> bool:
    low = line.lower()
    return any(p in low for p in SKIP_LINE_PATTERNS)


def should_skip_phase_heading(label: str, doc_title: str) -> bool:
    low = label.lower()
    if len(low) < 3:
        return True
    if low in doc_title.lower() or doc_title.lower() in low:
        return True
    return any(k in low for k in SKIP_PHASE_KEYWORDS)


def quality_to_blocks(text: str) -> list[Block]:
    blocks: list[Block] = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or should_skip_line(stripped):
            continue
        if stripped.startswith("- ") or stripped.startswith("* "):
            item = strip_markdown_inline(stripped[2:])
            if len(item) < 120 and "see [" not in item.lower():
                blocks.append(Block("bullet", item))
        elif "follows waiz voice" in stripped.lower() or "identity core" in stripped.lower():
            continue
        else:
            plain = strip_markdown_inline(stripped)
            if plain and len(plain) < MAX_TEAM_PARAGRAPH_LEN:
                blocks.append(Block("bullet", plain))
    return blocks[:8]


def is_schedule_row(line: str) -> bool:
    if "\t" in line:
        return True
    if re.match(r"^#+\s*\d", line):
        return True
    if re.match(r"^\d{1,2}:\d{2}\s", line):
        return True
    return False


def content_to_blocks(
    text: str,
    *,
    team_mode: bool = False,
    doc_title: str = "",
) -> list[Block]:
    blocks: list[Block] = []
    schedule_rows = 0
    phase_index = 0

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or should_skip_line(stripped):
            continue

        if team_mode and is_schedule_row(stripped):
            schedule_rows += 1
            if schedule_rows <= 3:
                blocks.append(Block("bullet", strip_markdown_inline(stripped.lstrip("#").strip())))
            elif schedule_rows == 4:
                blocks.append(
                    Block(
                        "callout",
                        "TIP: Follow your calendar blocks — Hunt days are all priority list + outbound; Normal days mix calls and list work.",
                    )
                )
            continue

        if stripped.startswith("▸") or stripped.upper().startswith("IMPORTANT:"):
            blocks.append(Block("callout", strip_markdown_inline(stripped.lstrip("▸ ").strip())))
            continue
        if stripped.startswith("- ") or stripped.startswith("* "):
            blocks.append(Block("bullet", strip_markdown_inline(stripped[2:])))
        elif re.match(r"^\d+\.\s", stripped):
            blocks.append(Block("numbered", strip_markdown_inline(stripped)))
        elif stripped.startswith("### "):
            label = stripped[4:].strip()
            if team_mode and should_skip_phase_heading(label, doc_title):
                continue
            phase_index += 1
            blocks.append(Block("heading3", f"Phase {phase_index} — {shorten_heading(label)}"))
        elif stripped.startswith("## "):
            label = stripped[3:].strip()
            if team_mode and should_skip_phase_heading(label, doc_title):
                continue
            phase_index += 1
            blocks.append(Block("heading3", f"Phase {phase_index} — {shorten_heading(label)}"))
        else:
            plain = strip_markdown_inline(stripped)
            if not plain:
                continue
            if team_mode and len(plain) > MAX_TEAM_PARAGRAPH_LEN:
                plain = plain[:MAX_TEAM_PARAGRAPH_LEN].rsplit(" ", 1)[0] + "…"
            if team_mode:
                for chunk in split_long_text(plain, max_len=200):
                    blocks.append(Block("bullet", chunk))
            else:
                blocks.append(Block("paragraph", plain))
    return blocks


def split_long_text(text: str, max_len: int = 200) -> list[str]:
    if len(text) <= max_len:
        return [text]
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks: list[str] = []
    current = ""
    for s in sentences:
        if len(current) + len(s) + 1 <= max_len:
            current = f"{current} {s}".strip()
        else:
            if current:
                chunks.append(current)
            current = s[:max_len]
    if current:
        chunks.append(current)
    return chunks[:4]


def shorten_heading(label: str) -> str:
    label = re.sub(r"\s*:\s*a guide.*$", "", label, flags=re.I).strip()
    label = re.sub(r"\s*\(.*\)\s*$", "", label).strip()
    if len(label) > 56:
        return label[:53] + "…"
    return label


def paragraphs_to_blocks(text: str) -> list[Block]:
    if not text.strip():
        return []
    blocks: list[Block] = []
    for para in truncate_paragraphs(text, max_paras=5).split("\n\n"):
        blocks.append(Block("paragraph", strip_markdown_inline(para)))
    return blocks


def strip_markdown_inline(text: str) -> str:
    text = LINK_RE.sub(r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    return text.strip()


def related_to_blocks(
    related_text: str,
    source_path: Path,
    registry_index: dict[str, dict],
) -> list[Block]:
    blocks: list[Block] = []
    for line in related_text.splitlines():
        m = LINK_RE.search(line)
        if not m:
            stripped = line.strip().lstrip("- ").strip()
            if stripped:
                blocks.append(Block("bullet", strip_markdown_inline(stripped)))
            continue
        label, href = m.group(1), m.group(2)
        if any(p in href for p in INTERNAL_LINK_PREFIXES):
            continue
        target = resolve_link_path(source_path, href)
        if not target:
            blocks.append(Block("bullet", f"{label} (coming soon)"))
            continue
        norm = normalize_repo_path(str(target.relative_to(repo_root())))
        entry = registry_index.get(norm)
        doc_id = entry.get("google_doc_id") if entry else None
        if doc_id:
            from .registry import doc_url

            blocks.append(Block("bullet", label, link_url=doc_url(doc_id)))
        else:
            blocks.append(Block("bullet", f"{label} (coming soon)"))
    return blocks


def resolve_link_path(source: Path, href: str) -> Path | None:
    if href.startswith("http"):
        return None
    target = (source.parent / href).resolve()
    if target.suffix != ".md":
        return None
    if not target.exists():
        return None
    return target


def format_role(owner: str) -> str:
    mapping = {
        "setter": "Setter",
        "closer": "Closer",
        "client_success": "Client Success",
        "client success": "Client Success",
        "operations": "Operations",
        "sales leadership": "Sales leadership",
        "all": "Everyone on the team",
    }
    return mapping.get(owner.lower(), owner.replace("_", " ").title())


def blocks_to_plain_text(blocks: list[Block]) -> str:
    lines: list[str] = []
    for b in blocks:
        if b.kind == "heading1":
            lines.extend(["", b.text, "=" * min(len(b.text), 48), ""])
        elif b.kind == "heading2":
            lines.extend(["", b.text, "-" * min(len(b.text), 40), ""])
        elif b.kind == "heading3":
            lines.extend(["", b.text, ""])
        elif b.kind == "callout":
            lines.append(f"  ▸ {b.text}")
        elif b.kind == "bullet":
            lines.append(f"  • {b.text}")
        elif b.kind == "numbered":
            lines.append(f"  {b.text}")
        else:
            lines.append(b.text)
    return "\n".join(lines).strip() + "\n"
