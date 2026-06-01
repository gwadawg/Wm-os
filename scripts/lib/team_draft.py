"""Team draft paths, scaffold, approval, and markdown export."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from .paths import repo_root, resolve_repo_path
from .publish_config import load_publish_config
from .registry import find_entry, load_registry
from .team_doc_formatter import (
    CALLOUT_LABELS,
    TEMPLATE_LABEL,
    blocks_to_formatted_doc,
    team_subtitle,
)
from .team_doc_translator import Block, format_role, translate

FRONTMATTER_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
SKIP_DRAFT_CHECKS = (
    "source-docs/",
    "docs/_inventory/",
    "migration-backlog",
    "open questions",
)

PROFILES_PATH = repo_root() / "docs" / "templates" / "wm-team-doc-profiles.yaml"
_PROFILES_CACHE: dict[str, Any] | None = None


def load_profiles() -> dict[str, Any]:
    """Load and cache the doc-type profiles config."""
    global _PROFILES_CACHE
    if _PROFILES_CACHE is None:
        if PROFILES_PATH.is_file():
            with PROFILES_PATH.open(encoding="utf-8") as f:
                _PROFILES_CACHE = yaml.safe_load(f) or {}
        else:
            _PROFILES_CACHE = {}
    return _PROFILES_CACHE


def resolve_profile_key(team_doc_type: str | None) -> str:
    """Map a team_doc_type (or alias) to a concrete profile key."""
    cfg = load_profiles()
    default = cfg.get("default_profile", "sop")
    if not team_doc_type:
        return default
    key = str(team_doc_type).strip().lower()
    aliases = cfg.get("aliases", {}) or {}
    key = aliases.get(key, key)
    if key in (cfg.get("profiles", {}) or {}):
        return key
    return default


def load_profile(team_doc_type: str | None) -> dict[str, Any]:
    """Return the resolved profile dict (with thresholds/contract/examples)."""
    cfg = load_profiles()
    profiles = cfg.get("profiles", {}) or {}
    key = resolve_profile_key(team_doc_type)
    profile = dict(profiles.get(key, {}))
    profile.setdefault("key", key)
    return profile


def drafts_dir(cfg: dict | None = None) -> Path:
    cfg = cfg or load_publish_config()
    return Path(cfg["team_drafts_dir"])


def slug_from_repo_path(repo_path: str | Path) -> str:
    p = Path(repo_path)
    return p.stem.replace("_", "-")


def draft_paths_for_repo(repo_path: str | Path, cfg: dict | None = None) -> tuple[Path, Path]:
    slug = slug_from_repo_path(repo_path)
    base = drafts_dir(cfg)
    return base / f"{slug}.team.md", base / f"{slug}.team.meta.yaml"


def load_meta(meta_path: Path) -> dict[str, Any]:
    if not meta_path.is_file():
        return {}
    with meta_path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_meta(meta_path: Path, data: dict[str, Any]) -> None:
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    with meta_path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)


def read_draft_frontmatter(draft_path: Path) -> dict[str, Any]:
    """Parse the YAML frontmatter block of a team draft."""
    if not draft_path.is_file():
        return {}
    text = draft_path.read_text(encoding="utf-8")
    if not text.lstrip().startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        data = yaml.safe_load(parts[1])
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}


def draft_cover_footer(draft_path: Path, entry: dict | None = None) -> dict[str, str]:
    """Resolve cover + footer for faithful rendering, from frontmatter with fallbacks."""
    fm = read_draft_frontmatter(draft_path)
    entry = entry or {}
    role = fm.get("team_role") or entry.get("team_role") or "team"
    owner = format_role(role)
    title = (
        fm.get("cover_title")
        or fm.get("team_title")
        or entry.get("team_title")
        or draft_path.stem.replace("-", " ").title()
    )
    subtitle = fm.get("cover_subtitle") or ""
    audience = fm.get("cover_audience") or team_subtitle(owner)
    footer = fm.get("footer") or "Waiz Media  |  Internal Document  |  Confidential"
    return {
        "cover_title": str(title),
        "cover_subtitle": str(subtitle),
        "cover_audience": str(audience),
        "footer": str(footer),
    }


def is_approved(draft_path: Path, meta_path: Path | None = None) -> bool:
    meta_p = meta_path or (draft_path.parent / f"{draft_path.stem}.meta.yaml")
    meta = load_meta(meta_p)
    if meta.get("approved") is True:
        return True
    text = draft_path.read_text(encoding="utf-8") if draft_path.is_file() else ""
    m = re.search(r"^approved:\s*true\s*$", text, re.MULTILINE | re.IGNORECASE)
    return bool(m)


MD_INLINE_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def parse_inline_markdown_links(text: str) -> tuple[str, list[tuple[int, int, str]]]:
    """Replace [label](url) with label; return link ranges in plain text."""
    parts: list[str] = []
    ranges: list[tuple[int, int, str]] = []
    last = 0
    for m in MD_INLINE_LINK_RE.finditer(text):
        parts.append(text[last : m.start()])
        pos = len("".join(parts))
        label, url = m.group(1), m.group(2)
        start = pos
        parts.append(label)
        end = start + len(label)
        ranges.append((start, end, url))
        last = m.end()
    parts.append(text[last:])
    plain = "".join(parts)
    plain = re.sub(r"\*\*([^*]+)\*\*", r"\1", plain)
    plain = re.sub(r"\*([^*]+)\*", r"\1", plain)
    return plain.strip(), ranges


def _parse_table_row_cells(
    row_line: str,
) -> tuple[list[str], list[list[tuple[int, int, str]]]]:
    """Split a markdown table row into plain cells + per-cell inline link ranges."""
    raw_cells = [c.strip() for c in row_line.strip().strip("|").split("|")]
    plain_cells: list[str] = []
    link_cells: list[list[tuple[int, int, str]]] = []
    for cell in raw_cells:
        plain, ranges = parse_inline_markdown_links(cell)
        plain_cells.append(plain)
        link_cells.append(ranges)
    return plain_cells, link_cells


def resolve_block_link_ranges(
    blocks: list[Block],
    *,
    registry_index: dict[str, dict],
    source_repo_path: str | None = None,
) -> list[Block]:
    """Turn repo paths in link ranges into published Google Doc URLs when possible.

    Applies to body link_ranges as well as per-cell table header/row link ranges.
    """
    from .registry import doc_url
    from .team_doc_translator import normalize_repo_path, resolve_link_path

    source = resolve_repo_path(source_repo_path) if source_repo_path else None

    def resolve_href(href: str) -> str:
        if href.startswith("http"):
            return href
        target: Path | None = None
        if href.startswith("docs/"):
            candidate = repo_root() / href
            if candidate.is_file():
                target = candidate
        elif source is not None:
            target = resolve_link_path(source, href)
        if target is not None:
            norm = normalize_repo_path(str(target.relative_to(repo_root())))
            entry = registry_index.get(norm)
            doc_id = entry.get("google_doc_id") if entry else None
            if doc_id:
                return doc_url(doc_id)
        return href

    def resolve_ranges(
        ranges: list[tuple[int, int, str]] | None,
    ) -> list[tuple[int, int, str]] | None:
        if not ranges:
            return ranges
        return [(s, e, resolve_href(h)) for s, e, h in ranges]

    def resolve_cell_grid(
        grid: list[list[list[tuple[int, int, str]]]] | None,
    ) -> list[list[list[tuple[int, int, str]]]] | None:
        if not grid:
            return grid
        return [[resolve_ranges(cell) or [] for cell in row] for row in grid]

    resolved: list[Block] = []
    for block in blocks:
        has_body = bool(block.link_ranges)
        has_table = bool(block.table_header_links or block.table_row_links)
        if not has_body and not has_table:
            resolved.append(block)
            continue
        resolved.append(
            Block(
                block.kind,
                block.text,
                link_url=block.link_url,
                link_ranges=resolve_ranges(block.link_ranges),
                callout_type=block.callout_type,
                table_headers=block.table_headers,
                table_rows=block.table_rows,
                table_header_links=resolve_cell_grid(
                    [block.table_header_links] if block.table_header_links else None
                )[0]
                if block.table_header_links
                else None,
                table_row_links=resolve_cell_grid(block.table_row_links),
            )
        )
    return resolved


def team_doc_type_for_draft(draft_path: Path) -> str | None:
    meta_path = draft_path.parent / f"{draft_path.stem}.meta.yaml"
    meta = load_meta(meta_path)
    if meta.get("team_doc_type"):
        return str(meta["team_doc_type"])
    src = meta.get("source_repo_path")
    if src:
        entry = find_entry(load_registry(), src)
        if entry and entry.get("team_doc_type"):
            return str(entry["team_doc_type"])
    return None


ANGLE_SECTION_RE = re.compile(r"^## Angle (\d+)\s+—", re.MULTILINE)


def validate_angle_library(draft_path: Path) -> list[str]:
    """Enforce repeating angle unit skeleton (see wm-team-angle-unit-template.md)."""
    errors: list[str] = []
    body = FRONTMATTER_RE.sub("", draft_path.read_text(encoding="utf-8"))

    footer_count = len(re.findall(r"(?im)^Waiz Media \|", body))
    if footer_count > 1:
        errors.append(
            f"Duplicate footer ({footer_count} lines starting with 'Waiz Media |')"
        )

    north_star_count = len(re.findall(r"📌\s*NORTH STAR", body, re.IGNORECASE))
    if north_star_count > 1:
        errors.append(
            f"Duplicate NORTH STAR callout ({north_star_count}); keep one in Overview"
        )

    angle_nums = [int(m.group(1)) for m in ANGLE_SECTION_RE.finditer(body)]
    if not angle_nums:
        errors.append(
            "No ## Angle N — sections found (angle_library requires angle units)"
        )
        return errors

    sections = re.split(r"(?=^## Angle \d+\s+—)", body, flags=re.MULTILINE)
    for section in sections:
        if not section.strip().startswith("## Angle"):
            continue
        m = ANGLE_SECTION_RE.match(section.strip())
        if not m:
            continue
        n = m.group(1)
        if not re.search(r"\*\*Signal:\*\*", section):
            errors.append(f"Angle {n}: missing **Signal:**")
        if "**✉️ COPY & PASTE**" not in section:
            errors.append(f"Angle {n}: missing **✉️ COPY & PASTE** banner")
        if "```" not in section:
            errors.append(f"Angle {n}: missing fenced paste block (```)")
        if not re.search(r"\*\*Avoid:\*\*", section):
            errors.append(f"Angle {n}: missing **Avoid:**")

    if angle_nums != sorted(angle_nums):
        errors.append(
            f"Angles out of index order ({angle_nums}); reorder sections to match Angle Index"
        )

    return errors


BARE_URL_RE = re.compile(r"(?<!\]\()(?<!\]\(<)https?://[^\s)>\]]+")


def _block_char_count(block: Block) -> int:
    if block.kind == "table":
        n = sum(len(c) for c in (block.table_headers or []))
        for row in block.table_rows or []:
            n += sum(len(c) for c in row)
        return n
    return len(block.text or "")


def _block_link_count(block: Block) -> int:
    n = len(block.link_ranges or [])
    for cell in block.table_header_links or []:
        n += len(cell)
    for row in block.table_row_links or []:
        for cell in row:
            n += len(cell)
    return n


def validate_profile_thresholds(draft_path: Path, profile: dict) -> list[str]:
    """Enforce profile acceptance thresholds derived from real good/bad WM docs."""
    errors: list[str] = []
    thresholds = profile.get("thresholds", {}) or {}
    body = FRONTMATTER_RE.sub("", draft_path.read_text(encoding="utf-8"))

    # Bare URLs (Goal 2: anchor-text links only).
    if "bare_url" in (profile.get("contract", {}).get("forbids", []) or []):
        bare = BARE_URL_RE.findall(body)
        if bare:
            errors.append(
                f"Bare URL(s) found ({len(bare)}); use [anchor text](url) instead: {bare[0]}"
            )

    try:
        blocks = parse_team_draft_md(draft_path)
    except ValueError:
        return errors  # overview/empty errors already reported by validate_draft

    # H2 nesting (reject all-H1 docs).
    if thresholds.get("require_h2_nesting"):
        h1 = sum(1 for b in blocks if b.kind == "h1")
        h2 = sum(1 for b in blocks if b.kind == "h2")
        if h1 >= 3 and h2 == 0:
            errors.append(
                f"No H2 subsections ({h1} H1 / 0 H2). Use H2 nesting, not all-H1 (flat doc)."
            )

    # Box-density floor (catch over-boxing of tiny snippets).
    floor = thresholds.get("min_chars_per_box")
    if floor:
        paste_exempt = bool(thresholds.get("paste_box_exempt_density"))
        box_kinds = {"callout", "table"} if paste_exempt else {"callout", "table", "template"}

        def is_counted_box(b: Block) -> bool:
            if b.kind not in box_kinds:
                return False
            # NORTH STAR is intentionally short; don't penalize it.
            if b.kind == "callout" and (b.callout_type or "") == "north_star":
                return False
            return True

        box_blocks = [b for b in blocks if is_counted_box(b)]
        text_chars = sum(_block_char_count(b) for b in blocks if b.kind != "h1")
        nboxes = len(box_blocks)
        if nboxes >= 4:
            avg = text_chars / nboxes
            if avg < floor:
                errors.append(
                    f"Over-boxing: ~{avg:.0f} chars per box across {nboxes} boxes "
                    f"(floor {floor}). Consolidate boxes or use bullets/prose."
                )

    # Link cap per section.
    cap = thresholds.get("max_links_per_section")
    if cap:
        section = "Overview"
        count = 0

        def flush_section() -> None:
            nonlocal count
            if count > cap:
                errors.append(
                    f"Section '{section}' has {count} links (cap {cap}); de-duplicate."
                )

        for b in blocks:
            if b.kind in ("h1", "h2"):
                flush_section()
                section = b.text
                count = 0
            else:
                count += _block_link_count(b)
        flush_section()

    return errors


def validate_draft(draft_path: Path) -> list[str]:
    errors: list[str] = []
    if not draft_path.is_file():
        return [f"Draft not found: {draft_path}"]
    text = draft_path.read_text(encoding="utf-8")
    body = FRONTMATTER_RE.sub("", text)
    low = body.lower()
    if not re.search(r"^#\s+(?:\d+\.\s+)?overview\b", body, re.MULTILINE | re.IGNORECASE):
        if "north star" not in low and "what this is for" not in low:
            errors.append("Missing Overview section (# Overview or ## Overview)")
    if not re.search(r"^#\s+.+", body, re.MULTILINE):
        errors.append("Missing at least one H1 section")
    for pat in SKIP_DRAFT_CHECKS:
        if pat in low:
            errors.append(f"Remove internal content: {pat}")
    if len(body.strip()) < 200:
        errors.append("Draft body too short")

    doc_type = team_doc_type_for_draft(draft_path)
    profile = load_profile(doc_type)
    errors.extend(validate_profile_thresholds(draft_path, profile))
    if profile.get("key") == "playbook" or doc_type == "angle_library":
        errors.extend(validate_angle_library(draft_path))
    return errors


def blocks_to_draft_markdown(
    blocks: list[Block],
    *,
    title: str,
    owner_line: str,
    source_repo_path: str,
    team_role: str,
    approved: bool = False,
) -> str:
    """Serialize translator blocks to Pandoc-friendly team draft markdown."""
    lines: list[str] = [
        "---",
        f'team_title: "{title}"',
        f"team_role: {team_role}",
        f'source_repo_path: "{source_repo_path}"',
        f"approved: {str(approved).lower()}",
        f"draft_updated: {date.today().isoformat()}",
        "---",
        "",
        "<!-- Edit below. Publish uses Google Doc template (Objection Categories styles). -->",
        "",
        "**WAIZ MEDIA**",
        "",
        f"*{owner_line}*",
        "",
    ]

    skip_title_h1 = title.strip().lower()

    for block in blocks:
        if block.kind in ("heading1", "h1"):
            if block.text.strip().lower() == skip_title_h1:
                continue
            lines.append(f"# {block.text}")
            lines.append("")
        elif block.kind in ("heading2", "h2"):
            lines.append(f"## {block.text}")
            lines.append("")
        elif block.kind == "label":
            lines.append(f"**{block.text}**")
            lines.append("")
        elif block.kind == "callout":
            label = CALLOUT_LABELS.get(block.callout_type or "important", "IMPORTANT")
            lines.append(f"> **{label}**")
            lines.append(f">")
            for para in block.text.strip().split("\n"):
                lines.append(f"> {para.strip()}")
            lines.append("")
        elif block.kind == "template":
            lines.append(f"**{TEMPLATE_LABEL}**")
            lines.append("")
            lines.append("```")
            lines.append(block.text.strip())
            lines.append("```")
            lines.append("")
        elif block.kind == "table" and block.table_headers and block.table_rows:
            hdr = block.table_headers
            lines.append("| " + " | ".join(hdr) + " |")
            lines.append("| " + " | ".join("---" for _ in hdr) + " |")
            for row in block.table_rows:
                cells = row + [""] * (len(hdr) - len(row))
                lines.append("| " + " | ".join(cells[: len(hdr)]) + " |")
            lines.append("")
        elif block.kind == "bullet":
            if block.link_ranges:
                label = block.text
                for start, end, url in reversed(block.link_ranges):
                    label = f"{label[:start]}[{label[start:end]}]({url}){label[end:]}"
                lines.append(f"- {label}")
            elif block.link_url:
                lines.append(f"- [{block.text}]({block.link_url})")
            else:
                lines.append(f"- {block.text}")
        elif block.kind == "numbered":
            text = block.text.strip()
            text = re.sub(r"^\d+\.\s*", "", text)
            lines.append(f"1. {text}")
        elif block.kind == "paragraph" and block.text.strip():
            lines.append(block.text.strip())
            lines.append("")

    lines.extend(
        [
            "",
            "<div align=\"center\">",
            "",
            "*Waiz Media | Internal Document | Confidential*",
            "",
            "</div>",
            "",
        ]
    )
    return "\n".join(lines)


def prepare_draft(
    repo_path: Path,
    *,
    registry_data: dict,
    entry: dict,
    overwrite: bool = False,
) -> tuple[Path, Path]:
    """Generate or refresh team draft from canonical markdown."""
    draft_path, meta_path = draft_paths_for_repo(entry["repo_path"])
    if draft_path.is_file() and not overwrite:
        return draft_path, meta_path

    role = entry.get("team_role", "team")
    title = entry.get("team_title") or repo_path.stem
    owner = format_role(role)
    blocks = translate(
        repo_path,
        registry_data=registry_data,
        team_title=title,
        team_role=role,
    )
    fd = blocks_to_formatted_doc(blocks, title=title, owner=owner)
    owner_line = fd.owner_line

    md = blocks_to_draft_markdown(
        fd.blocks,
        title=title,
        owner_line=owner_line,
        source_repo_path=entry["repo_path"],
        team_role=role,
        approved=False,
    )
    draft_path.parent.mkdir(parents=True, exist_ok=True)
    draft_path.write_text(md, encoding="utf-8")

    meta = {
        "source_repo_path": entry["repo_path"],
        "team_title": title,
        "team_role": role,
        "approved": False,
        "approved_at": None,
        "draft_path": str(draft_path.relative_to(repo_root())).replace("\\", "/"),
    }
    if entry.get("team_doc_type"):
        meta["team_doc_type"] = entry["team_doc_type"]
    save_meta(meta_path, meta)

    if entry.get("team_doc_type") == "angle_library":
        note = (
            "<!-- angle_library: every ## Angle N — section must follow "
            "docs/templates/wm-team-angle-unit-template.md -->\n\n"
        )
        if note not in md:
            md = md.replace(
                "<!-- Edit below.",
                f"{note}<!-- Edit below.",
                1,
            )
            draft_path.write_text(md, encoding="utf-8")

    return draft_path, meta_path


def approve_draft(draft_path: Path) -> None:
    errors = validate_draft(draft_path)
    if errors:
        raise ValueError("Draft validation failed:\n- " + "\n- ".join(errors))

    meta_path = draft_path.parent / f"{draft_path.stem}.meta.yaml"
    meta = load_meta(meta_path)
    meta["approved"] = True
    meta["approved_at"] = date.today().isoformat()
    save_meta(meta_path, meta)

    text = draft_path.read_text(encoding="utf-8")
    if re.search(r"^approved:\s*false", text, re.MULTILINE | re.IGNORECASE):
        text = re.sub(
            r"^approved:\s*false\s*$",
            "approved: true",
            text,
            count=1,
            flags=re.MULTILINE | re.IGNORECASE,
        )
        draft_path.write_text(text, encoding="utf-8")


def _strip_heading_number(text: str) -> str:
    return re.sub(r"^\d+\.\s+", "", text.strip()).strip()


def _is_overview_heading(line: str) -> bool:
    m = re.match(
        r"^#\s+(?:\d+\.\s+)?(?:overview|full process)\b",
        line.strip(),
        re.IGNORECASE,
    )
    return bool(m)


def parse_team_draft_md(draft_path: Path) -> list[Block]:
    """Parse approved team draft into publish blocks (template pipeline)."""
    text = draft_path.read_text(encoding="utf-8")
    body = FRONTMATTER_RE.sub("", text)
    lines = body.splitlines()
    blocks: list[Block] = []
    started = False
    i = 0
    in_callout = False
    callout_lines: list[str] = []
    callout_label = ""
    in_fence = False
    fence_lines: list[str] = []

    def flush_callout() -> None:
        nonlocal in_callout, callout_lines, callout_label
        if not in_callout and not callout_label:
            return
        msg = "\n".join(callout_lines).strip()
        ctype = "important"
        low = callout_label.lower()
        if "north star" in low:
            ctype = "north_star"
        elif "tip" in low:
            ctype = "tip"
        elif "critical" in low:
            ctype = "critical"
        elif "remember" in low:
            ctype = "remember"
        plain, link_ranges = parse_inline_markdown_links(msg or callout_label)
        blocks.append(
            Block(
                "callout",
                plain,
                callout_type=ctype,
                link_ranges=link_ranges or None,
            )
        )
        in_callout = False
        callout_lines = []
        callout_label = ""

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not started:
            if _is_overview_heading(stripped) or (
                stripped.startswith("# ")
                and (
                    "overview" in stripped.lower()
                    or "full process" in stripped.lower()
                )
            ):
                started = True
            else:
                i += 1
                continue

        if stripped.startswith("```"):
            if in_fence:
                plain, link_ranges = parse_inline_markdown_links("\n".join(fence_lines))
                blocks.append(
                    Block("template", plain, link_ranges=link_ranges or None)
                )
                fence_lines = []
                in_fence = False
            else:
                flush_callout()
                in_fence = True
            i += 1
            continue

        if in_fence:
            fence_lines.append(line)
            i += 1
            continue

        if stripped.startswith(">"):
            in_callout = True
            inner = stripped.lstrip(">").strip()
            if inner.startswith("**") and inner.endswith("**"):
                callout_label = inner.strip("*").strip()
            elif inner:
                callout_lines.append(inner)
            i += 1
            continue

        if in_callout:
            flush_callout()

        if stripped.startswith("|") and "|" in stripped[1:]:
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            if len(table_lines) >= 2:
                headers, header_links = _parse_table_row_cells(table_lines[0])
                rows: list[list[str]] = []
                row_links: list[list[list[tuple[int, int, str]]]] = []
                for tl in table_lines[2:]:
                    cells, links = _parse_table_row_cells(tl)
                    rows.append(cells)
                    row_links.append(links)
                blocks.append(
                    Block(
                        "table",
                        "",
                        table_headers=headers,
                        table_rows=rows,
                        table_header_links=header_links,
                        table_row_links=row_links,
                    )
                )
            continue

        if stripped.startswith("# "):
            blocks.append(Block("h1", _strip_heading_number(stripped[2:].strip())))
            i += 1
            continue

        if stripped.startswith("## "):
            blocks.append(Block("h2", _strip_heading_number(stripped[3:].strip())))
            i += 1
            continue

        if stripped.startswith("- "):
            raw = stripped[2:].strip()
            plain, link_ranges = parse_inline_markdown_links(raw)
            blocks.append(Block("bullet", plain, link_ranges=link_ranges or None))
            i += 1
            continue

        m = re.match(r"^(\d+)\.\s+(.+)", stripped)
        if m:
            raw = m.group(2).strip()
            plain, link_ranges = parse_inline_markdown_links(raw)
            blocks.append(Block("numbered", plain, link_ranges=link_ranges or None))
            i += 1
            continue

        if stripped.startswith("**") and stripped.endswith("**") and len(stripped) < 80:
            label = stripped.strip("*").strip()
            if label == TEMPLATE_LABEL:
                i += 1
                continue
            blocks.append(Block("label", label))
            i += 1
            continue

        if stripped.lower().startswith("waiz media") or "confidential" in stripped.lower():
            i += 1
            continue

        if stripped:
            plain, link_ranges = parse_inline_markdown_links(stripped)
            blocks.append(Block("paragraph", plain, link_ranges=link_ranges or None))
        i += 1

    flush_callout()
    if not blocks:
        raise ValueError(
            f"No publishable content parsed from {draft_path}. "
            "Ensure draft has '# Overview', '# Full Process', or '# 1. Overview' and body sections."
        )
    return blocks


def blocks_for_publish(
    entry: dict,
    registry: dict,
    publish_cfg: dict,
) -> list[Block]:
    """Approved team draft if present; otherwise translate canonical repo file."""
    from .registry import index_by_repo_path

    draft_path, _ = draft_paths_for_repo(entry["repo_path"], publish_cfg)
    if entry.get("team_draft_path"):
        draft_path = resolve_repo_path(entry["team_draft_path"])
    if draft_path.is_file() and is_approved(draft_path):
        blocks = parse_team_draft_md(draft_path)
        return resolve_block_link_ranges(
            blocks,
            registry_index=index_by_repo_path(registry),
            source_repo_path=entry.get("repo_path"),
        )
    repo_path = resolve_repo_path(entry["repo_path"])
    return translate(
        repo_path,
        registry_data=registry,
        team_title=entry.get("team_title"),
        team_role=entry.get("team_role", "team"),
    )
