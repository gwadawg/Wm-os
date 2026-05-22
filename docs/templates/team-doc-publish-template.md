---
title: Team Doc Publish Template
domain: templates
owner: operations
status: active
last_updated: 2026-05-21
review_cycle: quarterly
---

# Team Doc Publish Template

All team Google Docs must match the **WM Objection Categories** layout.

## Format reference (canonical)

- **Live doc:** https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit
- **Written spec:** [wm-team-doc-format-spec.md](wm-team-doc-format-spec.md)
- **Translation skill:** [.claude/skills/team-doc-translate/SKILL.md](../../.claude/skills/team-doc-translate/SKILL.md)
- **Formatter code:** `scripts/lib/team_doc_formatter.py`

## Required layout

1. Centered cover: WAIZ MEDIA → title → role | Internal Use Only | year
2. `HEADING_1` major sections (Overview, How To Do It, …)
3. `HEADING_2` subsections
4. Bold field labels (What It Is, How to Identify It, …) where applicable
5. Callout **tables** (📌 NORTH STAR, ⚠️ IMPORTANT, 💡 PRO TIP, …)
6. Data **tables** for categories / steps / quick reference when useful
7. Centered confidential footer

## Publish command

```bash
python scripts/publish-team-doc.py docs/path/to/sop.md
```

## Related

- [team-drive-publish.md](../operations/systems/team-drive-publish.md)
