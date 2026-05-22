"""Load and update team publish registry."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

import yaml

from .paths import registry_path, repo_root


def load_registry(path: Path | None = None) -> dict[str, Any]:
    p = path or registry_path()
    with p.open(encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    data.setdefault("entries", [])
    return data


def save_registry(data: dict[str, Any], path: Path | None = None) -> None:
    p = path or registry_path()
    with p.open("w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def find_entry(data: dict[str, Any], repo_path: str) -> dict[str, Any] | None:
    normalized = normalize_repo_path(repo_path)
    for entry in data.get("entries", []):
        if normalize_repo_path(entry.get("repo_path", "")) == normalized:
            return entry
    return None


def normalize_repo_path(repo_path: str) -> str:
    p = Path(repo_path)
    try:
        rel = p.resolve().relative_to(repo_root().resolve())
        return str(rel).replace("\\", "/")
    except ValueError:
        return str(p).replace("\\", "/")


def doc_url(doc_id: str) -> str:
    return f"https://docs.google.com/document/d/{doc_id}/edit"


def index_by_repo_path(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        normalize_repo_path(e["repo_path"]): e
        for e in data.get("entries", [])
        if e.get("repo_path")
    }


def update_entry_doc_id(
    data: dict[str, Any],
    repo_path: str,
    google_doc_id: str,
    *,
    published_date: str | None = None,
) -> None:
    entry = find_entry(data, repo_path)
    if not entry:
        raise KeyError(f"No registry entry for {repo_path}")
    entry["google_doc_id"] = google_doc_id
    entry["last_published"] = published_date or date.today().isoformat()
