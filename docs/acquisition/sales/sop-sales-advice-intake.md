---
title: Sales Advice Intake SOP
domain: acquisition
owner: sales-leadership
status: draft
last_updated: 2026-05-26
review_cycle: monthly
artifact_type: sop
---

# Sales Advice Intake SOP

## Purpose

Standardize how sales advice requests are submitted, diagnosed, and converted into concrete operational outputs without losing context or creating duplicate documents.

## Scope

Applies to acquisition sales advice requests from founder, setter, closer, and operations. Covers intake through routing decision. Execution of approved changes happens in downstream SOPs.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **sales-leadership**.

## Trigger

- Team member requests help on script, objection, stage conversion, or call handling
- Sales KPI warning appears in tracker review
- Founder requests strategic review of sales process behavior

## Inputs

- Intake request form/message with call stage and target outcome
- KPI context from [WM Sales Call Tracker](../wm-sales-call-tracker.md)
- Evidence: transcript snippet, recording notes, or objection examples
- Current canonical baseline from [Sales Operating Hub](README.md)

## Outputs

- One routing decision per request
- Assigned owner and deadline
- Chosen artifact path (if documentation update is required)
- Logged rationale for future audits

## Intake Schema

Every advice request must include:

- Requestor
- Funnel stage affected
- Desired business outcome
- Current KPI baseline (or current failure symptom)
- Evidence block (transcript line, objection sample, or call summary)
- Urgency and impact level
- Decision owner

## Process

1. **Collect complete context**
   - Validate all required intake fields.
   - Reject incomplete requests back to requestor with missing-field checklist.
2. **Classify request type**
   - Classify as: tactical wording issue, stage-level process issue, qualification issue, objection handling issue, or offer/policy issue.
3. **Assess impact**
   - Score business impact (low/medium/high) based on revenue risk, frequency, and stage criticality.
4. **Route outcome**
   - Pick exactly one route:
     - quick recommendation
     - controlled experiment
     - script update
     - SOP/process update
     - escalation
5. **Assign owner and timeline**
   - Assign doc/process owner and due date.
   - Define verification metric and review date.
6. **Log and close intake**
   - Add decision summary to request record.
   - Link to updated doc path or experiment tracker.

## Routing Outcomes

- **Quick recommendation**: no canonical doc change; include follow-up check date.
- **Controlled experiment**: temporary test with hypothesis, sample window, and success threshold.
- **Script update**: hand off to [Script Factory SOP](sop-script-factory.md) once approved.
- **SOP/process update**: hand off to [Sales Process Design SOP](sop-sales-process-design.md).
- **Escalation**: founder review for pricing/offer/policy/compliance-sensitive topics.

## Decision Rules

- If no evidence is attached, do not proceed beyond intake validation.
- If request implies offer/pricing shift, escalate before any script or SOP edits.
- If impact is high and recurring, route to SOP/process update over one-off advice.
- If issue is isolated and low impact, start with quick recommendation or small experiment.

## Quality Bar

- Every request is traceable from intake to decision to outcome.
- Advice does not bypass canonical documentation when persistent changes are needed.
- No duplicate SOP/script is created for an existing process; update existing source of truth instead.

## Escalation

- Offer/pricing/guarantee changes -> founder.
- Multi-stage funnel failure -> sales-leadership + operations review.
- Compliance-sensitive language -> compliance reference owner before rollout.

## Metrics

- Intake completion rate (requests with full schema fields)
- Median intake-to-decision time
- Percentage of requests routed to durable documentation updates
- KPI lift rate from completed routed actions

## Related Docs

### Prerequisites (read before this SOP)

- [Sales Operating Hub](README.md) - canonical acquisition sales map.
- [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md) - buyer context and reframe logic.

### Handoffs (what happens after this SOP)

- [Sales Process Design SOP](sop-sales-process-design.md) - route for process-level redesign.
- [Script Factory SOP](sop-script-factory.md) - route for script lifecycle updates.

### Reference (used during execution)

- [WM Sales Call Tracker](../wm-sales-call-tracker.md) - KPI baseline and performance evidence.
- [Objection Handling Hub](objection-handling-hub.md) - canonical objection routing.

## Open Questions

- [ ] Confirm who owns intake triage weekly when sales-leadership is unavailable.
- [ ] Confirm SLA targets by priority level.
