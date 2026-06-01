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
    "inputs / outputs": "inputs",
    "outputs": "outputs",
    "tools": "tools",
    "owners": "inputs",
    "process": "process",
    "operating content": "process",
    "quality bar": "quality",
    "escalation": "escalation",
    "owner": "owner",
    "related docs": "related docs",
}

RESERVED_SECTION_KEYS = frozenset(
    {
        "purpose",
        "scope",
        "when",
        "how to use",
        "inputs",
        "tools",
        "quality",
        "escalation",
        "related docs",
    }
)

PLAYBOOK_SECTION_ORDER = (
    "how to use",
    "voice variants",
    "connect micro-note (a/b test — under 200 characters)",
    "setter no-reply bump (one only, 48–72h after opener)",
    "gabriel ghost sequence (touches 1–3)",
    "comment-first opener (use with phase 0)",
    "angle index",
)

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
    kind: str  # heading1, heading2, label, north_star, meta_bullet, callout, template, table, paragraph, bullet, numbered
    text: str
    link_url: str | None = None
    link_ranges: list[tuple[int, int, str]] | None = None  # start, end, url within text
    callout_type: str | None = None
    table_headers: list[str] | None = None
    table_rows: list[list[str]] | None = None
    # Per-cell inline link ranges (parallel to table_headers / table_rows).
    table_header_links: list[list[tuple[int, int, str]]] | None = None
    table_row_links: list[list[list[tuple[int, int, str]]]] | None = None


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

    blocks.append(Block("h1", title))
    blocks.extend(build_at_a_glance(owner, sections, purpose_text=sections.get("purpose", "")))

    purpose = sections.get("purpose", "")
    if purpose:
        blocks.append(Block("h2", "What This Is For"))
        blocks.extend(paragraphs_to_blocks(truncate_paragraphs(sanitize_body(purpose, repo_path), max_paras=2)))

    inputs = sections.get("inputs", "") or sections.get("tools", "")
    when = sections.get("when", "")
    scope = sections.get("scope", "")
    before_parts = []
    if when:
        before_parts.append(sanitize_body(when, repo_path))
    if scope:
        before_parts.append(sanitize_body(scope, repo_path))
    if inputs:
        before_parts.append(sanitize_body(inputs, repo_path))
    if before_parts:
        blocks.append(Block("h2", "Before You Start"))
        for part in before_parts:
            blocks.extend(humanize_markdown_body(part, doc_title=title))

    is_playbook = _is_playbook_doc(meta, repo_path)

    if is_playbook:
        blocks.extend(_translate_playbook_sections(sections, repo_path, doc_title=title))
    else:
        process = gather_process_body(sections)
        if process:
            blocks.append(Block("h1", "How To Do It"))
            clean_process = sanitize_body(process, repo_path)
            blocks.extend(hunt_normal_callouts(clean_process))
            blocks.extend(humanize_markdown_body(clean_process, doc_title=title))

    how_to = sections.get("how to use", "")
    if how_to and not is_playbook:
        blocks.append(Block("h2", "Quick Start"))
        blocks.extend(humanize_markdown_body(sanitize_body(how_to, repo_path), doc_title=title))

    quality = sections.get("quality", "")
    if quality:
        blocks.append(Block("h2", "Done Right Looks Like"))
        blocks.extend(quality_to_blocks(sanitize_body(quality, repo_path)))

    escalation = sections.get("escalation", "")
    blocks.append(Block("h2", "When To Get Help"))
    if escalation:
        blocks.extend(paragraphs_to_blocks(sanitize_body(escalation, repo_path)))
    blocks.append(Block("paragraph", f"Questions, pricing, or exceptions → escalate to Gabriel ({owner} team)."))

    related_body = sections.get("related docs", "")
    if related_body:
        blocks.append(Block("h2", "Related Procedures"))
        blocks.extend(
            related_to_blocks(related_body, repo_path, registry_index),
        )

    return blocks


def _is_playbook_doc(meta: dict[str, str], repo_path: Path) -> bool:
    if meta.get("artifact_type") == "playbook":
        return True
    if repo_path.name in ("copy-angles.md", "linkedin-dm-angle-library.md"):
        return True
    if "copy" in repo_path.stem and repo_path.parent.name == "linkedin":
        return True
    return False


def _translate_playbook_sections(
    sections: dict[str, str],
    repo_path: Path,
    *,
    doc_title: str,
) -> list[Block]:
    """Rebuild playbook/script library docs for humans — not a flat markdown dump."""
    blocks: list[Block] = []
    seen: set[str] = set()

    how_to = sections.get("how to use", "").strip()
    if how_to:
        seen.add("how to use")
        blocks.append(Block("h1", "Quick Start"))
        blocks.extend(
            humanize_markdown_body(sanitize_body(how_to, repo_path), doc_title=doc_title)
        )

    for key in PLAYBOOK_SECTION_ORDER:
        if key not in sections or key in seen:
            continue
        seen.add(key)
        blocks.extend(_section_blocks(key, sections[key], repo_path, doc_title=doc_title))

    for key in sorted(sections.keys()):
        if key in seen or key in RESERVED_SECTION_KEYS or key.startswith("_"):
            continue
        blocks.extend(_section_blocks(key, sections[key], repo_path, doc_title=doc_title))

    return blocks


def _section_blocks(
    section_key: str,
    content: str,
    repo_path: Path,
    *,
    doc_title: str,
) -> list[Block]:
    content = sanitize_body(content, repo_path).strip()
    if not content:
        return []
    title = _section_display_title(section_key)
    blocks: list[Block] = [Block("h2", title)]
    if section_key == "angle index":
        blocks.append(
            Block(
                "callout",
                "Pick the angle number that matches the strongest signal on their profile, then scroll to that section for ready-to-send lines.",
                callout_type="tip",
            )
        )
    blocks.extend(humanize_markdown_body(content, doc_title=doc_title))
    return blocks


def _section_display_title(key: str) -> str:
    if re.match(r"^angle \d+", key, re.I):
        return key.title()
    parts = key.split("—", 1)[0].strip()
    return parts.title()


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


def gather_process_body(sections: dict[str, str]) -> str:
    """Merge process + SOP subsections + playbook angles into How To Do It."""
    parts: list[str] = []
    for key, content in sections.items():
        if key.startswith("_") or key in RESERVED_SECTION_KEYS:
            continue
        content = content.strip()
        if not content:
            continue
        if not content.lstrip().startswith("##"):
            title = " ".join(word.capitalize() for word in key.split())
            content = f"## {title}\n\n{content}"
        parts.append(content)
    return "\n\n".join(parts).strip()


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
    return [
        Block("north_star", outcome, callout_type="north_star"),
        Block("meta_bullet", f"Who: {owner}"),
        Block("meta_bullet", f"When: {when_short}"),
    ]


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


def humanize_markdown_body(text: str, *, doc_title: str = "") -> list[Block]:
    """Turn repo markdown into scannable team-doc blocks (tables, templates, headings)."""
    blocks: list[Block] = []
    lines = text.splitlines()
    i = 0
    schedule_rows = 0

    while i < len(lines):
        stripped = lines[i].strip()

        if not stripped or stripped in ("---", "***", "___"):
            i += 1
            continue

        if stripped.startswith("## "):
            label = stripped[3:].strip()
            if should_skip_phase_heading(label, doc_title):
                i += 1
                continue
            blocks.append(Block("h2", shorten_heading(label)))
            i += 1
            continue

        if stripped.startswith("### "):
            blocks.append(Block("label", stripped[4:].strip()))
            i += 1
            continue

        if stripped.startswith("|") and stripped.count("|") >= 2:
            headers, rows, i = _parse_markdown_table(lines, i)
            if headers and rows:
                blocks.append(
                    Block(
                        "table",
                        "",
                        table_headers=headers,
                        table_rows=rows,
                    )
                )
            continue

        if stripped.startswith(">"):
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote = strip_markdown_inline(lines[i].strip().lstrip(">").strip())
                if quote:
                    blocks.append(Block("template", quote))
                i += 1
            continue

        if re.match(r"^\*\*[^*]+\*\*:?\s*$", stripped):
            label = strip_markdown_inline(stripped.strip("*").strip(":"))
            blocks.append(Block("label", label))
            i += 1
            continue

        if is_schedule_row(stripped):
            schedule_rows += 1
            if schedule_rows <= 3:
                blocks.append(Block("bullet", strip_markdown_inline(stripped.lstrip("#").strip())))
            elif schedule_rows == 4:
                blocks.append(
                    Block(
                        "callout",
                        "Follow your calendar blocks — Hunt days are all priority list + outbound; Normal days mix calls and list work.",
                        callout_type="tip",
                    )
                )
            i += 1
            continue

        if stripped.startswith("▸") or stripped.upper().startswith("IMPORTANT:"):
            blocks.append(
                Block(
                    "callout",
                    strip_markdown_inline(stripped.lstrip("▸ ").strip()),
                    callout_type="important",
                )
            )
            i += 1
            continue

        if stripped.startswith("- ") or stripped.startswith("* "):
            item = strip_markdown_inline(stripped[2:])
            if item and not item.startswith("|"):
                blocks.append(Block("bullet", item))
            i += 1
            continue

        if re.match(r"^\d+\.\s", stripped):
            blocks.append(Block("numbered", strip_markdown_inline(stripped)))
            i += 1
            continue

        if stripped.startswith("**") and "**" in stripped[2:]:
            m = re.match(r"^\*\*([^*]+)\*\*:?\s*(.*)$", stripped)
            if m:
                label, rest = m.group(1).strip(), m.group(2).strip()
                blocks.append(Block("label", label))
                if rest:
                    blocks.append(Block("paragraph", strip_markdown_inline(rest) + "\n"))
                i += 1
                continue

        plain = strip_markdown_inline(stripped)
        if not plain or plain.startswith("|"):
            i += 1
            continue
        if len(plain) <= 100 and plain.endswith(":"):
            blocks.append(Block("label", plain.rstrip(":")))
        elif len(plain) <= MAX_TEAM_PARAGRAPH_LEN:
            blocks.append(Block("paragraph", plain + "\n"))
        else:
            for chunk in split_long_text(plain, max_len=180):
                blocks.append(Block("bullet", chunk))
        i += 1

    return blocks


def _parse_markdown_table(
    lines: list[str], start: int
) -> tuple[list[str], list[list[str]], int]:
    """Parse a GitHub-style markdown table starting at `start`."""
    table_lines: list[str] = []
    i = start
    while i < len(lines):
        s = lines[i].strip()
        if not s.startswith("|"):
            break
        table_lines.append(s)
        i += 1

    if len(table_lines) < 2:
        return [], [], start

    def split_row(row: str) -> list[str]:
        cells = [c.strip() for c in row.strip("|").split("|")]
        return [strip_markdown_inline(c) for c in cells]

    headers = split_row(table_lines[0])
    body_rows: list[list[str]] = []
    for row_line in table_lines[1:]:
        if re.match(r"^\|[\s\-:|]+\|$", row_line):
            continue
        body_rows.append(split_row(row_line))

    if not body_rows:
        return [], [], start
    return headers, body_rows, i


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
            if team_mode and re.match(r"^phase\s+[\db]", label, re.I):
                phase_index += 1
                blocks.append(Block("heading3", f"Phase {phase_index} — {shorten_heading(label)}"))
            elif team_mode:
                blocks.append(Block("heading2", shorten_heading(label)))
            else:
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
