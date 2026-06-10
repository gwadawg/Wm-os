---
title: Power Dialer New Leads SOP
domain: acquisition
owner: setter
status: draft
last_updated: 2026-06-10
review_cycle: weekly
artifact_type: sop
---

# Power Dialer New Leads SOP

## Purpose

Standardize how the setter works **new-lead power dialer blocks** — call order, texting, pipeline stages, and handoffs — so dialing stays fast and CRM stays accurate.

## Scope

- Acquisition **new leads** in the power dialer queue only.
- Runs at **Priority 5** on the [Setter Daily Checklist](setter-daily-checklist.md) — after P1–P4 are clear for the block.
- Does **not** cover watchshift alerts (see [Watchshift SOP](sop-watchshift.md)), fulfillment B2C call center, or intro script copy (see [Intro Call Script](script-intro-call-basic.md)).

## Owner

See [domain owners](../../_inventory/domain-owners.md): **setter**.

## Trigger

- P1–P4 are clear for the current work block, **and**
- Setter is running a new-lead dial session (scheduled block or open time in the priority stack)

**Stop the dialer block** when a watchshift or P1 interrupt fires — handle per [Watchshift SOP](sop-watchshift.md) / checklist **Always first**, then resume the list.

## Inputs

- **DQ-1 — Clear Today** smart list in GHL (Contacts → Smart Lists) — see [GHL Daily Queue](ghl-pipeline-disposition-reference.md#dq-1--clear-today-primary-outbound-queue)
- Dialer access and active line
- [Intro Call Script](script-intro-call-basic.md) — on connect use [Opening 3 — Dialer / impromptu](script-intro-call-basic.md#opening-3--dialer--impromptu) (other openings if they already booked)
- [Intro Call Qualification Framework](intro-call-qualification-framework.md)

## Outputs

- Every touched lead has an updated **pipeline stage**, notes, and next step (or explicit reason untouched)
- GHL **task** for setter or Gabriel when work carries past this block
- Booked intros/demos, **Setter quality lead**, lost/Boot Camp, or scheduled follow-up per outcome

---

## Process

1. Confirm P1–P4 are clear — do not start dialer while watchshift backlog or higher priorities are open.
2. Open **DQ-1 — Clear Today**. Work **top to bottom** until empty or every remaining row snoozed. Do not cherry-pick from Opportunities.
3. **Within DQ-1, prioritize:** fresh New Leads → Engaged replies → A-grade → everything else.
4. **Per lead:**
   1. **Call first** (live attempt per cadence below).
   2. If no connect → voicemail; then **value-based text** if they have never been texted or follow-up is due — see [Setter Lead Messaging](setter-lead-messaging.md).
   3. If connect → intro script + FUN; book next step or route disqualify/Boot Camp.
   4. **Notes required** — every lead you **speak with** gets CRM notes (what was said, motivators, objection, next step). A call without notes is incomplete.
   5. **Lead Grade** on every connect (A/B/C/Junk) — A-grade gets priority in DQ-1 next day
   6. **Immediately** update pipeline stage on the Opportunities board after the touch.
   7. If callback or Gabriel input needed → GHL task (assigned correctly).
   8. **Defer without closing:** set **Next Work Date** (tomorrow or future) + GHL task + note — lead leaves DQ-1 until that date.
5. **SMS during the block:** see [Texting during dial blocks](#texting-during-dial-blocks).
6. End block with DQ-1 empty or all remaining rows snoozed — aligns with EOD **pipeline cleared** on the checklist.

---

## Call cadence (default)

| Step | Action |
|------|--------|
| 1 | Live call |
| 2 | Immediate second dial if first rings out / no answer |
| 3 | Voicemail + short text (if appropriate) |
| 4+ | Retry per queue rules / GHL task for later |

### Voicemail (default)

- Who you are + Waiz Media
- Why you’re calling (they showed interest)
- Simple callback ask
- Under ~20 seconds

---

## Texting during dial blocks

Execution detail: **[Setter Lead Messaging](setter-lead-messaging.md)** (review lead file + form + history; value-first copy; word-tracking starters).

Matches the [daily checklist texting rules](setter-daily-checklist.md#texting-rules-all-priorities):

- **Call before text** when opening a new lead in the dialer.
- If the lead has **not been texted** after contact → send follow-up SMS per lead messaging doc (do not skip).
- If someone **texts back while you’re dialing**, reply with value, then **return to outbound** — the whole block does not stop unless you’re moving to a live call or a watchshift interrupt.
- **No long objection threads over text** — steer to a call; use [Objection Handling Hub](objection-handling-hub.md) for angles.
- **Pre-demo SMS** that needs Gabriel or a high-value founder answer → [Watchshift SMS rules](sop-watchshift.md#sms-responses-pre-demo) (tag Gabriel, do not guess).

---

## Pipeline stages and outcomes

Update the **GHL pipeline stage** on every lead you work in this block (not only call tags in a note). End of day: pipeline cleared per checklist.

| Outcome | Pipeline / action |
|---------|-------------------|
| Strong lead, not booked yet, worth prioritizing | Stage: **Setter quality lead** + note why + task |
| Qualified → intro on setter calendar | Book per intro script (BAMFAM); stage reflects booked intro |
| Qualified → demo with closer booked | Stage reflects demo booked; notes for closer |
| Not DFY fit | Route per [Disqualifying and Financial Qualification](disqualifying-financial-qualification.md) — Boot Camp or lost |
| Bad data / wrong number | Mark lost or bad lead per CRM convention + note |
| No answer, will retry tomorrow | Next Work Date = tomorrow + GHL task; Last Human Touch updates on attempt |

### Call attempt notes (optional layer)

If your workflow separates **stage** from **last attempt**, you may also log:

- Connected / no answer / voicemail left / bad number
- Same session rule: **stage + next step** must still be set before moving to the next lead

---

## Decision rules

- Work **DQ-1** top to bottom — one daily outbound queue, not Opportunities cherry-picking.
- **Touch today** (call/SMS) → Last Human Touch auto-updates → out of DQ-1 for the day.
- **Snooze** → Next Work Date + task when deferring without a full close.
- Do not skip P1–P4 to “just finish dials.”
- Connected leads use acquisition intro script — **not** fulfillment call-center scripts ([Call Center index](../../client-fulfillment/call-center/README.md)).
- Quality pre-demo lead → **Setter quality lead** stage (same definition as [Watchshift SOP](sop-watchshift.md#sms-responses-pre-demo)).
- Objections on text → short steer to book/call; escalate to Gabriel only when watchshift SMS escalation applies.

## Escalation

| Situation | Action |
|-----------|--------|
| Pre-demo SMS / quality lead needs Gabriel | Tag Gabriel + GHL task — [Watchshift SMS](sop-watchshift.md#sms-responses-pre-demo) |
| Pricing, policy, founder-only | Tag Gabriel + GHL task |
| Dialer outage, line, or delivery failure | Gabriel / ops |
| Bad-number spike | Flag Gabriel / data owner |

## Quality bar

- Every worked lead has **notes + pipeline stage + next step** before the next dial.
- No “called only” records — text follow-up when the file has no SMS and outreach is due.
- Dial blocks favor speed **without** empty dispositions at EOD.
- Texting does not stall the block unless interrupt rules apply.

## Metrics

- Dials per block
- Connect rate
- Qualified rate
- Booked rate from connects
- % leads with stage updated same session
- Bad-number rate

## Related Docs

- [Setter Daily Checklist](setter-daily-checklist.md) — P5
- [Watchshift SOP](sop-watchshift.md) — interrupts + pre-demo SMS
- [Intro Call Script](script-intro-call-basic.md)
- [Intro Call Qualification Framework](intro-call-qualification-framework.md)
- [Disqualifying and Financial Qualification](disqualifying-financial-qualification.md)
- [Objection Handling Hub](objection-handling-hub.md)
- [Setter Lead Messaging](setter-lead-messaging.md) — value-based SMS + notes discipline
- [EOD Report SOP](eod-report-sop-setters-closers.md) — pipeline cleared
- [GHL Pipeline And Disposition Reference](ghl-pipeline-disposition-reference.md) — DQ-1 build spec + Next Work Date rules
- [Client Fulfillment — Call Center](../../client-fulfillment/call-center/README.md) — out of scope

## Open Questions

- [ ] Confirm retry-day schedule after day 1 (ops).
- [ ] Confirm whether voicemail is required on every no-answer or only attempt 3.
- [x] Document full GHL pipeline stage list in one disposition reference — see [GHL Pipeline And Disposition Reference](ghl-pipeline-disposition-reference.md) (draft, 2026-06-10).
