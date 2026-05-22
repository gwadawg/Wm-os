#!/usr/bin/env python3
"""Publish canonical repo Markdown to team Google Docs (one-way)."""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib.google_publish import publish_blocks  # noqa: E402
from lib.paths import config_path, resolve_repo_path  # noqa: E402
from lib.registry import (  # noqa: E402
    doc_url,
    find_entry,
    load_registry,
    normalize_repo_path,
    save_registry,
    update_entry_doc_id,
)
from lib.team_doc_translator import format_role, translate  # noqa: E402

FRONTMATTER_STATUS_RE = re.compile(r"^status:\s*(\w+)", re.MULTILINE)


def load_folder_config() -> dict:
    with config_path("team-drive-folders.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def folder_id_for(cfg: dict, drive_folder_key: str) -> str:
    folders = cfg.get("folders", {})
    spec = folders.get(drive_folder_key, {})
    fid = (spec.get("id") or "").strip()
    if not fid:
        raise ValueError(
            f"No folder id for '{drive_folder_key}'. Run scripts/bootstrap-team-drive.py first."
        )
    return fid


def repo_status_active(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_STATUS_RE.search(text)
    return (m.group(1) if m else "draft") == "active"


def publish_entry(
    entry: dict,
    *,
    registry: dict,
    folder_cfg: dict,
    force: bool = False,
    archive: bool = False,
) -> str:
    repo_path = resolve_repo_path(entry["repo_path"])
    if not repo_path.exists():
        raise FileNotFoundError(repo_path)

    if not force and not repo_status_active(repo_path):
        raise ValueError(
            f"{entry['repo_path']} is not status: active. Use --force to publish anyway."
        )

    folder_key = entry.get("drive_folder", "operations")
    parent_id = folder_id_for(folder_cfg, folder_key)
    archive_id = None
    if archive:
        archive_id = folder_id_for(folder_cfg, "archive")

    blocks = translate(
        repo_path,
        registry_data=registry,
        team_title=entry.get("team_title"),
        team_role=entry.get("team_role", "team"),
    )

    owner = format_role(entry.get("team_role", "team"))

    doc_id = publish_blocks(
        blocks,
        folder_id=parent_id,
        title=entry.get("team_title") or repo_path.stem,
        owner=owner,
        existing_doc_id=entry.get("google_doc_id"),
        archive=archive,
        archive_folder_id=archive_id,
    )

    update_entry_doc_id(registry, entry["repo_path"], doc_id)
    return doc_id


def publish_spine(
    registry: dict,
    folder_cfg: dict,
    *,
    force: bool = False,
    delay_seconds: float = 12.0,
) -> list[str]:
    urls = []
    entries = [e for e in registry.get("entries", []) if e.get("publish_status") == "active"]
    for i, entry in enumerate(entries):
        if entry.get("google_doc_id") and not force:
            continue
        if i > 0 and delay_seconds > 0:
            time.sleep(delay_seconds)
        try:
            doc_id = publish_entry(
                entry,
                registry=registry,
                folder_cfg=folder_cfg,
                force=force or bool(entry.get("google_doc_id")),
            )
            save_registry(registry)
            urls.append(doc_url(doc_id))
            print(f"Published: {entry['repo_path']} -> {doc_url(doc_id)}")
        except Exception as e:
            print(f"Skip {entry['repo_path']}: {e}", file=sys.stderr)
    return urls


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish repo docs to team Google Drive.")
    parser.add_argument("path", nargs="?", help="Repo path to markdown file")
    parser.add_argument("--spine", action="store_true", help="Publish registry entries missing doc id")
    parser.add_argument("--start-here", action="store_true", help="Publish team-start-here.md")
    parser.add_argument("--force", action="store_true", help="Publish even if status is not active")
    parser.add_argument("--archive", action="store_true", help="Copy current doc to Archive before update")
    parser.add_argument("--update-all", action="store_true", help="With --spine, republish all active entries")
    args = parser.parse_args()

    registry = load_registry()
    folder_cfg = load_folder_config()

    if args.start_here:
        args.path = "docs/_inventory/team-start-here.md"

    if args.spine:
        publish_spine(
            registry,
            folder_cfg,
            force=args.update_all or args.force,
            delay_seconds=12.0 if args.update_all else 0.0,
        )
        return 0

    if not args.path:
        parser.print_help()
        return 1

    norm = normalize_repo_path(args.path)
    entry = find_entry(registry, norm)
    if not entry:
        print(f"No registry entry for {norm}. Add a row to team-publish-registry.yaml.", file=sys.stderr)
        return 1

    try:
        doc_id = publish_entry(
            entry,
            registry=registry,
            folder_cfg=folder_cfg,
            force=args.force,
            archive=args.archive,
        )
        save_registry(registry)
        print(f"Published: {doc_url(doc_id)}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
