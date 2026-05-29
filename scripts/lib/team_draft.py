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


def is_approved(draft_path: Path, meta_path: Path | None = None) -> bool:
    meta_p = meta_path or (draft_path.parent / f"{draft_path.stem}.meta.yaml")
    meta = load_meta(meta_p)
    if meta.get("approved") is True:
        return True
    text = draft_path.read_text(encoding="utf-8") if draft_path.is_file() else ""
    m = re.search(r"^approved:\s*true\s*$", text, re.MULTILINE | re.IGNORECASE)
    return bool(m)


ANGLE_SECTION_RE = re.compile(r"^## Angle (\d+)\s+—", re.MULTILINE)


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
    if team_doc_type_for_draft(draft_path) == "angle_library":
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
            label = block.text
            if block.link_url:
                label = f"{block.text} — {block.link_url}"
            lines.append(f"- {label}")
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
    m = re.match(r"^#\s+(?:\d+\.\s+)?overview\b", line.strip(), re.IGNORECASE)
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
        blocks.append(Block("callout", msg or callout_label, callout_type=ctype))
        in_callout = False
        callout_lines = []
        callout_label = ""

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not started:
            if _is_overview_heading(stripped) or (
                stripped.startswith("# ") and "overview" in stripped.lower()
            ):
                started = True
            else:
                i += 1
                continue

        if stripped.startswith("```"):
            if in_fence:
                blocks.append(Block("template", "\n".join(fence_lines)))
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
                headers = [c.strip() for c in table_lines[0].strip("|").split("|")]
                rows = []
                for tl in table_lines[2:]:
                    rows.append([c.strip() for c in tl.strip("|").split("|")])
                blocks.append(
                    Block("table", "", table_headers=headers, table_rows=rows)
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
            blocks.append(Block("bullet", stripped[2:].strip()))
            i += 1
            continue

        m = re.match(r"^(\d+)\.\s+(.+)", stripped)
        if m:
            blocks.append(Block("numbered", m.group(2).strip()))
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
            blocks.append(Block("paragraph", stripped))
        i += 1

    flush_callout()
    if not blocks:
        raise ValueError(
            f"No publishable content parsed from {draft_path}. "
            "Ensure draft has '# Overview' (or '# 1. Overview') and body sections."
        )
    return blocks


def blocks_for_publish(
    entry: dict,
    registry: dict,
    publish_cfg: dict,
) -> list[Block]:
    """Approved team draft if present; otherwise translate canonical repo file."""
    draft_path, _ = draft_paths_for_repo(entry["repo_path"], publish_cfg)
    if entry.get("team_draft_path"):
        draft_path = resolve_repo_path(entry["team_draft_path"])
    if draft_path.is_file() and is_approved(draft_path):
        return parse_team_draft_md(draft_path)
    repo_path = resolve_repo_path(entry["repo_path"])
    return translate(
        repo_path,
        registry_data=registry,
        team_title=entry.get("team_title"),
        team_role=entry.get("team_role", "team"),
    )
