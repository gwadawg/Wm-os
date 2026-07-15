---
title: Media Buyer Comp Design — Christian
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
  - docs/operations/people/media-buyer-role-scorecard.md
  - docs/operations/people/media-buyer-daily-os.md
  - docs/company/product-margin-model.md
  - docs/client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md
---

# Media Buyer Comp Design — Christian

## Purpose

Phase 1 pay design for Christian (Media Buyer + interim onboard tech blocks):
**stable base + CPL-at-KPI bonuses** that reward account-level buying and book
consistency — easy EOM, fair across geos, sized for a growing client book.

**North star:** pay him when assigned accounts hit their **written CPL targets**,
plus a book bonus when most of the scored book is at KPI.

## Status

**LOCKED — Phase 1 structure active** (2026-07-15).

Cash commissions do **not** pay until: (1) each scored account has a written CPL
target, and (2) one **shadow EOM** month is run and founder signs off. Do not
change the Phase 1 rates without a quarterly review note.

## Scope

| In | Out (for now) |
|---|---|
| Base + per-account CPL hits + 80% book bonus | Stickiness / consecutive paid-month commissions |
| Written per-account CPL targets (geo-aware) | Blended / average CPL as the pay number |
| Scorecard gate on variable | Temporary clean-onboarding bonus (separate when activated) |

## Design principles

1. **Base covers the seat** — buying, notes to Client Success, tech blocks.
2. **Leading KPI = CPL** vs written per-account target (not book average).
3. **Tight geos get higher targets**, not a harsher company-wide number.
4. **Low $/account + book consistency bonus** — no hard cash ceiling.
5. **Easy EOM** — target vs actual → count hits → check 80%.
6. **Quarterly knobs** — rates, grace, floors, geo bands with 30 days’ notice.

## V1 structure (monthly) — FINAL Phase 1

| Component | Amount | Notes |
|---|---|---|
| Base | **$1,000** | Fixed; unconditional |
| Per-account CPL hit | **$15** / eligible account at KPI | Flat each hit month |
| Book bonus | **$100** | If **≥ 80%** of eligible accounts hit |
| Scorecard gate | All commissions | Month scorecard **≥ B** or commissions = **$0** |
| Hard cash ceiling | **None** | ~$1,500 total needs ~27 hits + book bonus |

**Illustrative:**

| Hits | ≥80% hit-rate? | Variable | Total ≈ |
|---:|:---:|---:|---:|
| 8 | No | $120 | **$1,120** |
| 12 | Yes | $280 | **$1,280** |
| 20 | Yes | $400 | **$1,400** |
| 27 | Yes | $505 | **$1,505** |

## CPL KPI — FINAL Phase 1

### Hit

`actual CPL ≤ written target` **or** within **10% over** target (Phase 1 grace **on**).

```text
actual CPL = account ad spend that month ÷ leads that month
```

Same spend/lead source every month (Meta + agreed lead counter).

### Written target (required)

On file before month start (or within 5 business days of launch).

| Geo class | Meaning | Use |
|---|---|---|
| Broad | Many states / wide targeting | Lower CPL target |
| Mid | Regional cluster | Mid CPL target |
| Tight | 1–3 states / heavy restrictions | Higher CPL target |

**Target ownership:** Christian proposes; founder approves; number filed on the
EOM Sheet before the month counts.

Starter dollar bands by product/geo: publish in the EOM Sheet (founder) before
first live month — structure does not require them in this doc.

### Eligible account (scored)

All of:

1. Assigned to Christian for media buying that month.
2. Written CPL target on file.
3. Ads meaningfully running (not paused all month).
4. Signal floor: spend **≥ $1,000** and leads **≥ 15**.
5. DFY or mid-tier — both at **$15** per hit in Phase 1.

Paused / zero-spend / no-target / below floor → **out of pool** (neither help nor hurt 80%).

### Book bonus

```text
hit rate = hits ÷ eligible accounts
if hit rate ≥ 80% → +$100
else → +$0
```

Example: 8/10 = 80% → pays; 7/10 = 70% → no book bonus (still `$15 × 7`).

## Scorecard gate

- Graded monthly per [Media Buyer Role Scorecard](../operations/people/media-buyer-role-scorecard.md).
- Overall **≥ B** → commissions pay.
- Overall **&lt; B** → variable = **$0** (base still pays).

## EOM calculation

Target: **&lt;15 minutes**.

1. List assigned accounts; drop non-eligible.
2. Per eligible: spend, leads, CPL vs target (+ grace).
3. `hits × $15`.
4. If hit rate ≥ 80% → +$100.
5. If scorecard &lt; B → commissions = 0.
6. Total cash = `$1,000 + commissions`.

Sheet:  
`account | geo class | target CPL | spend | leads | actual CPL | eligible | hit | notes`

**EOM owner:** Christian prepares; founder approves before payroll.

## Funding / margin notes

- Media-buyer labor in fulfillment pools ([Product Margin Model](../company/product-margin-model.md)).
- Strong months land ~**$1.2–1.5k** until the scored book is very large.
- Raise `$15` or `$100` only at quarterly review after EOM habit + margin floor hold.

## Decisions locked

1. Base = **$1,000**/mo.
2. Leading KPI = **CPL vs written per-account target**.
3. **$15** per eligible hit; **$100** if ≥ **80%** hit-rate.
4. No hard total-cash ceiling.
5. Phase 1: 10% grace **on**; floor **$1k spend / 15 leads**; mid-tier full **$15**.
6. Scorecard ≥ B gate on commissions.
7. Stickiness / paid-month commissions out of scope.

## Go-live checklist

- [ ] Write CPL targets for all accounts that will be scored.
- [ ] Shadow-calc one closed month on the Sheet.
- [ ] Founder sign-off → first live commission month.
- [ ] Tell Christian the plan only after shadow sign-off (or with “shadow month” framing).

## Related docs

- [Media Buyer Role Scorecard](../operations/people/media-buyer-role-scorecard.md)
- [Media Buyer Daily OS](../operations/people/media-buyer-daily-os.md)
- [Product Margin Model](../company/product-margin-model.md)
- [Fulfillment KPI standards (CPL/CPQL)](../client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md)
