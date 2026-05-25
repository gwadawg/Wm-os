---
title: WM Team Doc Format Spec
domain: templates
owner: operations
status: active
last_updated: 2026-05-22
review_cycle: quarterly
---

# WM Team Doc Format Spec

Canonical visual standard for team Google Docs. **Match this layout on every publish.**

## Reference document (copy this look)

- **Live example:** [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)
- **Doc ID:** `19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y`
- **Config:** [config/team-drive-folders.yaml](../../config/team-drive-folders.yaml) → `format_reference_doc_id`
- **Formatter:** `scripts/lib/team_doc_formatter.py` (applies brand colors via Docs API)

## Brand colors (automated on publish)

| Element | Color | Usage |
|---------|--------|--------|
| WM Navy `#1a365d` | rgb(0.10, 0.21, 0.36) | WAIZ MEDIA header, H1/H2, callout label, table header fill |
| WM Blue `#2b6cb0` | rgb(0.17, 0.48, 0.72) | Document title, divider line, table borders |
| WM Gray | rgb(0.45, 0.45, 0.45) | Subtitle line, footer (italic) |
| Callout fill | rgb(0.91, 0.96, 1.0) | NORTH STAR / IMPORTANT boxes |
| White | rgb(1, 1, 1) | Text on navy table headers |

## Cover block (centered)

```
WAIZ MEDIA                    ← 26pt bold navy, centered
[Document Title]              ← 20pt blue, centered
[Role] Team | Internal Use Only | [Year]   ← 11pt gray italic, centered
────────────────────────────  ← light blue border under subtitle
```

Role examples: Sales & Setting, Client Success, Operations, Company.

## Body structure

| Element | Google Docs style | Usage |
|---------|-------------------|--------|
| Major section | `HEADING_1` + navy text | Overview, How To Do It |
| Subsection | `HEADING_2` + navy text | Categories, phases, workflows |
| Field label | Bold 11pt navy | `Before You Start`, `What It Is` |
| Body | 11pt normal text | Short paragraphs, max ~4 lines |
| Lists | Bullets | Who/When meta under Overview — not inside NORTH STAR |

## NORTH STAR callout (single shaded box)

**Not** a 2-column table. Use one full-width cell:

1. Line 1: `📌 NORTH STAR` (bold navy)
2. Blank line
3. **One sentence only** — the core rule or outcome (max ~220 chars)

Who / When / Questions go in **Overview bullets below** the box, not inside NORTH STAR.

## Other callouts

Same shaded box style for ⚠️ IMPORTANT, 💡 PRO TIP, 🚨 CRITICAL, 📌 REMEMBER.

## Data tables

- Header row: **navy background**, **white bold** text
- Body rows: white background, thin blue borders
- 2–4 columns max, short cell text

## Quick reference (end)

`HEADING_2` → **Quick Reference — At a Glance** → summary table (styled headers).

## Footer (centered)

```
Waiz Media | Internal Document | Confidential
```

## Human remake rules (not literal translation)

| Source in repo | Team doc |
|----------------|----------|
| Markdown tables | Styled Google Doc tables |
| `>` message lines | ✉️ COPY & PASTE boxes |
| Playbook `##` sections | Separate H2 sections + Quick Start |
| `---` | Omit |

Operators should never see raw `\| pipes \|` or markdown syntax.

## Do not use

- Plain black 1×2 callout tables with long text in one cell
- Dumping entire playbook into one "How to do it" wall of bullets
- ASCII underlines (`====`, `----`)
- Cramming Who/When/Outcome/Questions into NORTH STAR
- Repo/metadata language in team docs

## Related

- [team-doc-translate skill](../../.claude/skills/team-doc-translate/SKILL.md)
- [team-doc-publish-template.md](team-doc-publish-template.md)
- [team-drive-publish.md](../operations/systems/team-drive-publish.md)
