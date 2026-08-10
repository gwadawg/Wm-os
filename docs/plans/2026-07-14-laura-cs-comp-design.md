---
title: Client Success Comp Design — Laura
domain: operations
subdomain: people
owner: founder
status: active
confidentiality: owner-only
last_updated: 2026-07-15
review_cycle: quarterly
artifact_type: policy
structure_lock: phase-1-final
cash_live: after-shadow-eom
related_docs:
  - docs/operations/people/client-success-role-scorecard.md
  - docs/operations/people/client-success-daily-os.md
  - docs/company/product-margin-model.md
  - docs/company/reflections/2026-q3-pricing-retention-analysis.md
---

# Client Success Comp Design — Laura

## Purpose

Phase 1 pay design for Laura (Client Success): **stable base + uncapped retention
commissions** that scale with healthy logos, easy to calculate at month-end, and
aligned with DFY margins so raises are earned — not gifted.

**North star:** pay her for keeping clients as **full-freight paying** logos past
the danger window, with bigger checks at milestones and smaller trailers after
(hardest work is early stickiness, not long-tenure cruise).

## Status

**LOCKED — Phase 1 structure active** (2026-07-15).

Cash commissions do **not** pay until one **shadow EOM** month is run on the
closed roster and founder signs off. Until then: base continues as today;
commissions are calculated for practice only. Do not change the Phase 1 table
without a quarterly review note.

## Scope

| In | Out (for now) |
|---|---|
| Laura — Client Success base + stickiness commissions | Temporary clean-onboarding bonus (separate when activated) |
| DFY + mid-tier (lower rates) | Guaranteed large base with no performance layer |
| Paid-month eligibility rules | Ad-KPI or funded-loan bonuses |

## Design principles

1. **Base near today** — seat pay for cadence, rollup, payroll, people ops.
2. **Performance scales with the book** — more logos past stickiness → more pay;
   **no hard monthly dollar cap**.
3. **Milestone-up / trailer-down** — bigger payday when a logo clears the
   stickiness mark (and 2× that mark); smaller recurring while they stay
   full-freight. Not reversed (do not pay more merely because tenure is longer /
   work is lighter).
4. **Cash truth** — discounts, extensions, and short-pays do not count as paid
   months for commission.
5. **Easy EOM** — roster + ledger tags only.
6. **Quarterly knobs** — stickiness mark, rates, and optional logo-count tiers
   adjust **quarter to quarter** with 30 days’ notice — not mid-month.

## V1 structure (monthly) — FINAL Phase 1

| Component | Amount | Notes |
|---|---|---|
| Base | **$1,530** | Fixed; unconditional |
| Stickiness commissions | **Uncapped** | Per-logo milestones + trailers (below) |
| Scorecard gate | All commissions | Month scorecard **≥ B** or commissions = **$0** |
| Logo-count tier multiplier | **Off** in Phase 1 | May turn on at a later quarterly review |
| Clean onboard bonus | Out of this plan | Separate time-boxed policy when activated |

## Stickiness model — FINAL Phase 1

### Stickiness mark

| Term | Meaning | Phase 1 lock |
|---|---|---|
| **Stickiness mark** | Consecutive full-freight paid months to first milestone | **3** |
| **Second mark** | Always **2 × stickiness mark** | **6** |

Founder may change the stickiness mark (and thus the second mark) **once per
quarter**, with **30 days’ written notice** before the effective month.

No Month-9 / Month-12 bumps in Phase 1.

### Pay events per logo — FINAL Phase 1 dollars

| Event | When | DFY | Mid-tier (50%) |
|---|---|---:|---:|
| **First milestone** | First month the logo completes the stickiness mark | **$50** | **$25** |
| **Post-first trailer** | Each later month while streak continues, until the second milestone | **$30** | **$15** |
| **Second milestone** | First month the logo completes the second mark | **$100** | **$40** |
| **Post-second trailer** | Each later month while still full-freight consecutive | **$50** | **$20** |

**Rules:**

- Milestone fires **once** per logo per milestone.
- Trailer pays **every qualifying month** after the relevant milestone.
- Month of the second milestone: pay **milestone only** (no post-first trailer
  same month).
- Amounts may move at quarterly review; shape stays.

### Optional later — logo-count tiers

Off in Phase 1. If enabled later, trailer (or all) rates multiply by stickiness
logo count bands (1–8 / 9–15 / 16+); mid-tier logos count as 0.5 toward the band.

## What counts as a full-freight paid month

A calendar month counts toward the consecutive streak **only if all** of:

1. Logo is in the stickiness pool (DFY or mid-tier per roster).
2. Waiz **collected** cash for that month’s retainer.
3. Collected amount **≥ contracted retainer** for that logo for that month.
4. No active **billing extension / pause** covering that month.
5. No **refund or chargeback** that voids that month’s cash.

### Edge cases (locked)

| Situation | Counts? | Effect on streak |
|---|---|---|
| Paid full contracted retainer on time | **Yes** | Continues / advances |
| Discount to retain (below contracted retainer) | **No** | **Breaks** |
| Extension / “don’t charge until …” | **No** while $0 collected | **Breaks** |
| Short / partial pay | **No** until month balance cleared | **Breaks** until a cleared month counts |
| Lump-sum catch-up | Credit **only months the ledger applies cash to**, each full-freight | Per applied month |
| Refund / chargeback | Month **revoked** | Streak breaks |
| $0 “active” / Invisible | **No** | Breaks |
| Founder written retention exception | May count **one** named logo/month | Logged in EOM sheet |

**Contracted retainer** = current agreement amount. Permanent reprice = new
freight. Temporary retention discount below contract = **does not count**.

## Scorecard gate

- Graded monthly per [Client Success Role Scorecard](../operations/people/client-success-role-scorecard.md).
- Overall **≥ B** → commissions pay.
- Overall **&lt; B** → stickiness commissions **$0** (base still pays).

## EOM calculation

Target: **&lt;15 minutes**.

1. Export logos + collected amounts + contract retainers.
2. Tag DFY / mid-tier; full-freight Y/N.
3. Update consecutive full-freight streak (break if month does not count).
4. Per logo: first milestone, post-first trailer, second milestone, or post-second trailer.
5. Sum lines.
6. If scorecard &lt; B → commissions = 0.
7. Total cash = `$1,530 + commissions`.

Sheet: `logo | product | streak | event | amount`.

**EOM owner:** Laura prepares; founder approves before payroll.

## Funding / margin notes

- Comp sits in fulfillment/CS labor ([Product Margin Model](../company/product-margin-model.md)).
- Fund variable from retained full-freight logos + DFY ARPA stack — not underfunded logos.
- Hold blended DFY delivery GM **≥ 60%**.

## Decisions locked

1. Base = **$1,530**/mo.
2. Performance commissions uncapped; no hard monthly ceiling.
3. Milestone at stickiness mark **3** and second mark **6** + smaller trailers.
4. Phase 1 dollars: DFY **$50 / $30 / $100 / $50**; mid-tier **50%**.
5. Logo-count tiers **off** Phase 1.
6. Full-freight only; discount / extension / short-pay do not count.
7. Scorecard ≥ B gate on commissions.

## Go-live checklist

- [ ] Shadow-calc one closed month on the Sheet.
- [ ] Founder sign-off → first live commission month.
- [ ] Tell Laura the plan only after shadow sign-off (or with “shadow month” framing).

## Related docs

- [Client Success Role Scorecard](../operations/people/client-success-role-scorecard.md)
- [Client Success Daily OS](../operations/people/client-success-daily-os.md)
- [Product Margin Model](../company/product-margin-model.md)
- [Q3 Pricing + Retention Analysis](../company/reflections/2026-q3-pricing-retention-analysis.md)
- **Payment streak timeline (Mr. Waiz):** sibling reporting repo
  `docs/superpowers/specs/2026-08-10-payment-streak-timeline-design.md` —
  CS Hub **Stickiness** tab derives consecutive full-freight months from
  `client_billings` (hybrid overrides). Commission dollars stay on this plan.
