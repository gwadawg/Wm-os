"""Google Drive and Docs API helpers for team publish."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from .paths import config_path
from .pandoc_publish import PublishPipelineError
from .team_doc_formatter import (
    blocks_to_formatted_doc,
    render_draft_faithfully,
    write_formatted_doc,
)
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
    use_template_styles: bool = False,
) -> None:
    fd = blocks_to_formatted_doc(blocks, title=title, owner=owner)
    write_formatted_doc(docs, doc_id, fd, use_template_styles=use_template_styles)


FORMAT_REFERENCE_DOC_ID = "19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y"


def format_reference_doc_id(folder_cfg: dict) -> str:
    return (folder_cfg.get("format_reference_doc_id") or FORMAT_REFERENCE_DOC_ID).strip()


def publish_from_template(
    blocks: list[Block],
    *,
    folder_id: str,
    title: str,
    owner: str = "team",
    format_doc_id: str,
    existing_doc_id: str | None = None,
    template_based: bool = False,
    archive: bool = False,
    archive_folder_id: str | None = None,
    faithful: bool = False,
    cover_title: str | None = None,
    cover_subtitle: str = "",
    cover_audience: str = "",
    footer: str = "",
) -> str:
    """
    Copy the Claude-formatted reference Google Doc, clear body, write content.
    Inherits heading styles (blue left bar) from the template document.

    When `faithful` is set, the body + cover + footer are rendered EXACTLY as
    authored in the draft (no auto-injected cover/footer/callouts).
    """
    creds = get_credentials()
    drive = drive_service(creds)
    docs = docs_service(creds)

    reuse_existing = bool(existing_doc_id and template_based)

    if reuse_existing:
        target_id = existing_doc_id
        if archive and archive_folder_id:
            copy_file_to_folder(
                drive,
                existing_doc_id,
                archive_folder_id,
                f"{title} (archived)",
            )
    else:
        if existing_doc_id and archive and archive_folder_id:
            copy_file_to_folder(
                drive,
                existing_doc_id,
                archive_folder_id,
                f"{title} (archived)",
            )
        target_id = copy_file_to_folder(drive, format_doc_id, folder_id, title)
        if existing_doc_id and not reuse_existing:
            try:
                drive.files().delete(fileId=existing_doc_id, **DRIVE_KWARGS).execute()
            except Exception:
                pass

    if faithful:
        render_draft_faithfully(
            docs,
            target_id,
            blocks,
            cover_title=cover_title or title,
            cover_subtitle=cover_subtitle,
            cover_audience=cover_audience,
            footer=footer,
            use_template_styles=True,
        )
    else:
        write_blocks_to_doc(
            docs,
            target_id,
            blocks,
            title=title,
            owner=owner,
            use_template_styles=True,
        )
    drive.files().update(fileId=target_id, body={"name": title}, **DRIVE_KWARGS).execute()
    return target_id


DOCX_MIME = (
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
GOOGLE_DOC_MIME = "application/vnd.google-apps.document"


def upload_docx_as_google_doc(
    drive,
    docx_path: Path,
    *,
    folder_id: str,
    title: str,
    existing_doc_id: str | None = None,
    archive: bool = False,
    archive_folder_id: str | None = None,
) -> str:
    """Upload DOCX and convert to Google Doc. Updates existing doc in place when possible."""
    docx_path = Path(docx_path)
    if not docx_path.is_file():
        raise PublishPipelineError(f"DOCX not found: {docx_path}")

    media = MediaFileUpload(str(docx_path), mimetype=DOCX_MIME, resumable=True)

    if existing_doc_id:
        if archive and archive_folder_id:
            copy_file_to_folder(
                drive,
                existing_doc_id,
                archive_folder_id,
                f"{title} (archived)",
            )
        try:
            drive.files().update(
                fileId=existing_doc_id,
                media_body=media,
                body={"name": title},
                **DRIVE_KWARGS,
            ).execute()
            return existing_doc_id
        except Exception:
            media = MediaFileUpload(
                str(docx_path), mimetype=DOCX_MIME, resumable=True
            )
            created = (
                drive.files()
                .create(
                    body={
                        "name": title,
                        "mimeType": GOOGLE_DOC_MIME,
                        "parents": [folder_id],
                    },
                    media_body=media,
                    fields="id",
                    **DRIVE_KWARGS,
                )
                .execute()
            )
            new_id = created["id"]
            try:
                drive.files().delete(fileId=existing_doc_id, **DRIVE_KWARGS).execute()
            except Exception:
                pass
            return new_id

    created = (
        drive.files()
        .create(
            body={
                "name": title,
                "mimeType": GOOGLE_DOC_MIME,
                "parents": [folder_id],
            },
            media_body=media,
            fields="id",
            **DRIVE_KWARGS,
        )
        .execute()
    )
    return created["id"]


def publish_docx_file(
    docx_path: Path,
    *,
    folder_id: str,
    title: str,
    existing_doc_id: str | None = None,
    archive: bool = False,
    archive_folder_id: str | None = None,
) -> str:
    creds = get_credentials()
    drive = drive_service(creds)
    return upload_docx_as_google_doc(
        drive,
        docx_path,
        folder_id=folder_id,
        title=title,
        existing_doc_id=existing_doc_id,
        archive=archive,
        archive_folder_id=archive_folder_id,
    )


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
