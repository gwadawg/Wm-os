---
title: Power Dialer New Leads SOP
domain: acquisition
owner: setter-lead
status: draft
last_updated: 2026-05-26
review_cycle: weekly
artifact_type: sop
---

# Power Dialer New Leads SOP

## Purpose

Standardize how setters work new-lead dial blocks so dialing cadence, messaging, and CRM dispositions are consistent and performance-trackable.

## Scope

Applies to acquisition new-lead dialer activity after higher-priority blocks are handled. Excludes fulfillment B2C call-center scripts and workflows.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **setter lead**.

## Trigger

- Priority 1-4 blocks are complete for the current period
- New-lead dial block is scheduled

## Inputs

- New lead queue ordered newest to oldest
- Dialer system access and verified line
- Intro script + qualification framework

## Outputs

- Completed dial attempts with dispositions
- Booked intro/demo outcomes where qualified
- Clear retry queue for unresolved leads

## Process

1. Pull lead list sorted newest -> oldest; work in order.
2. Call each lead first before texting.
3. If no answer, follow voicemail/text fallback sequence.
4. If connected, run qualification via acquisition intro framework and route accordingly.
5. After each lead, record disposition and next action immediately.
6. Continue until block ends; leave clean retry queue and summary notes.

## Call Cadence (Default)

- Attempt 1: live call
- Attempt 2: immediate second call if first missed
- Attempt 3: voicemail + concise text follow-up
- Attempt 4+: scheduled retry based on queue priority and recent engagement

## Voicemail Framework (Default)

- Identify self/company
- State reason (response to expressed interest)
- Provide simple callback action
- Keep under 20 seconds

## CRM Disposition Tags (Minimum)

- Connected-qualified-booked
- Connected-qualified-not-booked
- Connected-not-qualified
- No-answer-voicemail-left
- No-answer-no-voicemail
- Bad-number
- Follow-up-scheduled

## Decision Rules

- Do not skip sequence order unless lead is explicitly time-sensitive.
- Do not run long objection handling over text; route to live call.
- If a lead is not a fit, route using [Disqualifying And Financial Qualification](disqualifying-financial-qualification.md).
- Do not use fulfillment call-center scripts in acquisition dial blocks.

## Escalation

- Dialer outage or call-delivery issue -> ops manager.
- High bad-number rate spike -> data/CRM owner.
- Repeated compliance-risk language in outreach -> sales-leadership review.

## Quality Bar

- Dispositions are complete and reliable.
- Dial blocks prioritize freshness and throughput without losing quality.
- Acquisition scripting remains isolated from fulfillment call-center scripting.

## Metrics

- Dials per block
- Connect rate
- Qualified rate
- Booked rate from connects
- Bad-number rate

## Related Docs

- [Setter Daily Operations Playbook](setter-daily-operations-playbook.md)
- [Intro Call Basic Script](script-intro-call-basic.md)
- [Intro Call Qualification Framework](intro-call-qualification-framework.md)
- [Disqualifying And Financial Qualification](disqualifying-financial-qualification.md)
- [Client Fulfillment — Call Center](../../client-fulfillment/call-center/README.md)

## Open Questions

- [ ] Confirm exact retry-day schedule after day 1.
- [ ] Confirm whether voicemail is mandatory on every no-answer attempt.
