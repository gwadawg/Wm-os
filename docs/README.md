---
title: Waiz Media OS
domain: company
owner: operations
status: active
last_updated: 2026-05-20
review_cycle: weekly
---

# Waiz Media OS

This is the AI-ready operating system for Waiz Media. It turns company knowledge, SOPs, workflows, prompts, KPIs, onboarding systems, sales processes, media buying systems, client success systems, and operational intelligence into a maintainable GitHub repository.

## Start Here By Role

| Role | Load first |
|------|------------|
| Anyone / AI | [Approved Operating Spine](SPINE.md) → [Company](company/README.md) |
| Setter | [Sales Operating Hub](acquisition/sales/README.md) — intro qualify through show rate |
| Closer | [Sales Operating Hub](acquisition/sales/README.md) — discovery, demo, [Objection Hub](acquisition/sales/objection-handling-hub.md) |
| Client success | [Constraint Troubleshooting](client-fulfillment/client-success/constraint-troubleshooting-sop.md), [KPI standards](client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md) |
| Ops | [OPS Priority Ladder](operations/systems/ops-manager-priority-ladder.md), [Operations](operations/README.md) |
| Migrating docs | [Drive inventory](_inventory/google-drive-inventory.md), [Migration backlog](_inventory/migration-backlog.md) |

**Superseded Drive files:** [archive/superseded-sources.md](archive/superseded-sources.md) — do not use raw `Archive/` copies for operations.

## Repo Layers

- `source-docs/waiz-drive-export/`: raw Google Drive export. Preserve this as source material.
- `docs/`: cleaned, canonical, AI-readable operating system.
- `docs/_inventory/`: import inventory, classification summaries, duplicate candidates, and migration backlog.
- `.claude/skills/`: agent skills — [index](../.claude/skills/README.md) (`waiz-business-os`, `docx`, `xlsx`).
- [AGENTS.md](../AGENTS.md): short map for coding agents.

## Folder Structure (Approved)

Top-level domains stay as listed below. Add **subfolders only as canonical docs are converted**—do not mirror the raw Drive tree.

| Domain | Subfolders |
|--------|------------|
| [Company](company/README.md) | Flat (doctrines, overviews) |
| [Acquisition](acquisition/README.md) | `sales/`, `marketing/`, `intelligence/`, `offer/` |
| [Operations](operations/README.md) | `people/`, `hiring/`, `systems/`, `reporting/` |
| [Client Fulfillment](client-fulfillment/README.md) | `onboarding/`, `client-success/`, `media-buying/`, `crm-architecture/`, `reverse-mortgage-dna/`, `course-material/` |
| [Automations](automations/README.md) | `crm/`, `ai-bots/`, `reporting/`, `sales/` |
| [Prompts](prompts/README.md) | Mirror operating domain |
| [KPIs](kpis/README.md) | Mirror operating domain |
| [Templates](templates/README.md) | Reusable doc shells |
| [Archive](archive/README.md) | Superseded canonical summaries |

**Acquisition stays one top-level domain** (sales + marketing together). See [SOURCE-OF-TRUTH.md](SOURCE-OF-TRUTH.md) and [Operating Map](OPERATING-MAP.md).

## Operating Domains

- [Company](company/README.md): identity, money model, brand, principles, company-level doctrine.
- [Acquisition](acquisition/README.md): offer, sales, marketing, lead stages, buyer intelligence, scripts.
- [Operations](operations/README.md): software stack, reporting systems, team responsibilities, internal operating cadence.
- [Client Fulfillment](client-fulfillment/README.md): client delivery, onboarding, media buying, client success, course material, reverse mortgage knowledge.
- [Automations](automations/README.md): automation specs, CRM architecture, AI bots, data flows.
- [Prompts](prompts/README.md): reusable AI prompts for operating workflows.
- [KPIs](kpis/README.md): metric definitions, reporting cadence, scorecards.
- [Templates](templates/README.md): reusable document and workflow templates.
- [Archive](archive/README.md): deprecated or historical docs.

## Current Migration Status

The first inventory has been generated from the exported Google Drive folder. Start here:

- [Google Drive Inventory](_inventory/google-drive-inventory.md)
- [Classification Summary](_inventory/classification-summary.md)
- [Duplicate Candidates](_inventory/duplicate-candidates.md)
- [Migration Backlog](_inventory/migration-backlog.md)
- [Approved Operating Spine](SPINE.md)
- [Source Of Truth Rules](SOURCE-OF-TRUTH.md)
- [Domain Owners](_inventory/domain-owners.md)
- [Repository Conventions](repo-conventions.md) (from Drive export; review vs `CLAUDE.md`)

## Rule Of Thumb

If a document tells Waiz Media how to operate, convert it into a canonical Markdown doc under `docs/`. If a file is a raw export, spreadsheet, deck, or asset, keep it in `source-docs/` and summarize/link to it from `docs/`.
