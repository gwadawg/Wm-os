"""Team publish configuration (local yaml + defaults)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .paths import config_path, repo_root

DEFAULTS: dict[str, Any] = {
    "default_publish_pipeline": "template",
    "pandoc_path": "pandoc",
    "reference_docx": "docs/templates/wm-team-reference.docx",
    "require_approved_draft": True,
    "team_drafts_dir": "docs/team-drafts",
}


def load_publish_config() -> dict[str, Any]:
    cfg = dict(DEFAULTS)
    local = config_path("team-publish.local.yaml")
    if local.is_file():
        with local.open(encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        cfg.update({k: v for k, v in data.items() if k in DEFAULTS or k == "credentials_path"})
    ref = cfg.get("reference_docx", "")
    if ref and not Path(ref).is_absolute():
        cfg["reference_docx"] = str(repo_root() / ref)
    drafts = cfg.get("team_drafts_dir", "")
    if drafts and not Path(drafts).is_absolute():
        cfg["team_drafts_dir"] = str(repo_root() / drafts)
    return cfg


def reference_docx_path(cfg: dict[str, Any] | None = None) -> Path:
    cfg = cfg or load_publish_config()
    return Path(cfg["reference_docx"])
