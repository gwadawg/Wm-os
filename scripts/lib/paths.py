"""Repository path helpers."""

from __future__ import annotations

from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def config_path(name: str) -> Path:
    return repo_root() / "config" / name


def registry_path() -> Path:
    return repo_root() / "docs" / "_inventory" / "team-publish-registry.yaml"


def resolve_repo_path(path: str | Path) -> Path:
    p = Path(path)
    if p.is_absolute():
        return p
    return repo_root() / p
