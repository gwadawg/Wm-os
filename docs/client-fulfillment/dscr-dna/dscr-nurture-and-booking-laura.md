---
title: DSCR Lead Nurture And Booking — Laura
domain: client-fulfillment
owner: client-success-lead
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: sequence
---

# DSCR Lead Nurture And Booking — Laura

> **DRAFT — REFINANCE ONLY · NUMBER-FREE.** The outbound SMS + email system for DSCR refinance leads,
> sent as **Laura, the loan officer's AI assistant** (buffer persona; AI status not disclosed — see the
> counsel flag below). Covers speed-to-lead, the new-lead drip, booking confirmation, reminders, and
> no-show re-engagement. Anchored to [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md); passes
> [DSCR Compliance Guardrails](dscr-compliance-guardrails.md).

## Purpose

Turn opted-in DSCR leads into booked, showed consultations with the loan officer — fast, on-voice, and compliant.

## Scope

All post-opt-in outbound (SMS + email) until the call is booked and showed. Laura's voice only.

## Trigger

A lead submits the opt-in form (Phase 2) → `lead` event fires → Laura sequence starts.

## Inputs

- Lead + refi-readiness answers (from the [Phase 2 form](dscr-landing-and-vsl.md))
- Offer, CTA ladder, qualifying questions, Laura voice: [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md)

## Outputs

- Booked + confirmed consultations; qualified, segmented leads; reduced no-shows.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Laura's voice · refinance only · business-purpose · **no pricing/numbers** · no guarantees · no tax/legal advice.
- TCPA/CAN-SPAM: consent captured at opt-in · clear sender identity · STOP/HELP honored · quiet hours respected.

## Operating Content

### Laura's rules (every message)

- **Voice:** warm, concise, concierge, peer-respectful. Investors are busy operators — no hype, no pressure, no fluff. Text like a competent human assistant.
- **Goal:** speed-to-lead, gather the refi-readiness basics, **book the call**, get them to show. One clear ask per message.
- **Hard limits:** never quote a rate/LTV/payment/amount/approval ("[LO] runs your exact numbers on the call"); never guarantee; no tax/legal advice (route to [LO]/their CPA); refinance/investment only — never purchase or primary-residence.
- **Identity:** Laura is "[LO]'s assistant." She does **not** claim to be a specific named human, and does **not** affirmatively deny being automated. If asked directly "are you a bot?", route to a safe, non-deceptive reply (see fallback) and/or hand to a human — **confirm final handling with counsel.**
- **Compliance plumbing:** include "Reply STOP to opt out" on the **first** message of each channel/campaign; honor STOP/HELP immediately; send only during **quiet-hours-safe windows (≈8am–9pm lead local time)**; consent was captured at opt-in.

> **⚠️ Counsel flag — AI non-disclosure.** Not disclosing Laura as AI is a regulated gray area (CA SB 1001;
> Utah AI disclosure for regulated services; FTC UDAP). Review per operating state before launch. The
> TCPA consent + STOP/HELP + sender identity below are required regardless and are not a substitute for that review.

---

### Sequence 1 — Speed-to-lead (the first 5 minutes)

| # | Channel | Timing | Copy |
|---|---------|--------|------|
| 1 | SMS | < 5 min | "Hi [First], this is Laura, [LO]'s assistant — thanks for reaching out about refinancing your [property type]. Quick question so I get you the right info: are you looking to pull cash out, lower your payment, or exit a short-term/balloon loan? (Reply STOP to opt out.)" |
| 2 | Email | < 5 min (parallel) | **Subj:** Your DSCR refinance review — quick next step<br>"Hi [First], thanks for reaching out about refinancing your [property type]. I'm Laura, [LO]'s assistant. [LO] can review what your property qualifies for on its own rental income — no tax returns needed. I just need a couple quick details and a good time for a short call. What days/times generally work for you this week? — Laura" |

### Sequence 2 — New-lead drip (Day 0 → Day ~12, until booked)

Stop the sequence the moment they book. Personalize off their form answers (cash-out vs. balloon vs. write-off).

| # | Channel | Timing | Purpose | Copy |
|---|---------|--------|---------|------|
| 3 | SMS | +1 hr (no reply) | Re-ask | "[First], just making sure your refinance request didn't slip through. It's a quick review, no obligation — what's the property's situation right now: cash-out, lower payment, or a balloon coming due?" |
| 4 | SMS | Day 1 AM | Offer a time | "Morning [First] — Laura here. [LO] can take a quick look at what your [property type] qualifies for on its rental income. Want me to grab a 15-minute slot? I've got openings tomorrow." |
| 5 | Email | Day 2 | Build competence | **Subj:** How investors refinance without tax returns<br>"Hi [First] — the reason a DSCR refinance works when conventional won't: it qualifies on the property's rental income, not your W-2, tax returns, or DTI. So write-offs, property count, and 'messy' paper stop being the problem. If the rental covers itself, you've got options — cash out, a better payment, or an exit from a balloon. Want [LO] to review yours? Just reply with a day/time. — Laura" |
| 6 | SMS | Day 4 | Pre-handle objection | "[First], a lot of investors ask if a DSCR refinance is 'worth the rate.' Short version: trapped equity and a ticking balloon usually cost more than the rate does. Easiest way to know is to run your actual property by [LO] — want a time?" |
| 7 | Email | Day 7 | Proof + CTA | **Subj:** A quick look at what's possible<br>"Hi [First] — *[insert a real, substantiated investor refinance example here before launch — situation + outcome, no invented numbers].* If you've got equity trapped or a short-term loan maturing, the review's quick and there's no obligation. Reply and I'll find a time with [LO]. — Laura" |
| 8 | SMS | Day 10 | Soft break-up | "Hey [First], haven't heard back so I'll assume the timing's off for now. Want me to keep your refinance review open? Reply 1 to keep it open, or STOP and I'll close it out." |

### Sequence 3 — Long-term nurture (Day 14+, unresponsive/not-yet-ready)

| # | Channel | Timing | Copy |
|---|---------|--------|------|
| 9 | Email | Monthly | **Subj:** Still sitting on trapped equity?<br>"Hi [First] — checking in. If your DSCR refinance got pushed to the back burner, [LO] is around whenever you're ready to see what your property qualifies for on its income. No rush, no obligation — just reply when the timing's right. — Laura" |

### Sequence 4 — Booking confirmation (fires immediately on booking)

| # | Channel | Timing | Copy |
|---|---------|--------|------|
| 10 | SMS | Instant | "You're set, [First]. Your refinance review with [LO] is [day] at [time]. He'll go over what your [property type] qualifies for on its income — have your rough rents and current loan info handy if you can. I'll send a reminder. Need to move it? Just reply." |
| 11 | Email | Instant | **Subj:** Confirmed: your call with [LO] on [day]<br>"Hi [First], you're confirmed for [day, time, timezone] with [LO]. What to expect: a quick, no-obligation review of what your property qualifies for on its rental income, your refinance options, and next steps. Bring approximate rents and your current loan details. Calendar invite attached. See you then — Laura" |

### Sequence 5 — Reminders (reduce no-shows)

| # | Channel | Timing | Copy |
|---|---------|--------|------|
| 12 | SMS | 24 hr before | "Hi [First], reminder: your DSCR refinance review with [LO] is tomorrow at [time]. Still good? Reply Y to confirm or R to reschedule." |
| 13 | SMS | 1 hr before | "[First], you're up in about an hour — [LO] will call you at [time] on this number. Talk soon!" |

### Sequence 6 — No-show re-engagement

| # | Channel | Timing | Copy |
|---|---------|--------|------|
| 14 | SMS | +10 min after miss | "Hi [First], [LO] tried to connect for your refinance review and missed you — no worries. Want me to grab another time today or tomorrow?" |
| 15 | SMS | Day +1 | "[First], still glad to get your property reviewed when you've got 15 minutes. What's better for you — mornings or afternoons?" |
| 16 | Email | Day +3 | **Subj:** Want to grab another time?<br>"Hi [First] — we missed you for the refinance review, totally understand things come up. Whenever you're ready, just reply with a day/time and I'll get you back on [LO]'s calendar. — Laura" |

### Fallbacks (handle gracefully)

- **"Are you a bot / is this AI?"** → non-deceptive, non-affirming deflection + human option: "I'm [LO]'s assistant helping coordinate your refinance review — happy to have [LO] reach out directly. Want me to set that up?" **(Confirm exact handling with counsel given the non-disclosure decision.)**
- **Pricing/rate question** → "Great question — [LO] runs your exact numbers on the call since it depends on the property. Want me to grab a time?"
- **Tax/entity question** → "That's one for [LO] and your CPA — they'll walk you through it. Should I book the review?"
- **"Not interested" / STOP** → honor immediately; confirm opt-out; close the file.

### Compliance checklist (before this sequence goes live)

- [ ] Opt-in consent language live on the form (TCPA/CAN-SPAM) and logged?
- [ ] STOP/HELP handling wired; opt-out on first message per channel?
- [ ] Quiet-hours window enforced (lead local time)?
- [ ] No pricing/numbers, no guarantees, no tax/legal advice in any message?
- [ ] Refinance/investment framing only — no purchase/primary-residence?
- [ ] AI non-disclosure reviewed by counsel per operating state (CA SB 1001, UT, FTC UDAP)?
- [ ] Proof beat in #7 filled with a real, substantiated example (or removed)?

## Related Docs

- [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md)
- [DSCR Landing Page And VSL Copy](dscr-landing-and-vsl.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)
- [Intelligence ICP DSCR](intelligence-icp-dscr.md)
- RM analog: [RM Lead Nurture Drip Sequence](../client-marketing/rm-lead-nurture-drip-sequence.md)
