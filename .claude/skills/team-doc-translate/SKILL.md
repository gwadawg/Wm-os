---
name: team-doc-translate
description: Translates canonical Waiz repo Markdown into WM-branded Google Doc layout (cover block, callout tables, heading hierarchy). Use when humanizing SOPs for team Drive, matching the Objection Categories format, or before team-doc-publish.
---

# Team Doc Translate

Turn `docs/` canonical files into **WM team Google Docs** that match the company visual standard.

## Format reference (required)

**Match this document exactly in layout and tone:**

[WM Objection Categories — format reference](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)

Spec: [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md)  
Doc ID: `19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y`

## Cover block (centered)

```
WAIZ MEDIA                         26pt bold
[Document Title]                   20pt
[Role] Team | Internal Use Only | [Year]   11pt
```

## Body layout

| Element | Style |
|---------|--------|
| Major section | `HEADING_1` — e.g. Overview, How To Do It |
| Subsection | `HEADING_2` — e.g. category, phase, Done Right Looks Like |
| Field label | Bold line — What It Is, How to Identify It, How to Handle It |
| Callout | 1×2 table — 📌 NORTH STAR, ⚠️ IMPORTANT, 💡 PRO TIP, 🚨 CRITICAL, 📌 REMEMBER |
| Lists | Bullets, short lines |
| Data tables | Header row + rows (categories, steps, quick reference) |
| Footer | `Waiz Media | Internal Document | Confidential` centered |

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
