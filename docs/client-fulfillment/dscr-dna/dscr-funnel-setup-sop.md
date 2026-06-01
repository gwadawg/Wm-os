---
title: DSCR Funnel Setup SOP
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: sop
cloned_from: docs/client-fulfillment/media-buying/perspective-funnel-setup-sop.md, docs/client-fulfillment/media-buying/new-client-campaign-setup-sop.md
---

# DSCR Funnel Setup SOP

> **DRAFT — REFINANCE ONLY.** Stand up the lead funnel + Meta campaign for a DSCR client. The funnel
> qualifies investors on **refi-readiness** (already owns the property, has a refinance reason, has equity).
> **No purchase paths.** **No invented pricing** on the funnel. Confirm Special Ad Category, licensed states,
> and the publish domain with the owner before launch.

## Purpose

Configure the landing/VSL funnel (Perspective + GoHighLevel + Meta Pixel) and launch the first DSCR refinance campaign.

## Scope

Funnel tech setup, refi-readiness qualifying questions, and the new-client campaign launch.

## Trigger

Implementation phase after a DSCR client kickoff.

## Inputs

- Client branding, NMLS/entity + licensed-state list, approved offer + pricing sheet
- DSCR refinance qualifying questions (below), creative + copy from the [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md)

## Outputs

- Live funnel URL, integrated CRM + Pixel, a launched, QA'd refinance campaign

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Funnel + campaign pass [DSCR Compliance Guardrails](dscr-compliance-guardrails.md). Refinance only. Licensed states only. No invented pricing.

## Operating Content

### How this differs from the RM funnel (read first)

| RM funnel | DSCR funnel |
|-----------|-------------|
| Qualify 62+ homeowners on age + equity | Qualify **investors** on **refi-readiness** (owns property, refi reason, equity) — **no age** |
| Opt-in variants: "Remove Mortgage Payment" / "Cash Out" | Variants: **Cash-Out Refi** / **Rate-Term / Escape Hard-Money** |
| Special Ad Category: Housing | **Confirm Financial Products & Services (Credit)** treatment for the investor refinance offer |
| Consumer trust/testimonial framing | Investor **competence/proof** framing (funded refinances, DSCR fluency) |
| Footer: MLO + NMLS | Footer: MLO + NMLS **+ business-purpose disclosure** where applicable |

### 1. Funnel duplication and initial setup

- Duplicate the DSCR funnel template; rename to the client (e.g., "Client Name — DSCR Refinance").
- **Logo:** upload the client logo (transparent background); if none, generate a simple one.
- **Footer:** client company name, MLO name, **NMLS ID**, address, contact. Add the **business-purpose / investment-property** disclosure line from the guardrails where applicable. Copy the footer to the thank-you page.

### 2. Page customization

- **Opt-in page variants:** confirm both DSCR variants are present and refinance-framed — **Cash-Out Refinance** and **Rate-Term / Escape Hard-Money**. Remove any purchase/primary-residence language.
- **Qualifying questions (refi-readiness — core of the DSCR funnel):**
  1. Do you currently **own** the investment property you want to refinance? (Yes/No — No → disqualify; this line is refinance only.)
  2. Property type (single-family rental / 2–4 unit / condo / short-term rental / other).
  3. Estimated property value and current loan balance (for rough LTV/equity — **ranges**, not a quoted number).
  4. Current loan type/rate situation (conventional / **hard-money or bridge with a balloon** / free-and-clear / other).
  5. Approximate monthly rent or STR revenue (feeds the DSCR sense-check).
  6. Will you close in an **LLC/entity** or personally?
  7. Property **state** (gate to licensed states).
  8. Name, email, phone (lead capture).
- **Thank-you page:** replace testimonials with the client's **real, substantiated** funded-refinance proof (update names; never fabricate). Replace "Meet [Client]" bio + square headshot; update the "Learn More" button to the client site. Link/produce privacy policy + terms.
- **No pricing on the funnel** unless it's on the approved sheet and framed illustrative.

### 3. Integration

- **GoHighLevel:** activate the integration, select the client account, map custom fields (including the qualifying answers above), add the tag `external form` (or DSCR-specific tag), save.
- **Meta Pixel:** activate the Meta integration, paste Pixel ID + Access Token, map the `lead` event to the final-step submission, save.

### 4. Campaign launch (1-1-3 framework, DSCR refinance)

- **Campaign:** Objective **Leads**. **Special Ad Category — confirm Financial Products & Services (Credit)** treatment for this investor refinance offer (do not assume Housing). Budget: ABO, typical start ~$35/day (or client setting).
- **Ad set:** Conversion location **Website** (the funnel). Choose the correct DSCR Pixel. **Location = licensed state(s) only — no age, no interest/behavior layering** (creative is the targeting). 
- **Ads (3, distinct angles):** client Facebook Page; funnel URL; three creatives each on a different refinance angle from the [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md); primary text + headline from [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md). Follow the ad naming convention.

### 5. Publishing

- Publish the funnel to the **approved DSCR domain** (confirm with owner — do not reuse the RM `hecm.homequityhacks.com` domain). Set the URL slug to the client account name.
- Copy the live URL into the client's ClickUp account page.

### Pre-launch checklist

- [ ] Funnel is **refinance only** — no purchase/primary-residence paths or copy?
- [ ] Refi-readiness qualifying questions live and mapped to CRM?
- [ ] Licensed-state gating in place (funnel + ad set geo)?
- [ ] Special Ad Category set (Financial Products / Credit — confirmed)?
- [ ] No invented pricing anywhere on the funnel?
- [ ] Footer carries NMLS + business-purpose disclosure; proof is real/substantiated?
- [ ] **Meta Pixel installed**; **test lead** submitted and verified in GoHighLevel + Meta Events Manager?

## Related Docs

- [DSCR Ads Playbook](dscr-ads-playbook.md)
- [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md)
- [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)
- [Intelligence ICP DSCR](intelligence-icp-dscr.md)
- RM analogs: [Perspective Funnel Setup SOP](../media-buying/perspective-funnel-setup-sop.md) · [New Client Campaign Setup SOP](../media-buying/new-client-campaign-setup-sop.md)
