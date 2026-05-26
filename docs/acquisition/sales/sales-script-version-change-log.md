---
title: Sales Script Version Change Log
domain: acquisition
owner: sales-leadership
status: draft
last_updated: 2026-05-26
review_cycle: weekly
artifact_type: reference
---

# Sales Script Version Change Log

## Purpose

Single source of truth for all acquisition sales script changes, including why a change was made, what was changed, who approved it, and whether performance improved.

## Scope

Applies to script changes under `docs/acquisition/sales/` (intro, discovery, demo, objections, and related stage scripts). Excludes fulfillment call-center scripts.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **sales-leadership**.

## Update Rule

Every script change must create or update one row in this log before rollout is considered complete.

## Required Fields

- Date
- Script file path
- Version tag
- Change type (new, update, rollback, deprecate)
- Trigger/reason
- Summary of exact change
- Expected KPI impact
- Pilot window
- Outcome decision (adopt, iterate, rollback)
- Approver

## Change Log

| Date | Script | Version | Change Type | Trigger / Reason | Change Summary | Expected KPI Impact | Pilot Window | Outcome | Approver |
|------|--------|---------|-------------|------------------|----------------|---------------------|--------------|---------|----------|
| 2026-05-26 | `acquisition/sales/script-intro-call-basic.md` | `v1.0` | baseline | Initial logging baseline | Established baseline version for future diffs | N/A baseline | N/A | baseline active | sales-leadership |
| 2026-05-26 | `acquisition/sales/discovery-call-script-2026.md` | `v1.0` | baseline | Initial logging baseline | Established baseline version for future diffs | N/A baseline | N/A | baseline active | sales-leadership |
| 2026-05-26 | `acquisition/sales/script-demo-call.md` | `v1.0` | baseline | Initial logging baseline | Established baseline version for future diffs | N/A baseline | N/A | baseline active | sales-leadership |

## Entry Template

Use this format for each new change:

| Date | Script | Version | Change Type | Trigger / Reason | Change Summary | Expected KPI Impact | Pilot Window | Outcome | Approver |
|------|--------|---------|-------------|------------------|----------------|---------------------|--------------|---------|----------|
| YYYY-MM-DD | `acquisition/sales/<script-file>.md` | `vX.Y` | update | Stage issue / objection cluster / offer alignment | 1-2 sentence summary of exact script edits | Metric + target direction | e.g., 7 days or 25 calls | adopt / iterate / rollback | role |

## Decision Rules

- Do not publish script updates without a log entry.
- If outcome is `rollback`, reference replacement version in the next row.
- Keep version tags sequential per script.

## Related Docs

- [Script Factory SOP](sop-script-factory.md)
- [Sales Process Design SOP](sop-sales-process-design.md)
- [Sales Advice Intake SOP](sop-sales-advice-intake.md)
- [Sales Operating Hub](README.md)

## Open Questions

- [ ] Confirm exact pilot minimum (calls or days) per stage so all entries use the same standard.
