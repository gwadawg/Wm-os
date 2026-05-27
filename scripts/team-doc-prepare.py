#!/usr/bin/env python3
"""Prepare a human-facing team draft from canonical repo markdown."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib.registry import find_entry, load_registry, normalize_repo_path  # noqa: E402
from lib.paths import resolve_repo_path  # noqa: E402
from lib.team_draft import prepare_draft  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate team draft markdown from canonical doc (no publish)."
    )
    parser.add_argument("path", help="Canonical repo path, e.g. docs/.../sop.md")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing draft",
    )
    args = parser.parse_args()

    norm = normalize_repo_path(args.path)
    registry = load_registry()
    entry = find_entry(registry, norm)
    if not entry:
        print(
            f"No registry entry for {norm}. Add to team-publish-registry.yaml.",
            file=sys.stderr,
        )
        return 1

    repo_path = resolve_repo_path(norm)
    if not repo_path.is_file():
        print(f"Not found: {repo_path}", file=sys.stderr)
        return 1

    draft_path, meta_path = prepare_draft(
        repo_path,
        registry_data=registry,
        entry=entry,
        overwrite=args.force,
    )
    print(f"Draft: {draft_path}")
    print(f"Meta:  {meta_path}")
    print("Edit the draft, then: python scripts/team-doc-approve.py", draft_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
