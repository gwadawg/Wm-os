---
title: Creative Research System (RM Ads)
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-05-30
review_cycle: monthly
artifact_type: sop
---

# Creative Research System (RM Ads)

A repeatable system for turning ads we admire into **named, reusable patterns** for
reverse-mortgage video creative — editing styles, script archetypes, and angle DNA.

> Core discipline: collect **winners, not favorites**; **decompose, don't admire**.
> Separate *what to say* (angle/script) from *how it's made* (editing/direction).

## Folder map

```text
creative-research/
├── README.md                       ← this method doc
├── swipe-decomposition-rubrics.md  ← how to break down a script + an edit
├── editing-styles-catalog.md       ← reusable EDITING styles (how it's made)
├── script-archetypes-catalog.md    ← reusable SCRIPT patterns (what it says)
└── swipes/
    ├── _TEMPLATE.md                ← copy this per ad
    └── assets/                     ← drop the actual video files / frames here
```

## The 4-phase method

1. **Collect** — source from Meta Ad Library (RM + adjacent finance/insurance/senior),
   our own winning ads, and high-craft DTC/UGC outside RM (for editing rhythm).
   Winner proxies: run length 3+ weeks, multiple variations, or real account data.
2. **Capture** — one `swipes/<id>.md` per ad (copy `_TEMPLATE.md`). Save the actual
   asset in `swipes/assets/` — ads disappear.
3. **Decompose** — run each swipe through the rubrics in
   [swipe-decomposition-rubrics.md](swipe-decomposition-rubrics.md). Output a *named pattern*.
4. **Codify** — roll repeated patterns into the two catalogs, each with an RM
   adaptation + compliance note checked against
   [RM Compliance Guardrails](../../reverse-mortgage-dna/rm-compliance-guardrails.md).

## Cadence

| Frequency | Action |
|-----------|--------|
| Weekly | Capture 5–10 swipes (bias to our own winners) |
| Monthly | Synthesize: a pattern shared by 3+ winners becomes a rule. Update catalogs. |
| Quarterly | Prune dead patterns; re-rank by what account data proved |

## How to feed ads to the agent (and what it can actually see)

The agent **cannot watch an `.mp4` or hear audio**. It analyzes **images and text**.
Pick whichever path fits:

| You provide | Agent can analyze | Notes |
|-------------|-------------------|-------|
| **Poppy.ai breakdown** (text) | Everything — full visual + audio + pacing decomposition | **Recommended primary path.** Use the fixed [Poppy extraction prompt](poppy-extraction-prompt.md) so output maps to the rubrics. |
| **Screenshots / key frames** (png/jpg) | First frame, composition, on-screen text, caption style, framing | Supplement when you want the agent's direct visual read on a moment. |
| **Burned-in captions in frames** | Reads the caption text directly from the image | No transcript tool needed if captions are on-screen. |
| **Transcript / pasted script** | Hook type, structure, frame mechanics, retention devices, CTA | Required for voiceover with no on-screen text. |
| **The raw `.mp4`** + `ffmpeg` installed | Agent extracts key frames + scene-change cut frequency, then reads frames | Fallback only; needs `ffmpeg`. Poppy is easier and sees audio/motion. |

### Optional: enable raw-video analysis with ffmpeg

If you want to just drop `.mp4` files and let the agent pull frames itself:

```bash
brew install ffmpeg
# extract 1 frame/sec:
ffmpeg -i swipes/assets/<file>.mp4 -vf fps=1 swipes/assets/<id>-frame-%03d.png
# detect cuts (pacing / cut frequency):
ffprobe -show_frames -of compact=p=0 -f lavfi \
  "movie=swipes/assets/<file>.mp4,select=gt(scene\,0.4)" 2>/dev/null
```

The agent then reads the `.png` frames as images. (Audio/voiceover still needs a
transcript — burned-in captions can be read straight from the frames.)
