---
title: RM Archetypes Canonical
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-09-18
review_cycle: monthly
artifact_type: reference
canonical_for: rm-persona-archetype-bridge
note: >-
  Active audience model for RM creative. 3 personas × 3 archetypes. Family/heirs
  = trigger content, not an archetype. Veteran deprecated. Archive of old model:
  reverse-mortgage-dna/drafts/rm-archetypes-pre-2026-09-cleanup.md
---

# RM Archetypes Canonical

**Single bridge for personas + archetypes.** Load this (plus ICP + doctrine)
when scripting. Campaign structure lives in
[rm-creative-taxonomy.md](../../reverse-mortgage-dna/rm-creative-taxonomy.md) —
do not invent ad sets from this file.

| List | Job | Active set |
|------|-----|------------|
| **Persona** | Who they look like — casting, VOC | **3:** Widowed · Married Couple · Pre-Retiree |
| **Archetype** | Why they buy — tone, language bans | **3:** Security-Seeker · Financially Squeezed · Strategic Retiree |
| **Family / heirs** | Gate + hook — not a fourth buyer type | Triggers: `burden` · `heirs` · `living-legacy` |

> **Sources:** [intelligence-icp-rm.md](../../reverse-mortgage-dna/intelligence-icp-rm.md)
> · [doctrine-rm-marketing.md](../../reverse-mortgage-dna/doctrine-rm-marketing.md)
> · **Archive (old 4–6 archetype model):**
> [rm-archetypes-pre-2026-09-cleanup.md](../../reverse-mortgage-dna/drafts/rm-archetypes-pre-2026-09-cleanup.md)

---

## Purchase psychology (why only three archetypes)

```text
JOB A — RELIEVE PRESENT PRESSURE   → cash-out / payment-gone
        Security-Seeker     (fear → safety; shame-sensitive)
        Financially Squeezed (fairness → earned access; pride-sensitive)

JOB B — PROTECT THE FUTURE         → standby-line / planning
        Strategic Retiree   (competence → optimization)

FAMILY / HEIRS                     → not a job — a gate on both paths
```

Same pressure job, two dignity registers — wrong tone kills the ad. Planner
job is a different purchase (often no present need). Legacy-as-archetype
over-counted a universal objection as a segment.

---

## Active personas (who)

Full VOC → [intelligence-icp-rm.md](../../reverse-mortgage-dna/intelligence-icp-rm.md) §6.

| Persona | Snapshot | Core fear | Core desire |
|---------|----------|-----------|-------------|
| **Widowed Homeowner** | Alone, income halved | Losing home / becoming a burden | Security, independence |
| **Married Couple** | Both retired, inflation | Worked hard, still stressed | Enjoy retirement · protect heirs |
| **Pre-Retiree** | Early retired / long runway | Money won't last 20–30 years | A plan that holds |

| Deprecated | Rule |
|------------|------|
| **Veteran** | Do not brief, tag, or open Scale ladder cells. Archive text remains in ICP. |

---

## Active archetypes (why / tone)

Full language banks → [doctrine-rm-marketing.md](../../reverse-mortgage-dna/doctrine-rm-marketing.md) §4.

| Archetype | Driver | Fear | Conversion language | Never |
|-----------|--------|------|---------------------|-------|
| **Security-Seeker** | Fear / survival | Running out of options | Peace of mind · safety net · breathe again | Pity, “last resort,” urgency, complex jargon |
| **Financially Squeezed** | Frustration / fairness | Retirement that never arrives | Unlock equity · you earned this · already yours | Help/charity framing, desperation, victim tone |
| **Strategic Retiree** | Optimization / control | Suboptimal decision | Portfolio buffer · standby credit · sequence-of-returns | Emotional relief as lead, “get cash now,” oversimplification |

| Demoted / removed | Use instead |
|-------------------|-------------|
| **Legacy Planner** | Trigger `heirs` / `burden` / `living-legacy` + heir myth content. Archive: [drafts](../../reverse-mortgage-dna/drafts/rm-archetypes-pre-2026-09-cleanup.md) |
| **Pre-Retiree** (as archetype) | Persona Pre-Retiree + Strategic Retiree or Squeezed / Security-Seeker |
| **Veteran** | Deprecated |

---

## Bridge (who × why)

One ad = **one archetype** (sharp TOF). Kitchen-sink MOF may touch more than
one callout — still pick a primary persona for casting.

| Persona ↓ · Archetype → | Security-Seeker | Financially Squeezed | Strategic Retiree |
|-------------------------|-----------------|----------------------|-------------------|
| **Widowed** | **Primary** | Common | Rare |
| **Married Couple** | Common | **Primary** | Common (quality) |
| **Pre-Retiree** | If crisis | If payment / cash stress | **Primary** |

### Family triggers (any persona × any archetype)

| Trigger | When to lead with it | Typical stage |
|---------|----------------------|---------------|
| `burden` | Fear of asking kids for help | TOF / MOF |
| `heirs` | Inheritance myth / remaining equity | MOF (myth-led or education) |
| `living-legacy` | Help family *now* while alive | TOF/MOF · still one outcome (usually cash-out) |

Heir / non-recourse proof belongs on **every** quality path — not only a
“Legacy” brief.

### Hook direction (compliance-screened)

| Pair | Stage | Hook direction |
|------|-------|----------------|
| Widowed × Security-Seeker | TOF | Alone, savings shrinking · stay in the home |
| Widowed × burden trigger | TOF/MOF | Kids shouldn't have to worry · independence |
| Couple × Financially Squeezed | TOF | House worth more · money tighter |
| Couple × Strategic Retiree | MOF | Smarter cash-flow tool · not a last resort |
| Couple × heirs trigger | MOF | Heirs get remaining equity · non-recourse |
| Pre-Retiree × Strategic Retiree | TOF/MOF | Early retirement · foundation · growing line |
| Pre-Retiree × Financially Squeezed | TOF | Still making a payment · free up cash flow |

---

## Quality dial (creative mix)

From [rm-high-quality-lead-acquisition.md](../../client-marketing/rm-high-quality-lead-acquisition.md):

| Goal | Weight |
|------|--------|
| Volume | Security-Seeker + Financially Squeezed |
| Qualified / closable | **Strategic Retiree** + equity callouts + heir proof on the path |

---

## Fit to creative taxonomy

| Taxonomy layer | Persona / archetype role |
|----------------|--------------------------|
| Product · strategy · outcome · stage | Structure / learning |
| Persona + archetype | Scripting only |
| Trigger (incl. family) | Hook on the ad |

Do not create ad sets named after archetypes. Persona in Scale names
(`scale_widowed`, `scale_married`, `scale_pre-retiree`) only when funded —
never `scale_veteran`.

---

## Compliance

- No age in copy · no product name opening TOF (outcome-led) · no guarantees
- Full gate: [rm-compliance-guardrails.md](../../reverse-mortgage-dna/rm-compliance-guardrails.md)

## Related

- [RM Creative Taxonomy](../../reverse-mortgage-dna/rm-creative-taxonomy.md)
- [Intelligence ICP RM](../../reverse-mortgage-dna/intelligence-icp-rm.md)
- [Doctrine RM Marketing](../../reverse-mortgage-dna/doctrine-rm-marketing.md)
- [RM High-Quality Lead Acquisition](../../client-marketing/rm-high-quality-lead-acquisition.md)
- [Creative Awareness Ladder](../creative-awareness-ladder.md)
- [Archive](../../reverse-mortgage-dna/drafts/rm-archetypes-pre-2026-09-cleanup.md)
