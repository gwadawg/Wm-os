---
title: Script Factory SOP
domain: acquisition
owner: sales-leadership
status: draft
last_updated: 2026-05-29
review_cycle: monthly
artifact_type: sop
---

# Script Factory SOP

## Purpose

Define a repeatable system for creating, testing, approving, publishing, and retiring acquisition sales scripts so script quality compounds over time.

## Scope

Applies to Waiz acquisition sales scripts (intro, discovery, demo, objections, follow-up messaging tied to sales stages). Excludes fulfillment call-center scripts.

## Owner

See [domain owners](../../_inventory/domain-owners.md): **sales-leadership**.

## Trigger

- New script need identified from [Sales Advice Intake SOP](sop-sales-advice-intake.md)
- KPI underperformance tied to script execution
- New objection class appears repeatedly
- Offer positioning update requires script alignment

## Inputs

- Script brief (stage, audience, objective, risk notes)
- Evidence from call tracker and transcript snippets
- Positioning source from [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md)
- Existing active script baseline in [Sales Operating Hub](README.md)

## Outputs

- Approved script draft in canonical path
- QA decision and rollout status
- Version log (current, prior, and deprecated references)

## Process

1. **Create script brief**
   - Define stage, objective, success metric, and known objections.
   - Include examples of current failure language and desired replacement behavior.
2. **Draft v0**
   - Build script using current positioning and qualification rules.
   - Apply reusable patterns from [Script Factory building blocks](script-factory/README.md) when relevant (e.g. [Flip the Frame — company description](script-factory/flip-the-frame-company-description.md)).
   - Keep it stage-specific and avoid cross-stage bloat.
3. **QA review**
   - Check for clarity, compliance-safe phrasing, objection handling quality, and role fit (setter vs closer).
   - Remove language that conflicts with qualification or pricing policy.
4. **Roleplay/test**
   - Test in internal roleplay before production calls.
   - Capture friction points and update to v1.
5. **Pilot deployment**
   - Run pilot on a defined sample window.
   - Compare KPI impact against pre-pilot baseline.
6. **Approve and publish**
   - If pilot passes threshold, publish as current script in canonical location.
   - Update related stage docs and hub links.
7. **Version and deprecate**
   - Mark replaced versions `deprecated`.
   - Ensure only one active script per stage/use-case.

## Decision Rules

- If script change modifies qualification boundaries, escalate before publish.
- If pilot results are statistically unclear, extend pilot instead of full rollout.
- If script reduces conversion or increases low-quality bookings, revert and redesign.
- If a script overlaps an existing active stage script, update the existing file instead of creating a duplicate.

## QA Checklist

- Stage objective is explicit
- Language aligns with ICP and offer
- Objection transitions are natural and non-combative
- CTA and next step are unambiguous
- Script is executable by assigned role without founder interpretation

## Versioning And Deprecation

- Use one canonical file per stage script where possible.
- When replacing, do not silently overwrite decision context; note change reason in an update section or linked change log.
- Deprecated scripts remain linkable but must not be listed as active in hub docs.

## Quality Bar

- Scripts are tied to measurable stage outcomes, not style preference.
- Script updates follow evidence -> pilot -> publish sequence.
- Active scripts are discoverable in one place for both humans and AI.

## Escalation

- Offer/pricing/compliance boundary ambiguity -> founder.
- Repeated script failures after two iterations -> sales-leadership review.
- Cross-domain wording risk affecting fulfillment expectations -> client-success review.

## Metrics

- Stage conversion lift after script update
- Objection conversion rate by category
- Time-to-competency for new script adoption
- Revert rate of newly published scripts

## Related Docs

### Prerequisites (read before this SOP)

- [Sales Operating Hub](README.md) - active scripts and funnel ownership.
- [WM Sales Intelligence Bible](../intelligence/wm-sales-intelligence-bible.md) - positioning and reframe source.

### Handoffs (what happens after this SOP)

- [Sales Process Design SOP](sop-sales-process-design.md) - process-level redesign when script-only change is insufficient.

### Reference (used during execution)

- [Script Factory — building blocks](script-factory/README.md) - reusable frameworks (company description, future patterns).
- [Flip the Frame — company description](script-factory/flip-the-frame-company-description.md) - Framework 1; reclaim frame.
- [Intro ICP tracks](script-factory/intro-icp-tracks.md) - “who we are” + demo pre-pitch (referral / marketing-system / forward→reverse).
- [Sales Advice Intake SOP](sop-sales-advice-intake.md) - intake and routing logic for script requests.
- [Sales Script Version Change Log](sales-script-version-change-log.md) - required record of script version decisions and outcomes.
- [Intro Call Script](script-intro-call-basic.md) - current intro baseline (`v2.0`).
- [Demo Appointment Confirmation Script](script-demo-appointment-confirmation.md) - setter demo confirm + pre-call video tie-down (`v1.0`, `draft`).
- [Discovery Call Script](discovery-call-script-2026.md) - current discovery baseline.
- [Demo Call Script](script-demo-call.md) - current demo baseline.
- [Objection Handling Hub](objection-handling-hub.md) - objection handling references.

## Open Questions

- [ ] Confirm minimum pilot sample size by stage.
