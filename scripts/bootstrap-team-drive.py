#!/usr/bin/env python3
"""Create role-based subfolders under Waiz Team SOPs root in Google Drive."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib.google_publish import create_folder, drive_service  # noqa: E402
from lib.paths import config_path  # noqa: E402


def main() -> int:
    cfg_file = config_path("team-drive-folders.yaml")
    with cfg_file.open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    root_id = (cfg.get("root_folder_id") or "").strip()
    if not root_id:
        print(
            "Error: Set root_folder_id in config/team-drive-folders.yaml\n"
            "Create a shared folder in Drive, share it with the service account, "
            "and paste the folder ID from the URL.",
            file=sys.stderr,
        )
        return 1

    drive = drive_service()
    folders = cfg.get("folders", {})
    shared_drive_id = (cfg.get("shared_drive_id") or "").strip() or None

    for key, spec in folders.items():
        folder_id = (spec.get("id") or "").strip()
        name = spec.get("name", key)
        if folder_id:
            print(f"Skip (exists): {name} -> {folder_id}")
            continue
        new_id = create_folder(drive, name, root_id, drive_id=shared_drive_id)
        spec["id"] = new_id
        print(f"Created: {name} -> {new_id}")

    cfg["root_folder_id"] = root_id
    with cfg_file.open("w", encoding="utf-8") as f:
        yaml.dump(cfg, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"\nUpdated {cfg_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
