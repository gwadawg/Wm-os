---
title: Lead Media Buyer — PJ Commission Appendix
domain: operations
subdomain: people
owner: founder
status: draft
confidentiality: owner-only
last_updated: 2026-09-15
review_cycle: quarterly
artifact_type: policy
related_docs:
  - docs/operations/people/lead-mb-pj-payment-agreement.md
  - docs/operations/people/lead-mb-pj-eom-sheet-template.md
  - docs/client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md
  - docs/superpowers/specs/2026-09-15-lead-media-buyer-pj-comp-design.md
---

# Lead Media Buyer — PJ Commission Appendix

## Purpose

Rules for variable pay after Level 2. Paid KPI is **CPQL** (cost per qualified lead),
not CPL.

## When commissions can pay

All of:

1. Contractor is unlocked at **L2 or higher**
2. Month is a **live** commission month (after shadow EOM sign-off)
3. Monthly media-buyer scorecard **≥ B** — else commissions = **R$0** (base still pays)

Month 1 and all **L1** months: commissions = **R$0**.

## Hit definition

```text
actual CPQL = account ad spend that month ÷ qualified leads that month
HIT = actual CPQL ≤ written per-account CPQL target
      OR within 10% over target (Phase 1 grace ON)
```

- **Qualified lead** = meets call-center pre-qualification criteria (same as fulfillment
  KPI standards).
- Company reference bands (e.g. ~US$20–29.99 “at KPI”) inform judgment; **pay uses the
  written per-account target**.

## Written CPQL target

- On file before month start (or within 5 business days of launch).
- Contractor proposes; founder approves; filed on the EOM Sheet before the month counts.
- Geo/product-aware (tight geos → higher CPQL targets).

## Eligible account (in the pool)

All of:

1. Assigned to Contractor for media buying that month
2. Written CPQL target on file
3. Ads meaningfully running (not paused all month)
4. Signal floor: spend **≥ US$1,000** and qualified leads **≥ 10**
5. DFY or mid-tier — both at **R$100** per hit in Phase 1

Paused / zero-spend / no-target / below floor → **out of pool** (neither help nor hurt).

## Payout

```text
if level < L2 OR scorecard < B:
  commissions = 0
else:
  commissions = hits × R$100

total = base(level) + commissions
```

Phase 1: **no book bonus**. No hard cash ceiling.

## EOM process (&lt;15 minutes)

1. List assigned accounts; drop non-eligible
2. Per eligible: spend, qualified leads, CPQL vs target (+ grace)
3. `hits × R$100`
4. If scorecard &lt; B → commissions = 0
5. Total = base + commissions
6. Founder approves → invoice → **pay on the 9th** (prior month)

Sheet: [EOM sheet template](lead-mb-pj-eom-sheet-template.md)

**EOM owner:** Contractor prepares; founder approves before payment.

## Go-live checklist (first live commission month)

- [ ] L2+ unlock signed on level checklist
- [ ] Written CPQL targets for all scored accounts
- [ ] One shadow EOM month run and founder signed off
- [ ] Scorecard process agreed for the live month
