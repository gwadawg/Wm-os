#!/usr/bin/env python3
"""Regenerate client playbooks catalog from repo docs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.lib.client_playbooks import catalog_md_path, catalog_yaml_path, sync_catalog  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if catalog.md would change (CI hygiene)",
    )
    args = parser.parse_args()

    md_path = catalog_md_path()
    before = md_path.read_text(encoding="utf-8") if md_path.is_file() else ""

    config = sync_catalog()
    count = config.get("entry_count", 0)

    after = md_path.read_text(encoding="utf-8")
    if args.check and before != after:
        print("client-playbooks/catalog.md is out of date — run sync-client-playbooks.py")
        return 1

    print(f"Synced {count} entries → {catalog_yaml_path().relative_to(ROOT)}")
    print(f"Generated → {md_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
