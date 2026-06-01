---
title: Poppy.ai Extraction Prompt (Swipe Intake)
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: reference
---

# Poppy.ai Extraction Prompt (Swipe Intake)

Paste this prompt into Poppy.ai with the ad video. It forces output that maps 1:1 to the
[decomposition rubrics](swipe-decomposition-rubrics.md), so the breakdown drops straight
into a `swipes/<id>.md` file with nothing lost.

> Keep Poppy **observational** — it reports what's in the video. The strategic layer
> (archetype mapping, funnel stage, RM compliance, named patterns) is done after, against
> our frameworks.

---

## The prompt

```text
Analyze this video ad and return a STRUCTURED, LITERAL breakdown. Describe only what is
actually in the video — no marketing opinions, no guesses about performance. Use these
exact sections and headers:

TRANSCRIPT: full verbatim spoken words, with timestamps.

FIRST 5 SECONDS: verbatim opening words + exactly what is on screen at 0:00–0:05.

ON-SCREEN TEXT: every caption/overlay, verbatim, each with timestamp and style
(font weight, color, position, and animation — e.g. static lower-third, or word-by-word).

SCENE-BY-SCENE: each shot/scene as a row — timestamp | what's shown (talking-head /
b-roll / graphic) | framing (close/medium/wide) | location | who's on screen.

CUTS: total cut count + approximate cuts per 10 seconds.

PATTERN INTERRUPTS: zooms, speed ramps, sound effects, text pops, location/wardrobe
changes — each with a timestamp.

AUDIO: music (yes/no + mood), voiceover (yes/no), raw ambient, or trending sound.

PACING: does the edit rhythm change when the message beat changes? Where?

TALENT: who appears, apparent role (customer / spokesperson / actor), tone and energy.

PRODUCTION TIER: phone-UGC / prosumer / studio.

CTA: final call to action verbatim + how it's delivered.
```

---

## After Poppy returns

1. Create `swipes/<id>.md` from `_TEMPLATE.md`.
2. Paste Poppy's output under a `## Poppy raw breakdown` section.
3. The agent maps it through rubrics A + B → fills **Named pattern** / **Named style**,
   funnel stage, archetype, and the **RM adaptation note** (compliance-checked).
4. Repeated patterns (3+ swipes) graduate into the catalogs.

## When to also grab a frame
Poppy describes; sometimes you want a direct visual read. Drop a screenshot of a specific
moment (usually the 0:00 first frame) into `swipes/assets/` when you want the agent's eye on
composition, color, talent expression, or scroll-stop strength — things a text description
can flatten.
