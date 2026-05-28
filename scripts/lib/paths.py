"""Repository path helpers."""

from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def drive_export_root() -> Path | None:
    """Root of frozen Drive export (sibling wm-os-archive or legacy source-docs/)."""
    sibling = repo_root().parent / "wm-os-archive" / "waiz-drive-export"
    if sibling.is_dir():
        return sibling
    legacy = repo_root() / "source-docs" / "waiz-drive-export"
    if legacy.is_dir():
        return legacy
    return None


def config_path(name: str) -> Path:
    return repo_root() / "config" / name


def registry_path() -> Path:
    return repo_root() / "docs" / "_inventory" / "team-publish-registry.yaml"


def resolve_repo_path(path: str | Path) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return repo_root() / p
