---
title: Watchshift SOP
domain: acquisition
owner: setter-lead
status: draft
last_updated: 2026-05-26
review_cycle: weekly
artifact_type: sop
---

# Watchshift SOP

## Purpose

Define the live monitoring and speed-to-lead execution standard for setter watchshift blocks so inbound and high-intent leads are contacted immediately.

## Scope

Applies to acquisition setter watchshift operations only. This SOP does not govern fulfillment B2C call-center scripting.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **setter lead**.

## Trigger

- Setter enters scheduled watchshift block
- New inbound notifications arrive during watchshift

## Inputs

- Active lead alerts from GHL, Slack, and assigned channels
- Current call queue and lead notes
- Qualification logic from [Intro Call Qualification Framework](intro-call-qualification-framework.md)

## Outputs

- Immediate call attempts on new inbound and watchshift outbound leads
- Updated lead dispositions in CRM
- Escalated issues and shift handoff notes

## Process

1. Start watchshift and verify alerts are active across all assigned channels.
2. Monitor channels continuously; do not run non-watchshift work in this block.
3. If a new inbound lead appears, call immediately (Priority 1 behavior).
4. During gaps, call watchshift outbound leads who showed interest but have not completed intro qualification.
5. Log each attempt outcome and next action in CRM before moving to the next lead.
6. If a lead replies by text during block, call immediately before further texting.
7. End block with a concise handoff note (open high-priority leads, escalations, system issues).

## Decision Rules

- Inbound lead during watchshift always overrides outbound queue.
- Texting supports calling, not replaces calling.
- If a lead cannot be reached after protocol steps, move to defined retry queue.
- Script and framework remain acquisition-side: use [Intro Call Basic Script](script-intro-call-basic.md) and [Intro Call Qualification Framework](intro-call-qualification-framework.md).

## Escalation

- Alert routing/system failure -> ops manager immediately.
- Repeated unreachable hot leads with missing contact data -> CRM owner.
- Qualification or pricing boundary confusion -> closer/founder per existing sales SOPs.

## Quality Bar

- Leads are called fast enough to preserve peak intent.
- CRM records are complete and usable by next shift.
- No mixing with fulfillment call-center process. Fulfillment scripts live in [Client Fulfillment — Call Center](../../client-fulfillment/call-center/README.md).

## Metrics

- Median speed-to-first-call
- Contact rate during watchshift block
- Qualified-demo booking rate from watchshift leads
- Missed inbound alert count

## Related Docs

- [Setter Daily Operations Playbook](setter-daily-operations-playbook.md)
- [Intro Call Qualification Framework](intro-call-qualification-framework.md)
- [Intro Call Basic Script](script-intro-call-basic.md)
- [No Shows And Maximizing Show Rates](no-shows-maximizing-show-rates-setter-levers.md)
- [Client Fulfillment — Call Center](../../client-fulfillment/call-center/README.md)

## Open Questions

- [ ] Confirm exact retry ladder timing by channel.
- [ ] Confirm required handoff format at end of each watchshift.
