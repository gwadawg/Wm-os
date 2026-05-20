---
title: Duplicate Resolutions
domain: inventory
owner: operations
status: active
last_updated: 2026-05-20
review_cycle: as-needed
---

# Duplicate Resolutions

Decisions for overlapping source files. **Do not create two canonical docs** for the same workflow.

## Media Buyer Job Scorecard

| Source | Action |
|--------|--------|
| `02 _ Operations/MB Hiring-Onboarding/Media Buyer Job Scorecard.docx` | **Canonical source** when converting |
| `02 _ Operations/MB Hiring-Onboarding/Media Buyer Job Scorecard(1).docx` | **Superseded** — same content with stray "January" header; do not convert separately |

**Canonical path:** [docs/operations/hiring/media-buyer-job-scorecard.md](../operations/hiring/media-buyer-job-scorecard.md)

## Operations Manager Priority Ladder

| Source | Action |
|--------|--------|
| `02 _ Operations/Ops (SOPs)/OPS Manager Priority Ladder.docx` | **Canonical source** (SOP location) |
| `02 _ Operations/Operations Manager Priority Ladder.docx` | **Superseded** — near-duplicate; title includes "& Responsibilities" only on root copy |

**Canonical path:** [docs/operations/systems/ops-manager-priority-ladder.md](../operations/systems/ops-manager-priority-ladder.md)

## Constraint Troubleshooting / Diagnosis

Three related docs; **not** one merge — different scope:

| Source | Action |
|--------|--------|
| `03 _ Client Fulfillment/Client Success (SOPs)/SOP -- Constraint Troubleshooting and Root Cause Diagnosis -- March 2026.docx` | **Canonical SOP** — full-funnel playbook, ClickUp rules, March 2026 |
| `02 _ Operations/Ops (SOPs)/Constraint Troubleshooting.docx` | **Superseded** — shorter hub; link to canonical SOP |
| `03 _ Client Fulfillment/Fulfillment Constraint Diagnosis & KPI standards.docx` | **Separate canonical** — KPI tiers, layer owners (MB, CS, LO); companion to SOP |

**Canonical paths:**

- [constraint-troubleshooting-sop.md](../client-fulfillment/client-success/constraint-troubleshooting-sop.md)
- [fulfillment-constraint-diagnosis-kpi-standards.md](../client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md)

Cross-link both; operations README points to client-success SOP.

## Meta Business Manager Creation Guide

| Source | Action |
|--------|--------|
| `.docx` in Skool Bootcamp | **Canonical source** if course material is converted |
| `.pdf` same folder | **Keep raw only** — do not maintain two Markdown versions |

## Facebook Page / Ad Account Setup

Multiple sources (Skool, media buying SOPs). **Before converting:** pick one internal SOP under `docs/client-fulfillment/media-buying/`; course copies link to it.

## Related

- [Duplicate Candidates](duplicate-candidates.md)
- [Source Of Truth Rules](../SOURCE-OF-TRUTH.md)
