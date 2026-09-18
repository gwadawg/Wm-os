---
title: Ad Naming Convention (Mr. Waiz + Meta)
domain: client-fulfillment
owner: founder
status: active
last_updated: 2026-09-16
review_cycle: monthly
artifact_type: playbook
---

# Ad Naming Convention (Mr. Waiz + Meta)

Canonical rules for `ad_name` — the same string in **Mr. Waiz** `ad_library` and **Meta Ads Manager** — plus **campaign and ad set** names, which are Meta-only.

**Controlled library (optional human seed):** [ad-name-library.yaml](ad-name-library.yaml)  
**Live name registry:** Mr. Waiz `ad_library` via dashboard `scripts/ad-name-lookup.ts` (agents: [ad-naming skill](../../../.cursor/skills/ad-naming/SKILL.md))

**Related:** [ad-intelligence-bridge.md](../../operations/ad-intelligence-bridge.md) · [ad-development-workflow.md](ad-development-workflow.md) · [dscr-static-image-generator-project.md](../dscr-dna/dscr-static-image-generator-project.md)

## Purpose

1. Scan Ads Manager and know the **idea** and **format** without opening the creative.
2. Keep **one permanent name** per creative — never rename after launch.
3. Keep **similar ads in the same family** with an obvious **variation marker**.
4. Leave topic / angle / funnel stage to Mr. Waiz **tags** + `summary` — do not stuff them into the name.
5. Leave **compliance numbers** (APR, LTV, FICO, loan range, disclaimer) out of the name — they change without changing the creative identity.

## Pattern (all products — including DSCR statics)

```text
{product}_{concept}_{fmt}_v{#}[letter]
```

| Slot | Required | Values | Job |
|------|----------|--------|-----|
| `product` | yes | `rm` · `dscr` · `bf` | Vertical (`bf` = broad forward) |
| `concept` | yes | Slug from [ad-name-library.yaml](ad-name-library.yaml) | The **idea / visual family** — layout + hook, never APR/specs |
| `fmt` | yes | Format code from library (maps 1:1 to Mr. Waiz `ad_format`) | What kind of creative (`st` for static) |
| `v{#}` | yes | `v1`, `v2`, … | **Generation** — next learning cycle of that concept × format |
| `[letter]` | optional | `a`, `b`, `c`… | **Parallel variation** of the same generation |

### Examples

| Name | Meaning |
|------|---------|
| `rm_equity-trap_ugc_v1` | First gen, sole creative in that gen |
| `rm_equity-trap_ugc_v1a` | Gen 1, variant A (same idea, different hook/edit/thumb) |
| `rm_equity-trap_ugc_v1b` | Gen 1, variant B — **sibling** of `v1a` |
| `rm_equity-trap_ugc_v2` | Gen 2 — rebuilt from what we learned on gen 1 |
| `rm_equity-trap_t2_v1` | Same concept family, **different format** (silent story) |
| `dscr_balloon-exit_st_v1` | DSCR concept static (angle-led) |
| `dscr_navy-suburban-headline_st_v1` | DSCR static — navy headline-stack layout family |
| `dscr_ratecard-centered_st_v1` | DSCR static — centered rate-card layout family |

### Variation rules (hard)

| Situation | How to name | Why |
|-----------|-------------|-----|
| Same concept, testing 2–3 hooks/edits at once | Same `concept` + `fmt` + `v{#}` + different **letters** (`v1a`, `v1b`) | Family stays searchable; letter = parallel test |
| Only one creative in that gen | `v1` with **no** letter | Don't invent `v1a` until a sibling exists |
| Remake after learnings (new cut, new script, new layout) | Bump **generation**: `v2`, `v3`… | Letters are siblings; numbers are successors |
| Same idea in a new format | Same `concept`, **new `fmt`**, reset to `v1` | Format is part of identity; don't overload letters |
| Only APR / LTV / FICO / range / disclaimer text changes | **Keep the same `ad_name`** | Numbers are not creative identity — update `visual_notes` + file |
| Meta renamed / client-specific copy of same file | **Do not** change primary `ad_name` — add `ad_library_aliases` | Join key stays stable |

**Never rename** a row that already has spend. Alias only.

### Static concepts (DSCR and others) — no numbers in the name

Statics — including rate-card / spec-stack layouts — use the **same** pattern as everything else. The concept slug names the **visual family** (layout + headline structure), not the rates printed this week.

| Do | Don't |
|----|-------|
| `dscr_navy-suburban-headline_st_v1` | `dscr_navy-suburban_5.99apr_noappr_nodocs` |
| `dscr_ratecard-centered_st_v1` | `dscr_ratecard_5.9apr_nodocs_85ltv` |
| Put APR, LTV, FICO, loan range, disclaimer in `visual_notes` (verbatim) | Encode those values in `ad_name` |

**Retired pattern:** `dscr_{visual}_{spec1}_{spec2}_{spec3}` — do not use for new ads. Existing spend-bearing names keep their string (never rename); new statics and remakes use the concept pattern above.

Prefer number-free TOF statics when the angle does not need rates. When MOF/BOF rate-cards need numbers, the master `ad_name` still stays number-free; the live figures live in `visual_notes` and the export file.

## Campaign and ad set names (Meta only)

> **Draft companion to**
> [creative-testing-structure.md](creative-testing-structure.md). Use only if /
> when that structure is approved. The `{product}_{concept}_{fmt}_v{#}[letter]`
> **ad** pattern above remains active either way.

Ad names are the cross-client join key and never change. **Campaign and ad set
names are Meta-only** — they do not exist in Mr. Waiz `ad_library` — and their
job is to make a Scale/Test structure machine-readable: automated rules filter
on them, and `utm_medium={{adset.name}}` carries the ad set into reporting.

### Campaign

```text
{client-slug}_{product}_{role}
```

| Slot | Values | Job |
|------|--------|-----|
| `client-slug` | lowercase kebab of the client account (`jp-dauber`, `community-first`) | Which account |
| `product` | `rm` · `dscr` · `bf` | Vertical — matches the ad `product` token |
| `role` | `scale` · `test` | Which job this campaign does |

Examples: `jp-dauber_rm_scale` · `jp-dauber_rm_test` ·
`community-first_dscr_scale`

**Why `role` is in the name:** the automated budget rules must filter on
`_scale` so they can never touch a Test campaign. Vertical-scaling a test ad set
mid-wave destroys the isolation the test was built for. Replace the legacy
`LO-[Name]-PGS` filter with a `_scale` name filter when migrating an account.

### Ad set

```text
scale_{persona}          # Scale campaign
test_w{n}_{concept}      # Test campaign
```

| Slot | Values | Job |
|------|--------|-----|
| `persona` | `broad` at mid tier; persona slug (`widowed`, `married`, `pre-retiree`) once persona ad sets are funded — **not** `veteran` (deprecated) | Which audience signal |
| `w{n}` | Global wave number, **roster-wide** — `w7` means the same wave on every account | Lets the roster pool be reconstructed |
| `concept` | Same concept slug as the ad inside it | Ties ad set to concept |

Examples: `scale_broad` · `scale_widowed` · `test_w7_estimate-request` ·
`test_w8_payment-gone`

### Hard rules

| Situation | How to name | Why |
|-----------|-------------|-----|
| Test ad set holds one ad | Ad set `concept` token **must equal** the ad's `concept` token | The ad set's numbers are the concept's numbers |
| New wave, same concept | New ad set, next `w{n}` | Waves are the time axis; never reuse an ad set across waves |
| Wave number | Global across the roster, never per client | A concept's pooled read is assembled from one wave number |
| Ad set already has spend | **Never rename** | Historical `events.adset_name` rows stop joining |
| Persona ad set added later | New ad set `scale_{persona}`; leave `scale_broad` until it is retired | Renaming breaks the join |
| APR / LTV / FICO / rates | Never in a campaign or ad set name | Same rule as ad names |
| Client name | In the **campaign** name only, never in an ad name | The ad library is cross-client |

## What does **not** go in the name

| Put in name | Put elsewhere |
|-------------|----------------|
| product, concept family, format code, gen/variation | — |
| — | Funnel stage → `summary` |
| — | Topic (rates, cash-out, HECM…) → Mr. Waiz **tags** |
| — | Client name → never (library is cross-client) |
| — | Full hook sentence → `summary` / `visual_notes` |
| — | APR, LTV, FICO, loan range, disclaimer → `visual_notes` (and export file) |
| — | Date → optional only if colliding; prefer library + version |

## Agent / human workflow — “Label this ad”

**Agents:** use [.cursor/skills/ad-naming/SKILL.md](../../../.cursor/skills/ad-naming/SKILL.md).  
**Sibling / uniqueness check = Mr. Waiz only** (`scripts/ad-name-lookup.ts` in the dashboard repo). Do not use this YAML or OS swipes as the live name registry.

When creating or logging a new creative:

1. Run `ad-name-lookup.ts` against Mr. Waiz (`--product` / `--prefix` / `--q`).
2. Reuse a **concept** token already present in Mr. Waiz `ad_name` values when the idea matches; otherwise introduce a new kebab slug (avoid synonyms of live names).
3. Pick **fmt** from the format table (and set matching Mr. Waiz `ad_format`).
4. From lookup `family_suggestions` for `{product}_{concept}_{fmt}`:
   - No siblings → `…_v1`
   - Parallel tests → next free letter on current gen (`v1a`, `v1b`…)
   - Learned remake → next gen (`v2`)
5. Output the label block: `ad_name`, `overview`, `summary`, `visual_notes`, plus `product` + `ad_format` + suggested **tags**.

### Label output shape

```text
ad_name: rm_equity-trap_ugc_v1b
product: reverse
ad_format: ugc
tags: [cash-out, education]   # from Mr. Waiz tag catalog — not invented in the name
overview: …
summary: …
visual_notes: …
```

## Quality bar

- [ ] Concept slug exists in the library (or was added in the same change)
- [ ] `fmt` matches Mr. Waiz `ad_format`
- [ ] Variation letter only when ≥2 parallel creatives share the same gen
- [ ] Same string pasted into Meta ad name
- [ ] No APR / LTV / FICO / loan-range / “apr” tokens in `ad_name`
- [ ] No rename of an existing spend-bearing name — aliases only
- [ ] Campaign named `{client-slug}_{product}_{role}` with `role` = `scale` or `test`
- [ ] Ad set named `scale_{persona}` or `test_w{n}_{concept}`
- [ ] Test ad set `concept` token matches the single ad inside it
- [ ] Wave number is the roster-wide wave, not a per-client counter
- [ ] Automated budget rules filter on `_scale` so they cannot touch a Test campaign

## Related

- [ad-name-library.yaml](ad-name-library.yaml) — concept + format registries
- [ad-creative-manifest.yaml](ad-creative-manifest.yaml)
- [creative-testing-structure.md](creative-testing-structure.md) — the structure these names describe
- [creative-awareness-ladder.md](creative-awareness-ladder.md) — rung and persona slugs
- [performance-learnings.md](performance-learnings.md)
