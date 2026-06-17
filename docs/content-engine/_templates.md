---
title: Content Format Templates
domain: content-engine
owner: founder
status: draft
last_updated: 2026-06-17
review_cycle: quarterly
---

# Content Format Templates

Canonical templates for scripted outputs. The content-engine skill uses these for `/script`.

Also mirrored in [format-templates.md](../../../.claude/skills/content-engine/format-templates.md).

## Reel / short-form

```yaml
---
title:
format: reel
lane: personal|business|client
pillar:
discoverability: searchable|shareable|both
hook:
body: |
  [VISUAL: ...]
  [LINE: ...]
cta:
length_target: 15s|30s|60s
editor_notes:
status: concept|scripted|filmed|published
date: YYYY-MM-DD
source_idea:
---
```

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
    headline:
    body:
  - slide: 2
    headline:
    body:
cta_slide:
caption:
status: concept|scripted|designed|published
date: YYYY-MM-DD
---
```

## Trial concept

```yaml
---
title:
format: trial-concept
lane:
pillar:
angle:
hook:
talent: self|ugc
length_target: 15s|30s
production_notes:
hypothesis:  # what you're testing
success_signal:  # views, saves, DMs, etc.
status: idea|testing|produced|killed
date: YYYY-MM-DD
---
```
