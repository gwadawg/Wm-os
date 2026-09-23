---
title: DSCR Video Script Playbook
domain: client-fulfillment
owner: media-buying-lead
status: active
last_updated: 2026-09-23
review_cycle: monthly
artifact_type: playbook
---

# DSCR Video Script Playbook

Thin path for **DSCR refinance** client UGC / talking-head scripts.  
**Not** reverse mortgage. Do **not** use `rm-creative-studio`, RM archetypes, or RM compliance.

**Skill entry:** [dscr-creative-studio](../../../.claude/skills/dscr-creative-studio/SKILL.md) runs this playbook as a gated chat flow (brainstorm → script → lock → handoff). This file is the rulebook.

Production: **wm-creative** (`wm-arcads-studio` + Arcads).

## Product fence

1. Confirm job is **DSCR** (investor refinance). If RM or Waiz, stop and switch.
2. Ideation load: [intelligence-icp-dscr.md](intelligence-icp-dscr.md) +
   [dscr-creative-taxonomy.md](dscr-creative-taxonomy.md) (buckets / jobs /
   naming). Do not load nurture, setter, or campaign-architecture docs.
3. After direction: [dscr-campaign-master-angles.md](dscr-campaign-master-angles.md) for winning-angle expand; [dscr-gtm-positioning-brief.md](dscr-gtm-positioning-brief.md) for test order.
4. Before ship: [dscr-compliance-guardrails.md](dscr-compliance-guardrails.md).
5. Stay inside the ICP **NEVER** list. Ask if claims are thin — do not invent.

## Gated flow (chat)

Pause after each step.

### Step 0 — Confirm + patterns
- Product line = DSCR.
- Optional: Mr. Waiz `ad_library` with `product=dscr` / winner refs (ask if summary thin).
- Do **not** pull RM swipes or RM script archetypes.

### Step 1 — Concept
Minimal: **bucket** (DENIED / DEADLINE / IDLE / IN-MARKET), angle (from ICP
slate or new within NEVER), creative job, stage (cold / warm), format (UGC
talking head default), count N.  
Present short concept table with `bucket · job · slug · angle`; pause for pick.

### Step 2 — Script (short beats)
Default for Arcads UGC (~10–15s speakable; ~2.5 wps):

| Beat | Job |
|------|-----|
| Hook | Investor world / myth / operator pain — not LO sales open |
| Problem | Specific refinance friction (rates, cash-out limits, DSCR math) |
| Mechanism | One plain how-it-works line (no illegal guarantees) |
| Proof | Real or clearly hypothetical; no fabricated testimonials |
| CTA | Low-friction info / call — match compliance |

Longer cuts only if user asks; still compliance-gated.

### Step 3 — Lock
Iterate until locked dialogue.

### Step 4 — Arcads handoff
```markdown
## Arcads handoff
- product_line: DSCR
- format: UGC (or named)
- stage / angle: …
- Compliance: PASS against dscr-compliance-guardrails
### Locked dialogue
…
### Production notes
- wm-creative → confirm DSCR → talent refs → dialogue gate → credit gate → 2 variants
- Prefer service/operator UGC (no CPG “holds the bottle” unless a real prop exists)
```

## Do not

- Route through RM Creative Studio or Higgsfield (retired)
- Use generic `ugc-scriptwriter` for client DSCR Meta ads (no compliance gate)
- Mix RM VOC (“retired homeowners”, HECM, FHA non-recourse) into DSCR copy
