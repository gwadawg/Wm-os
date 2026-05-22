---
title: WM Team Doc Format Spec
domain: templates
owner: operations
status: active
last_updated: 2026-05-21
review_cycle: quarterly
---

# WM Team Doc Format Spec

Canonical visual standard for team Google Docs. **Match this layout on every publish.**

## Reference document (copy this look)

- **Live example:** [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)
- **Doc ID:** `19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y`
- **Config:** [config/team-drive-folders.yaml](../../config/team-drive-folders.yaml) → `format_reference_doc_id`

## Cover block (centered)

```
WAIZ MEDIA                    ← 26pt bold, centered
[Document Title]              ← 20pt, centered
[Role] Team | Internal Use Only | [Year]   ← 11pt, centered
```

Role examples: Sales & Setting, Client Success, Operations, Company.

## Body structure

| Element | Google Docs style | Usage |
|---------|-------------------|--------|
| Major section | `HEADING_1` | Overview, main chapters |
| Subsection | `HEADING_2` | Categories, phases, workflows |
| Field label | Bold 11pt normal text | `What It Is`, `How to Identify It`, `How to Handle It` |
| Body | 11pt normal text | Short paragraphs, max ~4 lines |
| Lists | Bullets (not long prose blocks) | Identification criteria, steps |

## Callout boxes (1×2 table)

Use a **single-row table** with two cells:

| Cell 1 (label) | Cell 2 (message) |
|----------------|------------------|
| 📌 NORTH STAR | One-sentence rule or north star |
| ⚠️ IMPORTANT | Non-negotiable warning |
| 💡 PRO TIP | Helpful tactic |
| 🚨 CRITICAL MISTAKE TO AVOID | High-cost error |
| ⚠️ WATCH FOR THIS | Commonly missed case |
| 📌 RULE / 📌 REMEMBER | Closing rule |

## Data tables

Use when comparing categories, steps, or quick reference:

- Header row: bold column titles
- 2–4 columns max
- Short cell text

Examples: category matrix, step | what to do, objection | category | how to handle.

## Quick reference (end)

If the doc has categories or a summary, add:

`HEADING_2` → **Quick Reference — At a Glance** → summary table.

## Footer (centered)

```
Waiz Media | Internal Document | Confidential
```

## Do not use (old team format)

- ASCII underlines (`====`, `----`)
- `At a glance` as plain bullets only (use callout + optional table)
- `Phase N —` for every subheading
- Repo/metadata language

## Related

- [team-doc-translate skill](../../.claude/skills/team-doc-translate/SKILL.md)
- [team-doc-publish-template.md](team-doc-publish-template.md)
- [team-drive-publish.md](../operations/systems/team-drive-publish.md)
