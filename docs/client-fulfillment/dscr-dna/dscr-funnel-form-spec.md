---
title: DSCR Funnel Form Spec
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-03
review_cycle: monthly
artifact_type: spec
---

# DSCR Funnel Form Spec

> **DRAFT — REFINANCE ONLY · DISQUALIFY-FIRST.** The lead-intake form for the DSCR funnel, built in
> **Perspective** and integrated to the **DSCR Snapshot** GHL sub-account. Every question exists to
> **disqualify** an unfit prospect (or surface a deal-killer) — no decorative fields. Inherits the offer,
> voice, and compliance from [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md) and replaces the
> longer opt-in form in [DSCR Landing Page And VSL Copy](dscr-landing-and-vsl.md). Passes
> [DSCR Compliance Guardrails](dscr-compliance-guardrails.md).

## Purpose

Define the disqualification-focused questions for the DSCR lead form so the team builds one lean Perspective
funnel that screens out unfit prospects before they consume loan-officer time.

## Scope

The Perspective opt-in form questions, their answer options, the disqualification logic behind each, and the
GHL custom-field mapping (which fields already exist in the snapshot vs. which must be created). Does not
cover ads, landing/VSL hero copy, or the Laura nurture (see related docs).

## Trigger

Building or revising the DSCR lead funnel; creating fields in the DSCR Snapshot.

## Inputs

- Disqualifiers and program thresholds: [Intelligence DSCR Product](intelligence-dscr-product.md)
- Offer, CTA ladder, canonical questions: [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md)
- Build steps: [Perspective Funnel Setup SOP](../media-buying/perspective-funnel-setup-sop.md)

## Outputs

- A built, mapped, published Perspective funnel feeding qualified DSCR leads into the DSCR Snapshot.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Refinance only · business-purpose · investment property only. No purchase / down-payment framing.
- Form ranges are for qualification capture (not pricing) — keep client-facing **marketing** copy number-free.

## Operating Content

### Design principle — disqualify-first

Keep the form lean. Every question must map to a real DSCR refinance deal-killer, so unfit prospects are
screened (or flagged) rather than booked. Ownership is **not** asked directly — anyone who answers the
property value / balance / rent questions has self-identified as an owner, so an explicit "do you own it?"
question is redundant friction and is omitted.

### The questions (disqualifier set)

| # | Question | Answer options | Disqualifies when… |
|---|----------|----------------|---------------------|
| 1 | **What best describes this property?** | Primary residence (where I live) · Second / vacation home · Investment or rental property | Primary residence or Second home → **DQ** (DSCR is investment / non-owner-occupied only) |
| 2 | **What state is the property in?** | Dropdown (US states) | Outside the LO's licensed states → **DQ** (internal check) |
| 3 | **Estimated credit score** | Below 620 · 620–659 · 660–699 · 700–739 · 740+ | Below ~620 → **DQ** (credit floor); bands also tier pricing |
| 4 | **Approx. property value** | Ranges | Under ~$100k often below lender loan minimums → **DQ / weak** |
| 5 | **Approx. amount still owed (est. balance)** | Ranges | Paired with value = equity/LTV. Owing more than ~75% of value → **no cash-out room (DQ for cash-out)** |
| 6 | **Reserves / liquidity available** | No reserves · Under $25k · $25k–50k · $50k–100k · $100k+ | "No reserves" → **yellow/red flag** (lenders want ~3–6 months PITIA) |
| 7 | **Roughly what does it rent for per month?** | Ranges | Rent below the property's payment (DSCR < 1.0) → **DQ** (the silent killer: DSCR = rent ÷ PITIA) |

Plus contact + TCPA consent on the final step (name, email, phone, consent checkbox) per
[DSCR Landing Page And VSL Copy](dscr-landing-and-vsl.md).

> **Reserves wording note:** the reserves question is reframed for **refinance** — there is **no down
> payment** on a refi. Ask about reserves/liquidity (months of payment on hand), never "% down."

### GHL custom-field mapping (DSCR Snapshot)

Perspective → GoHighLevel mapping happens at integration (see SOP step 3). New fields **must exist in the
DSCR Snapshot before mapping**, or the integration breaks.

| Form question | GHL field | Status in DSCR Snapshot |
|---------------|-----------|-------------------------|
| Property use / occupancy | `property_use` | **Create (new)** |
| Property state | `state` (standard) | Exists |
| Estimated credit score | `credit_score_range` | **Create (new)** |
| Approx. property value | `property_value` | Exists (already in snapshot) |
| Approx. amount still owed | `est_balance` | Exists (already in snapshot) |
| Reserves / liquidity | `reserves_liquidity` | **Create (new)** |
| Monthly rent | `monthly_rent` | **Create (new)** |

*(Field API names illustrative — confirm/standardize against the snapshot's existing naming.)*

### Build outline (Perspective)

Follow [Perspective Funnel Setup SOP](../media-buying/perspective-funnel-setup-sop.md):
1. Duplicate the funnel template; rename for the DSCR client; set branding/logo/footer (company, MLO, NMLS).
2. Replace the opt-in questions with the disqualifier set above; set the occupancy question as an early screen.
3. Integrate GoHighLevel → **DSCR Snapshot**; map all fields (create the 4 new fields first); add the entry tag.
4. Integrate Meta Pixel; fire the `lead` event on the final-step button click.
5. Publish to the DSCR domain/slug; paste the live URL into the ClickUp task.

### Compliance

- Investment / business-purpose, refinance only — occupancy question hard-screens primary + second homes.
- No pricing/figures in marketing copy; form ranges are qualification capture, not quotes.
- TCPA/CAN-SPAM consent captured on the final step; honor STOP/HELP downstream (Laura).
- Confirm consent + business-purpose footer wording with counsel before traffic.

## Related Docs

- [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md)
- [DSCR Landing Page And VSL Copy](dscr-landing-and-vsl.md)
- [DSCR Lead Nurture And Booking — Laura](dscr-nurture-and-booking-laura.md)
- [Intelligence DSCR Product](intelligence-dscr-product.md)
- [Perspective Funnel Setup SOP](../media-buying/perspective-funnel-setup-sop.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)
