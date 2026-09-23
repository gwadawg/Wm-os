---
title: DSCR Campaign Launch SOP
domain: client-fulfillment
owner: media-buying-lead
status: active
last_updated: 2026-09-23
review_cycle: monthly
artifact_type: sop
product: dscr
shareability: internal-fulfillment
canonical_for: dscr-campaign-structure-launch
related_docs:
  - docs/client-fulfillment/dscr-dna/dscr-creative-taxonomy.md
  - docs/client-fulfillment/dscr-dna/intelligence-icp-dscr.md
  - docs/client-fulfillment/media-buying/creative-testing-structure.md
  - docs/client-fulfillment/media-buying/ad-naming-convention.md
---

# DSCR Campaign Launch SOP

**Status: active — use for new DSCR accounts.** Do not migrate live accounts
blindly; apply when opening a new cold test / rebuilding structure. Builds on
over time (warm splits, scale rules, roster waves).

> **Team PDF (external handout):**  
> [DSCR Campaign Launch Playbook](assets/dscr-campaign-launch-playbook/dscr-campaign-launch-playbook.pdf)

**Buckets / labeling:** [dscr-creative-taxonomy.md](../dscr-dna/dscr-creative-taxonomy.md)  
**Who + NEVER:** [intelligence-icp-dscr.md](../dscr-dna/intelligence-icp-dscr.md)

---

## Purpose

Give a media buyer one clear way to open a **new DSCR refinance** Meta account:
campaign names, ad sets, budgets, gates, and when to open warm / scale.

## Scope

Day-1 launch through first warm pool and first Scale campaign. DSCR only.
Housing Special Ad Category. Broad targeting — creative is the targeting.

**Out of scope (for now):** roster-wave testing across accounts, RM structure,
detailed creative brainstorming.

## Trigger

New DSCR client ad account ready to spend (funnel live, licensed states known,
at least one creative per cold bucket you plan to run).

## Owner

Media buyer (execution). Media-buying lead (standards + reviews).

## Inputs

- Client daily budget + licensed state(s)
- Perspective / external LP live (no native Meta lead forms)
- Creatives labeled per taxonomy (`bucket` · `creative_job` · `concept_slug`)
- Mr. Waiz `ad_name` checked
- DSCR CPL / CPQL targets written down (**do not** import RM $25 CPL)

## Outputs

- Live `{client}_dscr_test` ABO campaign
- Optional `{client}_dscr_warm` when engagers exist
- Optional `{client}_dscr_scale` CBO after winners prove
- UTMs firing with `ad_name` into reporting

## Quality bar

- One **constraint bucket** = one cold ad set = one primary creative
- Creative jobs (offer / authority / outcome) are **ads inside warm**, not
  separate warm ad sets at launch
- TOF cold ads number-free unless client-approved tokens
- Refinance only · business-purpose · peer-to-operator

---

## Operating content

### 1. The structure (memorize this)

```text
DAY 1
{client}_dscr_test          (ABO)
├── cold_denied             1 ad · DENIED · program reveal
├── cold_deadline           1 ad · DEADLINE · mapped exit   (smaller pool)
└── cold_idle               1 ad · IDLE · belief break      (largest pool, slower)

WHEN ENGAGERS EXIST (~week 2–3)
{client}_dscr_warm          (ABO)
└── warm_convert            2–3 ads in ONE set
                            · terms / checklist
                            · lo-authority (client brand)
                            · outcome / uses (optional)

AFTER A WINNER PROVES
{client}_dscr_scale         (CBO)
└── scale_winners           proven creatives only
```

| Layer | What earns a budget line |
|-------|--------------------------|
| Cold ad set | Constraint bucket (DENIED / DEADLINE / IDLE) |
| Warm ad set | Temperature (one convert set at launch) |
| Creative job | Tag on the **ad** — not an ad set |

**IN-MARKET** (rate-card / terms-only) lives in **warm_convert** at launch —
not a fourth cold ad set. Add a cold IN-MARKET set only later, with approved
numbers and enough budget to fund it without starving the core three.

### 2. Account settings (every campaign)

| Setting | Value |
|---------|-------|
| Objective | Leads → Website (Perspective / external LP) |
| Special Ad Category | Housing |
| Audience | Broad · licensed state(s) only · no detailed targeting |
| Advantage+ suggestions | Empty |
| Native Meta lead forms | **No** |
| UTMs | `utm_content={{ad.name}}` · `utm_medium={{adset.name}}` · `utm_campaign={{campaign.name}}` |

### 3. Day-1 budget split

DEADLINE is real but **smaller**. IDLE is **cold** (belief-break) but slower.
Don’t fund them equally forever.

| Daily budget | Ad sets | Split (guide) |
|--------------|---------|----------------|
| **$50–$75** | DENIED + IDLE | ~60% DENIED / ~40% IDLE — park DEADLINE |
| **$75–$150** (default) | All three | ~45% DENIED / ~35% IDLE / ~20% DEADLINE |
| **$150–$300** | All three + format twin optional | Same ratios; 2nd ad in a set only if **format** differs (static + UGC) |

**Default mid-tier example (~$90/day):** DENIED ~$40 · IDLE ~$30 · DEADLINE ~$20.

### 4. Ads per cold ad set

| Rule | Detail |
|------|--------|
| Strict (recommended) | **1 ad** per cold ad set |
| Stretch | **2 max** — same bucket, different format only |
| Do not | 3+ lookalike statics in one set |

Bleed headlines (e.g. “How investors take cash out of their rentals”) → sort
with taxonomy rule → **one primary bucket** (usually IDLE). Do not invent a
new niche ad set.

### 5. Suggested day-1 creatives

| Ad set | Concept slug | Job |
|--------|--------------|-----|
| `cold_denied` | `nodocs-speed` | Tax returns / write-offs → rent qualifies |
| `cold_deadline` | `balloon-exit` | Bridge / balloon → map the exit |
| `cold_idle` | `cashout-grow` | Idle equity → belief break (not outcome list) |

Ad name: `dscr_{slug}_{format}_v{n}` — see [ad-naming-convention.md](ad-naming-convention.md).

### 6. Hold and kill (test campaign)

1. **Gate 1:** no edits until **4,000 impressions** per ad set. Then CTR triage
   (kill only if CTR &lt; 0.8% **and** zero qualified leads).
2. **Gate 2:** at ≥ **~$500 spend** on that ad set (or ~2–3× target CPL once
   set), judge **qualified rate / CPQL**, not CPL alone.
3. **IDLE exception:** first pass may use engagement / LP views — still set a
   **review date** (e.g. day 14). Don’t kill IDLE on day-3 CPL alone; don’t run
   it forever with no CPQL path.
4. Runaway: one ad set eating &gt;70% of campaign spend with zero leads after
   3–4 days → pause that set only.

### 7. Warm campaign (week 2–3)

Open `{client}_dscr_warm` when you have engagers (e.g. 50%+ video viewers,
LP viewers, or form starters — enough volume to spend ~$15–25/day without
starving cold).

| Ad set | Ads inside (same set) |
|--------|------------------------|
| `warm_convert` | Checklist / terms · LO authority · outcome/uses (optional) |

Split offer vs authority into **separate warm ad sets** only when each can
hold ~$25–40/day and clear impression gates alone.

### 8. Scale campaign (after proof)

1. Open `{client}_dscr_scale` (CBO).
2. Move proven cold winners in — ladder Problem / Solution / Offer when you
   have the creatives (see [creative-awareness-ladder.md](creative-awareness-ladder.md)).
3. Keep `{client}_dscr_test` ABO for **one new concept at a time**.
4. Horizontal first: another proven bucket before hard budget raises.

### 9. Day-1 setup card (copy for the buyer)

```text
CLIENT: ________    DAILY $: ________    STATES: ________

□ Funnel live (Website) · Housing · broad · suggestions empty
□ CPL / CPQL targets written (not RM $25)

{client}_dscr_test (ABO)
□ cold_denied     dscr_nodocs-speed_…     $___
□ cold_idle       dscr_cashout-grow_…     $___
□ cold_deadline   dscr_balloon-exit_…     $___   (skip if budget <$75)

HOLD until 4,000 impr / ad set → then Gate 1 / Gate 2

LATER
□ {client}_dscr_warm  → warm_convert (terms + authority)
□ {client}_dscr_scale → winners only
```

### 10. Pre-launch checklist

- [ ] Taxonomy labels filled (bucket · job · slug · angle_ref)
- [ ] Ad names checked in Mr. Waiz
- [ ] Cold ads number-free (or tokens client-confirmed)
- [ ] One primary creative per cold ad set
- [ ] Test lead → Perspective → GHL / dashboard with `ad_name`
- [ ] Licensed states only

---

## What this replaces

| Old | Status |
|-----|--------|
| [dscr-abo-launch-setup.md](dscr-abo-launch-setup.md) | **Superseded** — stub redirects here |
| Labeling playbook §5 (7 ad sets) | **Corrected** — matches this SOP |

Advanced / later: [creative-testing-structure.md](creative-testing-structure.md)
(roster waves, Scale+Test doctrine) — do not load for day-1 launch.

## Related

- [DSCR Creative Taxonomy](../dscr-dna/dscr-creative-taxonomy.md)
- [Intelligence ICP DSCR](../dscr-dna/intelligence-icp-dscr.md)
- [Creative Testing Scorecard](creative-testing-scorecard.md)
- [Ad Naming Convention](ad-naming-convention.md)
- Team handout PDF: [assets/dscr-campaign-launch-playbook/](assets/dscr-campaign-launch-playbook/)
