---
name: team-doc-translate
description: Translates canonical Waiz repo Markdown into WM-branded Google Doc layout (cover block, callout tables, heading hierarchy). Use when humanizing SOPs for team Drive, matching the Objection Categories format, or before team-doc-publish.
---

# Team Doc Translate

Turn `docs/` canonical files into **WM team Google Docs** that match the company visual standard.

**Goal:** Remake content for **human operators** (scannable sections, real tables, copy-paste boxes) — not a literal markdown dump for AI.

## Format reference (required)

**Match this document exactly in layout and tone:**

[WM Objection Categories — format reference](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)

Spec: [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md)  
Doc ID: `19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y`

## Cover block (centered, branded)

- **WAIZ MEDIA** — 26pt bold navy
- **Title** — 20pt blue
- **Role | Internal Use Only | Year** — 11pt gray italic
- **Divider** — light blue line under subtitle

## Body layout

| Element | Style |
|---------|--------|
| Major section | `HEADING_1` + navy text |
| Subsection | `HEADING_2` + navy text |
| Field label | Bold 11pt navy |
| NORTH STAR | Shaded single-cell box — **one sentence only**; Who/When as bullets below |
| Other callouts | Same shaded box (IMPORTANT, PRO TIP, REMEMBER) |
| Data tables | Navy header row, white text; bordered body rows |
| Footer | Gray centered confidential line |

## Translation workflow

1. Read canonical file in `docs/`.
2. Apply [TRANSLATION-STANDARDS.md](TRANSLATION-STANDARDS.md) for content rules.
3. Apply [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md) for visual rules.
4. Publish: `python scripts/publish-team-doc.py <path>` (uses `team_doc_formatter.py`).

## Content rules (summary)

- Repo = AI structure; team doc = scannable, design-first.
- At-a-glance → **📌 NORTH STAR** callout table under Overview.
- No ASCII underlines, no repo links, no Open Questions.
- Pricing → escalate to Gabriel.
- Related procedures → hyperlinks to published team Docs only.

## Quality bar

- [ ] Cover matches reference (WAIZ MEDIA + title + role line).
- [ ] At least one callout table where a rule or warning matters.
- [ ] Headings use HEADING_1 / HEADING_2, not plain ALL CAPS.
- [ ] New hire understands what to do within 60 seconds.

## Examples

[examples.md](examples.md) — before/after content. Visual standard is the Objection Categories doc above.

## Related skills

- [team-doc-publish](../team-doc-publish/SKILL.md) — API publish to Drive
- [waiz-business-os](../waiz-business-os/SKILL.md) — canonical repo SOPs only
