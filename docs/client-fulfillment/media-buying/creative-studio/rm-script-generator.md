---
title: RM Script Generator
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: playbook
---

# RM Script Generator

Turns one ideation concept into a full, compliant, ready-to-shoot video ad script. Powers the
`script` command of the [rm-creative-studio skill](../../../../.claude/skills/rm-creative-studio/SKILL.md).

> Every script is self-documenting: it carries a **Frameworks Applied** block and per-beat
> source citations (see [frameworks-reference.md](frameworks-reference.md)), and it passes the
> [compliance gate](compliance-gate-checklist.md) before it is marked ready.

## Inputs

- A concept from the [ideation matrix](rm-ad-ideation-matrix.md) (archetype + angle + stage + hook type), OR
- A direct request: archetype + angle + stage.
- Optional **`winner_ref`**: `supabase:ad:{uuid}` or swipe id (e.g. `rm-2026-06-breaking-news-static`) — when hooks derive from a proven winner, cite the ref in hook options and Frameworks Applied.
- Pulls VOC, fears, desires, objections from the [ICP doc](../../reverse-mortgage-dna/intelligence-icp-rm.md)
  and structure rules from the [RM Ad Playbook](../../client-marketing/rm-ad-playbook.md).

## The 5-part structure (45-90s video)

Source: playbook Format B. Each beat has a job, a framework basis, and a compliance watch.

| Beat | Time | Job | Frameworks (cite per script) | Compliance watch |
|------|------|-----|------------------------------|------------------|
| 1. **Hook** | 0-5s | Stop the scroll; earn the next 10s. One line FOR the prospect, not about the speaker. | Hook taxonomy (F7); Zeigarnik open loop (F2); awareness-matched hook (F1) | No product name (TOF); no age; no guarantee |
| 2. **Empathy & Validation** | 5-20s | Name their world specifically; validate the fear before any product talk. | VOC mirroring (F3/F4); Liking/Similarity (F2); pain->impact pair (F4) | "Retired homeowners," never age; no pity/desperation |
| 3. **Frame Shift** | 20-45s | Move Debt Frame -> Retirement-Tool Frame. Introduce by outcome first, one concept. | Framing + Contrast (F2); mechanism standard (F1); benefit-over-feature (F3) | Product name only at MOF+ and in context; no jargon |
| 4. **Proof & Reassurance** | 45-70s | Address the archetype's #1 objection; FHA non-recourse reassurance; social proof if real. | Loss Aversion reframed + Authority + Social Proof (F2); proof standard (F1); objections (F4 §7) | No fabricated stats/testimonials; "may/could," not "will" |
| 5. **CTA** | 70-90s | One calm, low-friction next step framed as access to information. | Commitment & Consistency small-step (F2); approved CTA bank (F5) | No "act now"/scarcity unless ethical-advisor framed (ICP §9) |

## Beat-build rules

- **Hook:** choose the hook type from the concept; write 2-3 options. The first words must
  pass the "prospect or speaker?" test (speaker = fail). Open a loop the Empathy beat closes.
- **Empathy:** lift a verbatim or near-verbatim VOC line from ICP §5 for the persona; show the
  pain->impact, not just the pain.
- **Frame Shift:** name the mechanism in one sentence (F1: "explains why past attempts failed,
  names the root cause, connects to the solution"). Outcome before label. No feature lists.
- **Proof:** pick the single biggest objection for the archetype (ICP §7) and dismantle it;
  anchor reassurance in the FHA-insured / non-recourse facts; keep proof specific (name, number,
  context) or clearly hypothetical.
- **CTA:** use one line from the playbook approved CTA bank; match friction to stage
  (TOF/MOF = info access; BOF = direct conversation).

## Output template

```
# Script: <ID> — <archetype> / <angle> / <stage>

Format: Video (45-90s) | Talent: <LO to camera / UGC / VO>

## Script
HOOK (0-5s):       <line>
EMPATHY (5-20s):   <lines>
FRAME SHIFT (20-45s): <lines>
PROOF (45-70s):    <lines>
CTA (70-90s):      <line>

## Frameworks Applied
- Hook: <hook type F7> + <model F2>
- Empathy: VOC (F4 §5 "<phrase>") + Liking (F2)
- Frame Shift: <mechanism, F1> + Framing/Contrast (F2)
- Proof: objection #<n> (F4 §7) + Loss Aversion (F2) + FHA non-recourse
- CTA: approved CTA bank (F5) + Commitment small-step (F2)

## Compliance Gate
[ ] No product name in TOF  [ ] No age in copy  [ ] No guarantees  [ ] No false urgency
[ ] No tax advice  [ ] No fabricated proof  [ ] VOC + mechanism + proof + awareness present
Result: PASS / FIX

## Video Brief (for editor / future video agent)
| # | Beat | On-screen | Shot / framing | B-roll | On-screen text | Audio |
|---|------|-----------|----------------|--------|----------------|-------|
| 1 | Hook | <talent/visual> | <close/medium> | <cutaway> | <caption> | <music/VO> |
| 2 | Empathy | ... | ... | ... | ... | ... |
| 3 | Frame Shift | ... | ... | ... | ... | ... |
| 4 | Proof | ... | ... | ... | ... | ... |
| 5 | CTA | ... | ... | ... | ... | ... |

Pacing: <cuts/10s, tone for the retired-homeowner feed: warm, calm, no hype>
Caption style: <burned-in lower-third / word-by-word>
First frame (0:00): <what stops the scroll>
```

## The Video Brief is the future-proofing

The Video Brief block is structured so a Layer 2 AI-video-creator agent (see
[FUTURE-video-agent-spec.md](FUTURE-video-agent-spec.md)) can consume it directly — scene list,
shot type, on-screen text, b-roll, audio. Writing scripts in this format now means no rework later.

## Quality escalation (from F1)

If a draft script feels weak:
- **Generic** -> swap abstract words for VOC (F4); add a proprietary mechanism/proof detail.
- **Flat emotion** -> reopen the pain->impact pair; write a concrete scene, not adjectives.
- **Low credibility** -> strengthen proof; explain the mechanism; reduce the promise or mark `[TO FILL]`.

A script that cannot show VOC + mechanism + proof + awareness stays `draft`, never `final`.
