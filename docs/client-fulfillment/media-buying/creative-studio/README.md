---
title: Creative Studio (RM Ads)
domain: client-fulfillment
owner: media-buying-lead
status: active
last_updated: 2026-09-07
review_cycle: monthly
artifact_type: sop
---

# Creative Studio (RM Ads)

Outbound creative engine for **reverse-mortgage** client video: brainstorm and write
compliant scripts, then hand off to **wm-creative** (Arcads). Sibling to
[creative-research/](../creative-research/). Lifecycle:
[ad-development-workflow.md](../ad-development-workflow.md).
Skill: [rm-creative-studio](../../../../.claude/skills/rm-creative-studio/SKILL.md).

**DSCR:** use [dscr-video-script-playbook.md](../../dscr-dna/dscr-video-script-playbook.md) — not this folder.

## What this gives you

- Systematic brainstorm (archetype × angle × stage × hook × format)
- 5-part video scripts + Video Brief + compliance gate
- Format rules (T1/T2/E1) and **Arcads handoff packet** (Higgsfield retired)
- Silent story ads via [silent-story-ad-playbook.md](silent-story-ad-playbook.md)

## Folder map

```text
creative-studio/
├── README.md
├── frameworks-reference.md
├── rm-archetypes-canonical.md
├── rm-ad-ideation-matrix.md
├── rm-script-generator.md
├── format-rules-video.md      ← T1/T2/E1 rules (no render prompts)
├── arcads-handoff.md          ← Step 4 → wm-creative
├── silent-story-ad-playbook.md
├── compliance-gate-checklist.md
├── chatbot-deploy/            ← legacy Claude Project kit (update before reuse)
└── outputs/                   ← optional saved concept+script+handoff
```

## How to use it

| Step | What | Gate |
|------|------|------|
| **0. Patterns** | Catalogs + swipes / Mr. Waiz | Confirm patterns |
| **1. Concept** | Ideation matrix | Pick concept # |
| **2. Script** | 5-part + compliance | Approve / edit |
| **3. Lock** | Iterate script | Lock |
| **4. Handoff** | Arcads packet → **wm-creative** | Continue production |

Chat by default; one consolidated save file only when asked.

## Scope

- **Generic RM** only. Adapt per LO with `[TO FILL]`.
- Statics: OS Ideogram SOP or wm-creative `wm-static-studio`.
- Video render: **wm-creative**, not this repo.
