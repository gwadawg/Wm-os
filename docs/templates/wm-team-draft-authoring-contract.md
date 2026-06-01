---
title: WM Team Draft Authoring Contract
domain: templates
owner: operations
status: active
last_updated: 2026-05-29
review_cycle: quarterly
---

# WM Team Draft Authoring Contract

The exact, small markdown vocabulary that a `docs/team-drafts/<slug>.team.md` file may contain.

**This file is the single contract obeyed by both sides:**

- The **author** (Claude, via the [team-doc-author skill](../../.claude/skills/team-doc-author/SKILL.md)) writes ONLY this vocabulary.
- The **renderer** ([scripts/lib/team_doc_formatter.py](../../scripts/lib/team_doc_formatter.py) `render_draft_faithfully`) renders this vocabulary 1:1 to the Google Doc.

Core principle: **nothing appears in the Google Doc unless it is in the draft.** The renderer does zero injection — no auto cover, no auto footer, no surprise callouts.

## Frontmatter (required)

```yaml
---
team_title: "LinkedIn Outreach — Scripts And Angles"   # required
team_role: setter                                       # role key (setter, closer, client_success, operations, all)
team_doc_type: angle_library                            # profile key — see wm-team-doc-profiles.yaml (default: sop)
source_repo_path: "docs/acquisition/outbound/linkedin/copy-angles.md"
approved: false                                         # flipped to true by team-doc-approve.py
cover_title: "LinkedIn Outreach — Scripts And Angles"   # cover stack line 2 (defaults to team_title)
cover_subtitle: "First-touch DMs, bumps, and Gabriel handoff"  # one-line purpose
cover_audience: "Sales & Setting Team  |  Internal Use Only  |  2026"  # audience + internal-use line
footer: "Waiz Media  |  Setter Script Library  |  Internal Use Only  |  2026"  # single footer line
---
```

- Cover and footer come from frontmatter, NOT from body text. Do not write a `WAIZ MEDIA` cover block or footer line in the body.
- If `cover_*` / `footer` are omitted, the renderer falls back to brand defaults derived from `team_role`.

## Body vocabulary

The body begins at the first `# Overview` (or `# 1. Overview`, `# Full Process`). Everything before the first H1 is ignored.

| You write | Renders as |
|-----------|------------|
| `# Section` | HEADING_1 (major section). Leading numbers (`# 1. Overview`) are kept as written. |
| `## Subsection` | HEADING_2 |
| `**Label**` alone on a line | Bold label (navy/black) |
| `> 📌 NORTH STAR` then `> text` | NORTH STAR callout box |
| `> ⚠️ IMPORTANT` + `> text` | IMPORTANT callout box |
| `> 💡 PRO TIP` + `> text` | PRO TIP callout box |
| `> 🚨 CRITICAL` + `> text` | CRITICAL callout box |
| `> 📌 REMEMBER` + `> text` | REMEMBER callout box |
| ` ``` ` fenced block | ✉️ COPY & PASTE box (ready-to-send copy) |
| `\| a \| b \|` table (with `\|---\|` separator row) | Data table (navy header row) |
| `- item` | Bullet |
| `1. item` | Numbered item |
| `[anchor text](https://… or repo/path.md)` | Hyperlink — allowed **everywhere** incl. tables, callouts, paste boxes, bullets |

### Callout rules

- A callout is a blockquote whose first line is a known label (`📌 NORTH STAR`, `⚠️ IMPORTANT`, `💡 PRO TIP`, `🚨 CRITICAL`, `📌 REMEMBER`).
- Keep callouts **sparse**: roughly one intro/principle box per major section — not one per line.
- NORTH STAR is one sentence, max ~220 chars. Use it once, in Overview.

### Link rules (Goal: clean "link here" anchors)

- Always use anchor text: `[Process Guide](process.md)` — never a bare URL pasted into the doc.
- Internal repo links (`process.md`, `docs/...md`) are auto-resolved to the published Google Doc URL via the team publish registry. If the target is not yet published, the renderer keeps the anchor text and the author should append ` (coming soon)`.
- External links use full `https://` URLs.
- De-duplicate links: link a destination once per section, not on every mention.

### Lists vs boxes

- Use `-` / `1.` for lists. **Do not** wrap single-line list items in callouts or paste boxes (that produces the "over-boxing" failure mode).
- Use a paste box only for genuinely copy-pasteable messages.
- Use a data table only for true row/column content (mapping, contrast, index).

## Forbidden in the body

- A `WAIZ MEDIA` cover block or any footer line (these come from frontmatter).
- Bare URLs as visible text.
- Repo-internal scaffolding: `source_document:`, Open Questions, SPINE/inventory links, `---` horizontal rules, ASCII underlines (`====`, `----`).
- Pricing figures — escalate to Gabriel.

## Doc-type profiles

Each `team_doc_type` resolves to a profile in [wm-team-doc-profiles.yaml](wm-team-doc-profiles.yaml) that constrains which of the above elements are expected and sets acceptance thresholds (heading nesting, box density, link caps). See that file and [wm-team-doc-review-checklist.md](wm-team-doc-review-checklist.md).

## Related

- [wm-team-doc-profiles.yaml](wm-team-doc-profiles.yaml) — per-type contract subset + thresholds + exemplars
- [wm-team-doc-format-spec.md](wm-team-doc-format-spec.md) — visual standard (colors, cover, tables)
- [wm-team-angle-unit-template.md](wm-team-angle-unit-template.md) — angle_library unit skeleton
- [wm-team-doc-review-checklist.md](wm-team-doc-review-checklist.md) — pre-publish review gate
