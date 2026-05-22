---
name: team-doc-publish
description: Publish canonical repo docs to team Google Drive as layperson-readable Google Docs. One-way only — GitHub docs/ is source of truth. Use after creating or updating SOPs when the user wants team access, or when they say publish to Drive, team docs, or Google Drive.
---

# Team Doc Publish

## Mandate

- **Source of truth:** `docs/` in this repo only.
- **Team output:** Google Drive folder `Waiz Team SOPs` — readable copies, not canonical.
- **Never** sync Drive edits back into the repo.
- **Never** treat old `source-docs/waiz-drive-export/` or legacy Drive trees as publish sources.

## After creating or updating a canonical SOP

Ask verbatim:

> This SOP is updated in the repo (`status: …`). Do you want to publish a team-friendly version to Google Drive now? (yes / skip / publish later)

If **yes**:

1. Confirm [team-publish-registry.yaml](../../docs/_inventory/team-publish-registry.yaml) has a row for the file (`publish_status: active`, correct `drive_folder`).
2. Confirm `status: active` in repo frontmatter (or user approved `--force`).
3. Run publish (credentials in `config/team-publish.local.yaml` or `GOOGLE_APPLICATION_CREDENTIALS`):

```bash
pip install -r scripts/requirements-publish.txt
python scripts/verify-team-drive-access.py
python scripts/publish-team-doc.py docs/path/to/doc.md
```

Service account (share team folder with this email): `claude-drive-access@rugged-nucleus-383418.iam.gserviceaccount.com`

4. Return the Google Doc URL from script output.
5. If related docs were not published yet, note that links show “(coming soon)” until those docs are published.

## Registry and folders

| File | Purpose |
|------|---------|
| [team-publish-registry.yaml](../../docs/_inventory/team-publish-registry.yaml) | repo path ↔ `google_doc_id` |
| [team-drive-folders.yaml](../../config/team-drive-folders.yaml) | Role folder IDs |
| [team-drive-publish.md](../../docs/operations/systems/team-drive-publish.md) | Full setup and commands |

**Drive folders (team-facing):** `00 - Start Here`, `01 - Company Basics`, `02 - Setters`, `03 - Closers`, `04 - Client Success`, `05 - Operations`, `99 - Archive`.

## Commands

```bash
# First-time folder creation (after root_folder_id is set)
python scripts/bootstrap-team-drive.py

# One doc
python scripts/publish-team-doc.py docs/acquisition/sales/setter-daily-operations-playbook.md

# All registry entries without google_doc_id
python scripts/publish-team-doc.py --spine

# Republish everything active
python scripts/publish-team-doc.py --spine --update-all

# Start Here index
python scripts/publish-team-doc.py --start-here

# Archive copy before overwrite
python scripts/publish-team-doc.py docs/path/to/doc.md --archive
```

## Translator rules

Apply [team-doc-translate](../team-doc-translate/SKILL.md) **before** publish — design-focused, scannable team copy (not AI repo structure).

- Template: [team-doc-publish-template.md](../../docs/templates/team-doc-publish-template.md)
- Code: `scripts/lib/team_doc_translator.py`
- Strip frontmatter, Open Questions, migration paths
- Rewrite `## Related Docs` to hyperlinks when targets have `google_doc_id` in registry
- Pricing-sensitive docs: no dollar amounts — escalate to Gabriel
- After improving translation rules, republish with `--force` so Drive matches

## Adding a new publishable doc

1. Create or update canonical Markdown under `docs/`.
2. Set `status: active` when approved.
3. Add registry entry with `team_title`, `drive_folder`, `team_role`.
4. Ask publish question → run `publish-team-doc.py`.

## Related skills

- [team-doc-translate](../team-doc-translate/SKILL.md) — humanize and design team-facing copy
- [waiz-business-os](../waiz-business-os/SKILL.md) — structure and SOP templates
- [docx](../docx/SKILL.md) — legacy export conversion only (not team publish)
