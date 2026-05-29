---
title: Sales Script Version Change Log
domain: acquisition
owner: sales-leadership
status: draft
last_updated: 2026-05-30
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
| 2026-05-29 | `acquisition/sales/script-demo-appointment-confirmation.md` | `v1.0` | new | Setter morning-of demo confirm + content tie-down | Phone flow (open → double tie-down → calendar → video re-tie/send → closer handoff); SMS backup; CRM template; linked from P3 checklist | Demo show rate; pre-call watch rate before closer calls | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-intro-call-basic.md` | `v2.4` | update | Three ICP tracks for “who we are” + demo pre-pitch | Referral LO, marketing/system LO, forward→reverse — routing table + per-track scripts; script-factory intro-icp-tracks.md | Sharper relevance; higher demo show intent | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-factory/intro-icp-tracks.md` | `v1.0` | new | ICP-specific intro talk tracks | Mirror of intro script tracks for script factory reuse | Reusable in future scripts | N/A | active | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-intro-call-basic.md` | `v2.3.3` | update | Simplify setter call checklist to 5 items | Frame → qualify → sold demo → apt/info tie-down → watch material tie-down | Easier live-call compliance | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-intro-call-basic.md` | `v2.3.2` | update | Simple pre-book + post-book checklists for setters | Glance checklist before GHL book; gate at Stage 5; linked from setter daily checklist | Fewer incomplete handoffs to closer | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-intro-call-basic.md` | `v2.3.1` | update | Stage 2 frame — objection pre-handle without question laundry list | Four-point frame: not sales call; setter = fit/no wasted time; quick prep for strategy call; can send learn-about-us resources | Lower resistance early on intro | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-intro-call-basic.md` | `v2.3` | update | Setter ballpark pricing when prospect won’t proceed without a number | Wide [LOW]–[HIGH] + custom speed/scale framing + fit-check question; split “how it works” vs price; pricing sheet placeholders | Fewer stalled intros on price; better F qualification | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-intro-call-basic.md` | `v2.2` | update | LO-specific Flip the Frame copy (consistency, shared leads, front end) | Framework 1/2 scripts from reverse-LO rundown; discovery quartet + transition bridge before operational qualifiers | Self-qualification on intros; stronger pain recognition | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-factory/flip-the-frame-company-description.md` | `v1.1` | update | Replace generic Part 2 with speak-to-pain reverse LO script | Motivation table; Framework 2 three-paragraph pain; discovery quartet; transition bridge | Same as intro v2.2 | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-intro-call-basic.md` | `v2.1` | update | Integrate Flip the Frame for “what do you do?” | Replaced single high-level blurb with Part 1 deflect + Part 2 pain-anchored description; linked script-factory framework | Better frame control on intros; less pitch-on-command | 14 days | pending pilot | sales-leadership |
| 2026-05-30 | `acquisition/sales/script-factory/flip-the-frame-company-description.md` | `v1.0` | new | External sales framework + Waiz LO adaptation | Script-factory building block: deflect/redirect + answer/anchor; cheat sheet; ICP copy | Reusable across intro/SMS/future scripts | N/A new block | active | sales-leadership |
| 2026-05-29 | `acquisition/sales/script-intro-call-basic.md` | `v2.0` | update | Setter intro rewrite — low-pressure discovery frame, prospect frustration on pricing/programs | Replaced HBHF with six operational qualifiers; seven-stage checklist; four openings (booked, early confirmation, dialer, intro no-show); setter boundary scripts; single shared Stages 2–7 | Intro→demo book rate; demo show rate; fewer “wasted call” complaints | 14 days or ~40 intros | pending pilot | sales-leadership |
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
