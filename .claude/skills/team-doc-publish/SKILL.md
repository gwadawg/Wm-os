---
name: team-doc-publish
description: Publish canonical repo docs to team Google Drive as layperson-readable Google Docs. One-way only — GitHub docs/ is source of truth. Use after creating or updating SOPs when the user wants team access, or when they say publish to Drive, team docs, or Google Drive.
---

# Team Doc Publish

## Mandate

- **Source of truth:** `docs/` in this repo only.
- **Team output:** Google Drive folder `Waiz Team SOPs` — readable copies, not canonical.
- **Never** sync Drive edits back into the repo.
- **Never** treat `waiz-os-archive/waiz-drive-export/` or legacy Drive trees as publish sources.

## Default pipeline: Google Doc template (matches Claude web layout)

1. **Prepare** — scaffold human draft from canonical markdown
2. **Edit + approve** — operator-ready copy in `docs/team-drafts/`
3. **Publish** — **Copy** [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit) as a new Google Doc, clear body, write content using the template’s native heading styles (blue left bar on H1/H2).

Fallback order: template → DOCX (Pandoc) → API formatter.

Pandoc/DOCX does **not** match Claude-on-web formatting as well as the template copy path.

**Requires:** Pandoc (`python scripts/setup-pandoc.py` or `brew install pandoc`), reference DOCX in repo, approved draft when `require_approved_draft: true` in config.

## After creating or updating a canonical SOP

Ask verbatim:

> This SOP is updated in the repo (`status: …`). Do you want to **prepare a team draft** for Google Drive? (prepare / skip / later)

If preparing or publishing:

1. Confirm [team-publish-registry.yaml](../../docs/_inventory/team-publish-registry.yaml) has a row (`publish_status: active`, correct `drive_folder`).
2. Confirm `status: active` in repo frontmatter (or `--force`).

```bash
pip install -r scripts/requirements-publish.txt
python scripts/verify-team-drive-access.py

# Step 1–2: draft
python scripts/team-doc-prepare.py docs/path/to/doc.md
# Edit docs/team-drafts/<slug>.team.md, then:
python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md

# Step 3: publish (template default)
python scripts/publish-team-doc.py docs/path/to/doc.md
```

Or combined prepare flag:

```bash
python scripts/publish-team-doc.py docs/path/to/doc.md --prepare
```

Service account: `claude-drive-access@rugged-nucleus-383418.iam.gserviceaccount.com`


## Layout quality gate (before publish)

Run [wm-team-doc-review-checklist.md](../../docs/templates/wm-team-doc-review-checklist.md) on the draft. For angle libraries, also enforce [wm-team-angle-unit-template.md](../../docs/templates/wm-team-angle-unit-template.md).

```bash
python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md --check-only
```

Automated checks (overview, angle units, duplicate footer, etc.) run on approve and publish. Fix violations in the draft file — not in Google Docs after publish.

## Commands

```bash
python scripts/team-doc-prepare.py docs/path/to/doc.md
python scripts/team-doc-approve.py docs/team-drafts/<slug>.team.md
python scripts/publish-team-doc.py docs/path/to/doc.md
python scripts/publish-team-doc.py docs/path/to/doc.md --pipeline api   # force API only
python scripts/publish-team-doc.py docs/path/to/doc.md --archive
python scripts/publish-team-doc.py --spine --update-all
```

## Config

| File | Purpose |
|------|---------|
| [team-publish.local.example.yaml](../../config/team-publish.local.example.yaml) | `default_publish_pipeline`, `reference_docx`, `require_approved_draft` |
| [wm-team-reference.docx](../../docs/templates/wm-team-reference.docx) | Pandoc style template (Objection Categories) |
| [team-drive-publish.md](../../docs/operations/systems/team-drive-publish.md) | Full runbook |

## Translator rules

Apply [team-doc-translate](../team-doc-translate/SKILL.md) when editing the **team draft** (not when publishing raw canonical md).

- Spec: [wm-team-doc-format-spec.md](../../docs/templates/wm-team-doc-format-spec.md)
- Draft output: `docs/team-drafts/*.team.md`
- API fallback formatter: `scripts/lib/team_doc_formatter.py`

## Related skills

- [team-doc-translate](../team-doc-translate/SKILL.md) — humanize team draft content
- [waiz-business-os](../waiz-business-os/SKILL.md) — canonical repo SOPs
- [docx](../docx/SKILL.md) — reference template maintenance
