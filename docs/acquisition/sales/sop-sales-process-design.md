---
title: Sales Process Design SOP
domain: acquisition
owner: sales-leadership
status: draft
last_updated: 2026-05-26
review_cycle: monthly
artifact_type: sop
---

# Sales Process Design SOP

## Purpose

Define how Waiz designs, updates, and approves the acquisition sales process so process changes are deliberate, measurable, and retrievable by AI.

## Scope

Acquisition sales only (setter and closer workflow for selling Waiz offers). Excludes client-fulfillment call center scripts and post-sign execution.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **sales-leadership**.

## Trigger

- KPI drift on core funnel stages (booked, show, close, or qualified rate)
- Repeated call-pattern failures from reviews or transcripts
- Offer, pricing, or qualification logic changes
- New objection clusters that current scripts cannot handle

## Inputs

- Sales KPI snapshots from [WM Sales Call Tracker](../wm-sales-call-tracker.md)
- Call evidence (recordings, notes, transcript excerpts)
- Current active SOP/script set from [Sales Operating Hub](README.md)
- Constraints from [Money Model And Offer Architecture](../../company/overview-money-model-april-26.md)

## Outputs

- Approved process change brief (what changed and why)
- Updated script/SOP list with ownership and status
- Rollout plan (training, cutover date, success checkpoints)

## Process

1. **Diagnose the gap**
   - Define the exact stage breaking (intro qualify, show rate, discovery, demo, objections, handoff).
   - Separate signal vs noise using minimum sample size and recent period consistency.
2. **Map root cause**
   - Classify root cause as messaging, qualification, offer fit, objection handling, execution discipline, or handoff quality.
   - Confirm with at least two evidence sources (KPIs + transcripts).
3. **Design the change**
   - Decide if fix type is script update, SOP update, sequencing change, or role accountability change.
   - Draft a one-page change brief with expected KPI impact and risk.
4. **Review dependencies**
   - Validate alignment with [Intro Call Qualification Framework](intro-call-qualification-framework.md), [Discovery Call Script](discovery-call-script-2026.md), [Demo Call Script](script-demo-call.md), and [Objection Handling Hub](objection-handling-hub.md).
   - Confirm no conflict with pricing/offer boundaries.
5. **Approve and assign**
   - Owner approves change type, scope, and primary document to edit.
   - Assign one doc owner and one QA reviewer.
6. **Pilot and measure**
   - Run a defined pilot window before full rollout.
   - Compare baseline vs pilot metrics and keep/revert based on evidence.
7. **Publish and train**
   - Update canonical docs in `docs/acquisition/sales/`.
   - Mark deprecated assets explicitly and communicate go-live version.

## Decision Rules

- If issue is isolated to wording and stage behavior is stable, update script before SOP.
- If issue is execution inconsistency across team members, update SOP before script.
- If issue changes qualification thresholds or offer fit, escalate to founder before rollout.
- If pilot KPI impact is neutral/negative, revert and redesign.

## Quality Bar

- Every process change has measurable baseline, hypothesis, and decision outcome.
- Only one active source of truth per stage; legacy versions are marked deprecated.
- Changes align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and sales positioning standards.

## Escalation

- Pricing, guarantee, offer packaging, or compliance risk -> founder.
- Persistent KPI decline after two iterations -> sales-leadership review with operations.
- Cross-domain dependencies (CRM or fulfillment) -> involve client-fulfillment owner.

## Metrics

- Booked call rate
- Show rate
- Qualified-to-demo rate
- Demo close rate
- Stage-specific objection conversion by category

## Related Docs

### Prerequisites (read before this SOP)

- [Sales Operating Hub](README.md) - active funnel map and canonical sales docs.
- [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md) - positioning, belief patterns, and reframes.

### Reference (used during execution)

- [Intro Call Qualification Framework](intro-call-qualification-framework.md) - intro stage qualification logic.
- [Discovery Call Script](discovery-call-script-2026.md) - discovery-stage execution baseline.
- [Demo Call Script](script-demo-call.md) - demo and close execution baseline.
- [Objection Handling Hub](objection-handling-hub.md) - objection routing and depth library.
- [WM Sales Call Tracker](../wm-sales-call-tracker.md) - KPI and activity evidence source.

## Open Questions

- [ ] Confirm KPI thresholds that trigger mandatory process redesign.
- [ ] Confirm required pilot length before production rollout.
