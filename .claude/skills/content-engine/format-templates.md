# Format Templates

Use for `/script` outputs. Save files under `[lane]/scripts/`.

## Reel

```yaml
---
title:
format: reel
lane: personal|business|client
pillar:
discoverability: searchable|shareable|both
hook:
body: |
  [VISUAL: opening shot]
  [LINE: spoken hook — 0:00-0:03]

  [VISUAL: ...]
  [LINE: ...]

  [VISUAL: CTA shot]
  [LINE: CTA]
cta:
length_target: 30s
editor_notes: |
  - Captions: full burn-in
  - Music: low under voice
  - Cut pace: ...
status: scripted
date: YYYY-MM-DD
source_idea:
belief_ref:  # optional B1, S2
---
```

### Reel beat guide (30s)

| Beat | Time | Job |
|------|------|-----|
| Hook | 0:00–0:03 | Pattern interrupt + promise |
| Context | 0:03–0:10 | Stakes or relatability |
| Insight | 0:10–0:22 | Mechanism, story turn, or belief |
| CTA | 0:22–0:30 | Follow, DM, comment prompt |

## Carousel

```yaml
---
title:
format: carousel
lane:
pillar:
discoverability: searchable|shareable|both
topic:
slides:
  - slide: 1
    headline:  # hook slide
    body:
  - slide: 2
    headline:
    body:
  - slide: 3
    headline:
    body:
  - slide: 4
    headline:
    body:
  - slide: 5
    headline:  # CTA slide
    body:
caption: |
  [IG caption with keywords if searchable]
cta_slide: 5
status: scripted
date: YYYY-MM-DD
---
```

### Carousel structures

- **Myth → truth** (5–7 slides)
- **Listicle** (1 hook + 3–5 items + CTA)
- **Story arc** (setup → conflict → lesson → CTA)

## Trial concept

```yaml
---
title:
format: trial-concept
lane:
pillar:
angle:
hook:  # single line to test
talent: self
length_target: 15s
production_notes: |
  - One location, one take preferred
  - No b-roll required
hypothesis:  # e.g. "Contrarian hook on freedom vs vacation resonates"
success_signal:  # saves + shares > baseline
status: idea
date: YYYY-MM-DD
---
```

Trial filming: hook + one supporting line + hard stop. Upgrade to full reel if signal hits.

## Client ad extension

For client lane reels/UGC, extend with compliance block after scripting:

```yaml
compliance_review: pending|approved
disclosures:
claims_check:  # pass/fail notes
```

Load client DNA compliance doc before filling this section.
