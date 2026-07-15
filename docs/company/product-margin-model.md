---
title: Product Margin Model — RM/DSCR DFY
domain: company
owner: founder
status: active
confidentiality: owner-only
last_updated: 2026-07-15
review_cycle: quarterly
sources:
  - Supabase WM Reporting (fszmndldcvrrmitfbwde)
  - docs/company/reflections/2026-q2-pass-1-financial-funnel-truth.md
  - docs/company/reflections/2026-q2-pass-2-margin-comp-economics.md
  - docs/company/reflections/2026-q3-pricing-retention-analysis.md
  - docs/acquisition/offer/pricing-architecture.md
---

# Product Margin Model — RM/DSCR DFY

**What this is:** source of truth for **reverse mortgage / DSCR Done-For-You and media
mid-tier** — what each product costs to deliver, what it sells for, and margin — including
how team pay flows into cost. Pricing and comp decisions for this business get made here.

**Separate business:** the standalone call-center (performance / appointment-setting) line
does **not** belong in this doc. Waiz does not run lead gen for that SKU; continuation is
uncertain. Margin truth for that line:
[Call Center Margin Model](call-center-margin-model.md).

**How to maintain:** refresh cost pools each quarterly reflection. Do not fork — pricing
changes edit this file (or the CC margin file for that line).

**Current state: active** — Q2 2026 cost basis; Q3 2026 DFY pricing locks (2026-07-14).

---

## 1. Products and pricing (RM/DSCR — Q3 locks)


| Product                         | Price                                                   | Client also pays                                     | Q3 locks                                                |
| ------------------------------- | ------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------- |
| RM/DSCR full service (Solo DFY) | $2,500–3,000 first month → **$1,800–2,000/mo** retainer | **Min $2,000/mo** ad spend; kicker on spend over $4k | Min spend + 10% kicker + optional performance fee — §1a |
| Media buying mid-tier           | $1,800 first month → $1,100/mo                          | Own ad spend; **client owns follow-up/close**        | Escape hatch only — §1b                                 |


**Client ROI rule of thumb:**

```text
Client success KPI = their paid media ÷ funded/closed deals
Rule of thumb     ≈ $1,500–$1,900 ad spend per funded loan
LO economics      ≈ $7k–$25k revenue per funded loan
```

### 1a. Solo DFY / RM-DSCR full service — Q3 commercial locks

Canonical sales detail: [Pricing Architecture](../acquisition/offer/pricing-architecture.md).


| Lever                                   | Lock                                                          | Notes                                                                                                                       |
| --------------------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Monthly retainer floor                  | **$1,800–$2,000**                                             | Hold band; do **not** cut for broke prospects. Aggressive raise deferred until ≥5 non-CFNB clients report spend÷funded (G3) |
| Contractual min ad spend                | **$2,000/mo**                                                 | Two consecutive months below → renegotiate tier or exit                                                                     |
| Discovery cash gate                     | Retainer + min spend ≈ **≥$3,800/mo** client cash for 90 days | Sales math wall — Q3 analysis §5                                                                                            |
| Ad spend kicker                         | **10% of Meta (paid) spend over $4,000/mo**                   | Standard on **new** DFY contracts; grandfather existing only with founder approval                                          |
| Performance fee (optional, well-funded) | **$500 per funded loan after 2+ fundeds in a calendar month** | Risk-removal close; requires funded tracking (G3). Not rev-share.                                                           |
| Qualification fail                      | Route Boot Camp or **mid-tier** — never discounted DFY        | Money model routing                                                                                                         |


### 1b. Media mid-tier — positioning lock


| Rule          | Lock                                                                                      |
| ------------- | ----------------------------------------------------------------------------------------- |
| What they buy | Campaigns + leads; **not** setter fleet / AI booking ops / show SLAs                      |
| Success KPI   | CPL / lead quality — **not** show rate or funded loans                                    |
| Guarantees    | None on appointments, shows, or fundeds                                                   |
| Price         | $1,800 → $1,100/mo — must stay **below** DFY so it is not a guilt discount dressed as DFY |
| Upgrade       | When client can clear DFY cash gate + wants dial/booking ops → Solo DFY                   |


Full narrative: [Pricing Architecture — Mid-tier](../acquisition/offer/pricing-architecture.md#media-buying-mid-tier-leads-only).

---

## 2. Delivery cost pools (Q2 2026 actuals, quarterly)

Company-wide fulfillment COGS (includes capacity also used by the call-center line when
active — do not assume 100% of this pool is DFY-only):


| Pool                                                                                 | Q2 $        | Monthly    | What it is                                                 |
| ------------------------------------------------------------------------------------ | ----------- | ---------- | ---------------------------------------------------------- |
| Dial team labor (Bernardo, Luka)                                                     | $4,247      | $1,416     | Salaries + commissions — shared with CC line when both run |
| Fulfillment management/CS labor (Christian, Laura, Gabriela)                         | $8,305      | $2,768     | Manager + client success + support                         |
| Fulfillment software (GHL, Twilio, HotProspector, Closebot, Perspective, Make, etc.) | $7,842      | $2,614     | Platform stack                                             |
| Consulting + AI (CallCenterMastery, Anthropic)                                       | $2,439      | $813       | Review whether recurring                                   |
| **Total delivery (COGS)**                                                            | **$23,226** | **$7,742** | = `business_expenses` fulfillment bucket                   |


Company overhead (non-delivery): ~$458/mo. Own-acquisition costs (Meta, Pedro,
creative) are CAC, not COGS — see Pass 1 reflection.

**Allocation note:** when the call-center line consumes a large dial share (June: CC +
$0-Meta ≈ 48% of dials), DFY “feels” capacity-starved even if DFY cash margins are high.
See [Call Center Margin Model](call-center-margin-model.md).

---

## 3. Unit costs relevant to DFY dial delivery

DFY includes reverse sales assistant + AI booking. Unit dial economics:


| Unit              | Marginal cost          | Fully loaded* | Notes                                  |
| ----------------- | ---------------------- | ------------- | -------------------------------------- |
| Human-booked show | ~$9                    | ~$34          | 66% show rate on commissioned calendar |
| AI-booked show    | ~$6                    | ~$20          | 52.5% show; no setter commission       |
| Live transfer     | ~$8                    | ~$34          | Human-only premium unit                |
| Outbound dial     | **~$0.22** (June 2026) | —             | Setter payroll + Twilio/HP ÷ dials     |


 Company-wide fully loaded ÷ ~680 Q2 shows+transfers. Detail and CC-only contribution:
[Call Center Margin Model](call-center-margin-model.md).

**Structural fact:** AI produced 1.8× human shows in Q2 at ~1/6 marginal cost. Humans own
show-rate quality and 100% of live transfers. DFY retainer funds fixed pools; per-client
ad spend funds lead volume into the dial book.

---

## 3b. Fulfillment cost layers (DFY pricing)


| Layer                          | How it scales                   | Measured?                       | Pricing use                                   |
| ------------------------------ | ------------------------------- | ------------------------------- | --------------------------------------------- |
| **A. Dial variable**           | With dials / leads / pickup     | Yes — ~$0.22/dial + commissions | Watch dial intensity vs client spend (Pass 2) |
| **B. Outcome commissions**     | Bookings, shows, transfers      | Yes — $1 / $4 / $5 today        | Marginal delivery cost                        |
| **C. Client Success capacity** | With **# of clients**           | Modeled below                   | Floor under retainer                          |
| **D. Dial leadership (CCM)**   | Mostly fixed / spans dial books | Payroll known                   | Shared; reclaim capacity if CC winds down     |
| **E. Delivery software**       | Mostly fixed; some Twilio       | Pool $ known                    | Retainer recovers stack                       |


### C — Client Success (Laura) — capacity model (Q3 planning lock)

**Role:** Owns OB/launch and monthly check-ins; oversees dial delivery leadership so DFY
ops run.


| Touch                         | Duration (locked est.)       | When                        |
| ----------------------------- | ---------------------------- | --------------------------- |
| Onboarding + launch call      | 2.0 hours first-month set    | Once per new client         |
| Monthly check-in              | 0.67 hours (40 min midpoint) | Every active client / month |
| CCM oversight + coordination  | **8 hours / month** fixed    | Recurring                   |
| Slack / fire drills / rollout | **6 hours / month** buffer   | Recurring                   |


```text
Laura available for client touches ≈ 160 − 14 = 146 hrs / mo
hrs / client / mo ≈ 0.67 + (14 / N)
Planning max N ≈ 35–40 active CS logos before hire / quality wall
```

With Laura ≈ **$1,604/mo** Q2 run-rate, CS $/client is small vs $1,800+ retainer — the
constraint is **logo quality and count**, not CS dollars. Prefer fewer Underfunded logos.

**First-month additive:** ~2.0 hrs OB+launch (planning floor only).

### Dial intensity on DFY accounts (from Pass 2)

Spend ↑ raises dials mainly via leads. Margin killers: high dials/lead, low pickup, or
**cash = $0 while dialing**. Apply the same band language as ops:


| Band           | Rule                                            | Action                                        |
| -------------- | ----------------------------------------------- | --------------------------------------------- |
| Efficient      | Dials/lead ≤ 2 and dial $ ≤ 10% of cash         | Protect                                       |
| Healthy volume | High dials, dial $ ≤ 10% cash                   | Protect (e.g. CFNB)                           |
| Watch          | Dials/lead 3–5 or dial $ 10–25% cash            | Tighten list / cadence                        |
| Strain         | Dials/lead ≥ 5.5 or pickup ≤ 3% or dial $ ≥ 25% | Fix or pause — do not “save” with discounting |
| Invisible      | Dials > 0, cash = $0                            | Collect or stop                               |


### Still skip for pricing (low ROI)

- Minute-level Twilio export unless usage-billing
- Gabriela allocation until material
- Media-buyer hours on mid-tier until that product margin compresses

---

## 4. Margin by product (Q2 2026 basis — DFY lanes)


| Product               | Revenue shape                               | Est. delivery cost   | Margin                      | Confidence  |
| --------------------- | ------------------------------------------- | -------------------- | --------------------------- | ----------- |
| RM/DSCR full service  | $1,689–2,000/mo (+ kicker when spend > $4k) | ~$300–500/account/mo | **~75%+**                   | Medium-High |
| Media buying mid-tier | $1,100/mo                                   | Low marginal labor   | High, still weakly measured | Low         |


**GM floor after Q3 pay bumps (DFY book):** blended delivery gross margin on this business
**≥ 60%**. Fund raises from spend kickers + better qualification — not from signing
underfunded logos.

Call-center performance SKU margins: [Call Center Margin Model](call-center-margin-model.md).

---

## 5. Team pay structure (shared dial team — DFY view)

**Current setter comp:** $400/mo + $1/booking + $4/show + $5/live transfer.


| Person          | Role               | Q2 pay    | Notes                                        |
| --------------- | ------------------ | --------- | -------------------------------------------- |
| Bernardo Fabris | Setter             | $2,309    | Capacity shared with CC line                 |
| Luka Faccini    | Setter             | $1,938    | Same                                         |
| Laura Moço      | Client Success     | $4,811 Q2 | Phase 1 plan: [CS Comp — Laura](../plans/2026-07-14-laura-cs-comp-design.md) |
| Christian       | Media Buyer        | $2,762 Q2 | Phase 1 plan: [MB Comp — Christian](../plans/2026-07-15-christian-media-buyer-comp-design.md) |
| Pedro Rio       | Acquisition setter | $2,161    | CAC, not DFY COGS                            |


**Alignment issues:** booking-weighted pay; transfers underpriced vs value; attribution
leaks (G1/G2). Detail and performance-line impact:
[Call Center Margin Model §8](call-center-margin-model.md).

### 5b. Q3 target comp (foreshadow — gated)

**Gate (setters):** G1 + G2 green one full month
([Q3 analysis §7](reflections/2026-q3-pricing-retention-analysis.md)).


| Unit          | Current | Target          | Why                                      |
| ------------- | ------- | --------------- | ---------------------------------------- |
| Base salary   | $400/mo | **$500–600/mo** | Stability                                |
| Booking       | $1      | **$0**          | No pay for bookings — AI-commoditized    |
| Show          | $4      | **$6**          | Align to client value                    |
| Live transfer | $5      | **$10**         | Human-only premium                       |


**CS / Media Buyer (structure finalized Phase 1 — cash after shadow EOM):**

| Seat | Base | Variable |
|---|---:|---|
| Laura (CS) | **$1,530** | Stickiness milestones/trailers (M3/M6 full-freight); uncapped — [plan](../plans/2026-07-14-laura-cs-comp-design.md) |
| Christian (MB) | **$1,000** | $15/account at CPL KPI + $100 if ≥80% hit-rate — [plan](../plans/2026-07-15-christian-media-buyer-comp-design.md) |

**Funding stack (DFY):**

1. Ad-spend kickers on Healthy DFY accounts
2. Fewer Underfunded / Invisible dial subsidies on the DFY book
3. Reclaimed dial capacity if CC line freezes or winds down
4. Then float bases / go-live variable after shadow month

People ops: [Q3 Comp Foreshadow](../operations/people/q3-comp-foreshadow.md).

---

## 6. Pricing / comp decisions (DFY) — Q3 LOCKED


| #   | Decision                    | Lock                                                                                            | Status                                  |
| --- | --------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------- |
| 1   | Raise retainer toward value | Hold $1,800–2,000; grow ARPA via **min spend + 10% kicker**; no across-the-board spike until G3 | **LOCKED**                              |
| 2   | Show/transfer-only setter   | Target $0 booking / $6 show / $10 transfer after G1–G2 — §5b                                    | **LOCKED (structure)** — pay live gated |
| 3   | CS capacity floor           | Max ~35–40 logos on Laura — §3b                                                                 | **LOCKED (planning)**                   |
| 4   | Mid-tier escape hatch       | Leads-only; never “cheap DFY” — §1b                                                             | **LOCKED**                              |
| 5   | Laura CS Phase 1 pay        | $1,530 base + stickiness M3/M6 milestones/trailers — [plan](../plans/2026-07-14-laura-cs-comp-design.md) | **LOCKED / active** — cash after shadow EOM |
| 6   | Christian MB Phase 1 pay    | $1,000 base + $15 CPL hit + $100 @ 80% — [plan](../plans/2026-07-15-christian-media-buyer-comp-design.md) | **LOCKED / active** — cash after shadow EOM |


Call-center keep/kill and performance fee terms: open on
[Call Center Margin Model §10](call-center-margin-model.md) — **not** decided here.

---

## Related docs

- [Call Center Margin Model](call-center-margin-model.md) — separate performance business
- [2026-Q2 Pass 1 — Financial + Funnel Truth](reflections/2026-q2-pass-1-financial-funnel-truth.md)
- [2026-Q2 Pass 2 — Margin + Comp Economics](reflections/2026-q2-pass-2-margin-comp-economics.md)
- [2026-Q3 Pricing + Retention Analysis](reflections/2026-q3-pricing-retention-analysis.md)
- [Pricing Architecture (RM/DSCR)](../acquisition/offer/pricing-architecture.md)
- [Money Model And Offer Architecture](overview-money-model-april-26.md)
- [Q3 Comp Foreshadow](../operations/people/q3-comp-foreshadow.md)

