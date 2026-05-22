#!/usr/bin/env python3
"""Verify service account can access the team Drive folder."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib.google_publish import drive_service, resolve_credentials_path, service_account_email  # noqa: E402
from lib.paths import config_path  # noqa: E402


def main() -> int:
    print("Credentials:", resolve_credentials_path())
    print("Service account:", service_account_email())
    print()

    with config_path("team-drive-folders.yaml").open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    root_id = (cfg.get("root_folder_id") or "").strip()
    if not root_id:
        print("root_folder_id is empty in config/team-drive-folders.yaml")
        print()
        print("Next steps:")
        print("  1. In Google Drive, open your team folder (e.g. Waiz Team SOPs).")
        print("  2. Copy the ID from the URL: https://drive.google.com/drive/folders/FOLDER_ID")
        print(f"  3. Share that folder with: {service_account_email()} (Editor)")
        print("  4. Paste FOLDER_ID into config/team-drive-folders.yaml -> root_folder_id")
        print("  5. Re-run this script, then: python scripts/bootstrap-team-drive.py")
        return 1

    drive = drive_service()
    try:
        meta = (
            drive.files()
            .get(fileId=root_id, fields="id,name,mimeType", supportsAllDrives=True)
            .execute()
        )
    except Exception as e:
        print(f"Cannot access folder {root_id}: {e}")
        print(f"Share the folder with {service_account_email()} as Editor.")
        return 1

    print(f"OK — root folder: {meta.get('name')} ({meta.get('id')})")
    r = drive.files().list(
        q=f"'{root_id}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false",
        fields="files(id,name)",
        supportsAllDrives=True,
        includeItemsFromAllDrives=True,
    ).execute()
    children = r.get("files", [])
    if children:
        print("Subfolders:")
        for c in children:
            print(f"  - {c['name']} ({c['id']})")
    else:
        print("No subfolders yet. Run: python scripts/bootstrap-team-drive.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
