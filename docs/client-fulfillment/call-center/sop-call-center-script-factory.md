---
title: Call Center Script Factory SOP
domain: client-fulfillment
owner: client-success
status: draft
last_updated: 2026-05-26
review_cycle: monthly
artifact_type: sop
---

# Call Center Script Factory SOP

## Purpose

Create a repeatable system to design, improve, test, approve, and retire B2C fulfillment call-center scripts without mixing them with acquisition sales scripts.

## Scope

Applies to client-fulfillment call-center scripts used after client sign and launch preparation or post-launch lifecycle interactions. Excludes Waiz acquisition sales scripts.

## Owner

Primary owner: **client-success** until a dedicated call-center lead is assigned.

## Trigger

- New call scenario appears without a canonical script
- Script underperforms against fulfillment quality metrics
- New objection pattern emerges in client-side B2C calls
- Compliance/risk feedback requires script adjustment

## Inputs

- Script request brief (scenario, call objective, target outcome)
- Recent call evidence (notes/transcripts/recordings)
- Fulfillment context from [Fulfillment Operating System](../fulfillment-operating-system.md)
- Compliance constraints from [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)

## Outputs

- Approved script version in canonical fulfillment path
- QA decision and rollout notes
- Deprecated prior versions (if replaced)

## Script Categories

- Onboarding readiness and pre-launch expectation calls
- Appointment follow-up and no-response recovery
- Reset/recovery performance conversations
- Retention and trust-restoration conversations

## Process

1. **Intake and classify**
   - Define call type, customer state, risk level, and desired next action.
   - Confirm this is fulfillment-side (not acquisition-side).
2. **Draft script v0**
   - Build script from scenario objective, likely objections, and approved compliance language.
   - Include opening, discovery prompts, objection responses, and close/next step.
3. **Compliance and quality review**
   - Check against RM guardrails and promise-risk language.
   - Remove unsupported claims, guarantees, or advice beyond allowed scope.
4. **Internal roleplay**
   - Test script with real objection branches.
   - Capture breakdown points and revise to v1.
5. **Pilot in production**
   - Use script in a controlled sample period with call notes.
   - Track outcome quality and escalation frequency.
6. **Approve and publish**
   - Promote passing script as current canonical version.
   - Link it from [Client Fulfillment — Call Center](README.md).
7. **Version control**
   - Mark replaced versions as deprecated.
   - Keep one active script per scenario to avoid drift.

## Decision Rules

- If language creates compliance ambiguity, block publish and escalate.
- If script improves emotional quality but reduces objective completion, redesign before rollout.
- If scenario already has an active script, revise that source instead of creating duplicate files.
- If issue is process-level (not wording-level), hand off to relevant SOP in client-success/onboarding.

## Quality Bar

- Script is executable by trained team members without founder interpretation.
- Script balances empathy with objective progression.
- Script reflects post-sign fulfillment context and does not reuse acquisition positioning language.

## Escalation

- Compliance uncertainty -> founder/compliance reviewer.
- Recurring call failure across scenarios -> client-success leadership review.
- CRM automation/handoff dependency issues -> [CRM Architecture](../crm-architecture/README.md) owner.

## Metrics

- Scenario completion rate
- Escalation rate per script
- Repeat-contact reduction after script rollout
- QA failure rate during review

## Related Docs

### Prerequisites (read before this SOP)

- [Client Fulfillment — Call Center](README.md) - call-center domain index.
- [Fulfillment Operating System](../fulfillment-operating-system.md) - fulfillment context and handoff map.

### Handoffs (what happens after this SOP)

- [Client Success](../client-success/README.md) - post-launch account health and performance operations.
- [Onboarding](../onboarding/README.md) - launch-path operational dependencies.

### Reference (used during execution)

- [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md) - non-negotiable language boundaries.
- [Constraint Troubleshooting SOP](../client-success/constraint-troubleshooting-sop.md) - performance issue diagnosis when script quality is not root cause.
- [Reset Call SOP](../client-success/reset-call-sop.md) - recovery conversation operating context.

## Open Questions

- [ ] Confirm dedicated owner role (call-center lead vs client-success lead).
- [ ] Confirm pilot sample size by scenario category.
