---
title: Client Fulfillment — DSCR DNA
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-05-30
review_cycle: quarterly
---

# Client Fulfillment — DSCR DNA

DSCR product, ICP, marketing doctrine, and compliance for **client** campaigns and all generated copy targeting real-estate investors.

**Load before any DSCR ad, SMS, email, or bot script.**

This pod was built by cloning the [Reverse Mortgage DNA](../reverse-mortgage-dna/README.md) pod per the [Product Launch Playbook](../../prompts/product-launch-playbook.md). **DSCR is the near-inverse of RM:** the borrower is a real-estate *investor* (not a retiree), and DSCR is typically **business-purpose lending** with a different compliance regime than consumer HUD/FHA. Do not assume RM framing carries over — see each doc.

**Scope — refinance only.** The Waiz DSCR line covers **refinance transactions only** (rate/term and cash-out refinances of investment property the borrower already owns). **No purchase financing or purchase angles.** All docs and downstream assets must assume the investor already owns the property.

## Canonical docs

| Doc | Status |
|-----|--------|
| [DSCR Compliance Guardrails](dscr-compliance-guardrails.md) | `draft` |
| [Doctrine DSCR](doctrine-dscr.md) | `draft` |
| [Doctrine DSCR Marketing](doctrine-dscr-marketing.md) | `draft` |
| [Intelligence ICP DSCR](intelligence-icp-dscr.md) | `draft` |
| [Intelligence DSCR Product](intelligence-dscr-product.md) | `draft` |
| [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md) | `draft` |

## Launch build (offer → ads → funnel → nurture → setter)

End-to-end DSCR refinance funnel assets. **Start at the offer/funnel anchor** — every asset below inherits its offer, CTA ladder, qualifying questions, and the **Laura (LO's assistant)** outbound voice.

| Doc | Phase | Status |
|-----|-------|--------|
| [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md) | 0 — anchor | `draft` |
| [DSCR Ads Playbook](dscr-ads-playbook.md) | 1 — ad creative | `draft` |
| [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md) | 1 — ad creative | `draft` |
| [DSCR Ad Creative — Batch 01](dscr-ad-creative-batch-01.md) | 1 — ad creative | `draft` |
| _landing page / VSL copy_ | 2 | _to build_ |
| _lead nurture + booking reminders (Laura)_ | 3 | _to build_ |
| _setter script + objection guide_ | 4 | _to build_ |
| _KPI + test scorecard_ | 5 | _to build_ |

## Status note

Every doc in this pod is `status: draft` pending owner review. Product mechanics (rates, LTV, DSCR tiers, credit floors) are **illustrative 2026 market ranges from public sources — not Waiz or client pricing**, and must be reconciled against the approved pricing sheet and active lender programs before client use. The compliance doc requires **licensed-counsel / compliance review** before any copy ships.

## Related

- [Product Launch Playbook](../../prompts/product-launch-playbook.md)
- [Reverse Mortgage DNA (mirror source)](../reverse-mortgage-dna/README.md)
- [Fulfillment Operating System](../fulfillment-operating-system.md)
- [Identity Core](../../company/doctrine-identity-core-april-26.md)
- [Source Of Truth Rules](../../SOURCE-OF-TRUTH.md)
