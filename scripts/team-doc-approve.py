#!/usr/bin/env python3
"""Approve a team draft for DOCX publish."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib.paths import resolve_repo_path  # noqa: E402
from lib.team_draft import approve_draft  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Approve team draft for publish.")
    parser.add_argument("draft", help="Path to docs/team-drafts/*.team.md")
    args = parser.parse_args()

    draft_path = resolve_repo_path(args.draft)
    try:
        approve_draft(draft_path)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    print(f"Approved: {draft_path}")
    meta = draft_path.parent / f"{draft_path.stem}.meta.yaml"
    if meta.is_file():
        print(f"Meta: {meta}")
    print("Publish with: python scripts/publish-team-doc.py <source_repo_path>")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
