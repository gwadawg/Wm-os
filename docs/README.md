---
title: Waiz Media OS
domain: company
owner: operations
status: active
last_updated: 2026-05-28
review_cycle: weekly
---

# Waiz Media OS

This is the AI-ready operating system for Waiz Media. It turns company knowledge, SOPs, workflows, prompts, KPIs, onboarding systems, sales processes, media buying systems, client success systems, and operational intelligence into a maintainable GitHub repository.

## Updating This Repo

Edit files in `docs/`, save, then **Commit** and **Push** in GitHub Desktop (or Cursor Source Control). Large videos (`.mp4`) stay local — see `.gitignore`.

## Start Here By Role

| Role | Load first |
|------|------------|
| Anyone / AI | [Approved Operating Spine](SPINE.md) → [Company](company/README.md) |
| Setter | [Sales Operating Hub](acquisition/sales/README.md) — intro qualify through show rate; pre-call videos: [objection video assets](acquisition/marketing/pre-call-objection-videos.md) |
| Closer | [Sales Operating Hub](acquisition/sales/README.md) — discovery, demo, [Objection Hub](acquisition/sales/objection-handling-hub.md), [pre-call videos](acquisition/marketing/pre-call-objection-videos.md) |
| Client success | [Fulfillment Operating System](client-fulfillment/fulfillment-operating-system.md) → [Client success hub](client-fulfillment/client-success/README.md) |
| Media buyer | [Fulfillment OS](client-fulfillment/fulfillment-operating-system.md), [Media buying](client-fulfillment/media-buying/README.md), [Client marketing](client-fulfillment/client-marketing/README.md) |
| Ops | [OPS Priority Ladder](operations/systems/ops-manager-priority-ladder.md), [Operations](operations/README.md) |
| Migrating docs | [Drive inventory](_inventory/google-drive-inventory.md), [Migration backlog](_inventory/migration-backlog.md) |

**Superseded Drive files:** [archive/superseded-sources.md](archive/superseded-sources.md) — do not use raw `Archive/` copies for operations.

## Team access (Google Drive)

GitHub `docs/` is the **source of truth**. The shared Drive library `Waiz Team SOPs` holds one-way, team-friendly copies — publish on demand, not sync. See [Team Google Drive Publish](operations/systems/team-drive-publish.md) and [team-publish-registry.yaml](_inventory/team-publish-registry.yaml).

## Repo Layers

- **waiz-os-archive** (sibling repo): raw Google Drive export — [setup](_inventory/raw-export-archive.md). Not in this repo (keeps clones small).
- `docs/`: cleaned, canonical, AI-readable operating system.
- `docs/_inventory/`: import inventory, classification summaries, duplicate candidates, and migration backlog.
- `.claude/skills/`: agent skills — [index](../.claude/skills/README.md) (`waiz-business-os`, `docx`, `xlsx`, `team-doc-publish`).
- [AGENTS.md](../AGENTS.md): short map for coding agents.

## Folder Structure (Approved)

Top-level domains stay as listed below. Add **subfolders only as canonical docs are converted**—do not mirror the raw Drive tree.

| Domain | Subfolders |
|--------|------------|
| [Company](company/README.md) | Flat (doctrines, overviews) |
| [Acquisition](acquisition/README.md) | `sales/`, `outbound/`, `marketing/`, `intelligence/`, `offer/` |
| [Operations](operations/README.md) | `people/`, `hiring/`, `systems/`, `reporting/` |
| [Client Fulfillment](client-fulfillment/README.md) | `infrastructure/`, `client-marketing/`, `media-buying/`, `onboarding/`, `client-success/`, `crm-architecture/`, `reverse-mortgage-dna/`, `course-material/` — [Waiz vs client marketing](client-fulfillment/waiz-vs-client-marketing-boundaries.md) |
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

- [Raw export archive](_inventory/raw-export-archive.md) (sibling `waiz-os-archive` repo)
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
