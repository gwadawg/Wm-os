---
title: DSCR Lead Nurture And Booking — Laura
domain: client-fulfillment
owner: client-success-lead
status: draft
last_updated: 2026-06-03
review_cycle: monthly
artifact_type: sequence
---

# DSCR Lead Nurture And Booking — Laura

> **DRAFT — REFINANCE ONLY · CASH-OUT FOCUS · SMS-ONLY · NUMBER-FREE.** The outbound **SMS** system for
> DSCR refinance leads, sent as **Laura, the loan officer's AI assistant** (buffer persona; AI status not
> disclosed — see the counsel flag below). This is a **single unified cash-out drip** (marketing is geared
> to cash-out refinances) — no per-goal segmentation, no email for now. Covers speed-to-lead, the cash-out
> drip, booking confirmation, reminders, and no-show re-engagement. Built for the **DSCR Snapshot** GHL
> sub-account (cloned from the reverse snapshot). Uses a **two-tier voice**: polished/competent for the
> first ~2 days, then rawer/human for the cold chase. Anchored to
> [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md); passes
> [DSCR Compliance Guardrails](dscr-compliance-guardrails.md).

## Purpose

Turn opted-in DSCR leads into booked, showed consultations with the loan officer — fast, on-voice, and compliant.

## Scope

All post-opt-in outbound **SMS** until the call is booked and showed. Laura's voice only. SMS-only for now
(email is out of scope until re-enabled). Single cash-out drip — no per-goal segmentation.

## Trigger

A lead submits the opt-in form (Phase 2) → `lead` event fires → Laura sequence starts.

## Inputs

- Lead + refi-readiness answers (from the [Phase 2 form](dscr-landing-and-vsl.md))
- Offer, CTA ladder, qualifying questions, Laura voice: [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md)

## Outputs

- Booked + confirmed consultations; qualified leads; reduced no-shows.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Laura's voice · refinance only · business-purpose · **no pricing/numbers** · no guarantees · no tax/legal advice.
- TCPA/CAN-SPAM: consent captured at opt-in · clear sender identity · STOP/HELP honored · quiet hours respected.

## Operating Content

### Laura's rules (every message)

- **Voice (two-tier):** warm, concise, peer-respectful — investors are busy operators, no hype, no pressure, no fluff. **Tier 1 (Day 0–2):** polished/competent, capitalized, sets the trust frame. **Tier 2 (Day 4+ cold chase):** rawer and more human — lowercase, casual, the occasional imperfect line — so it doesn't feel automated. Text like a competent human assistant either way.
- **Goal:** speed-to-lead, anchor the **cash-out** outcome (equity unlocked, qualify on the rent), **book the call**, get them to show. One clear ask per message.
- **Hard limits:** never quote a rate/LTV/payment/amount/approval ("[LO] runs your exact numbers on the call"); never guarantee; no comparative "we'll beat them" claims; no tax/legal advice (route to [LO]/their CPA); refinance/investment only — never purchase or primary-residence.
- **Identity:** Laura is "[LO]'s assistant." She does **not** claim to be a specific named human, and does **not** affirmatively deny being automated. If asked directly "are you a bot?", route to a safe, non-deceptive reply (see fallback) and/or hand to a human — **confirm final handling with counsel.**
- **Compliance plumbing:** include "Txt STOP to opt out" on the **first** SMS of the campaign; honor STOP/HELP immediately; send only during **quiet-hours-safe windows (≈8am–9pm lead local time)**; consent was captured at opt-in.

> **⚠️ Counsel flag — AI non-disclosure.** Not disclosing Laura as AI is a regulated gray area (CA SB 1001;
> Utah AI disclosure for regulated services; FTC UDAP). Review per operating state before launch. The
> TCPA consent + STOP/HELP + sender identity below are required regardless and are not a substitute for that review.

---

> **Merge fields (GHL):** `{{contact.first_name}}` = lead · `{{user.first_name}}` = the loan officer (LO) ·
> `{{appointment.date}}` / `{{appointment.time}}` = booked slot. Stop the drip the moment they book or reply
> STOP. Once a lead replies, the AI bot takes over to book; a VA steps in if the bot can't close.

### Sequence 1 — New-lead actions / speed-to-lead (the first 5 minutes)

Touch 1 is also the campaign's first SMS, so it carries the STOP opt-out.

| # | Tier | Timing | Copy |
|---|------|--------|------|
| 1 | Polished | < 5 min | "{{contact.first_name}}, Laura here with {{user.first_name}} — saw you're looking to pull cash out of the property. The good part: we qualify it on the property's rent, not your tax returns or DTI. Want me to have {{user.first_name}} run your actual numbers on a quick call? (Txt STOP to opt out)" |

### Sequence 2 — Cash-out drip (Day 0 → Day ~13, until booked)

Single unified cash-out drip. Tier 1 stays polished/competent; Tier 2 loosens into a rawer, human chase. Stop the moment they book.

| # | Tier | Timing | Purpose | Copy |
|---|------|--------|---------|------|
| 2 | Polished | +4 hr (no reply) | Re-ask | "No rush {{contact.first_name}} — just making sure your cash-out request didn't slip through. Easiest next step is 15 min with {{user.first_name}} to see what the property pulls. Want me to grab a time?" |
| 3 | Polished | Day 1 AM | Offer a time | "Morning {{contact.first_name}} — {{user.first_name}} can take a quick look at how much equity your property frees up on its rental income. I've got openings today and tomorrow — which works better, mornings or afternoons?" |
| 4 | Polished | Day 1 PM | Kill the blocker | "{{contact.first_name}}, generally when I don't hear back it's because someone already told you that you couldn't pull cash out — too many properties, write-offs, DTI. Just so you know, we qualify on the property's rent, not your tax returns." |
| 5 | Polished | Day 2 | Trapped equity | "Quick thing {{contact.first_name}} — every month that equity sits in the property, it's not working for you. {{user.first_name}} can show you what's pullable so you can redeploy it. Worth a 15-min look?" |
| 6 | Raw | Day 4 | Rate reframe | "{{contact.first_name}}, a lot of investors tell me the rate scares them off cash-out. honestly the bigger cost is leaving the equity stuck doing nothing. {{user.first_name}} can run it both ways so you see the real tradeoff — want a time?" |
| 7 | Raw | Day 5 | Bump | "hey {{contact.first_name}} just bumping this to the top so it doesn't get buried ^" |
| 8 | Raw | Day 6 | Pattern interrupt | "are my texts even coming through? lmk if this is a bad number for you" |
| 9 | Raw | Day 8 | Permission to close | "no hard feelings if the timing's off {{contact.first_name}} — just don't want to keep bugging you. you still looking to free up some of that equity, or should I close things out?" |
| 10 | Raw | Day 10 | Second opinion | "{{contact.first_name}} I'm cleaning up files from a couple weeks back and came across yours. still sitting on equity you want to pull out? if you're working with another lender it's worth a second set of eyes before you sign anything." |
| 11 | Raw | Day 13 | Soft break-up | "last one from me {{contact.first_name}} — I'll close your file for now so I'm not cluttering your phone. reply 1 if you want me to keep it open, otherwise no worries, you can always reach back out." |

### Sequence 3 — Long-term nurture (Day 30+, unresponsive/not-yet-ready)

| # | Tier | Timing | Copy |
|---|------|--------|------|
| 11b | Polished | Monthly | "{{contact.first_name}}, Laura here — no agenda, just checking in. if you're still sitting on equity you'd want to pull out down the road, {{user.first_name}} is around whenever the timing's right. reply anytime." |

### Sequence 4 — Booking confirmation (fires immediately on booking)

| # | Tier | Timing | Copy |
|---|------|--------|------|
| 12 | Polished | Instant | "You're set, {{contact.first_name}}. You're booked with {{user.first_name}} on {{appointment.date}} at {{appointment.time}}. He'll walk you through how much the property pulls on its rent and what your options look like. If you can, have rough rents and your current loan balance handy. I'll send a reminder — need to move it, just reply." |

### Sequence 5 — Reminders (reduce no-shows)

| # | Tier | Timing | Copy |
|---|------|--------|------|
| 13 | Polished | 24 hr before | "Hi {{contact.first_name}}, reminder: you're with {{user.first_name}} tomorrow at {{appointment.time}} to run your numbers. Still good? Reply Y to confirm or R to reschedule." |
| 14 | Polished | 1 hr before | "{{contact.first_name}}, you're up in about an hour — {{user.first_name}} will call you at {{appointment.time}} on this number. Talk soon." |

### Sequence 6 — No-show re-engagement

| # | Tier | Timing | Copy |
|---|------|--------|------|
| 15 | Raw | +10 min after miss | "hey {{contact.first_name}}, {{user.first_name}} tried to connect and just missed you — no worries. want me to grab another time today or tomorrow?" |
| 16 | Raw | Day +1 | "{{contact.first_name}}, still happy to walk you through what the property frees up when you've got 15 min — that equity's just sitting there in the meantime. mornings or afternoons better?" |
| 17 | Raw | Day +3 | "{{contact.first_name}} I'll keep your spot open through the week. want me to get you back on {{user.first_name}}'s calendar, or close it out for now?" |

### Fallbacks (handle gracefully)

- **"Are you a bot / is this AI?"** → non-deceptive, non-affirming deflection + human option: "I'm {{user.first_name}}'s assistant helping coordinate your cash-out review — happy to have {{user.first_name}} reach out directly. Want me to set that up?" **(Confirm exact handling with counsel given the non-disclosure decision.)**
- **Pricing/rate question** → "Great question — {{user.first_name}} runs your exact numbers on the call since it depends on the property. Want me to grab a time?"
- **Tax/entity question** → "That's one for {{user.first_name}} and your CPA — they'll walk you through it. Should I book the call?"
- **"Not interested" / STOP** → honor immediately; confirm opt-out; close the file.

### Compliance checklist (before this sequence goes live)

- [ ] Opt-in consent language live on the form (TCPA/CAN-SPAM) and logged?
- [ ] STOP/HELP handling wired; opt-out on the **first SMS** (touch 1)?
- [ ] Quiet-hours window enforced (lead local time)?
- [ ] No pricing/numbers, no guarantees, no tax/legal advice in any message?
- [ ] No comparative "we'll beat them" claims (touch 10 stays "second set of eyes")?
- [ ] Refinance/investment framing only — no purchase/primary-residence?
- [ ] AI non-disclosure reviewed by counsel per operating state (CA SB 1001, UT, FTC UDAP)?

## Related Docs

- [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md)
- [DSCR Landing Page And VSL Copy](dscr-landing-and-vsl.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)
- [Intelligence ICP DSCR](intelligence-icp-dscr.md)
- RM analog: [RM Lead Nurture Drip Sequence](../client-marketing/rm-lead-nurture-drip-sequence.md)
