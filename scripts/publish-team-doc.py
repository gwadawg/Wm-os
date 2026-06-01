#!/usr/bin/env python3
"""Publish canonical repo Markdown to team Google Docs (one-way)."""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
import time
from pathlib import Path

from googleapiclient.errors import HttpError

import yaml

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from lib.google_publish import (  # noqa: E402
    format_reference_doc_id,
    publish_blocks,
    publish_docx_file,
    publish_from_template,
)
from lib.pandoc_publish import PublishPipelineError, render_team_docx  # noqa: E402
from lib.paths import config_path, resolve_repo_path  # noqa: E402
from lib.publish_config import load_publish_config  # noqa: E402
from lib.registry import (  # noqa: E402
    doc_url,
    find_entry,
    load_registry,
    normalize_repo_path,
    save_registry,
    update_entry_doc_id,
)
from lib.team_doc_translator import format_role, translate  # noqa: E402
from lib.team_draft import (  # noqa: E402
    blocks_for_publish,
    draft_cover_footer,
    draft_paths_for_repo,
    is_approved,
    validate_draft,
    prepare_draft,
)

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


def resolve_pipeline(entry: dict, publish_cfg: dict) -> str:
    return (
        entry.get("publish_pipeline")
        or publish_cfg.get("default_publish_pipeline")
        or "template"
    ).lower()


def _require_valid_draft(draft_path: Path) -> None:
    errors = validate_draft(draft_path)
    if errors:
        raise ValueError(
            "Draft validation failed:\n- "
            + "\n- ".join(errors)
            + "\n\nReview: docs/templates/wm-team-doc-review-checklist.md"
        )


def publish_entry_template(
    entry: dict,
    *,
    registry: dict,
    folder_cfg: dict,
    publish_cfg: dict,
    force: bool = False,
    archive: bool = False,
) -> str:
    repo_path = resolve_repo_path(entry["repo_path"])
    if not force and not repo_status_active(repo_path):
        raise ValueError(
            f"{entry['repo_path']} is not status: active. Use --force to publish anyway."
        )

    draft_path, _ = draft_paths_for_repo(entry["repo_path"], publish_cfg)
    if entry.get("team_draft_path"):
        draft_path = resolve_repo_path(entry["team_draft_path"])
    if publish_cfg.get("require_approved_draft", True):
        if not draft_path.is_file():
            raise ValueError(
                f"Team draft missing: {draft_path}\n"
                f"Run: python scripts/team-doc-prepare.py {entry['repo_path']}"
            )
        if not is_approved(draft_path):
            raise ValueError(
                f"Draft not approved: {draft_path}\n"
                f"Run: python scripts/team-doc-approve.py {draft_path}"
            )
        _require_valid_draft(draft_path)

    folder_key = entry.get("drive_folder", "operations")
    parent_id = folder_id_for(folder_cfg, folder_key)
    archive_id = folder_id_for(folder_cfg, "archive") if archive else None
    title = entry.get("team_title") or repo_path.stem
    owner = format_role(entry.get("team_role", "team"))
    blocks = blocks_for_publish(entry, registry, publish_cfg)
    if not blocks:
        raise ValueError(
            "No content blocks to publish. Check team draft parser output "
            f"for {entry.get('team_draft_path', 'docs/team-drafts/')}."
        )
    ref_id = format_reference_doc_id(folder_cfg)

    # Faithful render when an approved draft exists (cover/footer from frontmatter).
    use_faithful = draft_path.is_file()
    cover = draft_cover_footer(draft_path, entry) if use_faithful else {}

    doc_id = publish_from_template(
        blocks,
        folder_id=parent_id,
        title=title,
        owner=owner,
        format_doc_id=ref_id,
        existing_doc_id=entry.get("google_doc_id"),
        template_based=bool(entry.get("template_based")),
        archive=archive,
        archive_folder_id=archive_id,
        faithful=use_faithful,
        cover_title=cover.get("cover_title"),
        cover_subtitle=cover.get("cover_subtitle", ""),
        cover_audience=cover.get("cover_audience", ""),
        footer=cover.get("footer", ""),
    )
    update_entry_doc_id(
        registry, entry["repo_path"], doc_id, template_based=True
    )
    return doc_id


def publish_entry_api(
    entry: dict,
    *,
    registry: dict,
    folder_cfg: dict,
    force: bool = False,
    archive: bool = False,
) -> str:
    repo_path = resolve_repo_path(entry["repo_path"])
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


def publish_entry_docx(
    entry: dict,
    *,
    registry: dict,
    folder_cfg: dict,
    publish_cfg: dict,
    archive: bool = False,
) -> str:
    draft_path, _ = draft_paths_for_repo(entry["repo_path"], publish_cfg)
    if entry.get("team_draft_path"):
        draft_path = resolve_repo_path(entry["team_draft_path"])

    if not draft_path.is_file():
        raise ValueError(
            f"Team draft missing: {draft_path}\n"
            f"Run: python scripts/team-doc-prepare.py {entry['repo_path']}"
        )

    require = publish_cfg.get("require_approved_draft", True)
    if require and not is_approved(draft_path):
        raise ValueError(
            f"Draft not approved: {draft_path}\n"
            f"Run: python scripts/team-doc-approve.py {draft_path}"
        )
    _require_valid_draft(draft_path)

    folder_key = entry.get("drive_folder", "operations")
    parent_id = folder_id_for(folder_cfg, folder_key)
    archive_id = folder_id_for(folder_cfg, "archive") if archive else None
    title = entry.get("team_title") or draft_path.stem

    with tempfile.TemporaryDirectory() as tmp:
        docx_out = Path(tmp) / f"{draft_path.stem}.docx"
        render_team_docx(draft_path, docx_out, cfg=publish_cfg)
        doc_id = publish_docx_file(
            docx_out,
            folder_id=parent_id,
            title=title,
            existing_doc_id=entry.get("google_doc_id"),
            archive=archive,
            archive_folder_id=archive_id,
        )

    update_entry_doc_id(registry, entry["repo_path"], doc_id)
    return doc_id


def publish_entry(
    entry: dict,
    *,
    registry: dict,
    folder_cfg: dict,
    publish_cfg: dict,
    force: bool = False,
    archive: bool = False,
    pipeline_override: str | None = None,
    skip_docx_fallback: bool = False,
) -> str:
    pipeline = (pipeline_override or resolve_pipeline(entry, publish_cfg)).lower()

    if pipeline == "api":
        return publish_entry_api(
            entry,
            registry=registry,
            folder_cfg=folder_cfg,
            force=force,
            archive=archive,
        )

    if pipeline == "docx":
        try:
            return publish_entry_docx(
                entry,
                registry=registry,
                folder_cfg=folder_cfg,
                publish_cfg=publish_cfg,
                archive=archive,
            )
        except (PublishPipelineError, ValueError) as e:
            if not skip_docx_fallback:
                print(
                    f"DOCX pipeline failed ({e}); falling back to template copy.",
                    file=sys.stderr,
                )
                return publish_entry_template(
                    entry,
                    registry=registry,
                    folder_cfg=folder_cfg,
                    publish_cfg=publish_cfg,
                    force=force,
                    archive=archive,
                )
            raise

    try:
        return publish_entry_template(
            entry,
            registry=registry,
            folder_cfg=folder_cfg,
            publish_cfg=publish_cfg,
            force=force,
            archive=archive,
        )
    except Exception as e:
        print(
            f"Template pipeline failed ({e}); falling back to DOCX then API.",
            file=sys.stderr,
        )
        try:
            return publish_entry_docx(
                entry,
                registry=registry,
                folder_cfg=folder_cfg,
                publish_cfg=publish_cfg,
                archive=archive,
            )
        except (PublishPipelineError, ValueError) as e2:
            print(f"DOCX failed ({e2}); using API formatter.", file=sys.stderr)
            return publish_entry_api(
                entry,
                registry=registry,
                folder_cfg=folder_cfg,
                force=force,
                archive=archive,
            )


def publish_spine(
    registry: dict,
    folder_cfg: dict,
    publish_cfg: dict,
    *,
    force: bool = False,
    delay_seconds: float = 12.0,
    pipeline_override: str | None = None,
) -> list[str]:
    urls = []
    entries = [e for e in registry.get("entries", []) if e.get("publish_status") == "active"]
    for i, entry in enumerate(entries):
        if entry.get("google_doc_id") and not force:
            continue
        if i > 0 and delay_seconds > 0:
            time.sleep(delay_seconds)
        for attempt in range(4):
            try:
                doc_id = publish_entry(
                    entry,
                    registry=registry,
                    folder_cfg=folder_cfg,
                    publish_cfg=publish_cfg,
                    force=force or bool(entry.get("google_doc_id")),
                    pipeline_override=pipeline_override,
                )
                save_registry(registry)
                urls.append(doc_url(doc_id))
                print(f"Published: {entry['repo_path']} -> {doc_url(doc_id)}")
                break
            except HttpError as e:
                if e.resp.status == 429 and attempt < 3:
                    wait = 65 * (attempt + 1)
                    print(f"Rate limit — waiting {wait}s before retry...", file=sys.stderr)
                    time.sleep(wait)
                    continue
                print(f"Skip {entry['repo_path']}: {e}", file=sys.stderr)
                break
            except Exception as e:
                print(f"Skip {entry['repo_path']}: {e}", file=sys.stderr)
                break
    return urls


def main() -> int:
    parser = argparse.ArgumentParser(description="Publish repo docs to team Google Drive.")
    parser.add_argument("path", nargs="?", help="Repo path to markdown file")
    parser.add_argument("--spine", action="store_true", help="Publish registry entries missing doc id")
    parser.add_argument("--start-here", action="store_true", help="Publish team-start-here.md")
    parser.add_argument("--force", action="store_true", help="Publish even if status is not active")
    parser.add_argument("--archive", action="store_true", help="Copy current doc to Archive before update")
    parser.add_argument("--update-all", action="store_true", help="With --spine, republish all active entries")
    parser.add_argument(
        "--pipeline",
        choices=("template", "docx", "api"),
        help="Override publish pipeline (default: template = copy Objection Categories doc)",
    )
    parser.add_argument(
        "--prepare",
        action="store_true",
        help="Only prepare team draft, do not publish",
    )
    args = parser.parse_args()

    registry = load_registry()
    folder_cfg = load_folder_config()
    publish_cfg = load_publish_config()

    if args.start_here:
        args.path = "docs/_inventory/team-start-here.md"

    if args.spine:
        publish_spine(
            registry,
            folder_cfg,
            publish_cfg,
            force=args.update_all or args.force,
            delay_seconds=90.0 if args.update_all else 0.0,
            pipeline_override=args.pipeline,
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

    if args.prepare:
        repo_path = resolve_repo_path(norm)
        draft_path, meta_path = prepare_draft(
            repo_path,
            registry_data=registry,
            entry=entry,
            overwrite=True,
        )
        print(f"Draft: {draft_path}")
        print(f"Meta:  {meta_path}")
        return 0

    for attempt in range(4):
        try:
            doc_id = publish_entry(
                entry,
                registry=registry,
                folder_cfg=folder_cfg,
                publish_cfg=publish_cfg,
                force=args.force,
                archive=args.archive,
                pipeline_override=args.pipeline,
            )
            save_registry(registry)
            print(f"Published: {doc_url(doc_id)}")
            return 0
        except HttpError as e:
            if e.resp.status == 429 and attempt < 3:
                wait = 65 * (attempt + 1)
                print(f"Rate limit — waiting {wait}s before retry...", file=sys.stderr)
                time.sleep(wait)
                continue
            print(f"Error: {e}", file=sys.stderr)
            return 1
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
