---
title: Source Of Truth Rules
domain: company
owner: operations
status: active
last_updated: 2026-05-21
review_cycle: quarterly
---

# Source Of Truth Rules

Use this page before creating, moving, or converting any Waiz Media OS document.

## Layers

| Layer | Path | Role |
|-------|------|------|
| Raw export | Sibling repo `waiz-os-archive/waiz-drive-export/` | Frozen evidence from Google Drive. **Never edit.** Never cite as operating instructions once a canonical doc exists. See [raw-export-archive.md](_inventory/raw-export-archive.md). |
| Canonical OS | `docs/` | **Source of truth.** What you and AI create, update, and approve. One source of truth per process, policy, KPI, prompt, or playbook. |
| Migration control | `docs/_inventory/` | Inventory, duplicates, backlog, domain owners, [team publish registry](_inventory/team-publish-registry.yaml). |
| Team publish | Google Drive `Waiz Team SOPs` | **Downstream only.** Layperson-readable copies for team access. Not canonical; edits in Drive do not sync back. Publish via [team-drive-publish.md](operations/systems/team-drive-publish.md). |

## Before You Convert A File

1. Find the row in [google-drive-inventory.md](_inventory/google-drive-inventory.md).
2. Choose one **artifact type**: doctrine, overview, SOP, playbook, sales process, script, KPI, automation spec, prompt, course reference, or archive summary.
3. Check [duplicate-candidates.md](_inventory/duplicate-candidates.md) and [duplicate-resolutions.md](_inventory/duplicate-resolutions.md) (required before ops/MB/constraint conversions).
4. Pick **filename** (kebab-case) and **folder** per [README.md](README.md#folder-structure-approved).
5. Apply layout from [.claude/skills/waiz-business-os/TEMPLATES.md](../.claude/skills/waiz-business-os/TEMPLATES.md).
6. Wire: domain README, migration backlog checkbox, related links.

## Naming

- **Human title** (`title:` in frontmatter): plain English, no `Script --` or `SOP --` prefixes.
- **Filename**: lowercase kebab-case, stable once linked.

| Artifact | Pattern | Example |
|----------|---------|---------|
| Doctrine | `doctrine-{topic}.md` | `doctrine-identity-core-april-26.md` |
| Overview | `overview-{topic}.md` | `overview-money-model-april-26.md` |
| SOP | `{workflow}-sop.md` | `discovery-call-sop.md` |
| Playbook | `{topic}-playbook.md` | `setter-daily-operations-playbook.md` |
| Script | `script-{call}.md` | `script-demo-call.md` |
| KPI | `{metric}-kpi.md` | `setter-show-rate-kpi.md` |
| Automation | `{system}-automation-spec.md` | `wm-ai-bot-automation-spec.md` |

Fix typos in canonical names (`infrastructure` not `infrustructure`). Do not copy Drive punctuation, emoji, or trailing underscores into filenames.

## Merge Rules

- **One concept → one canonical file.** If two sources overlap, merge content and list both under `source_document` or a "Superseded sources" section.
- **Do not** create a second canonical doc for the same workflow in another folder.
- **Link, don't copy:** company DNA (identity, money model, brand) lives in [company/](company/). Other docs link to it instead of repeating blocks.
- **Pricing:** never invent numbers. Reference the live pricing sheet; pricing is founder-only per [overview-money-model-april-26.md](company/overview-money-model-april-26.md).

## Status Lifecycle

| Status | Meaning |
|--------|---------|
| `draft` | Converted; needs human review before team use. |
| `active` | Approved operating truth. |
| `deprecated` | Replaced; keep file with link to successor or move summary to [archive/](archive/). |

## What Stays Raw

| Type | Action |
|------|--------|
| `.docx` operating docs | Convert to `docs/` when `convert-first` or approved |
| `.xlsx` trackers | KPI/summary Markdown + keep spreadsheet in `waiz-os-archive/waiz-drive-export/` |
| `.pptx`, `.mp4`, `.png`, `.pdf` | Keep raw; optional short reference doc |
| Drive `Archive/` and old MASTER docs | Archive summary only after canonical replacement exists |
| Skool course material | Convert last; often duplicate internal SOPs |

## Team Publish Rules

- Publish only after repo doc is `status: active` (unless explicit `--force`).
- Register every published file in `team-publish-registry.yaml` before first publish.
- Repo wins on conflict: re-publish overwrites the team Doc body.
- Do not mirror the old `Waiz Media OS` Drive export tree; use role-based team folders only.

## Related Docs

- [Team Drive Publish SOP](operations/systems/team-drive-publish.md)
- [Waiz Media OS README](README.md)
- [Operating Map](OPERATING-MAP.md)
- [Domain Owners](_inventory/domain-owners.md)
- [Migration Backlog](_inventory/migration-backlog.md)
