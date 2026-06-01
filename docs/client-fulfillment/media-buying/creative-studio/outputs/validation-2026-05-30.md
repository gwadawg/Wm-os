---
title: Creative Studio Validation Run
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-30
review_cycle: once
artifact_type: validation
---

# Creative Studio Validation Run (2026-05-30)

First end-to-end test of the studio: a `brainstorm` batch and a full `script`, each run
through the [compliance gate](../compliance-gate-checklist.md) and compared against the
playbook's known-good examples and the pre-delivery checklist.

---

## Test 1 — `brainstorm` (Security-Seeker, TOF, N=3)

| ID | Archetype | Angle | Stage | Hook type | Format | One-line premise | Lead hook (direction) | VOC anchor | Frameworks | Gate |
|----|-----------|-------|-------|-----------|--------|------------------|-----------------------|-----------|------------|------|
| IDEA-001 | Security-Seeker | Burden | TOF | Confessional | Video | Validate the fear of becoming a burden, open the door to independence | "The last thing I want is for my kids to feel they have to take care of me." | "I don't want to ask my kids for help." | F7 confessional; F2 Liking; F4 burden pain | PASS |
| IDEA-002 | Security-Seeker | Trapped Asset | TOF | Paradox | Video | Reframe house-rich/cash-poor as solvable | "Your home has never been worth more — so why is money tighter than ever?" | "My house is worth a lot, but I can't touch any of it." | F7 paradox; F2 Contrast | PASS |
| IDEA-003 | Security-Seeker | No Monthly Payment | TOF | Rhetorical question | Static | Lead with the most concrete relief | "What would retirement feel like with no monthly mortgage payment?" | "I just want to stop worrying every month." | F7 rhetorical; F2 present-benefit | PASS |

Anti-overlap check: three different angles, three different hook types. PASS.

---

## Test 2 — `script` (from IDEA-001)

# Script: VAL-001 — Security-Seeker / Burden / TOF

Format: Video (45-90s) | Talent: LO or relatable spokesperson to camera

## Script
HOOK (0-5s):       "The last thing I ever want is for my kids to feel like they have to take care of me."
EMPATHY (5-20s):   "If you're a retired homeowner, you know the feeling. You spent your whole life taking care of your family. The thought of the roles reversing — of them worrying about you, rearranging their lives for you — that isn't the retirement you worked for."
FRAME SHIFT (20-45s): "Here's what most homeowners never learn: there's a federally-insured program that lets you tap the equity you've already built in your home — without selling, without moving, and without depending on anyone."
PROOF (45-70s):    "It's FHA-insured and has protections built in. Your heirs are never personally responsible, you keep the title, and you stay in your home. This isn't borrowing against your future — it's accessing what you've already earned."
CTA (70-90s):      "If that's worth understanding, tap below for our free guide. No pressure, no obligation — just clear information."

## Frameworks Applied
- Hook: confessional (F7) + open loop / Zeigarnik (F2); first words are FOR the prospect, not the speaker
- Empathy: VOC "I don't want to ask my kids for help" (F4 §5) + Liking/Similarity (F2) + burden pain->impact (F4 §3)
- Frame Shift: mechanism "access equity already built" stated once, outcome-first (F1) + Framing (F2); product not named (TOF)
- Proof: objection "my kids will inherit debt" (F4 §7 #2) + non-recourse reassurance + Loss Aversion reframed (F2)
- CTA: approved info-access CTA (F5) + Commitment small-step (F2)

## Compliance Gate
A Hard:    PASS — no product name in TOF; "retired homeowner" not age; no guarantee ("lets you tap," not "you will get $X"); no tax claim; no urgency; no fabricated proof
B Stage:   PASS — TOF leads with prospect's world; product unnamed; frame-shift by outcome
C Quality: PASS — VOC present; mechanism named; proof (FHA/non-recourse) specific; awareness matched (TOF/Problem-aware)
D Hygiene: PASS — hook passes "prospect or speaker?"; works without "Hi I'm..."; CTA low-friction
RESULT: READY (generic; insert client/LO specifics as [TO FILL] before publishing)

## Video Brief (for editor / future video agent)
| # | Beat | On-screen | Shot / framing | B-roll | On-screen text | Audio |
|---|------|-----------|----------------|--------|----------------|-------|
| 1 | Hook | Spokesperson to camera, warm home | Medium close-up | — | none (let the line land) | soft VO bed |
| 2 | Empathy | Same, slight push-in | Close-up | Family photo on mantel, quiet home | — | soft bed |
| 3 | Frame Shift | Spokesperson | Medium | Hand on door of paid-off home; equity-as-tool graphic | "Already earned" | bed lifts gently |
| 4 | Proof | Spokesperson | Medium close-up | "FHA-insured" + "You keep the title" supers | non-recourse line | calm, reassuring |
| 5 | CTA | Spokesperson | Medium | Free-guide mockup | "Free Guide — No Obligation" | resolve |

Pacing: 1-3 cuts / 10s, warm and calm for the retired-homeowner feed; no hype, no fast-UGC energy.
Caption style: clean burned-in lower-third (legibility for the audience).
First frame (0:00): spokesperson's face mid-sentence + the confessional line — relatability stops the scroll.

---

## Validation against known-good

Compared to the playbook's proven **Burden angle, Concept 1.3 (video script)** in
[rm-ad-playbook.md](../../client-marketing/rm-ad-playbook.md):

- Same 5-beat arc and timing. MATCH.
- Same frame discipline (no product name in TOF, outcome-first frame shift, FHA reassurance, info-access CTA). MATCH.
- Original wording (not copied), per playbook rule "concepts are inspiration, build something new." MATCH.

Against the playbook **Pre-Delivery Checklist**: archetype-specific (yes), funnel stage assigned + rules obeyed (yes), hook stops scroll in 5s without intro (yes), frame built not Debt-reinforced (yes), copy leads with prospect (yes), compliance items all clear (yes), CTA low-friction info-access (yes). PASS.

## Verdict

Studio produces compliant, framework-grounded, known-good-aligned output. The skill is ready
for use on generic RM. Remaining: founder review to flip `status: draft -> active`, and (later)
client-specific tailoring + the Layer 2 video agent.
