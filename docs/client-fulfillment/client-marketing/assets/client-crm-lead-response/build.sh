#!/usr/bin/env bash
# Build the Client CRM Lead Response Playbook PDF.
#
#   bash build.sh
#
# Runs the minimax-pdf pipeline step by step so the cover carries the Waiz
# brand lockup and every page carries a small logo. Mirrors
# reverse-mortgage-dna/assets/rm-creative-playbook/build.sh so Waiz PDFs
# read as one family.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL="$HOME/.agents/skills/minimax-pdf/scripts"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

TITLE="Your CRM Lead Response Playbook"
SUBTITLE="New leads, conversations, pipeline, and outcome reporting"
AUTHOR="Client Success"
DATE="September 2026"
ACCENT="#14386E"
COVER_BG="#F4F6FA"
OUT="$HERE/client-crm-lead-response-playbook.pdf"
LOGO_SRC="/Users/gwadawg/Desktop/Repos/wm-csm-kit/brand/waiz-wordmark.svg"

echo "1/6  brand assets"
cp "$LOGO_SRC" "$HERE/waiz-wordmark.svg"
node - <<EOF
const { chromium } = require('$HOME/.agents/skills/minimax-pdf/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const svg = fs.readFileSync(path.join('$HERE', 'waiz-wordmark.svg'), 'utf8');

async function render(out, color, w, h) {
  const html = \`<!DOCTYPE html><html><body style="margin:0;background:transparent;display:flex;align-items:center;justify-content:center;">
  <div style="color:\${color};width:\${w}px;height:\${h}px;">\${svg.replace('<svg', \`<svg width="\${w}" height="\${h}"\`)}</div>
  </body></html>\`;
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 2 });
  await page.setContent(html, { waitUntil: 'load' });
  await page.locator('svg').screenshot({ path: out, omitBackground: true });
  await browser.close();
}
(async () => {
  await render(path.join('$HERE', 'waiz-wordmark-navy.png'), '#061A4A', 480, 240);
  await render(path.join('$HERE', 'waiz-wordmark-cover.png'), '#061A4A', 720, 360);
})();
EOF

echo "2/6  figures"
python3 "$HERE/build-figures.py" >/dev/null

echo "3/6  content"
FIGDIR="$HERE" BUILT="$WORK/content.built.json" python3 - <<'PY'
import json, os, pathlib
here = pathlib.Path(os.environ["FIGDIR"])
blocks = json.loads((here / "content.json").read_text().replace("FIGDIR", str(here)))
missing = [b["path"] for b in blocks
           if b.get("type") in ("figure", "image") and not pathlib.Path(b["path"]).exists()]
if missing:
    raise SystemExit(f"missing figures: {missing}")
pathlib.Path(os.environ["BUILT"]).write_text(json.dumps(blocks, indent=1))
PY

echo "4/6  tokens"
python3 "$SKILL/palette.py" \
  --title "$TITLE" --type magazine --author "$AUTHOR" --date "$DATE" \
  --accent "$ACCENT" --cover-bg "$COVER_BG" \
  --out "$WORK/tokens.json" >/dev/null

PDF_TOKENS="$WORK/tokens.json" HERE="$HERE" python3 - <<'PY'
import json, os
p = os.environ["PDF_TOKENS"]
t = json.load(open(p))
t["doc_type"] = "Waiz Media"
t["cover_image"] = f"file://{os.environ['HERE']}/hero-cover.png"
t["abstract"] = ("Your operating manual for the CRM: what happens automatically "
                 "when a lead comes in, what to do when they reply, and how "
                 "logging outcomes feeds directly into better leads.")
json.dump(t, open(p, "w"), indent=2)
PY

echo "5/6  cover + body"
python3 "$SKILL/cover.py" --tokens "$WORK/tokens.json" \
  --out "$WORK/cover.html" --subtitle "$SUBTITLE" >/dev/null

# Brand the cover: large Waiz wordmark + MEDIA lockup above the title
HERE="$HERE" COVER_HTML="$WORK/cover.html" python3 - <<'PY'
import os, pathlib, re
html_path = pathlib.Path(os.environ["COVER_HTML"])
logo = pathlib.Path(os.environ["HERE"]) / "waiz-wordmark-cover.png"
html = html_path.read_text()

html = re.sub(
    r"\.org-name \{[^}]+\}",
    """.org-name {
    font-size: 28px; font-weight: 600; letter-spacing: 0.42em;
    text-transform: uppercase; color: #061A4A; text-align:center;
    margin: 10px 0 0;
}""",
    html,
    count=1,
)
html = re.sub(
    r"\.org-rule \{[^}]+\}",
    """.org-rule {
    width: 72px; height: 2.5px; background: #14386E;
    margin: 18px auto 36px;
}
.brand-lockup {
    display: flex; flex-direction: column; align-items: center;
    margin-bottom: 0;
}
.brand-lockup img {
    width: 280px; height: auto; display: block;
}""",
    html,
    count=1,
)

new_block = f"""    <div class="brand-lockup">
      <img src="file://{logo}" alt="Waiz"/>
      <div class="org-name">MEDIA</div>
    </div>
    <div class="org-rule"></div>"""

html = re.sub(
    r'<div class="org-name">[^<]*</div>\s*<div class="org-rule"></div>',
    new_block,
    html,
    count=1,
)
html = html.replace(
    '<div class="author-name">Client Success</div>',
    '<div class="author-name">Waiz Media \u00b7 Client Success</div>',
)
html_path.write_text(html)
print("cover branded")
PY

node "$SKILL/render_cover.js" --input "$WORK/cover.html" --out "$WORK/cover.pdf" >/dev/null
python3 "$SKILL/render_body.py" --tokens "$WORK/tokens.json" \
  --content "$WORK/content.built.json" --out "$WORK/body.pdf" >/dev/null

echo "6/6  merge + page logos"
python3 "$SKILL/merge.py" --cover "$WORK/cover.pdf" --body "$WORK/body.pdf" \
  --out "$OUT" --title "$TITLE" >/dev/null

# Stamp a small wordmark on every body page (footer left). Cover already has the lockup.
HERE="$HERE" OUT="$OUT" python3 - <<'PY'
import fitz, os, pathlib, tempfile, shutil

pdf_path = pathlib.Path(os.environ["OUT"])
logo_path = pathlib.Path(os.environ["HERE"]) / "waiz-wordmark-navy.png"
doc = fitz.open(pdf_path)
logo_bytes = logo_path.read_bytes()
stamped = 0

for i, page in enumerate(doc):
    if i == 0:
        continue  # cover already branded
    rect = page.rect
    footer_y = rect.height - 49
    page.draw_rect(
        fitz.Rect(70, footer_y - 6, 300, footer_y + 14),
        color=(1, 1, 1), fill=(1, 1, 1), width=0,
    )
    w, h = 42, 21
    x0 = 79
    y0 = footer_y - 8
    page.insert_image(
        fitz.Rect(x0, y0, x0 + w, y0 + h),
        stream=logo_bytes,
        keep_proportion=True,
    )
    page.insert_text(
        fitz.Point(x0 + w + 7, footer_y + 5),
        "Waiz Media \u00b7 Client Playbook",
        fontsize=7.5,
        fontname="helv",
        color=(0.48, 0.48, 0.52),
    )
    stamped += 1

tmp = pathlib.Path(tempfile.mkstemp(suffix=".pdf")[1])
doc.save(tmp)
doc.close()
shutil.move(tmp, pdf_path)
print(f"stamped logo on {stamped} body pages ({stamped + 1} total)")
PY

echo "\u2713 $OUT"
