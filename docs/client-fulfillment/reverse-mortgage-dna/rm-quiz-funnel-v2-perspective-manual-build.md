---
title: RM Quiz Funnel V2 — Perspective Manual Build
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-24
review_cycle: monthly
artifact_type: sop
companion: rm-quiz-funnel-v2-blueprint.md
---

# RM Quiz Funnel V2 — Perspective Manual Build

> **Use this SOP instead of Perspective AI funnel generation** for the V2 quiz architecture.
> AI-generated funnels (`create_funnel` / `update_funnel` MCP) bundle all steps into one HTML
> document with custom JavaScript routing. That pattern breaks editor preview (ThankYou → Q6_State
> redirect loop) and is unreliable for conditional quiz logic. **Native Perspective pages + branching**
> (Reverse Template pattern) is the supported build path.

## Source funnel

| Field | Value |
|-------|-------|
| Workspace | Reverse Mortgage |
| Duplicate from | **Reverse Template** (`69757cd00857d77751570047`) |
| New funnel name | `RM Quiz V2 Template` (or `{client_slug}-quiz-v2` per client) |
| Copy reference | [rm-quiz-funnel-v2-blueprint.md](rm-quiz-funnel-v2-blueprint.md) |
| Visual reference | [prototypes/rm-quiz-funnel-v2-prototype.html](prototypes/rm-quiz-funnel-v2-prototype.html) |
| V1 field mapping | [rm-funnel-form-spec.md](rm-funnel-form-spec.md) |

**Retire or ignore:** AI funnel `6a3c1ee3b4d5763f2121a4fc` — do not publish.

---

## V1 → V2 structural changes

| V1 (Reverse Template) | V2 change |
|-----------------------|-----------|
| Landing = hero + Q1 intent on same page | **Split:** hook-only landing → CTA starts quiz |
| Free numeric balance / value / age | **Range chips** (button select) |
| No progress bar | **Question X of 10** + thin progress bar every quiz step |
| No category labels | **3 categories:** Your Goal · Your Home · You & Eligibility |
| No primary residence question | **Add Q2** primary residence (No → soft exit) |
| Thank-you repeat valuation CTAs | **Remove** — Save Our Number + FAQ only |
| ~60 second subhead | **~3 minutes · 10 questions** |

---

## Page map (native Perspective pages)

Build **one Perspective page per row**. Use Perspective **Logic / Branching** (not custom JS).

| # | Page name | Type | Notes |
|---|-----------|------|-------|
| 1 | Landing | Content + CTA | No form fields |
| 2 | Q1_Goal | Question (single select) | 4 intent options |
| 3 | Loading | Content | Auto-advance 1s → Q2 |
| 4 | Q2_Primary | Question (Yes/No) | No → SoftExit |
| 5 | Q3_Mortgage | Question (Yes/No) | No → skip Q4 |
| 6 | Q4_Balance | Question (single select) | 5 range chips; only if mortgage Yes |
| 7 | Q5_Value | Question (single select) | 5 range chips |
| 8 | Q5_Insight | Content | 1 line micro-insight; auto-advance 1s |
| 9 | Q6_State | Question (dropdown) | `{licensed_states}` + Other |
| 10 | Q7_Age | Question (single select) | 5 age ranges |
| 11 | Q8_Married | Question (Yes/No) | No → skip Q9 |
| 12 | Q9_SpouseAge | Question (single select) | 2 options; only if married Yes |
| 13 | Q10_Timeline | Question (single select) | 3 options → OptIn |
| 14 | OptIn | Form | Post-quiz contact + SMS consent |
| — | SoftExit | **Result** page A | Non-primary residence |
| — | ThankYou | **Result** page B | Default success path |

**Result pages:** In Perspective, set **ThankYou** as the default result after OptIn submit. Set **SoftExit** as branch result from Q2 No. Result pages are independently editable in the sidebar (no JS conflict).

---

## Branching logic

```
Landing ──CTA──→ Q1 → Loading → Q2
Q2 No  ──────────────→ SoftExit (END)
Q2 Yes ──→ Q3
Q3 No  ──→ Q5 (skip Q4)
Q3 Yes ──→ Q4 → Q5 → Q5_Insight → Q6 → Q7 → Q8
Q8 No  ──→ Q10 (skip Q9)
Q8 Yes ──→ Q9 → Q10 → OptIn → ThankYou
```

Configure each branch in Perspective page settings → **Next page** / **Logic** panel.

---

## Copy blocks (placeholders)

### Landing

- **Eyebrow:** Retirement Equity Assessment
- **Headline:** Could Your Home Equity Help You Live More Comfortably in Retirement?
- **Body:** Many homeowners are sitting on significant equity — but aren't sure what options actually fit their situation. This short assessment helps you see where you stand — without a credit pull or obligation.
- **Offer:** Answer **10 quick questions** → get a personalized **Retirement Equity Assessment** and clear next steps.
- **CTA:** Check My Equity Options
- **Time:** Takes less than **3 minutes**

### Quiz questions

See [rm-quiz-funnel-v2-blueprint.md § Part 4](rm-quiz-funnel-v2-blueprint.md) question table.

**Q6 momentum** (text block above question): *Almost done — two more sections*

**Micro-insights:**

| After | Copy |
|-------|------|
| Q1 | Got it — we'll tailor your assessment around **[intent label]** |
| Q5 | Thanks — equity looks like a meaningful part of your picture. |

### Opt-in

- **Headline:** Where should we send your **personalized Retirement Equity Assessment**?
- **Subhead:** Enter your details to see your results and what happens next.
- **Fields:** First name · Last name · Phone · Email · SMS consent (required)
- **CTA:** See My Results
- **Consent:** I Consent to Receive SMS… from **{mlo_name}**. Reply STOP to unsubscribe.

### Thank-you (single template)

- **Greeting:** Thank you, `{first_name}`.
- **Insight:** Based on your answers — especially your goal to **[intent]** — you're in a **strong position to explore your options** with a licensed advisor.
- **Expectation:** Expect a call from `{company_name}` within **15 minutes**. Watch for a **`{area_code}`** number.
- **Timeline:** 3 steps (review → call → 15–20 min walkthrough)
- **Soft CTA:** Save Our Number → `{phone}`
- **FAQ:** Call length · No pressure · Nothing to prepare
- **Do not add:** Book now · Start valuation · Calendar embed

### Soft exit

- **Headline:** Thank you for your honesty.
- **Body:** This program is designed for **primary residences**. We won't add you to a sales call list.

### Footer (every page)

`{company_name}` · NMLS #{nmls}` · Equal Housing Lender · `{phone}` · `{address}` · Terms · Privacy · Not a commitment to lend…

---

## Design system (Perspective theme)

Apply in funnel **Design** / custom CSS:

| Token | Value |
|-------|-------|
| Canvas | `#FAF7F2` |
| Text | `#1B2A4A` |
| Muted | `#5C6478` |
| CTA | `#C4653A` |
| Category accent | `#2D6A6A` |
| Headlines | Fraunces |
| Body | DM Sans |
| Max width | ~480px |
| Option style | Large button cards, 16px radius, 2px terracotta border when selected |

Reference implementation: [prototypes/rm-quiz-funnel-v2-prototype.html](prototypes/rm-quiz-funnel-v2-prototype.html)

---

## Build checklist

1. [ ] Duplicate **Reverse Template** in Reverse Mortgage workspace
2. [ ] Rename funnel; delete unused A/B landers if present
3. [ ] Rebuild page order per table above (add Landing-only page; split intent from lander)
4. [ ] Convert balance / value / age to **button select** range options
5. [ ] Add Q2 primary residence + SoftExit result page
6. [ ] Wire all branches in Logic panel (no custom JS)
7. [ ] Add progress text + bar on each quiz page (Perspective progress element or text block)
8. [ ] Apply V2 copy + design tokens
9. [ ] Replace footer placeholders on **every** page including ThankYou and SoftExit
10. [ ] Remove hard valuation CTAs from thank-you
11. [ ] Map fields to GHL per [rm-funnel-form-spec.md](rm-funnel-form-spec.md)
12. [ ] Meta Pixel `lead` on OptIn submit click
13. [ ] Test: Q2 No → SoftExit · Q3 No skips Q4 · Q8 No skips Q9 · OptIn → ThankYou
14. [ ] **Editor test:** Click ThankYou in sidebar — must show thank-you content
15. [ ] Publish to `hecm.homequityhacks.com/{client_slug}`; update manifest

---

## Why AI funnel generation failed

| Issue | Cause |
|-------|-------|
| ThankYou opens Q6_State | Single-page JS funnel; `goToPage` + dropdown `change` on load hijacks editor |
| Dual sidebar highlight | Multiple sections active in one document |
| Fixes via `update_funnel` ineffective | Generator rewrites JS but cannot replicate native Perspective page isolation |

**Rule:** Use MCP `create_funnel` / `update_funnel` for simple lead-gen landers only. Use **manual duplicate + native pages** for qualify-first quiz funnels.

---

## Related docs

- [RM Quiz Funnel V2 Blueprint](rm-quiz-funnel-v2-blueprint.md)
- [RM Funnel Form Spec](rm-funnel-form-spec.md)
- [Perspective Funnel Setup SOP](../media-buying/perspective-funnel-setup-sop.md)
- [perspective-client-manifest.yaml](../media-buying/perspective-client-manifest.yaml)
