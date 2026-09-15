---
title: Lead Media Buyer — PJ EOM Sheet Template
domain: operations
subdomain: people
owner: founder
status: draft
confidentiality: owner-only
last_updated: 2026-09-15
review_cycle: quarterly
artifact_type: template
related_docs:
  - docs/operations/people/lead-mb-pj-commission-appendix.md
  - docs/operations/people/lead-mb-pj-payment-agreement.md
---

# Lead Media Buyer — PJ EOM Sheet Template

Copy into a spreadsheet each month. Contractor fills; founder approves before invoice.

## Header

| Field | Value |
|-------|--------|
| Contractor | {{HIRE_NAME}} |
| Work month | YYYY-MM |
| Level in force | L1 / L2 / L3 / L4 |
| Base (BRL) | |
| Scorecard grade | A / B / C / D |
| Scorecard ≥ B? | Yes / No |
| Live commission month? | Yes / Shadow / N/A (L1) |
| Pay date | 9th of next month |

## Account rows

| account | geo class | target CPQL | spend (USD) | qual leads | actual CPQL | eligible (Y/N) | hit (Y/N) | notes |
|---------|-----------|-------------|-------------|------------|-------------|----------------|-----------|-------|
| | Broad / Mid / Tight | | | | | | | |
| | | | | | | | | |
| | | | | | | | | |

**Formulas**

- `actual CPQL = spend ÷ qual leads`
- `eligible` = assigned + target on file + running + spend ≥ 1000 + qual leads ≥ 10
- `hit` = eligible AND (actual ≤ target OR actual ≤ target × 1.10)

## Totals

| Line | Amount (BRL) |
|------|----------------|
| Hits count | |
| Commissions (`hits × 100`) | |
| If scorecard &lt; B → commissions forced to | **0** |
| Base | |
| **Total due** | |

## Worked example (L2, live month, scorecard B)

| account | target CPQL | spend | qual leads | actual CPQL | eligible | hit |
|---------|-------------|-------|------------|-------------|----------|-----|
| Client A | 25 | 2,000 | 100 | 20.00 | Y | Y |
| Client B | 28 | 1,500 | 40 | 37.50 | Y | N (over target + grace) |
| Client C | 30 | 800 | 20 | 40.00 | N (spend floor) | — |
| Client D | 22 | 3,000 | 150 | 20.00 | Y | Y |

- Hits = 2 → commissions = **R$200**
- Base L2 = **R$5,000**
- Total = **R$5,200** (if scorecard ≥ B)

Grace check for Client B: target 28 × 1.10 = 30.80; actual 37.50 → miss.

## Approval

| Role | Name | Initials | Date |
|------|------|----------|------|
| Prepared by (Contractor) | | | |
| Approved by (Founder) | | | |

After approval: Contractor invoices → Company pays on the **9th**.
