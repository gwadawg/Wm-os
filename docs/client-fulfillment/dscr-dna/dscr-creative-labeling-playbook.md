---
title: DSCR Creative & Labeling Playbook (Media Buyer)
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-09-16
review_cycle: monthly
artifact_type: playbook
audience: media-buyer
---

# DSCR Creative & Labeling Playbook

Internal media-buyer PDF: buckets, sorting, labeling, campaign/ad-set shape.

**PDF:** [assets/media-buyer-creative-playbook/dscr-creative-labeling-playbook.pdf](assets/media-buyer-creative-playbook/dscr-creative-labeling-playbook.pdf)

**Sources (do not duplicate):**

- [dscr-creative-taxonomy.md](dscr-creative-taxonomy.md) — naming SOT
- [intelligence-icp-dscr.md](intelligence-icp-dscr.md) — who + NEVER

**Rebuild:**

```bash
cd docs/client-fulfillment/dscr-dna/assets/media-buyer-creative-playbook
python3 build-figures.py
bash ~/.agents/skills/minimax-pdf/scripts/make.sh run \
  --title "DSCR Creative & Labeling Playbook" \
  --type report --author "Waiz Media · Media Buying" \
  --date "September 2026" --accent "#1C4C80" --cover-bg "#061A4A" \
  --content content.json --out dscr-creative-labeling-playbook.pdf
```
