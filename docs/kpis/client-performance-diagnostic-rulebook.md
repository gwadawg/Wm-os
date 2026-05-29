---
title: Client Performance Diagnostic Rulebook
domain: kpis
owner: client-success
status: draft
last_updated: 2026-05-28
review_cycle: monthly
artifact_type: rulebook
---

# Client Performance Diagnostic Rulebook

## Purpose

Define **how to interpret** client and cross-client performance data before any dashboard, report, or AI analysis is built. This document is the logic layer: time windows, account states, layer order, root-cause labels, and when to act vs observe.

**Benchmark numbers** (911 / Below / At / Above tiers) live in [Fulfillment Constraint Diagnosis And KPI Standards](../client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md). This rulebook does not replace those thresholds — it defines **how to apply them**.

## Scope

- Reverse mortgage client fulfillment accounts (Meta → landing → call center → LO).
- **Per-client** account health reviews.
- **Cross-client** reviews of a shared asset (ad, creative, headline, landing page, audience).

Out of scope: acquisition sales KPIs ([sales-kpi-thresholds](acquisition/sales-kpi-thresholds.md)), dashboard wireframes, tool-specific Looker configuration.

## Owner

Primary: **client-success** (account health). Media buying and CSR own layer-specific actions per standards doc.

## Rule 0 — Diagnose before you fix

1. Never implement a fix until the **primary constraint layer** is identified.
2. Work **top of funnel down**: Ads → Landing / opt-in → Call center → Client (LO).
3. Do not blame a downstream layer until upstream layers are cleared or explicitly ruled out with evidence.
4. Every RED or WATCH outcome must produce a **documented root-cause label** and owner — not a list of random optimizations.

---

## Part 1 — North-star and guardrails

### 1.1 Primary account metric

| Rule | Statement |
|------|-----------|
| **NS-1** | **CQPCONV / CPConv** (cost per qualified conversation = ad spend ÷ showed appointments) is the **only metric that declares account health GREEN or not**. |
| **NS-2** | Layer metrics explain **why** CPConv is where it is; they do not override CPConv for account status. |
| **NS-3** | If CPConv is **At or Above KPI** on the active 14-day window, account status is **GREEN** unless **WATCH** rules in Part 2 fire. |

### 1.2 Golden guardrails (do not break these)

| ID | Guardrail |
|----|-----------|
| **G-1** | If CPConv is healthy, **do not chase CPL** or pause a campaign solely because CPL rose — the funnel may be self-selecting quality downstream. |
| **G-2** | If **all layer metrics appear At KPI** but CPConv is Below KPI or 911, label **Data / Attribution** — **no operational fixes** until tracking is validated. Escalate to founder. |
| **G-3** | If **Lead-to-Qual %** is Below KPI, treat as **ads / targeting / messaging** — not call center — until disproven. |
| **G-4** | High CTR + efficient traffic cost + high CPL → suspect **landing / opt-in** before new creative. |
| **G-5** | Check **external factors** (holidays, calendar, GHL, LO reputation, recent campaign edits) before structural diagnosis; if confirmed, **observe 48–72 hours** before funnel changes. |
| **G-6** | GHL or automation changes require **founder approval**; ops may diagnose only. |

---

## Part 2 — Time windows (how to look at data)

The team gets confused when **14 days looks fine** but the account is sliding, or when **recent improvement** is hidden inside a bad 14-day average. Use **multiple windows on purpose** — each answers a different question.

### 2.1 Window definitions

| Window | Code | Question it answers |
|--------|------|-------------------|
| Last 7 complete days | **W7** | What is happening **right now**? (momentum, recovery, early slide) |
| Last 14 complete days | **W14** | What is the **operational status** for Goldilocks and weekly review? |
| Prior 14 days (days 15–28) | **W14-prior** | How does this period compare to the last? (WoW-style) |
| Last 30 complete days | **W30** | Is this a **bad week** or a **structural** problem? |
| Campaign / client age | **Age** | Is the account in **learning** where long windows are misleading? |

**Calendar rule:** Windows are **rolling, complete days** in the account timezone (or reporting timezone if fixed). Partial “today” is excluded unless the whole team agrees otherwise in the dashboard spec.

### 2.2 What each window is for (mandatory use)

| Window | Required for | Not sufficient alone for |
|--------|----------------|---------------------------|
| **W14** | Account status gate, root-cause tree “last 2 weeks” conditions, weekly ops cadence | Declaring “safe” when W7 or W30 disagree |
| **W30** | Separating one-off dip vs chronic underperformance | Same-day tactical fixes on new launches |
| **W7** | Detecting **recovery** or **entering danger zone** before W14 moves | Final GREEN/RED by itself |
| **W14-prior** | Trend vs previous fortnight | New accounts with &lt;28 days of data |

### 2.3 Account status states (use all windows)

Status is **not** only GREEN vs RED. Use this state machine:

```
                    ┌─────────────┐
                    │  DATA_HOLD  │  (metrics don't reconcile)
                    └─────────────┘
                           ▲
     External factor ───────┼─────── observe 48–72h
                           │
    W14 CPConv At KPI ─────┼──── WATCH triggers (2.4)
           │               │
           ▼               ▼
      ┌────────┐      ┌───────────┐
      │ GREEN  │      │   WATCH   │
      └────────┘      └───────────┘
           ▲               │
           │               │ W14 Below KPI
           │               ▼
           │          ┌───────────┐     W7 improving + W30 not 911
           └──────────│    RED    │──────────────────────────────► RECOVERING
                      └───────────┘
```

| Status | Meaning | Typical action |
|--------|---------|----------------|
| **GREEN** | W14 CPConv At or Above KPI; no WATCH triggers | Log weekly; monitor W7 |
| **WATCH** | CPConv looks OK on W14 but **risk is building** (see 2.4) | No major fixes yet; increase review frequency; pre-document likely constraint |
| **RECOVERING** | W14 still Below KPI but W7 CPConv At KPI **and** W7 better than W14-prior on CPConv or primary driver | Continue current plan; do not panic-reset; re-check in 7 days |
| **RED** | W14 CPConv Below KPI or 911, **and** W30 confirms OR W7 not improving | Run full layer diagnosis (Part 4) |
| **DATA_HOLD** | G-2 fired or disposition/tracking incomplete | Fix data first |

### 2.4 WATCH triggers (14d looked fine; danger anyway)

Assign **WATCH** (not GREEN) if **any** of the following is true while W14 CPConv is At KPI:

| ID | Condition | Why |
|----|-----------|-----|
| **WT-1** | W30 CPConv is **Below KPI** while W14 is At KPI | Improvement is recent; structural issue may still exist |
| **WT-2** | W7 CPConv is **worse tier** than W14 CPConv (e.g. W14 At, W7 Below) | Recent slide not yet in 14d average |
| **WT-3** | W7 CPConv **≥15% worse** than W14-prior CPConv (same 7-day length) | Accelerating deterioration |
| **WT-4** | Any **911-tier layer metric** on W7 or W14 (CTR, frequency, CPQL, booking, show, etc.) | Upstream failure will hit CPConv on lag |
| **WT-5** | Lead volume on W7 **&lt;50%** of expected weekly pace (spend unchanged) | Funnel choking before cost metrics move |

**WATCH action:** Do not run full RED playbook. Document risk, identify likely layer from WT-4, review again in **7 days** or on next weekly cadence.

### 2.5 RED vs “bad week” (14d + 30d together)

| W14 CPConv | W30 CPConv | Label | Rule |
|------------|------------|-------|------|
| Below KPI | Below KPI | **RED — structural** | Full diagnosis; 5-business-day action plan |
| Below KPI | At KPI | **RECOVERING or bad week** | If WT-2/WT-3 false and W7 At KPI → **RECOVERING**; else **RED — acute** (recent break) |
| Below KPI | 911 | **RED — 911** | Same-day escalation per standards |
| At KPI | Below KPI | **WATCH** (WT-1) | Do not close account review as “fine” |

### 2.6 RECOVERING rules (recent improvement)

| ID | Rule |
|----|------|
| **RC-1** | **RECOVERING** only if W14 CPConv is still Below KPI but **W7 CPConv is At KPI** (or better tier than W14). |
| **RC-2** | Do not revert winning changes made in the last 7 days solely because W14 still looks red — W14 is a **lagging** summary. |
| **RC-3** | RECOVERING expires → **GREEN** when **full W14** rolls to At KPI; → **RED** if W7 slips back Below KPI. |
| **RC-4** | Communicate to team: “Improving — confirm on next weekly before scaling spend or declaring victory.” |

### 2.7 New and low-volume accounts

| Age / volume | Rule |
|--------------|------|
| **&lt;14 days live** | W14 status is **provisional**. Prefer W7 + spend pace + setup checklist over tier labels. Label **LAUNCH** in notes. |
| **&lt;30 days live** | W30 optional; use W14 + W7 + launch checklist. |
| **&lt;10 qualified conversations in W30** | Do not treat Close Rate or CPConv tiers as statistically stable; flag **low volume** on every review. |
| **&lt;5 leads in W7** | Do not compare opt-in or lead-to-qual % across weeks; flag **insufficient sample**. |

### 2.8 Which window drives which decision

| Decision | Primary window | Must also check |
|----------|----------------|-----------------|
| Weekly account color (Green / Watch / Red) | W14 CPConv | W7, W30, WATCH table |
| Root-cause tree “last 2 weeks” | W14 layer metrics | W30 for persistence |
| “Is it getting better?” | W7 vs W14-prior | W14 CPConv |
| “Are we safe for the month?” | W30 CPConv | W7 for early warning |
| Escalate 911 | W14 or W7 (either) | Same day if either hits 911 on CPConv or critical layer |

---

## Part 3 — Analysis modes

### 3.1 Mode A — Single client (account health)

**Question:** Is this client healthy, at risk, or failing — and **which layer** is the constraint?

**Order of operations:**

1. Data quality gate (dispositions, tracking, appointment sheet).
2. External factors (G-5).
3. Account status (Part 2) from CPConv on W14 + WATCH/RECOVERING.
4. If RED or WATCH with WT-4: layer scorecard on **W14** (tiers from standards doc).
5. If RED: persistence check on **W30**.
6. Apply root-cause label (Part 5) — **one primary**, optional secondary.
7. Action plan with owner and success metric.

### 3.2 Mode B — Cross-client asset (ad, headline, creative, LP)

**Question:** How does this **shared piece** perform across accounts — should we scale, kill, or test?

| ID | Rule |
|----|------|
| **XC-1** | Cross-client conclusions require **≥3 clients** with the asset active and **≥ combined 30 qualified leads** (or founder-approved lower bar documented). |
| **XC-2** | Exclude **LAUNCH** accounts (&lt;30 days) from pools unless reviewing launch-specific tests. |
| **XC-3** | Rank assets by **CPQL and lead-to-qual %** first for top-of-funnel; by **CPConv contribution** where downstream data is shared and reliable. |
| **XC-4** | A winning headline on Client A with **WT-1 on Client B** does not override Client B’s account status — fix per client, learn globally. |
| **XC-5** | Report **distribution**, not only average: min, max, median CPQL/CPConv across clients to catch one bad account skewing average. |
| **XC-6** | Tag asset reviews with **archetype, format, and offer angle** so “headline” is not isolated from message match. |

**Headline / LP cross-client:** Always pair **opt-in rate** with **lead-to-qual %** and **CPQL**. High opt-in + weak qual = soft qualification (standards §2.1).

---

## Part 4 — Layer rules (constraint identification)

### 4.1 Layer order (fixed)

| Layer | Metrics (tier from standards doc) | Owner role |
|-------|-----------------------------------|------------|
| **L1 — Ads** | CTR, Frequency, CPL, **CPQL** | Media buyer |
| **L2 — Landing** | Opt-in rate, Lead-to-Qual % | Media buyer (+ CSR for qual reasons) |
| **L3 — Call center** | Contact rate, **Booking rate** | CSR manager |
| **L4 — Client (LO)** | Show rate, Close rate | Client success |
| **L5 — Full funnel** | **CPConv / CQPCONV** | Client success |

### 4.2 Primary constraint rule

| ID | Rule |
|----|------|
| **L-R1** | The **primary constraint** is the **earliest layer** (lowest L number) with any metric at **Below KPI or 911** on **W14** that materially explains CPConv miss. |
| **L-R2** | If L1 CPQL is At KPI, **do not** label L1 as primary constraint even if CPL is high (G-1). |
| **L-R3** | **Contact rate** vs **booking rate**: diagnose split first — different fixes (technical dial vs script). |
| **L-R4** | Low show rate with healthy booking → **L4**, not L3. |
| **L-R5** | Low close rate with healthy show → investigate **lead quality (L1–L2)** before LO coaching. |

### 4.3 Lag awareness (why 14d hides problems)

| Layer metric | Typical lag before CPConv moves |
|--------------|--------------------------------|
| CTR / frequency | Days |
| CPL / CPQL | Days to ~1 week |
| Opt-in / lead-to-qual | Days to ~1 week |
| Booking / contact | ~1–2 weeks |
| Show rate | ~2–3 weeks |

**Rule L-LAG:** If W7 shows 911 or Below KPI on an upstream layer, assign **WATCH** or start layer fixes even when W14 CPConv is still At KPI.

---

## Part 5 — Root-cause labels (decision logic)

Use **one primary label** per review. Map from **W14** conditions unless noted.

| Label | Layer | When to assign (summary) |
|-------|-------|---------------------------|
| **Landing Page** | L2 | Strong CTR + traffic efficiency; CPL/CPQL high; opt-in Below KPI; message mismatch suspected |
| **Lead Quality** | L1–L2 | CPL OK; CPQL Below KPI; lead-to-qual Below KPI |
| **Lead Cost** | L1 | CPL and CPQL both Below KPI |
| **Call Center** | L3 | CPQL At KPI; contact and/or booking Below KPI |
| **Show Rate** | L4 | CPQL and booking At KPI; show Below KPI |
| **Close Rate / LO** | L4 | Shows healthy; close Below KPI after qual verified |
| **Data / Attribution** | — | All layers At KPI; CPConv bad; or tracking/disposition failure |
| **External / Seasonal** | — | G-5 confirmed; observe before layer fixes |
| **Launch / Setup** | — | Age &lt;14d or setup checklist incomplete |

**Decision tree (W14, after external factors cleared):**

1. CPQL Below + CPL OK → **Lead Quality**
2. CPQL Below + CPL Below → **Lead Cost**
3. CPQL OK + booking/contact Below → **Call Center** (split contact vs booking)
4. CPQL OK + booking OK + show Below → **Show Rate**
5. High CTR + CPL problem + opt-in Below → **Landing Page**
6. All layers pass + CPConv bad → **Data / Attribution**
7. Else → document **multi-factor** with ranked hypotheses; do not skip layer order

Full condition table: [standards doc §5](../client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md).

---

## Part 6 — Opt-in and headline testing rules

| ID | Rule |
|----|------|
| **OI-1** | Opt-in rate is interpreted **with** lead-to-qual % and CPQL — never alone. |
| **OI-2** | Opt-in **Above KPI** + CPQL **Below KPI** → qualification likely **too soft**; do not celebrate opt-in. |
| **OI-3** | Opt-in **Below KPI** + CTR **At KPI** → **Landing Page** constraint; test headline **message match** to ad before new creative. |
| **OI-4** | Headline tests: minimum **100 landing page visitors per variant** before winner/loser call (or 7 days, whichever is later). |
| **OI-5** | Cross-client headline winner requires **XC-1** sample rules and **OI-1** on aggregate qual metrics. |
| **OI-6** | Changing headline without aligning ad primary text = invalid test; flag **message mismatch**. |

---

## Part 7 — Review cadence and documentation

| Cadence | Scope | Windows | Output |
|---------|-------|---------|--------|
| **Weekly** | Every active client | W14 + W7 + WATCH check | Status + one-line reason |
| **Monthly** | Strategic / portfolio | W30 + cross-client themes | Pattern notes for creative/ops |
| **Ad hoc** | 911 or client complaint | W7 + W14 immediately | RED playbook + founder if required |

**Documentation minimum (any RED, WATCH, or RECOVERING):**

- Client name, date, windows used
- Account status (Part 2)
- Primary root-cause label (Part 5)
- Layer scorecard snapshot (tiers only — numbers in dashboard later)
- Owner + next check date

---

## Part 8 — Escalation (from standards; logic only)

| Trigger | Escalate to founder |
|---------|---------------------|
| Any metric **911** tier on W14 or W7 | Same day |
| CPConv 911 | Same day |
| **Data / Attribution** label | Immediately; no ops changes |
| RED with no layer explains CPConv | Same day |
| GHL change needed | Before change |

---

## Part 9 — Benchmark authority and known conflicts

| Source | Role |
|--------|------|
| [Fulfillment Constraint Diagnosis And KPI Standards](../client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md) | **Canonical tiers** for layers and CPConv ($80–149 At, etc.) |
| [RM Client KPI Check](../operations/systems/rm-client-kpi-check.md) | **Operational workflow** (Goldilocks steps, ClickUp) — if tiers conflict with standards, **standards win** until founder updates |
| [Constraint Troubleshooting SOP](../client-fulfillment/client-success/constraint-troubleshooting-sop.md) | **Playbook actions** after label is set |

**Open reconciliation (founder to confirm):**

- [ ] RM KPI check lists CPConv At KPI **$80–100**; standards doc lists **$80–149.99** — pick one band for dashboards and AI.
- [ ] Opt-in Below KPI band: troubleshooting SOP mentions **8–9.9%**; standards use **10–14.9%** — align tiers.
- [ ] Lead-to-Qual At KPI: **50–65%** (standards) vs **45–55%** (troubleshooting table) — align tiers.

Until reconciled, this rulebook uses **fulfillment-constraint-diagnosis-kpi-standards.md** for tier boundaries.

---

## Part 10 — What dashboards and AI must implement later

Any dashboard, sheet, or AI agent **must** implement:

1. **All windows** W7, W14, W14-prior, W30 on CPConv and layer metrics.
2. **Account status** from Part 2 (including WATCH and RECOVERING).
3. **Primary constraint layer** from Part 4, not “lowest metric on page.”
4. **Root-cause label** from Part 5.
5. **Mode switch**: client vs cross-client asset (Part 3).
6. **Low-volume and LAUNCH flags** (Part 2.7).
7. **Benchmark source** pinned to standards doc §6 quick reference.

---

## Related docs

- [Fulfillment Constraint Diagnosis And KPI Standards](../client-fulfillment/client-success/fulfillment-constraint-diagnosis-kpi-standards.md) — tiers and levers
- [Constraint Troubleshooting SOP](../client-fulfillment/client-success/constraint-troubleshooting-sop.md) — fixes after diagnosis
- [RM Client KPI Check](../operations/systems/rm-client-kpi-check.md) — weekly ops workflow
- [RM High-Quality Lead Acquisition](../client-fulfillment/client-marketing/rm-high-quality-lead-acquisition.md) — qual and CPConv optimization

## Open questions

- [ ] Confirm WATCH thresholds (15% CPConv W7 vs W14-prior — adjust if too sensitive).
- [ ] Confirm minimum sample sizes for cross-client and headline tests.
- [ ] Reconcile benchmark conflicts in Part 9 with founder sign-off.
