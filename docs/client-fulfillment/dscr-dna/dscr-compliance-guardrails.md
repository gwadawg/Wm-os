---
title: DSCR Compliance Guardrails
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: doctrine
cloned_from: docs/client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md
---

# DSCR Compliance Guardrails

> **DRAFT — REQUIRES LICENSED-COUNSEL / COMPLIANCE REVIEW BEFORE CLIENT USE.**
> This document is built from public sources (FTC, CFPB, MBA, AAPL, lender guidelines) as of 2026.
> It is **not legal advice**. DSCR is generally **business-purpose** lending, but the exemptions are
> nuanced and state-specific. Confirm the regime per client, per state, with qualified counsel before
> any copy ships. This doc gates all downstream DSCR copy.

## Purpose

Non-negotiable compliance rules for AI and human copy on **business-purpose DSCR** campaigns. This is the most important divergence from RM: DSCR is *not* consumer HUD/FHA lending, so the rules change.

## Scope

All DSCR ads, SMS, email, landing pages, and bot scripts.

## Trigger

Any DSCR copy draft or review.

## Inputs

- See operating content below.
- Active lender program guidelines and the approved pricing sheet.
- Per-client licensed-state list and entity/borrower posture.

## Outputs

- Compliant copy, or an explicit human/counsel review flag.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- All DSCR client-facing copy must pass this doc's pre-flight check.
- No invented pricing — reference the approved pricing sheet only.

## Operating Content

### The core divergence from RM (read first)

| | Reverse Mortgage | DSCR |
|---|---|---|
| Purpose | **Consumer** (personal/family/household) | **Business** (income-producing investment property) |
| Headline regime | HUD/FHA HECM, TILA/RESPA, required counseling | Business-purpose; TILA/RESPA **generally do not apply** |
| Borrower | Natural person, age 62+ | Investor — often an **LLC/entity**; no age rule |
| RM-specific rules that DO NOT apply to DSCR | "No age in copy," "don't lead with product name," counseling disclosure | — |

**Do not carry RM compliance habits into DSCR.** The RM rules ("say retired homeowners, not 62+", "never say reverse mortgage in the headline") are artifacts of the *consumer/senior* regime and do **not** apply here. DSCR investors search "DSCR loan" directly; the product name is an asset, not a liability.

### 1. Business-purpose is the foundation — and it is not automatic

- DSCR loans on **non-owner-occupied investment property** are generally treated as **business-purpose**, which means TILA, RESPA/TRID, and the ATR/QM rule **generally do not apply**. TILA also exempts loans made to **non-natural persons** (entities/LLCs).
- The exemption is **nuanced**, not a checkbox. Reg Z applies a **5-factor business-vs-consumer purpose test**. Lenders typically require a signed **Certification of Business Purpose** and **Occupancy Certification** at closing.
- **Never** position or imply a loan is business-purpose to dodge consumer protections when the real use is personal — misclassification is illegal and can carry **criminal penalties**.
- **Copy rule:** marketing must speak to **investment / income-producing property** use. Avoid any framing that markets DSCR for a primary residence or personal/household use.

### 2. Consumer-exempt does NOT mean rule-free

Even where TILA/RESPA do not apply, the following still bind every DSCR ad:

- **FTC / state UDAP & CFPB UDAAP** anti-deception standards apply to advertising regardless of business-purpose status. Claims must be **truthful, substantiated, non-misleading**, evaluated on the ad's **overall net impression**. No misleading cost/rate/term claims; no bait-and-switch; disclose material limitations.
- **FTC Mortgage Acts and Practices (MAP / Reg N) advertising rule** governs deceptive mortgage advertising broadly. Treat rate, payment, and approval claims as high-risk.
- **State licensing varies.** ~32 states + DC require **no** lender license for business-purpose loans regardless of collateral; ~18 states do (examples: AZ/CA/NV for commercial collateral; OR/UT/MN/ID/GA for 1–4 family business-purpose; IA/KS/WA when collateral is the borrower's primary residence). **MLO/SAFE Act** licensing turns on each state's own MLO definition. **Per-client, per-state confirmation is mandatory before running traffic.**
- **Ad-platform policy:** Meta still requires the **"Financial Products & Services" Special Ad Category** for U.S. mortgage ads (targeting restrictions; proof of authorization). Google has financial-products ad policies. Platform policy applies even when federal consumer law does not.

### 3. Hard rules for every DSCR output

- **No guarantees.** Never guarantee approval, rate, LTV, DSCR qualification, loan amount, or closing timeline. Use "may qualify," "could," "in many cases," "subject to underwriting."
- **No invented numbers.** Any rate / LTV / DSCR / credit / reserve figure must come from the approved pricing sheet or current lender guidelines, and be framed as illustrative and program-dependent. See [Intelligence DSCR Product](intelligence-dscr-product.md).
- **Business-purpose framing only.** Investment property, rental income, portfolio — never primary-residence or personal-use framing.
- **No tax / legal / financial advice.** LLC vesting, 1031 exchanges, depreciation, and entity structuring are common DSCR topics — always direct prospects to their own CPA / attorney.
- **Substantiate proof.** Investor testimonials, "funded $X in Y days," and portfolio claims must be real, representative, and documented.
- **Respect licensing geography.** Do not advertise into states where the client is not authorized to lend/broker for the relevant collateral.

### 4. Pre-flight language check — run before every DSCR output

1. Does it market the property as an **investment / income-producing** asset (business-purpose), never personal/primary-residence use?
2. Are all numbers from the approved pricing sheet / lender guidelines, framed as illustrative and subject to underwriting — with **zero invented pricing**?
3. Does it avoid **guarantees** of approval, rate, or terms ("may qualify," not "you qualify")?
4. Is it **truthful and substantiated** under UDAP/UDAAP — no misleading net impression?
5. Does it stay within **licensed states** and platform ad-policy (e.g., Meta Special Ad Category)?
6. Does it avoid **tax/legal/financial advice** and route entity/1031/tax questions to a qualified professional?

If any answer is no, the output is **not ready** — flag for human/counsel review.

## Related

- [DSCR DNA README](README.md)
- [Doctrine DSCR](doctrine-dscr.md)
- [Doctrine DSCR Marketing](doctrine-dscr-marketing.md)
- [Intelligence DSCR Product](intelligence-dscr-product.md)
- [Intelligence ICP DSCR](intelligence-icp-dscr.md)
- RM analog (do not apply RM rules to DSCR): [RM Compliance Guardrails](../reverse-mortgage-dna/rm-compliance-guardrails.md)

### Sources (public, 2026 — for the draft compliance summary above)

- MBA, *Application of Consumer Laws to Commercial / Business-Purpose Mortgage Lending* (white paper)
- Hunton, *Navigating the Regulatory Compliance Environment* (business-purpose exemptions; Reg Z 5-factor test)
- AAPL, *Mortgage Lender Licensing — What You Need to Know* (state business-purpose licensing map)
- Doss Law, *Business Purpose Exemption Simplified* (Reg Z purpose test)
- FTC *Mortgage Acts and Practices — Advertising Rule (Reg N / 16 CFR 1014)*; FTC Deception Policy Statement
- CFPB, *UDAAP Examination Procedures*
- Lender DSCR program guidelines (Certification of Business Purpose + Occupancy Certification practice)
