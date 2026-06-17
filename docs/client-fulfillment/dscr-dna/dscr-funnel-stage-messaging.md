---
title: DSCR Funnel-Stage Messaging (TOF / MOF / BOF)
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-06-12
review_cycle: monthly
artifact_type: playbook
---

# DSCR Funnel-Stage Messaging (TOF / MOF / BOF)

> **DRAFT — REFINANCE ONLY.** Stage-specific messaging system for DSCR refinance campaigns.
> All copy passes [DSCR Compliance Guardrails](dscr-compliance-guardrails.md). TOF copy is
> **number-free**. MOF/BOF copy may use **program-fact tokens** (see token system below) filled
> only from the client's current approved pricing sheet / lender guidelines — never invented,
> never hard-coded into this doc.

## Purpose

Define what messaging does the work at each funnel stage (TOF scroll-stop → MOF proof/mechanism → BOF qualification stack), with a reusable hook bank and the token system that lets number-driven MOF/BOF ads stay evergreen while rates, programs, and clients change.

## Scope

DSCR refinance Meta/Google campaigns: ad copy, retargeting, and the messaging handed to landers and setters. One persona per output, per [Doctrine DSCR Marketing](doctrine-dscr-marketing.md).

## Trigger

Building a new DSCR campaign, creative refresh, or retargeting layer; onboarding a new DSCR client's program facts.

## Inputs

- [Doctrine DSCR Marketing](doctrine-dscr-marketing.md) and [Intelligence ICP DSCR](intelligence-icp-dscr.md)
- [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md) (angle definitions)
- Client's **current approved pricing sheet / lender program guidelines** (sole source of token values)
- [DSCR Competitor Ad Intelligence](dscr-competitor-ad-intelligence.md)

## Outputs

- Stage-mapped ad copy (TOF hooks, MOF proof/mechanism, BOF qualification stack)
- A filled client token sheet per campaign

## Quality Bar

- Align with [Identity Core](../../company/doctrine-identity-core-april-26.md) and [SOURCE-OF-TRUTH](../../SOURCE-OF-TRUTH.md).
- Every variant passes the [compliance pre-flight](dscr-compliance-guardrails.md). Refinance only. One persona per output.
- TOF: zero numbers. MOF/BOF: tokens only, filled from the approved sheet, framed program-dependent ("FICO as low as," "up to," "may qualify").

## Operating Content

### The stage logic (why each stage says what it says)

| Stage | Audience state | Job of the message | Psychology doing the work | Numbers? |
|-------|---------------|--------------------|---------------------------|----------|
| **TOF** | Cold scroller; doesn't know you; pattern-matched to ignore "no income / fast" ads | Stop the scroll with an **idea or a pain**, not a feature list | Curiosity gap / Zeigarnik, loss aversion (trapped equity, balloon), contrast with conventional lending | **No** — numbers invite comparison-shopping before trust exists |
| **MOF** | Clicked/engaged; asking "are these people real specialists?" | Pass the **competence filter**: mechanism + proof | Authority, social proof, availability (vivid funded outcomes), mere exposure (retargeting frequency) | Sparingly — proof figures (substantiated funded outcomes) and soft program facts |
| **BOF** | Warm; asking "do *I* qualify, and will they execute?" | **Qualification stack** + certainty + low-friction next step | Specificity = credibility, self-qualification (filters lead quality), goal-gradient ("you're 2 minutes from knowing"), regret aversion (no-obligation framing) | **Yes** — tokenized program facts |

Rationale vs the market: competitor intel shows ~60% of active DSCR ads run the same number-free
"no income / no tax returns + fast" claim at every stage. Stage separation — idea-first TOF, proof MOF,
number-specific BOF — is itself the differentiator.

### The token system (how numbers stay evergreen)

Copy in this doc and in generated ads uses tokens. **Token values are never stored here** — they live
in a per-client token sheet filled from the client's current approved pricing sheet, re-verified on
every creative refresh (rates and programs change; clients differ).

| Token | Meaning | Framing rule when filled |
|-------|---------|--------------------------|
| `[FICO_FLOOR]` | Minimum qualifying credit score | "FICO as low as [FICO_FLOOR]" — never "you qualify at [FICO_FLOOR]" |
| `[MAX_LTV_CASHOUT]` | Max cash-out LTV | "Cash out up to [MAX_LTV_CASHOUT] of the property's value" + program-dependent |
| `[MAX_LTV_RT]` | Max rate/term LTV | "Up to [MAX_LTV_RT]" + program-dependent |
| `[MIN_DSCR]` | Minimum DSCR ratio | "Properties cash-flowing at [MIN_DSCR]+ may qualify" |
| `[CLOSE_RANGE]` | Typical closing window | "Many close in [CLOSE_RANGE]" — never a guaranteed timeline |
| `[MIN_LOAN]` / `[MAX_LOAN]` | Loan amount band | "Loans from [MIN_LOAN] to [MAX_LOAN]" |
| `[STATE]` | Licensed-state geo token | Per-client licensed list only |
| `[PROOF_OUTCOME]` | A real, documented funded outcome | Must be substantiated and representative |

**Hard rules:** no rates or payments in ad copy unless the client's compliance posture explicitly
approves it (rate claims are the highest-risk class under FTC MAP/Reg N). Every numeric claim carries
softening ("as low as," "up to," "many," "may qualify") and the standing business-purpose disclosure
where required.

---

### TOF — hook bank (number-free, idea/pain first)

One persona per ad. Grouped by the three gap lanes from competitor intel. Psychology noted so variants can be regenerated on-theme.

**Lane 1 — Trapped equity (Portfolio Scaler; loss aversion + capital velocity)**

1. Your equity is just sitting there. Put it to work.
2. The most expensive thing you own is the equity you're not using.
3. You don't have to sell a door to get your capital back.
4. Every month that equity sits idle, it costs you the next deal.
5. The bank already holds your rental. Your equity doesn't have to sit with it.

**Lane 2 — Balloon / hard-money urgency (Bridge Refinancer; urgency + certainty)**

6. Balloon coming due? Refinance before it hits.
7. Hard money got you in. It was never the plan to stay.
8. Your bridge loan has an expiration date. Your refinance shouldn't miss it.
9. The worst time to refinance a balloon is the month it matures.

**Lane 3 — The reframe (Self-Employed / Write-Off; vindication + contrast)**

10. Your tax returns say one thing. Your rentals say another.
11. The property qualifies itself. Your W-2 stays out of it.
12. You wrote your income down on purpose. Your lender shouldn't punish you for it.
13. Refinance on the rent — not your tax returns.
14. Conventional lenders read your 1040. DSCR lenders read your lease.

**Lane 4 — STR (Airbnb Operator; "credited for what it really earns")**

15. Your Airbnb out-earns most rentals. Refinance it like it does.
16. Conventional underwriting can't read an AirDNA report. We can.

**Soft-exclusivity variants (use sparingly; specific access, never vague "exclusive program"):**

17. The refinance program most investors don't know exists — for rentals they already own.
18. Banks built DSCR for institutions. Investors figured out it works for them too.

### MOF — proof and mechanism bridge (retargeting layer 1)

Job: pass the competence filter. Formats over headlines here — mechanism explainers ("how a DSCR
refinance actually underwrites: rent vs. PITIA"), `[PROOF_OUTCOME]` story ads (the most under-used
lever in the category per competitor intel), objection pre-handles ("yes, the rate runs higher —
here's the math against trapped equity"), and entity/STR fluency signals. Voice: operator-to-operator,
specific, zero reassurance tone. Soft tokens allowed (`[CLOSE_RANGE]`, `[PROOF_OUTCOME]`).

### BOF — qualification stack (retargeting layer 2 / warm lists)

Job: let the investor self-qualify and remove the last doubt. The stack format:

> **See if your rental qualifies:**
> ✅ FICO as low as `[FICO_FLOOR]`
> ✅ Cash out up to `[MAX_LTV_CASHOUT]` of the property's value
> ✅ Qualify on the property's rent — no tax returns, no W-2s
> ✅ Close in your LLC
> ✅ Many close in `[CLOSE_RANGE]`
> *Program-dependent; subject to underwriting and property qualification. Business-purpose investment financing — non-owner-occupied property only.*
>
> CTA: "Check your property in 2 minutes — no credit pull, no obligation."

BOF headline patterns (token-filled per client):

- `[FICO_FLOOR]`+ FICO? Your rental may already qualify.
- Cash out up to `[MAX_LTV_CASHOUT]` — qualified on the rent, not your returns.
- Own a rental in `[STATE]`? Here's exactly what it takes to qualify.
- Still on hard money? See the actual terms to exit into a 30-year DSCR.

BOF rules: one clear CTA (Hick's law — never "call, book, or download"), no-obligation/no-credit-pull
framing (regret aversion), and the qualification stack doubles as a lead-quality filter — investors
below the floor self-select out.

### Per-client activation checklist

1. Pull the client's current approved pricing sheet + lender guidelines; fill the token sheet.
2. Confirm licensed `[STATE]` list and Meta Special Ad Category setup.
3. Verify every `[PROOF_OUTCOME]` is real, documented, representative.
4. Run the [compliance pre-flight](dscr-compliance-guardrails.md) on each filled variant.
5. Re-verify token values at every creative refresh — stale numbers are a UDAP risk, not just a copy bug.

## Related Docs

- [DSCR DNA README](README.md)
- [Doctrine DSCR Marketing](doctrine-dscr-marketing.md)
- [Ad Copy And Angle Library (DSCR)](ad-copy-angle-library-dscr.md)
- [MB DSCR Ad Copy Standards](mb-dscr-ad-copy-standards.md)
- [DSCR Compliance Guardrails](dscr-compliance-guardrails.md)
- [DSCR Competitor Ad Intelligence](dscr-competitor-ad-intelligence.md)
- [DSCR Ads Playbook](dscr-ads-playbook.md)
