---
title: RM Ad Ideation Matrix
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-23
review_cycle: monthly
artifact_type: playbook
---

# RM Ad Ideation Matrix

The brainstorm engine. Turns a blank page into a structured combination space so new ad
ideas are systematic, distinct, and never random. Powers the `brainstorm` command of the
[rm-creative-studio skill](../../../../.claude/skills/rm-creative-studio/SKILL.md).

> Every concept this produces is tagged to its source frameworks (see
> [frameworks-reference.md](frameworks-reference.md)) and screened by the
> [compliance gate](compliance-gate-checklist.md) before it is shown.

## The five dimensions

A concept is one point in this space:

| Dimension | Options | Source |
|-----------|---------|--------|
| **Archetype** | Security-Seeker, Financially Squeezed, Strategic Retiree, Legacy Planner, Veteran, Pre-Retiree | [rm-archetypes-canonical.md](rm-archetypes-canonical.md) |
| **Angle** | Burden, Trapped Asset, Surviving vs Living, Breaking News / New Program, No Monthly Payment, Exclusive Access, Cash Out, State-Specific Bulletin, Regret / Social Proof, Heirs Get Equity, Inflation Hedge, Aging-in-Place | [rm-ad-playbook.md](../../client-marketing/rm-ad-playbook.md) + [ad-copy-angle-library-rm.md](../ad-copy-angle-library-rm.md) |
| **Awareness / Stage** | TOF (Unaware/Problem-aware), MOF (Solution/Product-aware), BOF (Most-aware) | frameworks-reference awareness bridge |
| **Hook type** | Rhetorical question, Confessional, Specific pain, Demonstration, Myth-bust, Authority, Curiosity gap, Social proof, Niche callout, Paradox | frameworks-reference hook taxonomy (F7) |
| **Format** | UGC video (Higgsfield, 18–32s), Spoken testimonial (Higgsfield, 25–40s), Silent text-overlay testimonial (Higgsfield b-roll, 45–60s), Educational explainer (Higgsfield + sourced b-roll, 30–60s), Long-form video script (45–90s, real talent), Static image, Carousel | [higgsfield-prompt-builder.md](higgsfield-prompt-builder.md) + [higgsfield-format-modules.md](higgsfield-format-modules.md) + playbook two-format system |

### Format ↔ stage fit (use when picking or recommending a format)

| Format | TOF | MOF | BOF | Natural hook pairings |
|--------|-----|-----|-----|------------------------|
| UGC video | Strong | Strong | OK | Confessional, Specific pain, Rhetorical question |
| Spoken testimonial | OK (product unnamed) | Strong | Strong | Confessional, Social proof, Paradox |
| Silent text-overlay testimonial | Strong | Strong | Weak | Specific pain, Paradox, Curiosity gap |
| Educational explainer | OK (myth-hook variant) | Strong | Strong | Myth-bust, Authority, Demonstration |
| Long-form script (real talent) | OK | Strong | Strong | Any (full education arc) |

Both testimonial formats are **composites (dramatizations)** and carry the disclosure rule —
see [higgsfield-format-modules.md](higgsfield-format-modules.md).

## Generation logic (how `brainstorm` works)

Input: an **archetype** (or "any"), a **stage**, a **count** N, and optionally a **format**
(or "any" — then recommend per the format ↔ stage fit table above).

1. **Anchor the emotion.** Pull the archetype's core fear + desire + best angles from
   [rm-archetypes-canonical.md](rm-archetypes-canonical.md), and the matching VOC phrases +
   pain->impact pairs from the [ICP doc](../../reverse-mortgage-dna/intelligence-icp-rm.md).
2. **Spread across the space.** Produce N concepts that vary on angle AND hook type — never
   N variations of the same idea. Aim for coverage: different angle for each, rotating hook types.
3. **Respect the stage rules.** TOF concepts never name the product and lead with the
   prospect's world; MOF can introduce the category in context + bust myths; BOF positions the LO.
4. **Tag + screen.** Each concept is tagged with its frameworks and run through the
   [compliance gate](compliance-gate-checklist.md). Anything that fails is fixed or dropped, not shown.

## Winner-informed ideation (Step 0)

When the user says "new ad" without naming a winner, **do not start blank-page**. Run Step 0 from
[ad-development-workflow.md](../ad-development-workflow.md) first:

1. Scan [script-archetypes-catalog.md](../creative-research/script-archetypes-catalog.md),
   [editing-styles-catalog.md](../creative-research/editing-styles-catalog.md), and recent
   [swipes/](../creative-research/swipes/).
2. Build a coverage map: which archetype × angle × format combos already have proven swipes.
3. **Ideation seed = the gap** — e.g. "Legacy Planner + UGC + comment-reply hook is unproven;
   Strategic Retiree + static + five-icon grid is covered."
4. Optionally pull Mr. Waiz `ad_library` via `supabase:ad:{uuid}` when user names a winner to `vary`.

Cite `winner_ref` or `supabase:ad:{uuid}` on every concept row when building from owned patterns.

## Output format (one concept = one row)

| Field | Example |
|-------|---------|
| ID | IDEA-001 |
| Archetype | Legacy Planner |
| Angle | Heirs Get the Equity |
| Stage | MOF |
| Hook type | Myth-bust |
| Format | Educational explainer (Higgsfield) |
| One-line premise | Dismantle the "my kids inherit the debt" fear by showing the non-recourse guarantee. |
| Lead hook (direction) | "Worried your kids will inherit a bill? Here's what actually happens." |
| VOC anchor | "I don't want to ask my kids for help." |
| winner_ref | `supabase:ad:{uuid}` or swipe id (when derived from owned winner) |
| Frameworks | F7 myth-bust hook; F2 Loss Aversion (reframed); F4 objection #2 |
| Compliance flag | OK (no guarantee, no age, real mechanism) |

## Anti-overlap rule

Two concepts are "too similar" if they share archetype + angle + hook type. The engine must
change at least one of those per concept. This is how a batch of 10 stays genuinely diverse
instead of 10 rewordings.

## Coverage presets (optional quick modes)

| Preset | What it generates |
|--------|-------------------|
| `cold-batch` | 6 TOF concepts, one per archetype, rotating hook types |
| `objection-batch` | One MOF myth-bust concept per top-5 objection (ICP §7) |
| `winner-expand` | Takes one proven angle and spreads it across 5 hook types (feeds the `vary` command) |
| `persona-deep` | 5 concepts all for one persona, across TOF->MOF->BOF |

## Worked mini-example (Security-Seeker, TOF, N=3)

1. **IDEA-A** — Angle: Burden | Hook: Confessional | "The last thing I want is for my kids to take care of me." (F7 confessional; F4 burden fear)
2. **IDEA-B** — Angle: Trapped Asset | Hook: Paradox | "House-rich, cash-poor — and it doesn't have to stay that way." (F7 paradox; F2 Contrast)
3. **IDEA-C** — Angle: No Monthly Payment | Hook: Rhetorical question | "What would retirement feel like with no mortgage payment?" (F7 rhetorical; F2 Hyperbolic discounting / present benefit)

All three: TOF, no product name, no age in copy, no guarantees -> pass gate.
