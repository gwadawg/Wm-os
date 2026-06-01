---
name: team-doc-translate
description: Translates canonical Waiz repo Markdown into WM-branded team drafts for Google Drive template publish. Use when humanizing SOPs for team Drive, matching the Objection Categories format, or before team-doc-publish.
---

# Team Doc Translate

> **Default authoring is now [team-doc-author](../team-doc-author/SKILL.md)** — an agent rewrite that follows the [authoring contract](../../docs/templates/wm-team-draft-authoring-contract.md) and the matching [doc-type profile](../../docs/templates/wm-team-doc-profiles.yaml), then publishes via the faithful renderer (the Google Doc matches the draft 1:1). Use the steps below only for the optional heuristic scaffold (`team-doc-prepare.py`), then rewrite by hand per the author skill.

Turn `docs/` canonical files into **WM team drafts** (`docs/team-drafts/`) that match the company visual standard when published.

**Goal:** Remake content for **human operators** (scannable sections, real tables, copy-paste boxes) — not a literal markdown dump for AI.

**Output target:** `docs/team-drafts/<slug>.team.md` — approve before publish.

## Format reference (required)

[WM Objection Categories — format reference](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)

- Spec: [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md)
- Pandoc template: [wm-team-reference.docx](../../docs/templates/wm-team-reference.docx)
- Gold mock: [wm-team-doc-human-example.md](../../docs/templates/wm-team-doc-human-example.md)

## Workflow

1. `python scripts/team-doc-prepare.py docs/path/to/canonical.md` — scaffold draft
2. Edit draft per [TRANSLATION-STANDARDS.md](TRANSLATION-STANDARDS.md) and format spec
3. **Review pass** — [wm-team-doc-review-checklist.md](../../docs/templates/wm-team-doc-review-checklist.md); fix all violations before approve
4. `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md --check-only` then approve
5. [team-doc-publish](../team-doc-publish/SKILL.md) runs template-copy publish (Objection Categories styles)

## Angle / script libraries (`team_doc_type: angle_library`)

Use the rigid unit in [wm-team-angle-unit-template.md](../../docs/templates/wm-team-angle-unit-template.md) for **every** angle. Do not vary section labels or order per angle. Obey the **FORBIDDEN** table in that doc.

Set `team_doc_type: angle_library` in registry + `*.team.meta.yaml` for copy-angles-style docs. Approve/publish will reject inconsistent angles.

## Draft markdown conventions (WM doctrine style)

- Cover stack: `WAIZ MEDIA` (or `WAIZ MEDIA — INTERNAL REFERENCE`) → title → one-line purpose → internal-use line
- Start with `# Overview` then one doctrine callout (`📌 NORTH STAR`, `📌 WHAT THIS DOCUMENT IS`, or equivalent)
- Use numbered major sections when instructional (`1.`, `2.`, `3.`)
- Include role headers where relevant: `CONTEXT`, `Pain Points`, `How to Position / Speak to Them`, `Objection & Reframe`, `Key Phrases`
- Use contrast and mapping tables heavily:
  - `WHAT THEY SAY` vs `WHAT'S ACTUALLY TRUE`
  - `Step/Type` vs `What It Means` / `When to Use`
  - `Avatar` / `Core Problem` / `Urgency`
- Keep copy blocks as `**✉️ COPY & PASTE**` + fenced code block
- Footer: `Waiz Media | <Doc Family> | Internal Use Only | <Month Year>` (or `Internal Document | Confidential` for SOP/doctrine)

## Body layout (in Google Doc after publish)

| Element | Style |
|---------|--------|
| Major section | Heading 1 |
| Subsection | Heading 2 |
| NORTH STAR | Blockquote / shaded box |
| Data tables | Navy header (from reference DOCX) |
| Body | Black readable text |


## Required callout set

Use doctrine callouts consistently:

- `📌` rule/principle
- `💡` spotting cue or coaching tactic
- `🚨` critical distinction / mistake to avoid
- `⭐` performance standard / mastery bar

At least one `📌` and one `🚨` or `💡` callout should appear in every training-heavy doc.

## Content rules (summary)

- Repo = AI structure; team doc = scannable, design-first.
- No ASCII underlines, no repo links, no Open Questions.
- Pricing → escalate to Gabriel.
- Related procedures → hyperlinks to published team Docs only.

## Quality bar

- [ ] Cover matches reference (WAIZ MEDIA + title + role line).
- [ ] At least one NORTH STAR or IMPORTANT callout where a rule matters.
- [ ] New hire understands what to do within 60 seconds.
- [ ] Draft approved before publish.

## Related skills

- [team-doc-publish](../team-doc-publish/SKILL.md) — template copy publish to Drive
- [waiz-business-os](../waiz-business-os/SKILL.md) — canonical repo SOPs only
