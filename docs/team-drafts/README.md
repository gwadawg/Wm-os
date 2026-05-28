# Team publish drafts

Human-facing markdown for Google Drive publish. **Not canonical** — source of truth stays in `docs/`.

## Workflow

1. `python scripts/team-doc-prepare.py docs/path/to/canonical.md`
2. Edit the generated `*.team.md` for operators (scannable sections, tables, copy-paste blocks).
3. Review against [wm-team-doc-review-checklist.md](../templates/wm-team-doc-review-checklist.md) (angle libraries also use [wm-team-angle-unit-template.md](../templates/wm-team-angle-unit-template.md)).
4. `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md --check-only` (optional gate before approve).
5. `python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md`
6. `python scripts/publish-team-doc.py docs/path/to/canonical.md`

Each draft has a sidecar `*.team.meta.yaml` with `approved`, `source_repo_path`, optional `team_doc_type` (e.g. `angle_library`), and publish metadata.
