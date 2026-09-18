---
title: DSCR Creative Taxonomy
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-09-16
review_cycle: monthly
artifact_type: doctrine
canonical_for: dscr-creative-buckets-angles-naming
note: >-
  Creative-layer standard of truth for buckets, angles, creative jobs, and
  labeling. Not campaign architecture. Not nurture / setter / product ops.
  Promote from draft after founder approval + transcript validation.
---

# DSCR Creative Taxonomy

> **Naming + creative sorting SOT (draft).**
> Use this when brainstorming ads, tagging concepts, or deciding which
> angle a creative belongs to.
>
> **Load with:** [intelligence-icp-dscr.md](intelligence-icp-dscr.md)
> **Expand winners in:** [dscr-campaign-master-angles.md](dscr-campaign-master-angles.md)
> **Do not use for:** nurture drips, setter scripts, product mechanics,
> RM creative, or campaign/ad-set structure (those are separate docs).

---

## 1. One governing question

Every DSCR creative answers:

> **What stops this investor from acting today?**

Not who they are. Not the property type. Not what they'd do with the money.
The **constraint**. Under Meta Housing Special Ad Category, creative *is*
the targeting — so the constraint is the only segmentation that changes
what the ad says.

---

## 2. The map (visual)

```text
                    ┌─────────────────────────────────────┐
                    │  What stops them from acting today? │
                    └─────────────────┬───────────────────┘
                                      │
              ┌───────────────────────┼───────────────────────┐
              │                       │                       │
              ▼                       ▼                       ▼
        ┌──────────┐           ┌──────────┐           ┌──────────┐
        │  DENIED  │           │ DEADLINE │           │   IDLE   │
        │ bank says│           │ note has │           │ equity   │
        │    no    │           │  a date  │           │  sits    │
        └────┬─────┘           └────┬─────┘           └────┬─────┘
             │                      │                      │
             ▼                      ▼                      ▼
      Program reveal          Mapped exit            Belief break
      `nodocs-speed`          `balloon-exit`         `cashout-grow`
             │                      │                      │
             └──────────────────────┼──────────────────────┘
                                    │
                                    ▼
                    ┌───────────────────────────────┐
                    │  Shared warm jobs (any door)  │
                    │  outcome · terms · authority  │
                    └───────────────────────────────┘

  Exception (no constraint — already shopping):
  ┌────────────┐
  │ IN-MARKET  │  terms / rate-card · `ratecard-centered`
  └────────────┘
```

---

## 3. Constraint buckets

| Bucket | One-line definition | Enemy | Entry awareness | Cold creative job | Concept slug |
|--------|---------------------|-------|-----------------|-------------------|--------------|
| **DENIED** | Would fail conventional underwriting today | The bank's basis of approval | Problem-aware, solution-unaware | Program reveal | `nodocs-speed` |
| **DEADLINE** | Note has a maturity date forcing action | The calendar | Solution / most-aware | Mapped exit | `balloon-exit` |
| **IDLE** | Nothing broken — equity sits by choice | Status-quo bias | Problem-unaware | Belief break | `cashout-grow` |
| **IN-MARKET** | Already shopping DSCR — no constraint to speak to | — | Product / most-aware | Offer / terms | `ratecard-centered` |

**Aliases (do not invent new ones):**

| Use | Do not use as peer labels |
|-----|---------------------------|
| DENIED | Blocked, Write-Off, Self-Employed, property-count, STR, Foreign National *(modifiers — §5)* |
| DEADLINE | Cornered, Hard-Money, Balloon, Bridge |
| IDLE | Dormant, Trapped, Portfolio Scaler, Idle-Equity |
| IN-MARKET | BOF-only, rate shopper, product-aware |

---

## 4. Sorting rule (mutual exclusivity)

One ad · one lead · one concept = **exactly one bucket**. Check in order:

1. **Date on the note?** → **DEADLINE**
2. **No date, but conventional would say no?** → **DENIED**
3. **Could act but isn't?** → **IDLE**
4. **Already knows DSCR and is shopping terms?** → **IN-MARKET**

If an ad speaks to a pain/constraint, it is **never** tagged IN-MARKET.
IN-MARKET is only for product-named + terms/spec creatives with no
constraint messaging.

---

## 5. Modifiers (not buckets)

Same enemy + same job = one bucket. These only change the *example*:

| Modifier | Usually lives in | Example line |
|----------|------------------|--------------|
| Write-offs / self-employed | DENIED | "Tax returns say broke; rentals say otherwise." |
| Property-count cap | DENIED | "Bank capped you at 10; DSCR underwrites each door." |
| STR income not credited | DENIED | "Refinance on what the bookings earn." |
| Foreign national | DENIED | "Qualify on the US property." *(program-gated)* |
| LLC vesting | Any | Close-like-an-operator proof point |
| Free-and-clear | IDLE / DENIED | Cash-out without an existing mortgage |

---

## 6. Use cases (fuel, not buckets)

Pay off balloon · fund rehab · build reserves · lower payment · move into LLC.

These answer **"what would you do with it?"** — not **"what stops you?"**
Organize ads by bucket; *illustrate* with a use case. Form "goal" question
routes nurture — it does not create a new creative bucket.

---

## 7. Proven angles → bucket address

Nothing cut. Every old angle has a home:

| # | Angle | Bucket | Stage home | Creative job | Slug |
|---|-------|--------|------------|--------------|------|
| 3 | Did You Know? / Program Call-Out | DENIED | Cold | Program reveal | `nodocs-speed` |
| 2 | The Deadline | DEADLINE | Cold | Mapped exit | `balloon-exit` |
| 1 | The Idle-Equity Tax | IDLE | Cold | Belief break | `cashout-grow` |
| 5 | What You Could Do With It | IDLE-flavored → shared | Warm / MOF | Outcome / uses | `cashout-grow` (variant) |
| 4 | The Checklist / rate-card | Shared **or** IN-MARKET | Warm; cold if terms-only | Offer / terms | `ratecard-centered` · proposed `qualify-stack` |
| — | Lender authority | Shared | Warm / BOF | Why this LO / shop | proposed `lo-authority` |

**Cold default test order (when you need a starting slate):** DENIED + IDLE
carry volume; DEADLINE is smaller — fund less (~20%). Old proven order 3 → 2 → 1
maps to DENIED → DEADLINE → IDLE; **budget share** is not equal thirds.
Day-1 structure: [DSCR Campaign Launch SOP](../media-buying/dscr-campaign-launch-sop.md).

Full writeups: [dscr-campaign-master-angles.md](dscr-campaign-master-angles.md).

---

## 8. Creative jobs

| Job | Who owns it | What the ad must make them think | Funnel home |
|-----|-------------|----------------------------------|-------------|
| Program reveal | DENIED cold | "Wait — that's me. Why hasn't anyone offered this?" | Cold |
| Mapped exit | DEADLINE cold | "Price the exit now, not the month it matures." | Cold |
| Belief break | IDLE cold | "Idle equity isn't safety — it's cost." | Cold |
| Outcome / uses | Shared warm | "Here's what the capital unlocks." | Warm / MOF |
| Offer / terms | Shared warm **or** IN-MARKET | "Here's exactly what it takes." | Warm; cold if terms-only |
| Lender authority | Shared warm | "This is the shop / LO to work with." | Warm / BOF |

**Rule:** one primary job per ad. Don't average two jobs into one bland concept.
Authority may sit *secondary* on an IN-MARKET terms card ("our program") —
tag primary job = offer/terms.

---

## 9. Honesty clause (creative expectations)

| Bucket | Audience size | Speed to action | Creative implication |
|--------|---------------|-----------------|----------------------|
| DEADLINE | Smallest | Fastest (calendar sells) | Calm operator exit — never panic aesthetics |
| DENIED | Medium | Fast once revealed | Curiosity + recognition |
| IDLE | Largest | Slowest (belief change) | Sequence-friendly; still needs a kill metric later |
| IN-MARKET | Shoppers only | Fast (1–2 touches) | Specificity is the creative; watch rate-shopper quality |

---

## 10. Labeling cheat sheet (brainstorm / Mr. Waiz)

When naming or tagging a concept, fill these fields in Mr. Waiz:

```text
bucket:        Denied | Deadline | Idle | In-market     (required, one)
creative_job:  Reveal | Exit | Belief | Outcome | Terms | Authority  (required, one)
concept:       nodocs-speed | balloon-exit | cashout-grow |
               qualify-stack | lo-authority | ratecard-centered  (required, one)
topic:         Write-offs | Property count | STR | Foreign national |
               LLC | Free and clear | Cash-out | Rehab | Reserves | Rate/term
               (optional, multi)
angle:         legacy optional only — not used for rollups
```

Ad name stays: `dscr_{concept}_{format}_v{n}` — see
[ad-naming-convention.md](../media-buying/ad-naming-convention.md).
Bucket, job, concept, and topic are logged as **product × category tags**
in Mr. Waiz (live catalog) — **not** in the `ad_name` token. Angle is
deprecated. This doc owns meaning; Mr. Waiz owns selectable rows.

Pairing (soft): In-market → Terms; Reveal → Denied + nodocs-speed;
Exit → Deadline + balloon-exit; Belief/Outcome → Idle + cashout-grow;
Authority → lo-authority.

---

## 11. Fence (what this doc is not)

| This taxonomy owns | Other docs own |
|--------------------|----------------|
| Buckets, angles, creative jobs, labeling | **Campaign / ad-set structure** → [DSCR Campaign Launch SOP](../media-buying/dscr-campaign-launch-sop.md) |
| Cold vs warm *creative* jobs | Nurture / drip copy → cash-out drip + playbooks |
| Angle → slug map | Product mechanics → [intelligence-dscr-product.md](intelligence-dscr-product.md) |
| IN-MARKET terms exception | Compliance essay → [dscr-compliance-guardrails.md](dscr-compliance-guardrails.md) |
| DSCR only | RM creative → reverse-mortgage-dna |

Do **not** put campaign/ad-set counts in this file. Structure lives in the launch SOP only.

---

## 12. Open before `status: active`

- [ ] Founder approves DENIED / DEADLINE / IDLE / IN-MARKET names
- [ ] Validate sorting rule against ~20–30 call transcripts / form answers
- [ ] Register `qualify-stack` + `lo-authority` in [ad-name-library.yaml](../media-buying/ad-name-library.yaml) when ready

## Related

- [DSCR Campaign Launch SOP](../media-buying/dscr-campaign-launch-sop.md) — day-1 Meta structure
- [Intelligence ICP DSCR](intelligence-icp-dscr.md) — who + NEVER + creative bar
- [Campaign Master Angles](dscr-campaign-master-angles.md) — full angle writeups + tokens
- [GTM Brief](dscr-gtm-positioning-brief.md) — beachhead / test waves
- [Ad name library](../media-buying/ad-name-library.yaml)
- Working brainstorm dump: [demos/dscr-knowledge-breakdown-WORKING-DRAFT.md](../../../demos/dscr-knowledge-breakdown-WORKING-DRAFT.md) (not canonical)
