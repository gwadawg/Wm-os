# Lead Media Buyer PJ Comp — Implementation Plan

> **For agentic workers:** Execute task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Do not invent new pay numbers — follow the locked spec only.

**Goal:** Turn the approved comp design into a hire-ready PJ onboarding pack (payment agreement, SOW, level checklist, commission appendix, EOM sheet) plus OS index links so founder can fill name/start date, run accountant review, and send for signature.

**Architecture:** Spec remains owner-only source of truth. Hire-facing docs are plain-language Markdown under `docs/operations/people/` (confidentiality: owner-only until shared). No code, no payroll automation in Phase 1 — Sheet + invoice on the 9th.

**Tech Stack:** Markdown in Wm-os; optional Google Sheet / CSV for EOM (founder-owned). Brazilian PJ legal wording deferred to accountant/lawyer (thin wrapper only in our docs).

**Spec:** [docs/superpowers/specs/2026-09-15-lead-media-buyer-pj-comp-design.md](../specs/2026-09-15-lead-media-buyer-pj-comp-design.md)

**Repo:** Wm-os only.

```bash
cd "/Users/gwadawg/Desktop/Repos/Wm-os"
```

---

## File map

| File | Responsibility |
|------|----------------|
| `docs/superpowers/specs/2026-09-15-lead-media-buyer-pj-comp-design.md` | Locked design (already committed) |
| `docs/plans/2026-09-15-lead-media-buyer-pj-comp-design.md` | Pointer or mirror next to Christian/Laura comp plans for discoverability |
| `docs/operations/people/lead-mb-pj-payment-agreement.md` | Hire-facing payment + expectations agreement |
| `docs/operations/people/lead-mb-pj-sow.md` | Role / SOW attachment (L1–L4 accountabilities) |
| `docs/operations/people/lead-mb-pj-level-checklist.md` | Skills checklist; initial on each unlock |
| `docs/operations/people/lead-mb-pj-commission-appendix.md` | CPQL hit rules, eligibility, EOM steps |
| `docs/operations/people/lead-mb-pj-eom-sheet-template.md` | Column defs + worked example for EOM |
| `docs/operations/hiring/README.md` | Link pack from hiring hub |
| `docs/operations/people/README.md` | Link pack from people hub |

**Do not modify:** Christian Phase 1 rates in `docs/plans/2026-07-15-christian-media-buyer-comp-design.md`.

---

### Task 1: Discoverability — mirror/pointer beside other comp plans

**Files:**
- Create: `docs/plans/2026-09-15-lead-media-buyer-pj-comp-design.md`
- Modify: spec frontmatter `status: draft` → keep draft until agreement pack ships, or set `active` only after founder signs hire (prefer leave **draft** until pack complete)

- [ ] **Step 1: Add pointer file in `docs/plans/`**

Create a short file that states this is the canonical pointer to the superpowers spec (avoid duplicating the full policy):

```markdown
---
title: Lead Media Buyer PJ Comp Design (pointer)
domain: operations
subdomain: people
owner: founder
status: draft
confidentiality: owner-only
last_updated: 2026-09-15
canonical: docs/superpowers/specs/2026-09-15-lead-media-buyer-pj-comp-design.md
related_docs:
  - docs/plans/2026-07-15-christian-media-buyer-comp-design.md
---

# Lead Media Buyer PJ Comp Design

Canonical design:

[docs/superpowers/specs/2026-09-15-lead-media-buyer-pj-comp-design.md](../superpowers/specs/2026-09-15-lead-media-buyer-pj-comp-design.md)

Hire-facing pack (after Task 2–5):

- Payment agreement, SOW, level checklist, commission appendix, EOM template under `docs/operations/people/lead-mb-pj-*`
```

- [ ] **Step 2: Commit**

```bash
git add docs/plans/2026-09-15-lead-media-buyer-pj-comp-design.md
git commit -m "$(cat <<'EOF'
Add pointer for Lead MB PJ comp next to other people plans.

EOF
)"
```

---

### Task 2: Payment & expectations agreement (hire-facing)

**Files:**
- Create: `docs/operations/people/lead-mb-pj-payment-agreement.md`

- [ ] **Step 1: Draft agreement from locked decisions**

Must include, in plain language (placeholders `{{HIRE_NAME}}`, `{{START_DATE}}`, `{{PJ_TAX_ID}}`):

1. Parties / PJ status (not CLT; invoices in BRL)
2. Month 1: flat R$4,000; no commissions
3. Month 2+: base by level (table 4/5/6/7)
4. Commissions only at L2+; R$100 × CPQL hits; scorecard ≥ B gate
5. Payday: **9th** of each month for **prior** month
6. Level unlocks = founder checklist; new base starts next full pay month
7. 30 days’ notice for structure changes; quarterly review
8. Shadow EOM before first live commission month
9. Signature blocks (founder + contractor)

Use Waiz Business OS frontmatter: `status: draft`, `confidentiality: owner-only`, `owner: founder`, link `related_docs` to the spec.

- [ ] **Step 2: Self-check against spec**

Verify no numbers disagree with the spec (especially: no commission at L1; CPQL not CPL; no mentoring-Christian gate; no book bonus).

- [ ] **Step 3: Commit**

```bash
git add docs/operations/people/lead-mb-pj-payment-agreement.md
git commit -m "$(cat <<'EOF'
Draft Lead MB PJ payment and expectations agreement.

EOF
)"
```

---

### Task 3: SOW / role attachment

**Files:**
- Create: `docs/operations/people/lead-mb-pj-sow.md`

- [ ] **Step 1: Write SOW**

Sections:

- Mission (Lead MB; senior buying seat; progressive creative)
- Core accountabilities (all levels)
- Creative progression L1→L4 (match ladder gates)
- Month 1 ramp expectations
- Tools / OS pointers (Daily OS, scorecard, media-buying SOPs, CPQL standards)
- Explicit out: mentoring Christian not required for levels

- [ ] **Step 2: Commit**

```bash
git add docs/operations/people/lead-mb-pj-sow.md
git commit -m "$(cat <<'EOF'
Draft Lead MB PJ statement of work.

EOF
)"
```

---

### Task 4: Level unlock checklist

**Files:**
- Create: `docs/operations/people/lead-mb-pj-level-checklist.md`

- [ ] **Step 1: One checklist per level**

| Level | Base | Checkbox items (exact from spec) |
|-------|------|----------------------------------|
| L2 | R$5,000 | Manage all accounts; onboard a client; basic funnel; headlines; KPI client reviews |
| L3 | R$6,000 | Clear analysis + scripts/concepts written for production |
| L4 | R$7,000 | Produce and edit ads end-to-end |

Each level block: date, evidence notes, founder initials, contractor initials, effective pay month.

- [ ] **Step 2: Commit**

```bash
git add docs/operations/people/lead-mb-pj-level-checklist.md
git commit -m "$(cat <<'EOF'
Add Lead MB PJ level unlock checklist.

EOF
)"
```

---

### Task 5: Commission appendix + EOM sheet template

**Files:**
- Create: `docs/operations/people/lead-mb-pj-commission-appendix.md`
- Create: `docs/operations/people/lead-mb-pj-eom-sheet-template.md`

- [ ] **Step 1: Commission appendix**

Copy rules from spec into hire-facing language:

- Eligibility (L2+, live month, scorecard ≥ B)
- CPQL formula + 10% grace ON
- Written target ownership
- Eligible account floors: US$1,000 spend + ≥10 qualified leads
- R$100 × hits; no book bonus
- Go-live: L2 + targets + shadow EOM
- Payday 9th

- [ ] **Step 2: EOM sheet template**

Document columns:

`account | geo class | target CPQL | spend | qual leads | actual CPQL | eligible | hit | notes`

Plus:

- Worked example (e.g. 3 accounts, 2 hits → R$200)
- Scorecard gate line
- Total = base + commissions
- Approval line (founder) before invoice

- [ ] **Step 3: Commit**

```bash
git add docs/operations/people/lead-mb-pj-commission-appendix.md \
  docs/operations/people/lead-mb-pj-eom-sheet-template.md
git commit -m "$(cat <<'EOF'
Add Lead MB PJ commission appendix and EOM sheet template.

EOF
)"
```

---

### Task 6: Hub links

**Files:**
- Modify: `docs/operations/hiring/README.md`
- Modify: `docs/operations/people/README.md`

- [ ] **Step 1: Add “Lead MB PJ pack” bullets** linking agreement, SOW, checklist, commission, EOM, and the design spec
- [ ] **Step 2: Commit**

```bash
git add docs/operations/hiring/README.md docs/operations/people/README.md
git commit -m "$(cat <<'EOF'
Link Lead MB PJ comp pack from hiring and people hubs.

EOF
)"
```

---

### Task 7: Founder handoff (human; agent prepares checklist only)

**Files:**
- Modify: spec “Open before first live commission month” checkboxes as items clear
- Optional: export agreement to PDF/DOCX via docx skill **only if founder asks**

- [ ] **Step 1: Create a short handoff block** at bottom of payment agreement:

```markdown
## Founder fill-in before send
- [ ] Hire legal name
- [ ] PJ / CNPJ or CPF billing details
- [ ] Start date (Month 1 calendar)
- [ ] Accountant/lawyer review of PJ wrapper
- [ ] Initial account assignment list
```

- [ ] **Step 2: Mark spec status** — after pack is complete and founder OK to use: set spec `status: active` (or keep draft until countersigned — founder chooses)
- [ ] **Step 3: Final commit** if status/frontmatter updated

---

## Done when

- [ ] All five hire-facing docs exist and match the locked spec numbers
- [ ] Hubs link the pack
- [ ] Pointer exists under `docs/plans/`
- [ ] Founder can fill placeholders → accountant pass → send for signature
- [ ] No changes to Christian’s Phase 1 plan

## Out of scope (do not do in this plan)

- Building payroll/commission software in Mr. Waiz
- Changing fulfillment CPQL dollar bands
- Mentoring-Christian requirements
- USD conversion guarantees in the contract
