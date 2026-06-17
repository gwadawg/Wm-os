---
title: DSCR KPI And Test Scorecard
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: reference
---

# DSCR KPI And Test Scorecard

> **DRAFT.** How we judge the DSCR refinance test: per-stage KPIs, the lead-quality bar, and the
> decision rules for killing/scaling. **Targets are placeholders to set with the media buyer** — RM
> benchmarks do **not** transfer (different audience, Special Ad Category, CPMs, sales cycle). Internal
> metrics doc; the "no pricing in copy" rule is about ads, not these internal numbers.

## Purpose

Define what "working" means for the DSCR funnel so the team can judge the test on data, not vibes — and know when to kill, iterate, or scale.

## Scope

Funnel measurement from ad impression → closed refinance, plus the lead-quality definition and decision rules.

## Trigger

Test launch; weekly review thereafter.

## Inputs

- Ad/funnel data (Meta/Google, GoHighLevel, calendar), close data from the LO.

## Outputs

- A weekly scorecard, kill/scale decisions, and a winning-angle shortlist.

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Decisions are data-driven and tied to the [funnel map](dscr-offer-and-funnel-map.md) stages.

## Operating Content

### Funnel KPIs by stage

| Stage | Metric | What it tells you | Target |
|-------|--------|-------------------|--------|
| Ad | CPM, CTR, hook-rate (3s views) | Is the creative stopping the scroll? | `[set]` |
| Ad → page | CPC, landing-page CTR | Is the click intent-rich? | `[set]` |
| Landing | Opt-in / form-completion rate | Does the offer + page convert? | `[set]` |
| Lead | **Cost per lead (CPL)** | Blended efficiency | `[set]` |
| Lead quality | **% refi-ready** (passes §4 below) | Are we buying real investors, not tire-kickers? | `[set]` |
| Booking | Lead → booked-call rate | Is Laura/setter converting leads? | `[set]` |
| Show | Booked → showed rate | Reminder/confirm system working? | `[set]` |
| Close | Showed → funded refinance | LO close + program fit | `[set]` |
| Economics | **Cost per funded loan**, ROAS | The number that actually matters | `[set]` |

> Set targets by working backward from the LO's average commission per funded DSCR refinance and an acceptable cost per funded loan. Do not import RM's CPL/CPA.

### Lead-quality bar (a "qualified DSCR lead")

A lead counts as **refi-ready** only if it passes the canonical [refi-readiness questions](dscr-offer-and-funnel-map.md):

1. **Owns** the investment property (refinance, not purchase).
2. It's investment / income-producing (business-purpose, not primary residence).
3. Has a refinance reason (cash-out / lower payment / exit balloon / move to LLC).
4. Plausible equity and the property is in a **licensed state**.

Leads failing 1–2 are **disqualified** (out of scope), not "low quality" — track them separately so they don't distort CPL.

### Creative decision rules (Andromeda / concept-led)

- **Judge on the funnel, not vanity metrics.** A high-CTR ad that produces unqualified leads loses to a lower-CTR ad that books refi-ready investors. Weight toward **CPL at acceptable lead quality** and, once volume allows, **cost per booked/showed**.
- **Let an ad spend ~2–3× target CPL before judging** (set the figure with the media buyer).
- **Kill** concepts below the lead-quality or CPL bar; **scale** winners with variations (per the [ads playbook](dscr-ads-playbook.md)).
- Track **winning angle × persona** so the next creative batch leans into what books, not just what clicks.

### Weekly scorecard (template)

| Week | Spend | Leads | CPL | % refi-ready | Booked | Showed | Funded | Cost/funded | Top angle | Action |
|------|-------|-------|-----|--------------|--------|--------|--------|-------------|-----------|--------|
| | | | | | | | | | | |

### Pre-launch tracking checklist

- [ ] Meta/Google pixel + `lead` event firing on form submit (verified with a test lead)?
- [ ] UTM convention live (see [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md))?
- [ ] CRM tags for refi-ready vs. DQ vs. booked vs. showed?
- [ ] Calendar/booking events flowing back to the scorecard?
- [ ] Funded-loan outcomes reported back from the LO (close the loop)?

## Related Docs

- [DSCR Offer And Funnel Map](dscr-offer-and-funnel-map.md)
- [DSCR Ads Playbook](dscr-ads-playbook.md)
- [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md)
- [DSCR Lead Nurture And Booking — Laura](dscr-nurture-and-booking-laura.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)
