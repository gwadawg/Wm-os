---
title: Sales KPI Thresholds
domain: kpis
owner: sales-leadership
status: draft
last_updated: 2026-05-26
review_cycle: weekly
artifact_type: kpi
---

# Sales KPI Thresholds

## Purpose

Define KPI guardrails and trigger thresholds that determine when to monitor, pilot changes, redesign process, or escalate in acquisition sales.

## Scope

Applies to acquisition sales funnel KPIs only. Excludes fulfillment call-center performance metrics.

## Owner

Primary owner: **sales-leadership** with operations support.

## KPI Trigger Model

Use three levels:

- **Monitor**: early warning, track closely
- **Action**: run script/SOP intervention or pilot
- **Escalate**: leadership/founder review required

## Threshold Table (Initial Draft)

| KPI | Monitor | Action | Escalate | Primary Response SOP |
|-----|---------|--------|----------|----------------------|
| Speed-to-first-call | Above internal target for 3 days | Above target for 7 days | Persistent over 14 days | [Watchshift SOP](../../acquisition/sales/sop-watchshift.md) |
| Show rate | Down vs baseline for 1 week | Down vs baseline for 2 weeks | Down vs baseline for 4 weeks | [No Shows And Maximizing Show Rates](../../acquisition/sales/no-shows-maximizing-show-rates-setter-levers.md) |
| Qualified-to-demo rate | Down vs baseline for 1 week | Down vs baseline for 2 weeks | Down vs baseline for 4 weeks | [Intro Call Qualification Framework](../../acquisition/sales/intro-call-qualification-framework.md) |
| Demo close rate | Down vs baseline for 1 week | Down vs baseline for 2 weeks | Down vs baseline for 4 weeks | [Script Factory SOP](../../acquisition/sales/sop-script-factory.md) |
| Objection conversion rate | New drop pattern appears | Pattern repeats across 2 review cycles | No lift after 2 iterations | [Objection Handling Hub](../../acquisition/sales/objection-handling-hub.md) |

## Trigger Actions

1. Monitor: add diagnostic note and assign owner.
2. Action: route through [Sales Advice Intake SOP](../../acquisition/sales/sop-sales-advice-intake.md) and launch intervention.
3. Escalate: open leadership review via [Sales Process Design SOP](../../acquisition/sales/sop-sales-process-design.md).

## Data Source

- [WM Sales Call Tracker](../../acquisition/wm-sales-call-tracker.md)
- Script change outcomes from [Sales Script Version Change Log](../../acquisition/sales/sales-script-version-change-log.md)

## Boundary Rule

If issue belongs to client-fulfillment call center, route to [Client Fulfillment — Call Center](../../client-fulfillment/call-center/README.md) and do not log as acquisition sales KPI failure.

## Related Docs

- [Sales Operating Hub](../../acquisition/sales/README.md)
- [Sales Process Design SOP](../../acquisition/sales/sop-sales-process-design.md)
- [Sales Advice Intake SOP](../../acquisition/sales/sop-sales-advice-intake.md)
- [Script Factory SOP](../../acquisition/sales/sop-script-factory.md)

## Open Questions

- [ ] Replace relative thresholds with explicit numeric targets by KPI.
- [ ] Confirm required sample size before escalation by stage.
