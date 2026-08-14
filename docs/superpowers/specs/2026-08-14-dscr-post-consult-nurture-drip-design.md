---
title: DSCR Post-Consult Nurture Drip — Design
domain: client-fulfillment
subdomain: dscr-dna
owner: founder
status: draft
last_updated: 2026-08-14
review_cycle: monthly
artifact_type: sequence
related_docs:
  - docs/client-fulfillment/dscr-dna/dscr-nurture-and-booking-laura.md
  - docs/client-fulfillment/dscr-dna/dscr-compliance-guardrails.md
  - docs/client-fulfillment/dscr-dna/dscr-objection-handling-guide.md
  - docs/client-fulfillment/dscr-dna/intelligence-icp-dscr.md
  - docs/client-fulfillment/client-marketing/playbook-nurture-framework.md
---

# DSCR Post-Consult Nurture Drip — Design

## Purpose

Close the gap **after a completed LO consult** when the investor did not apply.
Clients currently lose these people to ghosting, comparison-shopping, and
forgotten follow-up. This sequence is an automated, long-term SMS drip from the
**loan officer** that keeps trust with value — not a booking chase.

Canonical implementation (after this spec is approved) lives at:

`docs/client-fulfillment/dscr-dna/dscr-post-consult-nurture-drip.md`

It sits beside [Laura new-lead nurture](../../client-fulfillment/dscr-dna/dscr-nurture-and-booking-laura.md).
Laura owns opt-in → book → show. This drip owns **consult complete → application**.

## Problem

- Pre-book drips exist. Post-consult drips do not.
- Automation cannot reliably know the last live-call timestamp.
- LO first-person chase texts ("just checking in") feel needy and get muted.
- Investors stall on beliefs (rate vs equity, docs, conventional cap, timing),
  not because they forgot the LO exists.

## Audience

**DSCR refinance investors** who already completed an LO consult (numbers
walked, options discussed) and left without applying. Reusable for every
spoken-with lead on that disposition — not a per-file custom sequence.

**User of the asset:** Waiz CS installs in GHL; the LO dispositions after the
consult and replies when someone texts back.

## Scope

| In | Out (v1) |
|----|----------|
| SMS-only, LO first person | Email, Laura/assistant sender |
| Enroll 3 days after post-consult disposition | Trigger off actual call timestamp |
| 13 weekly texts (~90 days from disposition) | 90-day RM-style high-volume arc |
| Mix of education + composite case studies | Per-lead consult-note merge fields |
| Exit on reply / apply / rebook / STOP | Pre-book Laura drip, no-show reminders, BAMFAM on the call |
| Cloneable GHL workflow + OS copy | Booking link on every text |

Refinance / investment property only. No purchase angles.

## Trigger and clock

1. LO (or VA) dispositions the contact as **consult complete, no application**
   (tag or pipeline stage — one enrollment signal).
2. Workflow waits **3 days**.
3. If still eligible, send Week 1. Then **one SMS every 7 days** through Week 13.

The clock is **disposition time**, not conversation time. Copy must never claim
"yesterday's call," "Tuesday," or any recency the system cannot know.

Suggested enrollment signal: tag `dscr-post-consult` **or** a dedicated LO
pipeline stage with the same meaning. Pick one per client snapshot; do not
require both.

## Eligibility (must all be true at send)

- Post-consult disposition present
- No application in (started or submitted)
- No follow-up consult on the calendar
- Not in Laura pre-book / no-show workflows
- SMS consent on file; not STOP'd

## Exits (kill workflow immediately)

| Event | Action |
|-------|--------|
| Any inbound SMS | Stop drip; notify LO; human thread |
| Application started/submitted | Stop drip |
| New consult booked | Stop drip |
| STOP / opt-out | Stop drip; honor immediately |
| Re-dispositioned into a live deal | Stop drip |

**Re-enroll** only after a **new** completed consult with no application.
Silence alone never re-enrolls.

## Cadence

| Item | Rule |
|------|------|
| Channel | SMS |
| Count | 13 messages |
| Spacing | 7 days between sends |
| First send | Disposition + 3 days |
| Last send | Disposition + 3 + 84 days ≈ 87 days |
| Window | Quiet hours ~8am–9pm lead local time |
| Volume | One idea per text; never two texts in one week |

## Sequence architecture (belief arc)

Each week moves **one** post-consult stall. Alternate education and case study.
Most weeks have **no CTA**. Soft reply-ask only on weeks **5, 9, 13**.

| Week | Type | Belief | Content |
|------|------|--------|---------|
| 1 | Education | Pain / trapped equity | Something noticed on *their* file — equity idle. Not a follow-up ping. |
| 2 | Case | Desire | **Marcus** — scaler. Cash-out on a rental already owned, capital into the next deal. |
| 3 | Education | Docs / write-offs | Rent qualifies the loan, not tax returns. |
| 4 | Case | Trust | **Dana** — self-employed. Conventional said no; property cash flow was the file. |
| 5 | Education | Cost | Rate-in-a-vacuum vs cost of sitting equity or a balloon. Soft CTA. |
| 6 | Case | Timing (calm) | **Chris** — hard-money / balloon, refinanced before it got expensive. No guaranteed close date. |
| 7 | Education | Conventional cap | Financed-property cap is a bank rule, not a DSCR rule. |
| 8 | Case | Entity | **Priya** — refinanced in the LLC; didn't unwind the structure. |
| 9 | Education | Qualify | Rent vs the property's payment. Soft CTA to look again. |
| 10 | Case | STR income | **Jordan** — Airbnb. Conventional couldn't read the income. |
| 11 | Education | Wait-for-rates | Waiting is a decision too. Peer, not scare. |
| 12 | Case | Second look | **Sam** — almost signed with the retail bank; ran it as an investor deal. |
| 13 | Value + door | Support | Last useful note. Easy reply. No "closing your file," no last chance. |

Case-study first names above are **locked composites** for v1. Clients may swap
in a real, approved funded story later. Education weeks stay generic so one
sequence fits every post-consult lead.

## Voice

- LO, first person. Casual. Looks thumbed out, not designed.
- First-name basis. Use `{{contact.first_name}}` in the opener **or** the
  "reminded me of you" line — not both every week.
- Recurring texture: *saw / ran into / just got off a file that reminded me of
  you when we went over yours.*
- One idea. Short. Lowercase allowed. Questions used sparingly.
- Case studies: first name only, no last name, no city unless a later real story
  is approved. One situation + one outcome in investor language.
- Tie-back must stay generic enough for every enrollee.

### Banned

- Just checking in / circling back / bumping this / still interested
- Closing your file / last chance / don't want to bug you
- Recency claims the CRM cannot prove
- Rates, payments, LTV, approvals, guarantees, close-by dates
- Tax/legal advice (route to their CPA/attorney if it comes up in replies)
- Laura, "the team," bot identity
- Two CTAs or a booking link on education/case weeks other than 5, 9, 13

### Soft CTAs (weeks 5, 9, 13 only)

Reply-based, e.g. want me to look at it again? A reply exits the drip and
notifies the LO.

## Compliance

All copy passes [DSCR Compliance Guardrails](../../client-fulfillment/dscr-dna/dscr-compliance-guardrails.md):

- Business-purpose refinance / investment only
- No invented pricing or program numbers
- Composite stories, not fabricated funded stats
- No comparative "we'll beat your bank" claims (week 12 is a second set of eyes,
  not a beat-rate claim)
- TCPA: consent already captured at original opt-in; honor STOP; quiet hours
- Counsel flag on AI: this sequence is **LO-attributed SMS**, not Laura. Do not
  disclose or imply a bot in the copy. If a client later automates send-as-LO
  from GHL, that is a send-channel fact, not a persona.

## GHL / ops

1. Snapshot workflow: wait 3 days → 13 SMS with 7-day waits → done.
2. Enrollment from one disposition signal.
3. Goal/exit conditions on reply, apply, appointment, STOP, live-deal stage.
4. Inbound reply: remove from this workflow; Slack/SMS/GHL notification to the LO.
5. Do not dual-enroll with Laura Sequences 1–6.
6. Clients clone the workflow; they do not rewrite the arc. They may replace
   composite names with approved real stories.

LO daily job after a consult: disposition. They do not remember to nurture.

## Success criteria

- Spoken-with, no-app leads stay in a system without LO memory
- Texts read as 1:1 continuation, not a campaign
- Reply rate over apply-CTA rate is the leading indicator
- Unsub / STOP stays in normal SMS range (not a spike vs Laura drip)
- CS can install from one OS doc + one GHL clone

## Testing

- Test contact: disposition → no send for 3 days → week 1 fires
- Reply after week 2 kills remaining sends and notifies LO
- Application / new appointment kills remaining sends
- STOP honored
- Quiet-hours skip (does not send at 11pm)
- Contact still in Laura pre-book does **not** enroll
- Copy review: no banned phrases, no pricing, no false recency

## Related docs

- [Nurture Framework](../../client-fulfillment/client-marketing/playbook-nurture-framework.md) — ghost ≠ gone; one belief per touch; volume without neediness
- [Laura nurture](../../client-fulfillment/dscr-dna/dscr-nurture-and-booking-laura.md) — upstream; do not merge
- [DSCR objections](../../client-fulfillment/dscr-dna/dscr-objection-handling-guide.md) — belief list behind the arc
- [ICP DSCR](../../client-fulfillment/dscr-dna/intelligence-icp-dscr.md) — archetypes for case studies
