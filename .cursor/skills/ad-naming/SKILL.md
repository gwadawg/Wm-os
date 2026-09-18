---
name: ad-naming
description: >-
  Assigns Meta / Mr. Waiz ad_name labels using the Waiz naming convention and
  live siblings from the Mr. Waiz ad_library. Use when the user asks to label
  an ad, name a new creative, pick a variation letter, or register a creative
  in Mr. Waiz before launch.
---

# Ad Naming (Mr. Waiz)

Give every new creative a **permanent** `ad_name` for Meta + Mr. Waiz.

**Live reference = Mr. Waiz `ad_library` only.** Do not scan Wm-os swipes,
catalogs, or `ad-name-library.yaml` to decide the next name or find siblings.
OS docs are human rules; the agent’s source of truth for “what exists” is
Supabase via the lookup script in the dashboard repo.

## When to use

- “Label this ad” / “Name this creative”
- “What’s the next variation?”
- New ad ready to log in Mr. Waiz before Meta upload

## Pattern

```text
{product}_{concept}_{fmt}_v{#}[letter]
```

| Slot | Values |
|------|--------|
| `product` | `rm` · `dscr` · `bf` |
| `concept` | kebab idea family (2–4 words) |
| `fmt` | `st` · `ugc` · `t1` · `t2` · `edu` · `ext` |
| `v{#}` | Generation (`v1`, `v2`…) |
| `[letter]` | Parallel sibling (`a`, `b`…) — only when ≥2 tests share a gen |

### Variation rules

| Situation | Name |
|-----------|------|
| First creative in family × format | `…_v1` (no letter) |
| Parallel hooks/edits same gen | `…_v1a`, `…_v1b` |
| Remake after learnings | bump gen → `…_v2` |
| Same concept, new format | new `fmt`, reset `v1` |
| Only APR / LTV / FICO / range / disclaimer changes | **same** `ad_name` — update `visual_notes` + file |
| Meta rename / client copy | **never** change primary `ad_name` → `ad_library_aliases` |

### Statics (including DSCR rate-cards)

Use the **same** pattern. Concept slug = visual / idea family (layout + hook).  
**Never** put APR, LTV, FICO, loan range, or “apr” tokens in `ad_name`.

| Good | Bad (retired) |
|------|----------------|
| `dscr_navy-suburban-headline_st_v1` | `dscr_navy-suburban_5.99apr_noappr_nodocs` |
| `dscr_ratecard-centered_st_v1` | `dscr_ratecard_5.9apr_nodocs_85ltv` |

Put verbatim on-image numbers in `visual_notes`. Existing spend-bearing names keep their string; do not mint new names in the retired `dscr_{visual}_{spec…}` shape.

### Format → Mr. Waiz `ad_format`

| Name `fmt` | `ad_format` field |
|------------|-------------------|
| `st` | `static` |
| `ugc` | `ugc` |
| `t1` / `t2` | `testimonial` |
| `edu` / `ext` | `ext` (prefer adding a dedicated format in Mr. Waiz when needed) |

Product field: `rm`→`reverse`, `dscr`→`dscr`, `bf`→`broad_forward`.

## Step 1 — Query Mr. Waiz (required)

From the dashboard repo
(`/Users/gwadawg/Desktop/Repos/call-center-reporting-template - Copy`):

```bash
npx tsx scripts/ad-name-lookup.ts --product reverse
npx tsx scripts/ad-name-lookup.ts --prefix rm_equity-trap
npx tsx scripts/ad-name-lookup.ts --product dscr --q balloon
```

If the script fails, **stop** — do not invent siblings from memory or OS files.

Read the JSON: `ads`, `family_suggestions`.

## Step 2 — Choose concept + format

1. From the creative brief, pick a `concept` slug (kebab, 2–4 words).
2. Search lookup results for the same idea (prefix / `--q`). Prefer an
   **existing** concept token already used in Mr. Waiz names over a synonym.
3. Pick `fmt` from the table above.
4. Family key = `{product}_{concept}_{fmt}`.

## Step 3 — Assign version (never reuse a taken name)

Use `family_suggestions[familyKey]` when present:

- Empty family → `…_v1`
- Adding a parallel test → `next_parallel_letter`
- Learned remake → `next_generation`

**Uniqueness (hard rule):** every new `ad_name` must be unused in Mr. Waiz —
not as a primary `ad_library.ad_name` and not as any `ad_library_aliases.alias_name`
(case-insensitive). Similar creatives get the next free `v#` / letter; they do
**not** reuse an old string.

Before you output labels, verify each candidate:

```bash
npx tsx scripts/ad-name-lookup.ts --check dscr_nodocs-cashout_st_v1a
```

If `available: false` / `taken: true`, pick the next free slot and `--check` again.
Exit code `2` means taken. Never ship a colliding name.

Never rename a row that already has spend.

## Step 4 — Output label block

```text
ad_name: rm_equity-trap_ugc_v1b
product: reverse
ad_format: ugc
tags:                    # product × category catalog in Mr. Waiz — pick ids/slugs, do not invent
  track: [hecm]
  strategy: [myth-led]
  outcome: [cash-out]
  stage: [tof]
  equity_callout: [soft]
  concept: [myth-scary]
  trigger: [burden]
overview: …
summary: …
visual_notes: …
```

Tags are **not** a flat list. Pick `product` first, then select from that product’s
category dropdowns in Ad Library (DSCR: bucket / creative_job / concept /
topic; Angle is legacy optional only. RM: track / strategy / outcome / stage /
equity_callout / concept / trigger).
Taxonomy docs define *which values mean what*; Mr. Waiz owns the live catalog.

Remind: paste the same `ad_name` into Meta; set `status=testing` at launch.

## Do not

- Invent names without running `ad-name-lookup.ts`
- Reuse any `ad_name` or alias that already exists in Mr. Waiz
- Use Wm-os files as the sibling / uniqueness check
- Put funnel stage, client name, full hook text, or compliance numbers (APR/LTV/FICO/range) in `ad_name`
- Mint new names in the retired `dscr_{visual}_{spec…}` shape
- Rename spend-bearing `ad_name` rows
- Invent tag slugs or use flat legacy tags (`[cash-out, education]`) — only catalog rows for the ad’s product
