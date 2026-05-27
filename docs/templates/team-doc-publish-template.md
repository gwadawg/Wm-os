---
title: Team Doc Publish Template
domain: templates
owner: operations
status: active
last_updated: 2026-05-27
review_cycle: quarterly
---

# Team Doc Publish Template

All team Google Docs must match the **WM Objection Categories** layout.

## Format reference (canonical)

- **Live doc:** https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit
- **Pandoc reference:** [wm-team-reference.docx](wm-team-reference.docx)
- **Written spec:** [wm-team-doc-format-spec.md](wm-team-doc-format-spec.md)
- **Team drafts:** [docs/team-drafts/README.md](../team-drafts/README.md)

## Workflow

```bash
python scripts/team-doc-prepare.py docs/path/to/sop.md
# Edit docs/team-drafts/<slug>.team.md
python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md
python scripts/publish-team-doc.py docs/path/to/sop.md
```

## Required layout (in draft + final Doc)

1. Centered cover: WAIZ MEDIA → title → role | Internal Use Only | year
2. Overview + NORTH STAR callout (one sentence)
3. Who / When bullets under Overview
4. How To Do It (H1) with H2 subsections
5. COPY & PASTE fenced blocks for messages
6. GFM tables for reference data
7. Centered confidential footer

## Related

- [team-drive-publish.md](../operations/systems/team-drive-publish.md)
- [team-doc-publish skill](../../.claude/skills/team-doc-publish/SKILL.md)
