---
title: WM Team Doc Format Spec
domain: templates
owner: operations
status: active
last_updated: 2026-05-27
review_cycle: quarterly
---

# WM Team Doc Format Spec

Canonical visual standard for team Google Docs. **Match this layout on every publish.**

## Reference document (copy this look)

- **Live example:** [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)
- **Doc ID:** `19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y`
- **Config:** [config/team-drive-folders.yaml](../../config/team-drive-folders.yaml) → `format_reference_doc_id`
- **Pandoc reference (preferred):** [wm-team-reference.docx](wm-team-reference.docx) — copy of Objection Categories; Pandoc applies Heading1/2/Normal and table styles on publish
- **API formatter (fallback):** `scripts/lib/team_doc_formatter.py` (Docs API rgbColor when DOCX path fails)

## Publish pipeline (default: template)

1. **Prepare** — `python scripts/team-doc-prepare.py docs/.../sop.md` → human draft under `docs/team-drafts/`
2. **Approve** — `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md`
3. **Publish** — `python scripts/publish-team-doc.py docs/.../sop.md` → **copy** live [Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit) Google Doc as template, write content with native H1/H2 styles (blue left bar — same as Claude-on-web).

Fallback: DOCX (Pandoc) → API formatter. Pandoc alone does not fully replicate Claude web layout.

Body text must be readable **black** in the final Google Doc.


## Layout patterns from recent WM docs

These patterns are extracted from:

- `/Users/gwadawg/Desktop/WM Sales Intelligence Bible.pdf`
- `/Users/gwadawg/Desktop/WM _ ICP Document.pdf`
- `/Users/gwadawg/Desktop/WM Sales Objection Doctorine.pdf`

Use these as the default design language for future team docs.

### 1) Cover stack

1. `WAIZ MEDIA` (or `WAIZ MEDIA — INTERNAL REFERENCE` for references)
2. Clear doc title
3. One-line purpose / subtitle
4. Audience + internal-use line (`Internal Use Only | Team | Month Year`)

### 2) Section architecture

- Use numbered major sections for training/SOP docs (`1.`, `2.`, `3.`).
- Use clear role headers: `CONTEXT`, `Profile`, `Pain Points`, `How to Position / Speak to Them`, `Objection & Reframe`, `Key Phrases`.
- Prefer short explanatory paragraphs followed by actionable bullets.

### 3) Signature table patterns

- **Contrast table:** `WHAT THEY SAY` vs `WHAT'S ACTUALLY TRUE`
- **Map table:** `Step` / `Type` / `When to Use` / `What It Means` / `Sample Language`
- **Category table:** `Avatar` / `Core Problem` / `Urgency`

### 4) Callout hierarchy

Use emoji-prefixed labels exactly like the doctrine docs:

- `📌` rule / doctrine / important principle
- `💡` tactical spotting or coaching cue
- `🚨` critical warning or distinction
- `⭐` standard / mastery expectation

Callouts should be short, high-signal, and immediately usable in a live call or training context.

### 5) Voice + readability

- Assertive, operator-facing tone (clear standards, no fluff).
- Use concrete language over generic business language.
- Keep paragraphs compact; avoid long walls of prose.
- End sections with practical anchors (checklist, key phrases, or action prompt).

### 6) Footer convention

Use a consistent footer line where applicable:

`Waiz Media | [Doc Family] | Internal Use Only | [Month Year]`

For doctrine/SOP docs, `Waiz Media | [Doc Name] | Internal Document | Confidential` is also valid.

## Brand colors (API fallback only)

| Element | Color | Usage |
|---------|--------|--------|
| WM Navy `#1a365d` | rgb(0.10, 0.21, 0.36) | WAIZ MEDIA header, H1/H2, callout label, table header fill |
| WM Blue `#2b6cb0` | rgb(0.17, 0.48, 0.72) | Document title, divider line, table borders |
| WM Gray | rgb(0.45, 0.45, 0.45) | Subtitle line, footer (italic) |
| WM Black | rgb(0, 0, 0) | **All body copy** — paragraphs, bullets, callout body, template messages, table body rows |
| Callout fill | rgb(0.91, 0.96, 1.0) | NORTH STAR / IMPORTANT boxes |
| White | rgb(1, 1, 1) | **Header row text only** on navy table headers — never body copy |

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
| Body | 11pt **black** normal text | Short paragraphs, max ~4 lines |
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

- Header row: **navy background**, **white bold** text (headers only)
- Body rows: **black** text, white background, thin blue borders
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

## Doc-type extensions

Use these only when the doc matches the type — do not add to generic SOPs.

| Doc type | Template | Review |
|----------|----------|--------|
| Angle / script library | [wm-team-angle-unit-template.md](wm-team-angle-unit-template.md) | [wm-team-doc-review-checklist.md](wm-team-doc-review-checklist.md) Pass 2 |
| All team publishes | — | [wm-team-doc-review-checklist.md](wm-team-doc-review-checklist.md) Pass 1 + 3 |

Registry: optional `team_doc_type: angle_library` on the publish row enables approve/publish validation.

## Related

- [wm-team-draft-authoring-contract.md](wm-team-draft-authoring-contract.md) — exact markdown vocabulary (single source for author + renderer)
- [wm-team-doc-profiles.yaml](wm-team-doc-profiles.yaml) — per-type contract subset + thresholds + exemplars
- [team-doc-author skill](../../.claude/skills/team-doc-author/SKILL.md) — default authoring step
- [team-doc-translate skill](../../.claude/skills/team-doc-translate/SKILL.md) — legacy scaffold
- [team-doc-publish-template.md](team-doc-publish-template.md)
- [team-drive-publish.md](../operations/systems/team-drive-publish.md)
