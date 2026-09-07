---
title: RM Video Format Rules (T1 / T2 / E1)
domain: client-fulfillment
owner: media-buying-lead
status: active
last_updated: 2026-09-07
review_cycle: monthly
artifact_type: playbook
---

# RM Video Format Rules (T1 / T2 / E1)

Format craft for reverse-mortgage **client video** after the script is locked.
Production rendering happens in **wm-creative** (Arcads) — this doc is rules +
editor notes only, not a paste prompt pack.

Powers Part E of [compliance-gate-checklist.md](compliance-gate-checklist.md).
Silent caption stories: prefer [silent-story-ad-playbook.md](silent-story-ad-playbook.md).

## Format selector

| Format | Module | Runtime | Best stage | Talent |
|--------|--------|---------|------------|--------|
| UGC creator-to-camera | Script gen + Arcads UGC | ~10–30s (model-capped) | TOF + MOF/BOF | Retired homeowner to camera |
| Spoken testimonial | **T1** | 25–40s (often multi-clip) | MOF/BOF | Homeowner/couple story |
| Silent text-overlay | **T2** | 45–60s | TOF + MOF | Proof on camera; captions = editor |
| Educational / explainer | **E1** | 30–60s | MOF/BOF | Educator or “what I learned” |

Pick from the concept’s format field ([rm-ad-ideation-matrix.md](rm-ad-ideation-matrix.md)).

---

## Module T1 — Spoken testimonial

First-person, past-tense story to camera: life before → doubt → discovery → life after.
Reflective, not explanatory.

### Dramatization rule (hard)

An AI person “giving a testimonial” is a fabricated testimonial unless disclosed.

1. **Disclosure** in Editor Notes (editor burns in — never AI-rendered text):
   `Dramatization. Composite of real homeowner experiences. Individual results vary.`
2. **Never** present the speaker as a real named client.
3. **No result dollar figures.** Struggle-side numbers only; approved results = `[TO FILL]` → HUMAN REVIEW.
4. Tag: `Story type: Composite (dramatization)`.

### Beat structure (25–40s)

| Beat | Job |
|------|-----|
| 1. Life before | Past-tense VOC squeeze |
| 2. Doubt / failed attempts | Debt-frame attempts + skepticism (mandatory) |
| 3. Discovery + mechanism | Plain mechanism; product unnamed at TOF |
| 4. Life after | Dignified specifics — no dollar promises |
| 5. Soft CTA | Peer-to-peer, approved bank |

Hand off locked dialogue to **wm-creative** (`wm-arcads-studio`) with Editor Notes
(disclosure placement, captions, CTA).

---

## Module T2 — Silent text-overlay testimonial

Story in burned-in captions over dignified b-roll. Works on mute.
Canonical workflow: [silent-story-ad-playbook.md](silent-story-ad-playbook.md).

- AI / Arcads generate **b-roll / people only** — no dialogue to camera, no rendered captions or music.
- Captions + disclosure + music = **editor**.
- Dramatization rule (T1) applies.
- Numbers on the struggle side only.

---

## Module E1 — Educational / explainer

Calm educator: myth → why it persists → mechanism → nuance → soft CTA.
**Explains, never advises.** Close with “talk to a qualified professional” where relevant.

### B-roll sourcing matrix

| Tag | What | Why |
|-----|------|-----|
| **GENERATE** | Talking-head, in-home human moments | Character continuity; Arcads / AI human scenes |
| **SOURCE** | Charts, archival, real places, legible docs | AI text/data is unreliable; license stock or client footage |
| **EDITOR** | Captions, CTA cards, disclosure, music | Never model-rendered |

**Licensing:** every SOURCE item flagged for license check. Never grab from the open web.

### B-Roll Sourcing Plan (required for E1)

```
| # | Beat | What's on screen | Source | Detail |
|---|------|------------------|--------|--------|
| 1 | Myth hook | Educator to camera | GENERATE | Arcads / talent refs |
| 2 | Why it persists | Archival housing headlines | SOURCE | Stock terms + license check |
```

---

## Editor Notes (always with handoff)

- Format module name (T1 / T2 / E1 / UGC)
- Captions / CTA text / music direction
- Disclosure + placement when testimonial
- B-Roll Sourcing Plan when E1
