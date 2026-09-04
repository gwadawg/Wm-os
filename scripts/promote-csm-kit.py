#!/usr/bin/env python3
"""Promote allowlisted Wm-os docs (+ brand tokens) into sibling wm-csm-kit.

Usage (from Wm-os root):
  python3 scripts/promote-csm-kit.py
  python3 scripts/promote-csm-kit.py --dry-run

Does not commit the kit repo. Review, then commit/push wm-csm-kit yourself.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST = ROOT / "config" / "csm-kit-allowlist.yaml"

REDACTIONS = [
    (
        r"The % of money you should collect that you actually collect \(pay plans, MRR…\)",
        "The % of money you should collect that you actually collect (pay plans, recurring receivables…)",
    ),
    (
        r"a client paying you a JUICY retainer, one of those is when a client pays you, seems excited on the sales call, and then disappears off the face of the earth\. That shit triggers",
        "an active client — one of those is when a client pays you, seems excited on the sales call, and then disappears off the face of the earth. That triggers",
    ),
    (
        r"especially if you're sub-\$100k/mo\.",
        "especially while the agency is still small.",
    ),
    (
        r"To motivate your VA, you can put a simple commission structure in place based on the percentage of projected receivables they collect each month\.\n\n"
        r"95%\+ collected = \$300 bonus\n\n"
        r"90% – 94% = \$200 bonus\n\n"
        r"85% – 89% = \$100 bonus\n\n"
        r"The way this works is for example, if you have \$100k in MRR you're projected to collect that month, if she collects \$95k\+ she gets \$300\. Pretty damn simple\.",
        "To motivate your VA, put a simple commission structure in place based on the percentage of projected receivables they collect each month. "
        "Exact bonus tiers are owner-set (not listed in this kit). Keep the rule simple: higher collect rate → higher bonus, paid against that month's projected receivables.",
    ),
]


def load_allowlist() -> dict:
    if yaml is None:
        # Minimal fallback parser for our simple YAML shape
        text = ALLOWLIST.read_text()
        docs = re.findall(r"^\s+- (docs/[^\s]+)$", text, re.M)
        return {
            "kit_relative_root": "../wm-csm-kit",
            "source_subdir": "source/wm-os",
            "docs": docs,
            "redact": [
                "docs/client-fulfillment/client-success/overdue-payments-and-ghosting-clients.md"
            ],
            "mirrors": [],
            "brand": {
                "css_source": "docs/content-engine/production/carousel-kit/canvas.html",
                "css_fallback": "docs/acquisition/offer/angelo-castello-dscr-offer-sheet.html",
            },
        }
    return yaml.safe_load(ALLOWLIST.read_text())


def apply_redactions(text: str) -> str:
    out = text
    for pattern, repl in REDACTIONS:
        out = re.sub(pattern, repl, out, flags=re.S)
    return out


def extract_css_vars(html: str) -> dict[str, str]:
    m = re.search(r":root\s*\{([^}]+)\}", html)
    if not m:
        return {}
    block = m.group(1)
    return dict(re.findall(r"--([a-z0-9-]+):\s*([^;]+);", block, re.I))


def write_brand_tokens(kit: Path, vars_map: dict[str, str], dry: bool) -> None:
    # Normalize to kit token set
    def g(*keys, default=""):
        for k in keys:
            if k in vars_map:
                return vars_map[k].strip()
        return default

    tokens = {
        "navy": g("navy", default="#061A4A"),
        "royal": g("royal", default="#0E2F73"),
        "accent": g("accent", default="#4FA3FF"),
        "accent-deep": g("accent-deep", default="#2B7DE0"),
        "green": g("green", default="#7CFF7A"),
        "gold": g("gold", default="#F5C842"),
        "white": g("white", default="#FFFFFF"),
        "light": g("light", default="#F4F7FC"),
        "dark": g("dark", default="#0B1220"),
        "mid": g("mid", default="#5B6475"),
        "soft": g("soft", default="#8B93A7"),
        "divider": g("divider", default="#D1D9F0"),
    }
    css = f"""/**
 * Waiz Media — client-facing brand tokens (auto-refreshed by promote-csm-kit.py)
 * Fonts: Barlow Condensed (display) + IBM Plex Sans (body)
 */
:root {{
  --navy: {tokens['navy']};
  --royal: {tokens['royal']};
  --accent: {tokens['accent']};
  --accent-deep: {tokens['accent-deep']};
  --green: {tokens['green']};
  --gold: {tokens['gold']};
  --white: {tokens['white']};
  --light: {tokens['light']};
  --light-doctrine: #F5F7FB;
  --dark: {tokens['dark']};
  --mid: {tokens['mid']};
  --soft: {tokens['soft']};
  --divider: {tokens['divider']};
  --line: rgba(255, 255, 255, 0.12);
  --shadow: 0 22px 56px rgba(6, 26, 74, 0.14);
  --radius: 8px;
  --font-display: "Barlow Condensed", sans-serif;
  --font-body: "IBM Plex Sans", sans-serif;
  --wrap: 1180px;
}}

.team-doc-lane {{
  --team-navy: #1a365d;
  --team-blue: #2b6cb0;
}}
"""
    payload = {
        "client": {
            "navy": tokens["navy"],
            "royal": tokens["royal"],
            "accent": tokens["accent"],
            "accentDeep": tokens["accent-deep"],
            "green": tokens["green"],
            "gold": tokens["gold"],
            "white": tokens["white"],
            "light": tokens["light"],
            "lightDoctrine": "#F5F7FB",
            "dark": tokens["dark"],
            "mid": tokens["mid"],
            "soft": tokens["soft"],
            "divider": tokens["divider"],
            "radiusPx": 8,
            "wrapPx": 1180,
            "fonts": {
                "display": "Barlow Condensed",
                "body": "IBM Plex Sans",
                "googleFontsUrl": "https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800;900&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap",
            },
        },
        "teamDoc": {
            "navy": "#1a365d",
            "blue": "#2b6cb0",
            "note": "Internal Google Doc lane only — never mix into client HTML packets",
        },
    }
    css_path = kit / "brand" / "tokens.css"
    json_path = kit / "brand" / "tokens.json"
    if dry:
        print(f"DRY brand → {css_path}")
        return
    css_path.parent.mkdir(parents=True, exist_ok=True)
    css_path.write_text(css)
    json_path.write_text(json.dumps(payload, indent=2) + "\n")
    print(f"Wrote {css_path.relative_to(kit)} and tokens.json")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    cfg = load_allowlist()
    kit = (ROOT / cfg.get("kit_relative_root", "../wm-csm-kit")).resolve()
    if not kit.is_dir():
        print(f"ERROR: kit not found at {kit}", file=sys.stderr)
        return 1

    source_root = kit / cfg.get("source_subdir", "source/wm-os")
    redact_set = set(cfg.get("redact") or [])
    copied = 0
    missing = 0

    for rel in cfg.get("docs") or []:
        src = ROOT / rel
        dest = source_root / rel
        if not src.is_file():
            print(f"MISSING {rel}")
            missing += 1
            continue
        text = src.read_text()
        if rel in redact_set:
            text = apply_redactions(text)
        if args.dry_run:
            print(f"DRY {rel} → {dest.relative_to(kit)}")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text)
            print(f"OK {rel}")
        copied += 1

    for mirror in cfg.get("mirrors") or []:
        src_rel = mirror["src"]
        dest_rel = mirror["dest"]
        src = ROOT / src_rel
        dest = kit / dest_rel
        if not src.is_file():
            print(f"MISSING mirror {src_rel}")
            continue
        text = src.read_text()
        if src_rel in redact_set:
            text = apply_redactions(text)
        if args.dry_run:
            print(f"DRY mirror {dest_rel}")
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text)
            print(f"MIRROR {dest_rel}")

    brand = cfg.get("brand") or {}
    css_path = ROOT / brand.get("css_source", "")
    if not css_path.is_file():
        css_path = ROOT / brand.get("css_fallback", "")
    if css_path.is_file():
        vars_map = extract_css_vars(css_path.read_text())
        write_brand_tokens(kit, vars_map, args.dry_run)
    else:
        print("WARN: no brand CSS source found; skipped token refresh")

    print(f"\nDone. copied={copied} missing={missing} dry_run={args.dry_run}")
    print("Review wm-csm-kit, then commit/push that repo (this script does not commit).")
    return 0 if missing == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
