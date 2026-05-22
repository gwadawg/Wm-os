"""Google Drive and Docs API helpers for team publish."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from google.oauth2 import service_account
from googleapiclient.discovery import build

from .paths import config_path
from .team_doc_formatter import blocks_to_formatted_doc, write_formatted_doc
from .team_doc_translator import Block

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
]

# Shared Drive / "My Drive" folder shared with service account
DRIVE_KWARGS = {"supportsAllDrives": True}


def resolve_credentials_path() -> str:
    env_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if env_path and Path(env_path).is_file():
        return env_path

    local_cfg = config_path("team-publish.local.yaml")
    if local_cfg.is_file():
        with local_cfg.open(encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        cred_path = (data.get("credentials_path") or "").strip()
        if cred_path and Path(cred_path).expanduser().is_file():
            return str(Path(cred_path).expanduser())

    raise EnvironmentError(
        "Set GOOGLE_APPLICATION_CREDENTIALS or create config/team-publish.local.yaml "
        "with credentials_path (see config/team-publish.local.example.yaml)."
    )


def get_credentials():
    path = resolve_credentials_path()
    os.environ.setdefault("GOOGLE_APPLICATION_CREDENTIALS", path)
    return service_account.Credentials.from_service_account_file(path, scopes=SCOPES)


def service_account_email() -> str:
    import json

    path = resolve_credentials_path()
    with Path(path).open(encoding="utf-8") as f:
        data = json.load(f)
    return data.get("client_email", "")


def drive_service(creds=None):
    return build("drive", "v3", credentials=creds or get_credentials(), cache_discovery=False)


def docs_service(creds=None):
    return build("docs", "v1", credentials=creds or get_credentials(), cache_discovery=False)


def create_folder(drive, name: str, parent_id: str, *, drive_id: str | None = None) -> str:
    meta: dict[str, Any] = {
        "name": name,
        "mimeType": "application/vnd.google-apps.folder",
        "parents": [parent_id],
    }
    if drive_id:
        meta["driveId"] = drive_id
    f = drive.files().create(body=meta, fields="id", **DRIVE_KWARGS).execute()
    return f["id"]


def create_doc_in_folder(drive, title: str, folder_id: str) -> str:
    meta = {
        "name": title,
        "mimeType": "application/vnd.google-apps.document",
        "parents": [folder_id],
    }
    f = drive.files().create(body=meta, fields="id", **DRIVE_KWARGS).execute()
    return f["id"]


def copy_file_to_folder(drive, file_id: str, folder_id: str, new_name: str) -> str:
    body = {"name": new_name, "parents": [folder_id]}
    copied = drive.files().copy(
        fileId=file_id, body=body, fields="id", **DRIVE_KWARGS
    ).execute()
    return copied["id"]


def clear_document_body(docs, doc_id: str) -> None:
    doc = docs.documents().get(documentId=doc_id).execute()
    content = doc.get("body", {}).get("content", [])
    if not content:
        return
    end_index = content[-1].get("endIndex", 1)
    if end_index <= 2:
        return
    requests = [
        {
            "deleteContentRange": {
                "range": {"startIndex": 1, "endIndex": end_index - 1},
            }
        }
    ]
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": requests}).execute()


def write_blocks_to_doc(
    docs,
    doc_id: str,
    blocks: list[Block],
    *,
    title: str = "Team Document",
    owner: str = "team",
) -> None:
    fd = blocks_to_formatted_doc(blocks, title=title, owner=owner)
    write_formatted_doc(docs, doc_id, fd)


def publish_blocks(
    blocks: list[Block],
    *,
    folder_id: str,
    title: str,
    owner: str = "team",
    existing_doc_id: str | None = None,
    archive: bool = False,
    archive_folder_id: str | None = None,
) -> str:
    creds = get_credentials()
    drive = drive_service(creds)
    docs = docs_service(creds)

    if existing_doc_id:
        if archive and archive_folder_id:
            copy_file_to_folder(
                drive,
                existing_doc_id,
                archive_folder_id,
                f"{title} (archived)",
            )
        write_blocks_to_doc(docs, existing_doc_id, blocks, title=title, owner=owner)
        drive.files().update(
            fileId=existing_doc_id, body={"name": title}, **DRIVE_KWARGS
        ).execute()
        return existing_doc_id

    doc_id = create_doc_in_folder(drive, title, folder_id)
    write_blocks_to_doc(docs, doc_id, blocks, title=title, owner=owner)
    return doc_id
