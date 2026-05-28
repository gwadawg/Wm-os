---
title: WM Team Doc Review Checklist
domain: templates
owner: operations
status: active
last_updated: 2026-05-28
review_cycle: quarterly
---

# WM Team Doc Review Checklist

Run this **after** editing a team draft, **before** `team-doc-approve.py` and publish.  
Goal: catch layout drift and one-pass generation mistakes before they reach Google Docs.

## Pass 1 — Global layout (all team docs)

- [ ] Cover: 4-line stack (brand → title → purpose → internal-use / role line)
- [ ] Exactly one overview: `# Overview` or `# 1. Overview` with a single `📌` doctrine callout
- [ ] Who / When / CONTEXT live **outside** the NORTH STAR box (bullets or labeled line below)
- [ ] Major sections numbered where instructional (`1.`, `2.`, `3.`)
- [ ] At least one high-signal table (contrast, step map, or index)
- [ ] Body uses doctrine callouts consistently (`📌` `💡` `🚨` `⭐`) — not random emoji
- [ ] **One footer only** at end of document
- [ ] No repo paths, Open Questions, or markdown artifacts (`---` rules, ASCII underlines)
- [ ] `approved: false` in draft frontmatter until this checklist passes

## Pass 2 — Angle libraries only

*When `team_doc_type: angle_library` — see [wm-team-angle-unit-template.md](wm-team-angle-unit-template.md).*

- [ ] Angle Index table exists once before angle sections
- [ ] Every `## Angle N —` section uses the **same section order**: Signal → opener variant(s) → ✉️ COPY & PASTE → Avoid
- [ ] Every paste block has **✉️ COPY & PASTE** + fenced code (no raw paste in tables)
- [ ] Every angle has **Avoid:** (or explicit `**Avoid:**` + bullets)
- [ ] Angles appear in numeric order matching the index (1, 2, 3 … not 1, 10, 2)
- [ ] No duplicate NORTH STAR, weekly-update boilerplate, or second footer
- [ ] Shared blocks (connect note, bump, ghost) use the same paste banner pattern as angles

## Pass 3 — Publish readiness

- [ ] `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md` succeeds (includes parser + type-specific checks)
- [ ] Spot-read Google Doc after publish: black body text, navy headers, paste boxes readable on mobile

## AI / Claude Code usage

1. Generate or translate draft using [team-doc-translate skill](../../.claude/skills/team-doc-translate/SKILL.md).
2. Run this checklist explicitly; list any **FORBIDDEN** violations from the angle template doc.
3. Fix violations in the draft file — do not patch only in Google Docs.
4. Approve and publish.

## Related

- [wm-team-doc-format-spec.md](wm-team-doc-format-spec.md)
- [wm-team-angle-unit-template.md](wm-team-angle-unit-template.md)
- [team-drive-publish.md](../operations/systems/team-drive-publish.md)
