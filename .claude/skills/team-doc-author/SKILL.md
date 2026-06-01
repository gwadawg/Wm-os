---
name: team-doc-author
description: Rewrite a canonical Waiz repo doc into a publish-ready team draft (docs/team-drafts/<slug>.team.md) for Google Drive. Use when preparing or refreshing a team Google Doc, when the user says publish to Drive / team docs, or when a published doc reads like slop. This is the readability rewrite step — the publish script then renders the draft 1:1.
---

# Team Doc Author

You (the agent) are the rewrite step. Turn a canonical `docs/` file into a **digestible, scannable team draft** that the deterministic publisher renders to Google Docs exactly as written.

**Source of truth stays in `docs/`. The draft is the single source of VISUAL truth.** The renderer does zero injection — whatever you write is exactly what the team sees.

## Read first (every time)

1. The canonical doc you are converting.
2. [Authoring contract](../../docs/templates/wm-team-draft-authoring-contract.md) — the exact markdown vocabulary you may use.
3. [Doc-type profiles](../../docs/templates/wm-team-doc-profiles.yaml) — find the profile for this doc's `team_doc_type` (registry / meta). It lists allowed elements, thresholds, and good/bad exemplar doc IDs.
4. [Format spec](../../docs/templates/wm-team-doc-format-spec.md) and, for `angle_library`/`playbook`, [angle unit template](../../docs/templates/wm-team-angle-unit-template.md).

## Workflow

1. **Determine the profile.** Read `team_doc_type` from the registry row / `*.team.meta.yaml`. Default `sop`. Aliases: `angle_library`/`script_library` -> `playbook`, `doctrine` -> `reference`.
2. **Scaffold (optional).** `python scripts/team-doc-prepare.py docs/.../doc.md` gives a rough starting point. It is a draft only — you must rewrite it.
3. **Rewrite for humans.** Produce `docs/team-drafts/<slug>.team.md` per the contract + profile.
4. **Self-check** against the profile thresholds and the [review checklist](../../docs/templates/wm-team-doc-review-checklist.md).
5. **Validate:** `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md --check-only`. Fix every error.
6. **Approve + publish:** see [team-doc-publish](../team-doc-publish/SKILL.md).

## How to rewrite (match GOOD, avoid BAD)

The good exemplars (WM Objection Categories, WM Sales Objection Doctrine) and the failure modes are encoded as thresholds. Concretely:

- **Real hierarchy.** Numbered H1 for major sections, H2 for subsections. Never a wall of all-H1. (BAD-1 = 17 H1 / 0 H2.)
- **Sparse boxes.** Roughly one principle/intro callout per major section. Do not wrap every snippet in a box. Aim for >=~300 chars of real content per box. (BAD-2 = 34 tiny tables.)
- **Lists are bullets.** Use `-` / `1.` for steps and lists — never one-line boxes pretending to be a list. (Both bad docs had 0 bullets.)
- **Links are anchor text.** Always `[descriptive text](url)` — never a bare URL in the body. Resolve related repo docs to their published Drive URL via the registry; if unpublished, write the anchor text + ` (coming soon)`. De-duplicate: link a destination once per section. (BAD-1 = 42 links.)
- **Tables for true row/column content.** Mapping, contrast (`WHAT THEY SAY` vs `WHAT'S TRUE`), index. 2-4 columns, short cells. Links inside cells are allowed and will render clickable.
- **Plain operator voice.** Short sentences. Concrete words. No fluff, no repo metadata, no Open Questions, no ASCII rules.

## Frontmatter you must fill

```yaml
---
team_title: "..."
team_role: setter            # setter | closer | client_success | operations | all
team_doc_type: sop           # profile key (see profiles.yaml)
source_repo_path: "docs/.../doc.md"
approved: false
cover_title: "..."           # cover line 2 (defaults to team_title)
cover_subtitle: "one-line purpose"
cover_audience: "Sales & Setting Team  |  Internal Use Only  |  2026"
footer: "Waiz Media  |  <Doc Family>  |  Internal Use Only  |  2026"
---
```

Cover and footer come ONLY from frontmatter. Do not write a `WAIZ MEDIA` block or footer line in the body.

## Quality bar

- [ ] `--check-only` passes (contract + profile thresholds + angle units if playbook).
- [ ] Reads cleanly top to bottom; a new hire knows what to do in 60 seconds.
- [ ] Every link is anchor text and points somewhere real.
- [ ] No surprise content will appear — the draft is exactly the doc.

## Related

- [team-doc-publish](../team-doc-publish/SKILL.md) — render + publish the approved draft
- [team-doc-translate](../team-doc-translate/SKILL.md) — legacy heuristic scaffold (now optional)
- [waiz-business-os](../waiz-business-os/SKILL.md) — canonical repo SOPs only
