"""Render team draft markdown to styled DOCX via Pandoc."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from .paths import repo_root
from .publish_config import load_publish_config, reference_docx_path


class PublishPipelineError(Exception):
    """DOCX render or import failed; caller may fall back to API pipeline."""


def bundled_pandoc_path() -> Path | None:
    """Repo-local pandoc from scripts/setup-pandoc.sh (gitignored under .tools/)."""
    tools = repo_root() / ".tools" / "pandoc"
    if not tools.is_dir():
        return None
    for candidate in sorted(tools.glob("*/bin/pandoc")):
        if candidate.is_file():
            return candidate
    direct = tools / "bin" / "pandoc"
    return direct if direct.is_file() else None


def find_pandoc(cfg: dict | None = None) -> str:
    cfg = cfg or load_publish_config()
    path = (cfg.get("pandoc_path") or "pandoc").strip()
    if Path(path).is_file():
        return str(Path(path).resolve())
    resolved = shutil.which(path)
    if resolved:
        return resolved
    bundled = bundled_pandoc_path()
    if bundled:
        return str(bundled)
    raise PublishPipelineError(
        f"Pandoc not found ({path!r}). Run: python scripts/setup-pandoc.py "
        "or install: brew install pandoc"
    )


def render_team_docx(
    draft_path: Path,
    output_path: Path,
    *,
    reference_docx: Path | None = None,
    cfg: dict | None = None,
) -> Path:
    """Convert team draft markdown to DOCX using WM reference styles."""
    cfg = cfg or load_publish_config()
    ref = reference_docx or reference_docx_path(cfg)
    if not ref.is_file():
        raise PublishPipelineError(f"Reference DOCX missing: {ref}")

    pandoc = find_pandoc(cfg)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        pandoc,
        str(draft_path),
        "-o",
        str(output_path),
        f"--reference-doc={ref}",
        "--from=gfm",
        "--to=docx",
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        msg = (e.stderr or e.stdout or str(e)).strip()
        raise PublishPipelineError(f"Pandoc failed: {msg}") from e

    if not output_path.is_file() or output_path.stat().st_size == 0:
        raise PublishPipelineError(f"Pandoc produced empty file: {output_path}")

    return output_path
