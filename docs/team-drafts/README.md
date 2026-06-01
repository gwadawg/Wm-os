# Team publish drafts

Human-facing markdown for Google Drive publish. **Not canonical** — source of truth stays in `docs/`.

## Workflow

1. **Author** the `*.team.md` per [team-doc-author](../../.claude/skills/team-doc-author/SKILL.md) — rewrite canonical for readability using the [authoring contract](../templates/wm-team-draft-authoring-contract.md) and the doc's [profile](../templates/wm-team-doc-profiles.yaml). (`python scripts/team-doc-prepare.py docs/path/to/canonical.md` is an optional rough scaffold.)
2. Review against [wm-team-doc-review-checklist.md](../templates/wm-team-doc-review-checklist.md) (angle libraries also use [wm-team-angle-unit-template.md](../templates/wm-team-angle-unit-template.md)).
3. `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md --check-only` (contract + profile gate).
4. `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md`
5. `python scripts/publish-team-doc.py docs/path/to/canonical.md` (faithful render — Google Doc matches the draft 1:1).

Each draft has a sidecar `*.team.meta.yaml` with `approved`, `source_repo_path`, optional `team_doc_type` (e.g. `angle_library`), and publish metadata. Cover/footer live in the draft frontmatter (`cover_title`, `cover_subtitle`, `cover_audience`, `footer`).
