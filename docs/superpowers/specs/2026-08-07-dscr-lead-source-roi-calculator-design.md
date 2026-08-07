---
title: DSCR Lead Source ROI Calculator Design
domain: acquisition
owner: founder
status: draft
last_updated: 2026-08-07
review_cycle: monthly
artifact_type: overview
related_docs:
  - docs/client-fulfillment/dscr-dna/dscr-gtm-positioning-brief.md
  - docs/client-fulfillment/dscr-dna/dscr-kpi-and-test-scorecard.md
  - docs/client-fulfillment/dscr-dna/dscr-offer-and-funnel-map.md
  - docs/acquisition/sales/intro-call-qualification-framework.md
---

# DSCR Lead Source ROI Calculator Design

## Purpose

Give sales a **visual, screen-shareable side-by-side ROI calculator** that
compares a DSCR loan officer’s **current lead source** to **Waiz as a lead
source** at the same ad spend. The story is not “you have no leads” (typical
Reverse angle) — DSCR LOs usually already buy leads and spend hard. The pitch
is: **same (or comparable) media spend → better CPL quality, contact rate,
close rate, cost per conversation, and net commission.**

Primary use: founder (or closer) drives the call, fills **Current**, seeds
**With Waiz**, and makes the delta obvious. Secondary: public link so the LO
can sandbox after the call without Mr. Waiz access.

## Strategic framing (DSCR vs Reverse)

| Reverse sales tilt | DSCR sales tilt |
|--------------------|-----------------|
| Market problem in reverse marketing; education-heavy | LO already has lead gen / referrals / spend |
| “We generate pipeline you don’t have” | “We improve ROI on budget you already spend” |
| Funnel sophistication / channel leverage | Bake-off: their source vs ours on downstream KPIs |

This calculator is a **sales proof asset**, not the full internal Funnel
Simulator (which remains the ops/RM-style multi-stage model).

## Relationship to existing product

| Existing | Relationship |
|----------|----------------|
| Mr. Waiz **Funnel Simulator** (`FunnelSimulatorView` + `kpi-simulator`) | **Sibling, not merge.** Add a sub-tab: **Funnel** \| **Lead source ROI**. Do not cram this simpler bake-off into the multi-stage rate model. |
| Funnel Simulator URL encode/decode (`encodeSimulatorState`) | **Reuse the pattern** (base64 JSON query param) with a **separate** state schema for this calculator. |
| DSCR DNA KPI scorecard | Supplies future real range seeds; v1 uses configurable placeholders until deliverable bands are approved. |

## Scope

### In (v1)

- Two-column **Current stack** vs **With Waiz**
- Linked **ad spend** (Current → Waiz by default; optional unlink)
- Bidirectional **spend / CPL / leads** (driver-based)
- Inputs: contact rate, close rate (of contacts), avg commission
- Optional **program fee** toggle (ad spend only by default)
- Outcomes: contacts, deals, cost per conversation, net commission $, ROI×, ROI%
- **Delta** strip as visual hero (especially net $)
- `?` tooltips on every field
- Waiz **worst / best** range captions on key inputs + outcome band
- Public full **sandbox** (all fields editable both sides)
- Shareable URL state (no auth on public shell)
- Shared calc core + two shells (internal Mr. Waiz + public page)
- Unit tests for math + encode/decode

### Out (v1)

- Live client metrics autofill from Supabase
- Writing results to client records or CRM
- Full RM stage funnel (qual → book → show → funded pipeline)
- Login / accounts on public page
- Email capture or lead forms on the calculator
- PDF export
- Multi-currency
- Guarantees of results (disclaimer required)
- Mixing this into `kpi-simulator` rate tables as one model

## Product decisions (locked)

| Decision | Choice |
|----------|--------|
| Column story | **A** — Current stack vs With Waiz |
| Waiz column behavior | **1** — Linked spend + editable rates (seed defaults) |
| Cost model | **C** — Ad spend primary; optional “Include program fee” |
| ROI presentation | **C** — Hero = net commission $; secondary = × and % |
| Public openness | **A** — Full sandbox both sides |
| Worst/best guidance | **C** — Captions under Waiz inputs + band on outcomes |
| Architecture | **2** — Shared calc core + internal shell + public shell |

---

## Architecture

```
┌──────────────────────────────────────┐
│  lead-source-roi core (pure TS)      │
│  math · drivers · link rules         │
│  ranges · encode/decode · config     │
└──────────────────┬───────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
  Mr. Waiz shell        Public shell
  Funnel Simulator      /tools/lead-source-roi
  sub-tab (auth)        (no chrome, no client data)
```

**Implementation home:** Mr. Waiz app
(`call-center-reporting-template`), not Wm-os. Wm-os owns this design
spec and sales/process narrative; the live calculator lives next to
existing Funnel Simulator code.

### Surfaces

| Surface | Audience | Placement | Auth |
|---------|----------|-----------|------|
| Internal | Founder / sales | Funnel Simulator area → sub-tab **Lead source ROI** | Yes (existing app) |
| Public | Prospect LO | Public route e.g. `/tools/lead-source-roi` | No |

Same UI component; shells differ only by chrome, share helpers, and branding weight.

### Module layout (proposed)

| Unit | Responsibility |
|------|----------------|
| `src/lib/lead-source-roi/math.ts` | Pure outcomes from inputs |
| `src/lib/lead-source-roi/state.ts` | Drivers, link sync, encode/decode |
| `src/lib/lead-source-roi/config.ts` | Seeds, ranges, tooltips, disclaimer |
| `src/lib/lead-source-roi/types.ts` | Input/output types |
| `src/components/LeadSourceRoiCalculator.tsx` | Shared interactive UI |
| Funnel Simulator parent | Internal sub-tab host |
| `src/app/tools/lead-source-roi/page.tsx` | Public shell |

Exact paths may adjust to repo conventions; boundaries above are required.

---

## UI design

### Layout (screen-share first)

One composition: story controls → two input columns → outcomes + delta.
Not a multi-widget dashboard.

```
Header: title, one-line pitch, Share link, Reset
Controls: Ad spend only | Include program fee · Spend linked | Unlinked
┌─────────────────────┬─────────────────────┐
│ CURRENT STACK       │ WITH WAIZ           │
│ spend, CPL↔leads,   │ same fields         │
│ contact, close,     │ + worst/best captions│
│ avg commission      │ fee when toggle on  │
│ ? tooltips          │ ? tooltips          │
└─────────────────────┴─────────────────────┘
Outcomes (side by side) + center DELTA
  contacts · deals · cost/convo · net $ · ROI× · ROI%
  base = live Waiz inputs; thin worst–best band from config pack
```

### Field model

| Field | Both columns | Notes |
|-------|--------------|-------|
| Ad spend | Yes | Linked Current → Waiz by default |
| CPL | Yes | Bidirectional with leads |
| Leads | Yes | Calculated or driving |
| Contact rate | Yes | % of leads that became a real conversation |
| Close rate | Yes | % of **contacts** that fund/close (not % of all leads) |
| Avg commission | Yes | Linked Current → Waiz by default |
| Program / vendor fee | Optional | Toggle global; fee fields relevant when on |

### Tooltips

Every field has a `?` control (corner or label-adjacent):

- Plain definition (1 line)
- Why it matters for ROI (1 line)

Copy lives in `config.ts` so ops can edit without UI rewrites.

### Waiz worst / best (full sandbox still)

Public and internal: **all inputs remain freely editable** on both sides.

Additionally on **With Waiz**:

1. **Under inputs** (CPL, contact rate, close rate at minimum): light caption  
   `Typical deliverable: {worst}–{best}`  
   For CPL, “best” is the **lower** dollar cost.
2. **On outcomes**: large **base** numbers from live typed rates; secondary
   **worst–best band** on net commission $ and deals from the approved
   **conservative pack** and **optimistic pack** at the same Waiz spend
   (and fee if toggle on).

Base case is always “what is currently typed,” not a third forced column.

### Visual hierarchy (close moment)

1. **Delta net commission $** (primary)
2. Side-by-side net $ and deals
3. Cost per conversation, ROI×, ROI%
4. Minimal comparison bars only if they aid scan (no chart clutter)

### Public shell extras

- No app nav / client data
- Light Waiz branding
- Fixed disclaimer (illustrative model, not a guarantee)
- Full field sandbox

### Internal shell extras

- “Copy public link” → absolute URL with encoded state
- “Reset” → config seeds
- Sub-tab next to existing Funnel view

### Aesthetic direction (frontend)

Built inside Mr. Waiz: **match existing Funnel Simulator / app visual
language** (dark ops UI, tabular numbers, existing tokens) rather than a
marketing landing-page aesthetic. Distinctiveness comes from clarity of
the two-column compare and delta hierarchy, not a separate brand system.
Public shell may slightly simplify chrome but should feel like the same
tool so screen share and LO sandbox match.

---

## Math and link rules

### Per-column formulas

```
leads              = spend / cpl          when driver = cpl
cpl                = spend / leads        when driver = leads

contacts           = leads × contact_rate
deals              = contacts × close_rate
gross_commission   = deals × avg_commission

investment         = ad_spend
                   + (program_fee if fee toggle on for that side)

net_commission     = gross_commission − investment     // hero $
roi_multiple       = gross_commission / investment     // e.g. 4.2×
roi_pct            = (gross_commission − investment) / investment

cost_per_conversation (ad only) =
  ad_spend / contacts

cost_per_conversation (loaded, fee on) =
  investment / contacts
  label clearly as loaded when fee toggle is on
```

### Spend / CPL / leads drivers

Each column keeps `driver: 'cpl' | 'leads'`.

| User action | Effect |
|-------------|--------|
| Edit CPL | `driver = cpl`; recompute leads |
| Edit leads | `driver = leads`; recompute cpl |
| Edit spend + driver cpl | recompute leads |
| Edit spend + driver leads | recompute cpl |

Never divide by zero: invalid/zero denominators yield `—` on dependents and
block ROI display until valid.

### Linked fields

| Link | Default | Behavior |
|------|---------|----------|
| Ad spend | On | Waiz.spend mirrors Current.spend |
| Avg commission | On | Waiz mirrors Current until unlinked |
| Rates (contact, close, CPL) | Never auto-synced | Story is intentional rate gap |
| Fee toggle | Off | Global; when on, investment includes fees |

### Fee toggle (cost model C)

- **Off:** investment = ad spend; pure lead-source bake-off.
- **On:** each side may include a fee field (Waiz program fee required for
  the point; Current vendor fee optional so left can stay media-only).

### Worst / base / best packs (Waiz)

Config shape (example keys):

```ts
waiz_ranges = {
  cpl: { worst: number, best: number },           // worst = higher $
  contact_rate: { worst: number, best: number },  // rates as decimals or %
  close_rate: { worst: number, best: number },
}
```

- **Base outcomes** = live Waiz inputs
- **Worst outcomes** = Waiz spend (+ fee if on) + conservative pack  
  (higher CPL, lower contact, lower close)
- **Best outcomes** = same spend (+ fee) + optimistic pack  
- Captions show per-field range; **band uses packed bounds** (not
  cherry-picking mid-call extremes)

### Edge cases

| Case | Behavior |
|------|----------|
| contact or close outside 0–100% | Soft clamp and/or field error; no silent absurd ROI |
| contacts = 0 | Hide ROI/cost-per-convo hero; message “Need contacts to model revenue” |
| Corrupt URL state | Fall back to demo seeds; non-blocking notice |
| Spend unlinked | Columns independent on spend only |

### Disclaimers

Public (and shareable state always renders public disclaimer):

> Illustrative model for planning discussion. Results vary. Not a guarantee of performance or ROI.

Internal tooltips may be coachier; never guarantee language in UI chrome.

---

## State, sharing, defaults

### URL state

Mirror Funnel Simulator pattern:

- Query param e.g. `?s=<base64url JSON>`
- Payload: both columns’ inputs, drivers, link flags, fee toggle, fees
- No PII, no DB, no accounts
- Invalid payload → demo seeds + soft error toast

Internal **Copy public link** builds:

`https://{host}/tools/lead-source-roi?s=...`

Public route always full sandbox; encoded state only pre-fills.

### Default seeds (placeholders — retune in config)

Structure required; numeric seeds are **illustrative until ops approves real
DSCR deliverable bands**.

| Input | Current demo | Waiz base seed | Range captions |
|-------|--------------|----------------|----------------|
| Ad spend | e.g. $10,000 | linked same | — |
| CPL | e.g. $75 | e.g. $55 | worst–best $ |
| Contact % | e.g. 20% | e.g. 32% | worst–best % |
| Close % | e.g. 15% | e.g. 18% | worst–best % |
| Avg commission | e.g. $4,500 | linked same | — |
| Program fee | $0 / off | editable when toggle on | — |

**Reset** restores config seeds. Shared links with `s=` skip blank demo.

### Config single source

`config.ts` (or adjacent JSON) owns:

- Demo seeds
- Waiz worst/best ranges
- Default fee when toggle on
- Tooltip strings
- Disclaimer string
- Product label (“DSCR lead source ROI”)

---

## Data flow

```
User edits field
  → state.ts applies driver + link rules
  → math.ts computes Current + Waiz base + Waiz worst pack + Waiz best pack
  → UI renders columns, outcomes, delta, bands
  → optional: encode to URL on Share
```

No server math required for v1; pure client-side.

---

## Error handling

| Failure | UX |
|---------|-----|
| Division by zero / empty required | Em dashes; no fake infinite ROI |
| Bad percentage | Inline field validation |
| Decode failure | Seeds + toast |
| Copy link failure | Toast failure; state still in-memory |

---

## Testing

| Suite | Covers |
|-------|--------|
| `math` unit | Formulas; fee on/off; zero guards |
| `state` unit | CPL↔leads drivers; spend link; commission link |
| `encode/decode` | Round-trip fidelity |
| Range sanity | For approved seeds, worst net $ ≤ base ≤ best under normal packs (document exceptions if fee dominates) |

No E2E required for v1 if unit coverage of core is solid.

---

## Success criteria

1. On a DSCR sales call, **Current** can be filled in ~90 seconds.
2. Delta **net commission $** is readable at a glance on screen share.
3. Tooltips explain each lever without a separate deck.
4. Fee toggle supports “what about your cost?” without leaving ad-spend story first.
5. Public link opens the same comparison; LO can change any field (sandbox).
6. Worst/best captions and outcome band keep open sandbox grounded in what
   Waiz is willing to call deliverable range.

---

## Implementation notes (for planning — not approval to code yet)

1. Add pure modules + tests first.
2. Build shared `LeadSourceRoiCalculator` UI against existing dark ops styles.
3. Wire Funnel Simulator sub-tab.
4. Add public route and confirm it is allowed without auth middleware.
5. Seed ranges; founder retunes before first live use.
6. Optional later: “apply client actuals” from metrics (explicitly out of v1).

---

## Open items for founder (config, not design blockers)

- Final numeric **Waiz CPL / contact / close** worst–best bands from real DSCR
  delivery once stable.
- Default **program fee** and how to label package levels if fee toggle is on.
- Exact **public path** and hosting URL for copy-link.

Design is complete without those; they land as config constants at ship.
