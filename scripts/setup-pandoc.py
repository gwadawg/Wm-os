#!/usr/bin/env python3
"""Download Pandoc into .tools/pandoc for DOCX team publish (no Homebrew required)."""

from __future__ import annotations

import platform
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / ".tools" / "pandoc"
PANDOC_VERSION = "3.6.4"


def arch_tag() -> str:
    machine = platform.machine().lower()
    if machine in ("arm64", "aarch64"):
        return "arm64"
    return "amd64"


def download_url() -> str:
    tag = arch_tag()
    return (
        f"https://github.com/jgm/pandoc/releases/download/"
        f"{PANDOC_VERSION}/pandoc-{PANDOC_VERSION}-{tag}-macOS.zip"
    )


def main() -> int:
    if shutil.which("pandoc"):
        print(f"Pandoc already on PATH: {shutil.which('pandoc')}")
        return 0

    url = download_url()
    print(f"Downloading {url} ...")
    TOOLS.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        zpath = Path(tmp) / "pandoc.zip"
        urlretrieve(url, zpath)
        with zipfile.ZipFile(zpath) as zf:
            zf.extractall(TOOLS)

    sys.path.insert(0, str(ROOT / "scripts"))
    from lib.pandoc_publish import bundled_pandoc_path

    bundled = bundled_pandoc_path()
    if not bundled:
        print("Extract failed — no pandoc binary under .tools/pandoc", file=sys.stderr)
        return 1

    out = subprocess.run([str(bundled), "--version"], capture_output=True, text=True)
    print(out.stdout.strip() or out.stderr.strip())
    print(f"Installed: {bundled}")
    print("Add to config/team-publish.local.yaml:")
    print(f'  pandoc_path: "{bundled}"')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
