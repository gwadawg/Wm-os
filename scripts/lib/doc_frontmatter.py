"""Parse YAML frontmatter from Markdown docs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    data = yaml.safe_load(parts[1])
    return data if isinstance(data, dict) else {}


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        return text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text
    return parts[2].lstrip("\n")


def read_doc_meta(path: Path) -> dict[str, Any]:
    text = read_text(path)
    meta = parse_frontmatter(text)
    meta["_path"] = path
    meta["_title"] = meta.get("title") or path.stem.replace("-", " ").title()
    return meta
