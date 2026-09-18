---
title: RM Creative Taxonomy
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-09-18
review_cycle: monthly
artifact_type: doctrine
product: rm
canonical_for: rm-creative-process-campaign-structure
note: >-
  How we think about RM marketing, develop creatives, read results, and
  structure campaigns. Backend tags are a logging layer only — not the
  strategy. Promote from draft after founder approval.
---

# RM Creative Taxonomy

> **Process + structure SOT (draft).**
> How the team develops RM creatives, reads what's working, and structures
> campaigns for qualified leads.
>
> **Load with:** [doctrine-rm-marketing.md](doctrine-rm-marketing.md) ·
> [intelligence-icp-rm.md](intelligence-icp-rm.md) ·
> [rm-product-lines.md](rm-product-lines.md) ·
> [rm-archetypes-canonical.md](../media-buying/creative-studio/rm-archetypes-canonical.md)
>
> **Not this doc:** nurture / setter / product mechanics / DSCR.
> Backend tagging lives in Mr. Waiz — see §7 (logging only).
>
> DSCR sibling: [dscr-creative-taxonomy.md](../dscr-dna/dscr-creative-taxonomy.md)

---

## North star

**More qualified reverse-mortgage leads, learned faster, across every client.**

Everything below exists to support three jobs:

1. **Develop** the next creative without guessing
2. **Read** what's working without drowning in noise
3. **Structure** campaigns so learning compounds instead of resetting

---

## 1. How to look at RM marketing

Four questions, in order. Answer them before you write a word of copy.

```text
1. PRODUCT     Which product?          HECM  or  SECOND
2. STRATEGY    How does it open?       OUTCOME-LED  or  MYTH-LED
3. OUTCOME     What does it promise?   PAYMENT-GONE · CASH-OUT · STANDBY-LINE
4. STAGE       How warm is the viewer? TOF · MOF · BOF
```

Then pick a **trigger** (the hook — widow, inflation, healthcare…) and write
the ad. Trigger is unbounded. Everything above is closed.

### Product (never mix)


|                | HECM                 | SECOND                       |
| -------------- | -------------------- | ---------------------------- |
| First mortgage | Paid off             | Stays — keep the rate        |
| Trust language | Federally insured OK | Not FHA                      |
| Default        | Yes                  | Only when client is licensed |


Separate campaigns. Always.

### Strategy (your anti / pro reverse)


| Strategy        | Opens with           | Says "reverse"?                    | Old name     |
| --------------- | -------------------- | ---------------------------------- | ------------ |
| **OUTCOME-LED** | The result they want | No                                 | Anti-reverse |
| **MYTH-LED**    | The false belief     | Yes — as the thing being corrected | Pro-reverse  |


Both run cold. Neither is "warmer." This is the strategic dial for the
account: lean outcome-led when the LO handles objections well; lean myth-led
when they don't.

### Outcomes (exactly three)


| Outcome          | Promise                             | Who it selects                            |
| ---------------- | ----------------------------------- | ----------------------------------------- |
| **PAYMENT-GONE** | Monthly mortgage payment disappears | Still has a mortgage · HECM only          |
| **CASH-OUT**     | Money out of the house now          | Needs money now                           |
| **STANDBY-LINE** | Line they don't touch; grows unused | No present need · slower · higher quality |


Lump sum / monthly deposits / draws = all **CASH-OUT**. Form of money is not
a separate bucket. Kitchen-sink "does everything" ads = `multi` at MOF only.

### Stage (temperature)


| Stage   | Job                       | Creative shape                             |
| ------- | ------------------------- | ------------------------------------------ |
| **TOF** | Select the right stranger | Short · one trigger · one outcome          |
| **MOF** | Build conviction          | Education · stories · kitchen-sink · proof |
| **BOF** | Get the hand-raise        | Authority · next step · offer              |


Myth work is a **strategy**, not a stage. Education can be outcome-led or
myth-led. Testimonials are a **format**, not a category.

---

## 2. Process — develop a new creative

Follow this every time. No freestyle.

```text
STEP 1  Track          hecm | second
STEP 2  Strategy       outcome-led | myth-led
STEP 3  Outcome        payment-gone | cash-out | standby-line
                       (or multi if MOF kitchen-sink)
STEP 4  Stage          tof | mof | bof
STEP 5  Trigger        one pain / situation for the hook
STEP 6  Who + tone     persona + archetype (below) · write · compliance
STEP 7  Name           rm_{concept}_{format}_v{n}  (existing convention)
STEP 8  Log            backend tags (§7) — after the creative exists
STEP 9  Place          into the right campaign / ad set (§3)
```

### Who you're writing to (already in the KB)

Scripting inputs — **not** campaign buckets. Full VOC and language bans live
in the linked docs; do not recreate.

| Kind | Active set | Canonical doc |
|------|------------|---------------|
| **Persona (3)** | Widowed · Married Couple · Pre-Retiree | [intelligence-icp-rm.md](intelligence-icp-rm.md) |
| **Archetype (3)** | Security-Seeker · Financially Squeezed · Strategic Retiree | [doctrine-rm-marketing.md](doctrine-rm-marketing.md) §4 |
| **Bridge** | Who × why + family triggers | [rm-archetypes-canonical.md](../media-buying/creative-studio/rm-archetypes-canonical.md) |

| Persona | Natural archetype fit | Natural triggers |
|---------|----------------------|------------------|
| Widowed | Security-Seeker (+ burden / heirs triggers) | Burden, stay in home, healthcare |
| Married Couple | Financially Squeezed · Strategic Retiree | Inflation, surviving vs living, heirs |
| Pre-Retiree | Strategic Retiree · Financially Squeezed | Payment-gone, standby-line, long runway |

**Do not use:** Veteran (deprecated). Do not brief `archetype: legacy-planner` or
`archetype: pre-retiree` — family = trigger; Pre-Retiree = persona. Archive:
[drafts/rm-archetypes-pre-2026-09-cleanup.md](drafts/rm-archetypes-pre-2026-09-cleanup.md).

### Coverage grid (what to make next)

For each client (or roster-wide), keep this 2 × 3 grid filled. An empty cell
is the next brief — not a neutral gap.


|                 | PAYMENT-GONE | CASH-OUT | STANDBY-LINE |
| --------------- | ------------ | -------- | ------------ |
| **OUTCOME-LED** |              |          |              |
| **MYTH-LED**    |              |          |              |


Fill TOF cells with sharp ads first. Fill MOF with education / kitchen-sink /
testimonials second. Don't invent a seventh angle when a cell is empty.

### Kitchen-sink rule

Long ads that call out widow + burden + every use + objections:

- Default home = **MOF**
- Not a new category
- Every keeper gets **mined** into 1–3 sharp TOF ads from best-watched segments
- That quarry is your fastest source of new concepts

### What is NOT a campaign / ad-set category

| Thing | Where it belongs |
|-------|------------------|
| Unaware / skeptic | Sales diagnostic — who shows up |
| Persona / archetype | Scripting — §2 above · existing KB |
| Veteran | Deprecated — do not brief |
| Testimonials | Format (`t1` / `t2`) |
| Education | Job inside MOF (outcome-led or myth-led) |
| Uses (roof, travel, medical) | Illustration inside the ad |
| Old "12 angles" | Split into outcome / trigger / myth / audience — not peers |


---

## 3. Campaign structure — scalable + fast learning

Goal: isolate what you're testing, protect winners, graduate only what proves
on **qualified** leads.

### The shape

```text
DAY 1 / LEARNING
{client}_rm_hecm_test          (ABO)
├── cold_outcome-led           sharp TOF ads · outcome unnamed
└── cold_myth-led              sharp TOF ads · myth-first
    (skip myth-led if daily budget < ~$75)

WHEN ENGAGERS EXIST
{client}_rm_hecm_warm          (ABO)
└── warm_convert               kitchen-sink · education · testimonials
                               · objection / proof

AFTER A CONCEPT PROVES (CPQL)
{client}_rm_hecm_scale         (CBO)
└── scale_winners              proven creatives only

IF CLIENT OFFERS SECOND
{client}_rm_second_test        ← same shape, never mixed with HECM
```

### Why this shape


| Layer       | What earns a budget line   | Why                                                             |
| ----------- | -------------------------- | --------------------------------------------------------------- |
| Campaign    | Product track              | Different mechanics, trust language, audiences                  |
| Cold ad set | Strategy (outcome vs myth) | Different lead economics; share a set and Meta starves myth-led |
| Warm ad set | Temperature                | Conviction job, not selection job                               |
| Ad          | Outcome × trigger × format | Learning signal; read in reporting                              |


When the account is on the **roster wave system**
([creative-testing-structure.md](../media-buying/creative-testing-structure.md)),
use concept-isolated test ad sets (`test_w{n}_{concept}`). That is finer
isolation than strategy — use it once the account is past day-1. Day-1 above
is the simple launch shape.

### Budget dial (starting guides — validate with spend)


| Client                    | Cold split                       |
| ------------------------- | -------------------------------- |
| Strong objection handling | ~65% outcome-led / ~35% myth-led |
| Weak / new / setter-heavy | ~55% myth-led / ~45% outcome-led |
| Thin budget               | Outcome-led only                 |


---

## 4. How to read what's working

Same scorecard as the rest of fulfillment:
[creative-testing-scorecard.md](../media-buying/creative-testing-scorecard.md).


| Gate                | Rule                                                                  |
| ------------------- | --------------------------------------------------------------------- |
| Hold                | No verdict before **4,000 impressions**                               |
| Gate 1              | CTR < 0.8% **and** zero QLs → kill; QLs present → keep / re-edit hook |
| Gate 2              | Verdict on **CPQL + Lead-to-Qual** — never on CPL alone               |
| Warm / kitchen-sink | Compare to other warm ads; use watch-through as early flag            |
| Standby-line        | Needs a **review date** — do not kill on day-3 CPL                    |


### What "working" means for this north star


| Signal                                      | Means                                                                               |
| ------------------------------------------- | ----------------------------------------------------------------------------------- |
| Strong CPQL + Lead-to-Qual                  | Graduate to Scale · reuse concept family                                            |
| Cheap CPL, weak qual %                      | Creative is attracting the wrong people — tighten equity callout or switch strategy |
| Strong myth-led CPQL, weak outcome-led qual | Client can't handle deferred objections — weight myth-led higher                    |
| Kitchen-sink holds watch + books            | Keep in warm · cut TOF children from best segments                                  |


Log wave readouts in
[performance-learnings.md](../media-buying/performance-learnings.md).

---

## 5. Equity callout (quality dial — not a bucket)

Lead quality is improved on the ad, not by inventing new categories.


| Setting                        | When                                                                      |
| ------------------------------ | ------------------------------------------------------------------------- |
| No callout                     | Max volume (rarely)                                                       |
| Soft ("home mostly paid off…") | Default cold                                                              |
| Hard (equity + exclusion)      | Client quality complaints · Second track · prior-decline leak on myth-led |


---

## 6. Sorting any existing ad

1. **Track** — keep-rate / first lien stays → SECOND; else HECM
2. **Strategy** — first line names/defends reverse → MYTH-LED; else OUTCOME-LED
3. **Outcome** — payment gone → PAYMENT-GONE; needs money now → CASH-OUT;
  protection unused → STANDBY-LINE; does everything → multi (MOF)
4. **Stage** — where it should run (TOF sharp vs MOF broad vs BOF authority)

---

## 7. Backend logging (not the strategy)

Mr. Waiz tags / summary exist so we can **query** the library later. They do
not decide campaign structure. Structure is §3. Process is §2.

When logging a creative, record the decisions you already made:

```text
track:          hecm | second
strategy:       outcome-led | myth-led
outcome:        payment-gone | cash-out | standby-line | multi
stage:          tof | mof | bof
equity_callout: yes | no
```

Ad name stays `rm_{concept}_{format}_v{n}` per
[ad-naming-convention.md](../media-buying/ad-naming-convention.md).
Do not stuff strategy / stage / outcome into the name.

---

## 8. Fence


| This doc owns                                | Other docs own                                                                                   |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| How to think · develop · read · structure RM | Copy library → [ad-copy-angle-library-rm.md](../media-buying/ad-copy-angle-library-rm.md)        |
| Day-1 campaign shape                         | Roster waves → [creative-testing-structure.md](../media-buying/creative-testing-structure.md)    |
| Outcome / strategy definitions               | Product mechanics → [rm-product-lines.md](rm-product-lines.md)                                   |
|                                              | Scorecard bands → [creative-testing-scorecard.md](../media-buying/creative-testing-scorecard.md) |
|                                              | Archetype language → [doctrine-rm-marketing.md](doctrine-rm-marketing.md)                        |


Detailed budget tiers, kill calendars, and day-1 setup cards → **RM Campaign
Launch SOP** (not yet written; next artifact after this is approved).

---

## 9. Open before `status: active`

- Founder approves: product · strategy · outcome · stage as the four
thinking questions
- Founder approves day-1 campaign shape (§3)
- Validate cold weightings with real spend
- Reconcile 12-angle copy library against outcome / trigger / myth /
audience split
- Write RM Campaign Launch SOP (budgets, gates, setup card)
- Register missing concept slugs (`payment-gone`, `standby-line`,
`heirs-protected`, `lo-authority`, `second-not-reverse`)

## Related

- [Doctrine RM Marketing](doctrine-rm-marketing.md) — 4 active archetypes
- [Intelligence ICP RM](intelligence-icp-rm.md) — 3 active personas
- [RM Archetypes Canonical](../media-buying/creative-studio/rm-archetypes-canonical.md) — bridge
- [RM Product Lines](rm-product-lines.md)
- [Creative Testing Scorecard](../media-buying/creative-testing-scorecard.md)
- [Ad Naming Convention](../media-buying/ad-naming-convention.md)
- [DSCR Creative Taxonomy](../dscr-dna/dscr-creative-taxonomy.md)
- [DSCR Campaign Launch SOP](../media-buying/dscr-campaign-launch-sop.md) — sibling shape

