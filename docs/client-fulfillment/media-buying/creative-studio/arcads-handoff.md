---
title: Arcads Handoff Packet (RM Creative Studio Step 4)
domain: client-fulfillment
owner: media-buying-lead
status: active
last_updated: 2026-09-07
review_cycle: monthly
artifact_type: playbook
---

# Arcads Handoff Packet

Replaces the old Higgsfield prompt step. After the RM script is **locked**, package
a handoff for **wm-creative** (`wm-arcads-studio` + Arcads). Do not invent Arcads
API payloads here — production prompts live in the creative repo.

## When to use

- End of [rm-creative-studio](../../../../.claude/skills/rm-creative-studio/SKILL.md) Step 4
- Shortcut `prompt` / `handoff` from a locked concept + script

## Required fields (paste inline)

```markdown
## Arcads handoff
- product_line: RM
- product: hecm | homesafe-second | (confirm)
- format: UGC | T1 spoken testimonial | T2 silent | E1 educational
- stage: TOF | MOF | BOF
- archetype / angle: …
- Compliance Gate: READY (paste result block)
- Format rules: see format-rules-video.md (Part E if T1/T2/E1)

### Locked dialogue
(exact lines only — this is what gets dialogue-gated in wm-creative)

### Editor notes
- disclosure / captions / CTA / music / B-Roll Sourcing Plan as needed

### Production notes for wm-creative
- Target duration / word budget (~2.5 wps)
- Talent: drop refs under references/people/<talent>/
- Default path: Seedance UGC + referenceImages (or workflow user names)
- Next: open wm-creative → confirm RM → dialogue gate → credit gate → 2 variants
```

## Do not

- Paste Higgsfield / “Clean Frame” model packs
- Generate Arcads credits from Wm-os
- Use this handoff for **DSCR** — use [dscr-video-script-playbook.md](../../dscr-dna/dscr-video-script-playbook.md)
