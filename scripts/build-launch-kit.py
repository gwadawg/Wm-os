#!/usr/bin/env python3
"""Render a Waiz-branded Client Launch Kit PDF from a content.json.

Thin driver over the minimax-pdf skill (~/.agents/skills/minimax-pdf). Applies the
Waiz client-lane brand on top of the skill's `report` type:

  cover      navy #061A4A, accent blue #4FA3FF, dot grid, eyebrow "CLIENT LAUNCH KIT"
  headings   Barlow Condensed Bold
  body       IBM Plex Sans (Regular / Bold)

Fonts are fetched once into ~/.cache/waiz-fonts/ (not committed).

Usage:
  python3 scripts/build-launch-kit.py \
    --content docs/client-fulfillment/onboarding/assets/launch-kit-sample/content.json \
    --subtitle "Jordan Hale · Hale Capital Lending<br>Reverse Mortgage · Go-live 15 September 2026" \
    --date "September 2026" \
    --out /tmp/hale-launch-kit.pdf

SOP: docs/client-fulfillment/onboarding/sop-client-launch-kit.md
Template: docs/templates/client-launch-kit-template.md
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

SKILL_DIR = Path(os.environ.get("MINIMAX_PDF_DIR", Path.home() / ".agents/skills/minimax-pdf"))
SCRIPTS = SKILL_DIR / "scripts"
FONT_CACHE = Path.home() / ".cache/waiz-fonts"

# Waiz client-lane brand (docs/company/doctrine-brand-and-visual-identity-april-26.md)
NAVY = "#061A4A"
ROYAL = "#0E2F73"
ACCENT = "#4FA3FF"
ACCENT_LT = "#EAF3FF"
DARK = "#0B1220"
BODY_TEXT = "#1F2A3D"
MUTED = "#6B7A99"
LIGHT = "#F4F7FC"

FONTS = {
    "BarlowCondensed-Bold": "https://github.com/google/fonts/raw/main/ofl/barlowcondensed/BarlowCondensed-Bold.ttf",
    "IBMPlexSans": "https://github.com/IBM/plex/raw/master/packages/plex-sans/fonts/complete/ttf/IBMPlexSans-Regular.ttf",
    "IBMPlexSans-Bold": "https://github.com/IBM/plex/raw/master/packages/plex-sans/fonts/complete/ttf/IBMPlexSans-Bold.ttf",
    "IBMPlexSans-Italic": "https://github.com/IBM/plex/raw/master/packages/plex-sans/fonts/complete/ttf/IBMPlexSans-Italic.ttf",
    "IBMPlexSans-BoldItalic": "https://github.com/IBM/plex/raw/master/packages/plex-sans/fonts/complete/ttf/IBMPlexSans-BoldItalic.ttf",
}

GFONTS_IMPORT = (
    "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800"
    "&family=IBM+Plex+Sans:wght@400;500;600&display=swap"
)


def ensure_fonts() -> dict[str, str]:
    FONT_CACHE.mkdir(parents=True, exist_ok=True)
    paths: dict[str, str] = {}
    for name, url in FONTS.items():
        dest = FONT_CACHE / f"{name}.ttf"
        if not dest.exists():
            print(f"  fetching {name} …", file=sys.stderr)
            urllib.request.urlretrieve(url, dest)
        paths[name] = str(dest)
    return paths


def build_tokens(title: str, author: str, date: str, font_paths: dict[str, str]) -> dict:
    sys.path.insert(0, str(SCRIPTS))
    import palette  # type: ignore

    t = palette.build_tokens(title, "report", author, date, accent_override=ACCENT, cover_bg_override=NAVY)
    t.update(
        {
            # Cover eyebrow reads "{doc_type} · {date}"
            "doc_type": "Welcome Packet",
            "accent": ACCENT,
            "accent_lt": ACCENT_LT,
            "text_light": "#FFFFFF",
            "page_bg": "#FFFFFF",
            "dark": DARK,
            "body_text": BODY_TEXT,
            "muted": MUTED,
            # Cover (HTML) fonts
            "font_display": "Barlow Condensed",
            "font_body": "IBM Plex Sans",
            "gfonts_import": GFONTS_IMPORT,
            # Body (ReportLab) fonts
            "font_paths": font_paths,
            "font_display_rl": "BarlowCondensed-Bold",
            "font_body_rl": "IBMPlexSans",
            "font_body_b_rl": "IBMPlexSans-Bold",
            "font_heading": "BarlowCondensed-Bold",
            "font_body_b": "IBMPlexSans-Bold",
            # Condensed display reads small — scale headings up
            "size_h1": 28,
            "size_h2": 18,
            "size_h3": 11.5,
            "size_body": 10.5,
            "line_gap": 16.5,
            "section_gap": 22,
            "margin_top": 82,
            "margin_bottom": 72,
        }
    )
    return t


def render_cover(tokens_path: Path, subtitle: str, workdir: Path) -> Path:
    html = workdir / "cover.html"
    pdf = workdir / "cover.pdf"
    args = [sys.executable, str(SCRIPTS / "cover.py"), "--tokens", str(tokens_path), "--out", str(html)]
    if subtitle:
        args += ["--subtitle", subtitle]
    subprocess.run(args, check=True, cwd=SCRIPTS)
    subprocess.run(["node", str(SCRIPTS / "render_cover.js"), "--input", str(html), "--out", str(pdf)], check=True, cwd=SCRIPTS)
    return pdf


def render_body(tokens: dict, content: list, out: Path) -> None:
    sys.path.insert(0, str(SCRIPTS))
    import render_body  # type: ignore
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.lib.fonts import addMapping

    for name, fpath in tokens["font_paths"].items():
        pdfmetrics.registerFont(TTFont(name, fpath))
    # Map <b>/<i> inside IBM Plex paragraphs to the right faces
    addMapping("IBMPlexSans", 0, 0, "IBMPlexSans")
    addMapping("IBMPlexSans", 1, 0, "IBMPlexSans-Bold")
    addMapping("IBMPlexSans", 0, 1, "IBMPlexSans-Italic")
    addMapping("IBMPlexSans", 1, 1, "IBMPlexSans-BoldItalic")
    addMapping("BarlowCondensed-Bold", 0, 0, "BarlowCondensed-Bold")
    addMapping("BarlowCondensed-Bold", 1, 0, "BarlowCondensed-Bold")

    render_body.build(tokens, content, str(out))


def merge(cover: Path, body: Path, out: Path, title: str) -> None:
    subprocess.run(
        [sys.executable, str(SCRIPTS / "merge.py"), "--cover", str(cover), "--body", str(body), "--out", str(out), "--title", title],
        check=True,
        cwd=SCRIPTS,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--content", required=True, help="content.json for the body")
    ap.add_argument("--out", required=True, help="output PDF path")
    ap.add_argument("--title", default="Client Launch Kit")
    ap.add_argument("--subtitle", default="", help="Cover line under the title. Use <br> for a second line.")
    ap.add_argument("--author", default="Waiz Media")
    ap.add_argument("--date", default="", help="e.g. 'September 2026'")
    args = ap.parse_args()

    if not SCRIPTS.exists():
        print(f"minimax-pdf skill not found at {SKILL_DIR}. Set MINIMAX_PDF_DIR.", file=sys.stderr)
        return 2
    if shutil.which("node") is None:
        print("node is required for the cover render.", file=sys.stderr)
        return 2

    content_path = Path(args.content).resolve()
    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    font_paths = ensure_fonts()
    tokens = build_tokens(args.title, args.author, args.date, font_paths)

    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        tokens_path = workdir / "tokens.json"
        tokens_path.write_text(json.dumps(tokens, indent=2), encoding="utf-8")

        cover_pdf = render_cover(tokens_path, args.subtitle, workdir)
        body_pdf = workdir / "body.pdf"
        content = json.loads(content_path.read_text(encoding="utf-8"))
        render_body(tokens, content, body_pdf)
        merge(cover_pdf, body_pdf, out_path, args.title)

    print(f"✓ {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
