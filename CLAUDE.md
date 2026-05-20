# Waiz Media OS AI Instructions

This repository is the Waiz Media operating system for future AI use. Treat it as the company memory and operational source of truth.

## How To Work Here

1. Start in `docs/README.md` to understand the repo map.
2. Read `docs/SOURCE-OF-TRUTH.md` and `docs/_inventory/domain-owners.md` before converting or editing canonical docs.
3. Check `docs/_inventory/google-drive-inventory.md` before creating new documents from the raw Drive export.
4. Prefer updating canonical Markdown docs under `docs/` instead of editing raw files under `source-docs/`.
5. Preserve one source of truth per process, policy, KPI, prompt, or playbook.
6. Link related docs instead of duplicating large sections.
7. Use clear metadata, stable lowercase kebab-case filenames, and operational headings.
8. Flag missing owners, triggers, inputs, outputs, metrics, escalation paths, and duplicate docs.
9. Check `docs/_inventory/duplicate-resolutions.md` before converting overlapping source files.

## Important Paths

- `source-docs/waiz-drive-export/`: raw exported Google Drive files. Do not treat these as canonical operating docs.
- `docs/`: AI-ready company knowledge base and operating documentation.
- `docs/_inventory/`: source inventory, classification map, duplicate candidates, and migration backlog.
- `.claude/skills/`: repo-local skills — see [`.claude/skills/README.md`](.claude/skills/README.md) (waiz-business-os + docx + xlsx for migration).
- [AGENTS.md](AGENTS.md): agent entry map.

## Default Documentation Standard

Use the Waiz Business OS skill standards. Durable operating docs should include purpose, scope, owner, trigger, inputs, outputs, process, quality bar, metrics, and related docs when applicable.

Last updated: 2026-05-20
