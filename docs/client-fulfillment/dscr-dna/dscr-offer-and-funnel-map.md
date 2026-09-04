---
title: DSCR Offer And Funnel Map
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: reference
---

# DSCR Offer And Funnel Map

> **DRAFT — REFINANCE ONLY · BUSINESS-PURPOSE.** Phase 0 anchor for the DSCR build. Every downstream
> asset (ads, landing/VSL, nurture, booking reminders, setter scripts) **must inherit the offer, CTA ladder,
> qualifying questions, and voice defined here.** Generic across clients; outbound conversational messaging
> is sent as **Laura, the loan officer's assistant**. **No pricing or specific figures in any copy.** All copy
> passes [DSCR Compliance Guardrails](dscr-compliance-guardrails.md).

## Purpose

Single source of truth for what the DSCR refinance funnel sells, what the click goes to, what gets booked, and the voice it's all delivered in — so every asset downstream stays consistent and doesn't get rebuilt.

## Scope

The end-to-end DSCR refinance lead funnel: offer, lead magnet/CTA ladder, journey map, canonical qualifying questions, and the Laura messaging identity. Generic LO template (no specific client).

## Trigger

Read before building any DSCR asset. Update here first if the offer, funnel, or voice changes.

## Inputs

- [Intelligence ICP DSCR](intelligence-icp-dscr.md), [GTM Brief](dscr-gtm-positioning-brief.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)

## Outputs

- The fixed reference every ad, page, sequence, and script anchors to.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Refinance only · business-purpose · no pricing/numbers in copy · no guarantees · licensed states only.

## Operating Content

### 1. The Offer (what we actually sell at the lead-gen stage)

The ad does not sell a loan — it sells a **next step**. The conversion event is a **booked consultation** with the loan officer (or a submitted refi-readiness request that the team books). The "offer" the investor opts in for is **clarity on their refinance**, framed number-free:

- **Core promise:** "See what your property qualifies for on its own income — without W-2s or tax returns."
- **Lead magnet / opt-in (pick one per campaign, all number-free):**
  - A **DSCR refinance review** ("see your refinance options on this property")
  - A **property-qualification check** ("see if your rental qualifies on its rent")
  - A **payoff/exit review** for bridge/hard-money/balloon borrowers ("map your exit before the balloon hits")
- **What it is NOT:** a quoted rate, a guaranteed amount, an instant approval, or a price. No numbers.
- **The conversion = the booked call.** Everything in the funnel exists to get a qualified investor to book that call (and show up).

### 2. The Funnel Map

```
[Ad: video / static]  → get the click (qualified investor, one persona/angle)
        ↓
[Landing page / VSL]  → present the offer, build competence, opt-in
        ↓
[Refi-readiness form] → capture lead + qualify (questions in §4)
        ↓
[Laura: nurture + booking]  → speed-to-lead, answer basics, book the call, remind/confirm
        ↓
[Booked consultation]  → loan officer runs the numbers, structures the refi, closes
```

| Stage | Asset | Job | Build phase |
|-------|-------|-----|-------------|
| Ad | video scripts + static briefs | Get the click | Phase 1 |
| Landing / VSL | page copy + VSL script | Get the opt-in; qualify | Phase 2 |
| Lead capture | refi-readiness questions (§4) | Capture + segment | Phase 2 |
| Nurture + booking | SMS/email drip; confirmation + reminders (Laura) | Book + show | Phase 3 |
| Sales conversation | setter script; objection guide | Book/qualify; hand to LO | Phase 4 |
| Measurement | KPI + scorecard | Judge the test | Phase 5 |

### 3. The CTA Ladder (per stage — all from the approved bank, number-free)

| Stage | Primary CTA | Notes |
|-------|-------------|-------|
| Ad (TOF/MOF) | "See If Your Property Qualifies" · "Run Your Numbers" | Low-friction, access-to-info framing |
| Ad (BOF) | "Get a DSCR Refinance Review" · "Talk to a DSCR Specialist" | Direct, book-a-call |
| Landing/VSL | "See My Refinance Options" → start refi-readiness form | One clear action |
| Nurture (Laura) | "Want me to grab a time with [LO]?" | Conversational, concierge |
| Reminder | "Confirm your call with [LO]" | Reduce no-shows |

No CTA promises pricing, approval, a rate, or a timeline. Use "may qualify," "see options," "in many cases."

### 4. Canonical refi-readiness qualifying questions

The master list. The **landing form**, **Laura's qualifying messages**, and the **setter script** all pull from this — do not invent divergent versions.

1. Do you currently **own** the investment property you want to refinance? *(No → not a fit; this line is refinance only.)*
2. Property type: single-family rental / 2–4 unit / condo / short-term rental / other.
3. Is it currently **rented / producing income**? (or STR revenue)
4. Rough property value and current loan balance — **ranges, no exact figures needed** (for equity/LTV sense only).
5. Current loan situation: conventional / **hard-money or bridge with a balloon** / free-and-clear / other.
6. Refinance goal: cash-out / lower or stabilize the payment / exit a balloon / move into an LLC.
7. Will you hold/refinance in an **LLC or entity**, or personally?
8. Property **state** (gates to the LO's licensed states — internal check).
9. Name, email, phone (+ TCPA/consent capture for SMS/email).

### 5. Messaging identity — "Laura, the loan officer's assistant"

All **outbound conversational** messaging (SMS, email nurture, booking confirmations, reminders, setter follow-up) is sent as **Laura**, the LO's assistant. (Ad creative stays in the brand/LO outcome voice; Laura is the human-touch follow-up layer.)

- **What Laura is (decided):** Laura is an **AI assistant** that runs the outbound drip. She is a **consistent buffer persona** — presented as "[LO]'s assistant," never using the LO's personal identity — so that if the AI errs, it does not put words in the client's mouth or misrepresent them personally.
- **Who Laura is:** the LO's helpful, organized assistant. Her job is to make the investor feel handled — answer simple logistics, gather the refi-readiness basics, and get them on the LO's calendar.
- **Tone:** warm, concise, concierge, peer-respectful (investors are busy operators — no fluff, no hype, no pressure). Text like a competent human assistant, not a marketing bot.
- **What Laura does:** confirm interest, ask the qualifying basics (§4), offer times, confirm + remind, re-engage no-shows. Speed-to-lead is her #1 job.
- **What Laura never does (hard limits):**
  - No quoting rates, LTV, payments, amounts, or approval — "[LO] will run your exact numbers on the call."
  - No guarantees ("may qualify," not "you qualify").
  - No tax/legal/financial advice — route entity/depreciation/1031 questions to the LO/their CPA.
  - No purchase or primary-residence framing — refinance/investment only.
- **AI disclosure (decided — but flagged for counsel):** the business has chosen **not to disclose Laura as AI**; she reads as a human assistant. This is a **regulated gray area** and must be reviewed per operating state before launch: **California B.O.T. Act (SB 1001)** (bot-disclosure for commercial transactions), **Utah AI disclosure** rules for regulated services (mortgage/lending qualifies), and **FTC UDAP / impersonation** standards. To limit risk: Laura stays a generic "assistant" buffer (never claims to be a specific named human, never affirmatively denies being automated), and **TCPA/CAN-SPAM consent + clear sender identity + opt-out ("reply STOP") are mandatory regardless** (these are separate from AI disclosure). See [DSCR Compliance Guardrails](dscr-compliance-guardrails.md). **Confirm with counsel per state before traffic.**

### 6. Compliance anchors (inherited by every asset)

- **Refinance only · business-purpose / investment property.** No purchase, no primary-residence/personal-use framing.
- **No pricing or specific figures in any copy.** Number-free.
- **No guarantees** of approval, rate, LTV, amount, or timeline.
- **No tax/legal/financial advice.** Route to LO/CPA/attorney.
- **Licensed states only;** confirm per-client, per-state before traffic.
- **Platform + outreach policy:** Meta Special Ad Category (Financial Products & Services); TCPA/CAN-SPAM consent + opt-out for SMS/email.
- **Substantiate all proof.** No fabricated testimonials/stats.

### 7. What downstream assets inherit from this doc

- **Ads (Phase 1):** the offer/promise, persona→angle map, ad CTA ladder.
- **Landing/VSL (Phase 2):** the offer presentation, the §4 qualifying questions, the opt-in CTA.
- **Nurture + reminders (Phase 3):** Laura's voice/limits, the booked-call goal, the §4 questions for qualifying.
- **Setter + objections (Phase 4):** the §4 questions, the booked-call goal, Laura handoff, compliance limits.
- **Measurement (Phase 5):** conversion = booked + showed; lead = passed §4 refi-readiness.

## Related Docs

- [DSCR DNA README](README.md)
- [Intelligence ICP DSCR](intelligence-icp-dscr.md)
- [GTM Brief](dscr-gtm-positioning-brief.md)
- [Campaign Master Angles](dscr-campaign-master-angles.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)
