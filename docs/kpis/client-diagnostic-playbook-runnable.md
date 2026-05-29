---
title: Client Diagnostic Playbook (Runnable)
domain: kpis
owner: client-success
status: draft
last_updated: 2026-05-28
review_cycle: monthly
artifact_type: playbook
---

# Client Diagnostic Playbook (Runnable)

## Purpose

A **step-by-step procedure** an AI agent or ops person executes on **one client per run** to produce an account verdict, a single primary constraint, and an owner-tagged action plan. It is the executable form of the [Client KPI Judgment Standard](client-kpi-judgment-standard.md) — all tiers, bands, and override rules come from there.

## Scope

One client, one run. For time-window mechanics (W7/W14/W30, RECOVERING) see [Client Performance Diagnostic Rulebook](client-performance-diagnostic-rulebook.md). For the fixes/levers applied after a label is set, see [Constraint Troubleshooting SOP](../client-fulfillment/client-success/constraint-troubleshooting-sop.md).

## Owner

See [domain owners](../_inventory/domain-owners.md): **client-success**.

## When to use

- Weekly account health review, or
- Ad-hoc on a 911 flag or client complaint.

## Inputs

The [AI-ready schema](client-kpi-judgment-standard.md#10-ai-ready-schema-paste-weekly-for-automated-diagnosis) object for the client (raw counts per window). If the schema is incomplete, Step 0 may halt the run.

---

## Procedure (execute in order — do not skip)

### Step 0 — Data-quality gate

1. `data_quality.appt_sheet_complete == true`? If not → **STOP. Output "Fix data first"** and list the exact missing fields (dispositions, show/no-show flags, spend reconciliation). No layer fixes.
2. `tracking_issues` empty? If a known tracking/attribution issue exists → **DATA_HOLD**, escalate to founder, stop.
3. Confirm `appts_showed` and `spend` exist for **W14** (CPConv denominator + numerator). Missing → cannot compute verdict; request data.

### Step 1 — External factors (Guardrail G-4)

Run `external_factors`. If `holiday`, `meta_platform_change`, `calendar_open_4plus_slots_10d == false`, `lo_reputation_issue`, or `recent_campaign_edit` is true and plausibly explains the dip → **Observe 48–72h**, state what to monitor (CPConv W7, lead volume), and **do not** make structural changes yet. Document the factor.

### Step 2 — CPConv verdict (the Goldilocks gate)

1. Compute `CPConv(W14) = spend ÷ appts_showed`.
2. Classify against [§3.1 bands](client-kpi-judgment-standard.md#31-cpconv-the-verdict-metric): Above < $90 · At $90–150 · Below $150.01–215 · 911 > $215.
3. **At/Above** → check Step 7 leading flags; if none, **GREEN**, log and stop. Apply G-1 (do not chase CPL).
4. **Below** → continue to Step 3.
5. **911** → continue on the fast path **and** add to the same-day founder escalation list.

### Step 3 — Persistence check (bad week vs structural)

Compare `CPConv(W14)` vs `CPConv(W30)` and `CPConv(W7)`:

- W14 Below + W30 Below → **RED — structural** (5-business-day action plan).
- W14 Below + W30 At + W7 At/improving → **RECOVERING** (hold plan, recheck 7d).
- W14 Below + W30 911 → **RED — 911**.
- Insufficient W30 (LAUNCH / low volume) → label provisional, lean on W7 + setup checklist.

### Step 4 — Relational layer scan (top → bottom)

Compute every metric for W14 and assign tiers from [§3.2](client-kpi-judgment-standard.md#32-upstream-bands-re-derived-from-cpconv--cpql--cy):

`CPL`, `CPQL`, `Lead-to-Qual`, `Opt-in`, `Booked/QL`, `Show`, `CY = Booked/QL × Show`, `Close`. Note CTR/frequency as **leading indicators only**.

Walk layers L1 → L4. Stop at the **first layer with a Below/911 metric that materially explains the CPConv miss** — that is the **primary constraint**. Record lower-layer reds as **secondary** (only actioned after upstream clears).

### Step 5 — Root-cause label (relational override rules)

Apply [§6 override rules](client-kpi-judgment-standard.md#6-relational-override-rules-the-it-depends-engine), first matching row wins; tie-break to the earliest layer:

- R1: CPL Below + CPQL At/Above + CPConv At/Above → **GREEN, ignore CPL**
- R2: CPL cheap + CPQL Below → **Lead Quality**
- R3: CPQL Below + Lead-to-Qual Below → **Lead Quality**
- R4: CPQL Below + Lead-to-Qual At + CPL Below → **Lead Cost**
- R5: CPQL At + CY Below → **Downstream conversion** (split Booked/QL vs Show)
- R6: CPQL At + Booked/QL At + Show Below → **Show Rate**
- R7: Opt-in Above + CPQL Below → **Qualification too soft**
- R8: CTR/Freq weak + CPConv At/Above → **WATCH — creative fatigue**
- R9: All layers At + CPConv Below/911 → **DATA_HOLD — attribution**
- R10: Show At + Close Below (lead quality verified) → **LO Consultation**

Headline branch (if `headline_variants` present): opt-in spread > 5pp between variants with similar traffic (≥100 visitors each) → **message-match / headline** diagnosis, not creative fatigue. Opt-in up + CPQL up on the winner → qualification too soft (R7).

### Step 6 — Action plan

For each action, specify all five fields:

| Field | Source |
|-------|--------|
| **Owner role** | media buyer (L1–L2) · CSR manager (L3) · client success (L4 + CPConv) · ops (GHL) · founder (911/data/GHL approval) |
| **Specific lever** | from [Constraint Troubleshooting SOP](../client-fulfillment/client-success/constraint-troubleshooting-sop.md) |
| **Timebox** | e.g. 7d creative refresh, 5 business-day booking audit |
| **Success metric** | the exact number that must move (and to which band) |
| **Do-not-do** | fixes that would violate layer order or guardrails (e.g. "do not pause campaign — R1") |

### Step 7 — Escalation

- Any **911** tier (CPConv or a layer metric) → founder **same day**.
- **DATA_HOLD** / R9 → founder **immediately, no ops changes**.
- **GHL automation** change → ops diagnoses, **founder approves** before change (G-5).

---

## Required output format

### Part 1 — Executive summary (≤8 bullets)
- Account status: GREEN | WATCH | RED | RECOVERING | DATA_HOLD
- Primary constraint layer + label
- CPConv W14 / W30 + trend
- One sentence: "why underperforming"

### Part 2 — Layer scorecard

| Metric | W14 | W30 | Tier | Owner | Contributes to CPConv? |
|--------|-----|-----|------|-------|------------------------|

### Part 3 — Headline / opt-in insights (if variants provided)
- Winner/loser, message-match assessment, recommended next test.

### Part 4 — Action plan (numbered, owner-tagged)
- Each with owner / lever / timebox / success metric / do-not-do.

### Part 5 — AI/dashboard spec (condensed)
- The [§10 schema](client-kpi-judgment-standard.md#10-ai-ready-schema-paste-weekly-for-automated-diagnosis) block to paste next week + the verdict fields the dashboard must surface (status, CPConv tier, primary constraint, CY).

### Part 6 — Open questions / missing data
- Only blockers preventing confident diagnosis.

---

## Worked example

**Input (W14):** spend `$4,200`, leads `210`, qualified_leads `120`, appts_booked `38`, appts_showed `22`, deals_closed `5`. W30 CPConv `$182`.

**Step 0–1:** appt sheet complete, no tracking issues, no external factor. Proceed.

**Step 2 — CPConv verdict:**
`CPConv = 4,200 ÷ 22 = $190.91` → **Below KPI** ($150.01–215). Continue.

**Step 3 — persistence:** W14 $191 Below + W30 $182 Below → **RED — structural**.

**Step 4 — layer scan (W14):**

| Metric | Calc | Value | Tier |
|--------|------|-------|------|
| CPL | 4,200 ÷ 210 | $20.00 | Below (diagnostic only) |
| Lead-to-Qual | 120 ÷ 210 | 57.1% | At KPI (50–65) |
| CPQL | 4,200 ÷ 120 | $35.00 | **911** (> $32) |
| Booked/QL | 38 ÷ 120 | 31.7% | At KPI (28–34) |
| Show | 22 ÷ 38 | 57.9% | Below (52–60) |
| CY | 0.317 × 0.579 | 0.183 | At KPI (0.167–0.24) |
| Close | 5 ÷ 22 | 22.7% | At KPI (20–35) |

**Cross-check:** `CPConv = CPQL ÷ CY = 35 ÷ 0.183 = $191` ✅ (matches spend ÷ showed).

First layer with a verdict-grade miss: **L1 (CPQL 911)**. Lead-to-Qual is healthy, so leads *do* qualify — they are simply expensive. Show rate Below is a **secondary** L4 constraint (actioned after L1).

**Step 5 — label:** CPQL Below(911) + Lead-to-Qual At + CPL Below → **R4 → Lead Cost (L1)**. Not a quality problem (R2/R3 don't match), not downstream (CY is At, so R5 doesn't fire as primary).

**Step 6 — action plan (abridged):**
1. **Media buyer** — rotate 3–5 new creatives + check frequency/audience size. Timebox 7d. Success: CPQL → ≤ $25 (At). Do-not-do: don't tighten qualification (lead-to-qual already At — that would cut volume without fixing cost).
2. **Client success** — secondary: audit GHL reminder sequence for show rate. Timebox 5 business days. Success: Show → ≥ 60%. Do-not-do: don't prioritize over L1; CPConv won't clear until CPQL drops.

**Step 7 — escalation:** CPQL is **911** → notify founder **same day**.

**Verdict:** RED — structural. Primary constraint **Lead Cost (L1)**: qualified leads cost $35 (911) while they qualify fine, dragging CPConv to $191.

---

## Quality bar

- Show arithmetic for CPConv (`spend ÷ showed`) and the `CPQL ÷ CY` cross-check.
- Cite the band/row used for every tier and label.
- One **primary** constraint; secondary only after upstream clears.
- No single upstream metric (CPL/CTR/frequency/opt-in) convicts an account (G-6).
- No generic advice — levers only from the troubleshooting SOP or stated client context.

## Related docs

- [Client KPI Judgment Standard](client-kpi-judgment-standard.md) — bands, override rules, schema
- [Client Performance Diagnostic Rulebook](client-performance-diagnostic-rulebook.md) — windows and account states
- [Constraint Troubleshooting SOP](../client-fulfillment/client-success/constraint-troubleshooting-sop.md) — fixes/levers

## Open questions

- [ ] Confirm with founder that the worked-example thresholds match the approved §11.2 numbers.
