---
title: Client Launch Kit Template
domain: templates
owner: client-success
status: draft
last_updated: 2026-09-11
review_cycle: quarterly
shareability: paying-client
artifact_type: template
audience:
  - team
content_layer: canonical
product: general
---

# Client Launch Kit Template

> **North star:** One branded PDF they can review on the Launch Call and keep. Living files stay in Drive.

Use this template to generate a per-client Launch Kit. Execution lives in the [Client Launch Kit SOP](../client-fulfillment/onboarding/sop-client-launch-kit.md) and runs in **Mr. Waiz → Client Roster → Kit**. Visual reference: [sample PDF](../client-fulfillment/onboarding/assets/launch-kit-sample/client-launch-kit-sample.pdf).

Do not invent URLs, owners, or numbers. Use `[TO FILL]` when a field is missing.

## Copy mirror rule (read first)

This file and the [sample `content.json`](../client-fulfillment/onboarding/assets/launch-kit-sample/content.json) are the **source of truth for every word** in a kit. Mr. Waiz renders the same copy from typed constants in `src/lib/launch-kit/copy/` (`shared.ts`, `week1.ts`, `resources.ts`) and stamps `TEMPLATE_VERSION` on the cover and in the `launch_kit` submission.

- Copy edits happen **here first**, then get ported to Mr. Waiz and `TEMPLATE_VERSION` is bumped.
- Mr. Waiz substitutes **only** the intake fields below. No AI, no free text in the PDF.
- The minimax-pdf build script below is the fallback renderer. Both renderers must produce the same section order and wording.

## Variant matrix (product × who works leads)

| | **Client works leads** (LO / VA — `lead_gen`) | **Waiz works leads** (`core`) |
|---|---|---|
| **Reverse mortgage** | Week 1 = LO / VA dials; resource index lists Nurture, HQ Lead, Ads, BAMFAM playbooks | Week 1 = Waiz call center dials + books, LO owns the appointment; index = Ads + HQ Lead + swipe folder |
| **DSCR** | Week 1 = self-serve (first 48 hours, BAMFAM, drip is the safety net); index = DSCR Self-Serve Lead Response | Week 1 = Laura owns SMS + booking, LO owns the consult; index = swipe folder only (do not hand them the self-serve playbook) |

Shared sections (Welcome, What's live, Engine, Creative, First 30 days, Who to ping) are the same for all four with small "what you do" swaps when Waiz works the leads. Legacy Call Center clients prefill *Waiz works leads* and the CSM picks the product.

## Intake (fill before generate)

| Field | Value |
|-------|-------|
| Client name | `[TO FILL]` |
| Company / DBA | `[TO FILL]` |
| Product | `reverse-mortgage` \| `dscr` |
| Who works new leads (variant) | `client` (LO / VA) \| `waiz` (call center / Laura) |
| Go-live date | `[TO FILL]` |
| CSM | `[TO FILL]` |
| Slack channel | `[TO FILL]` |
| Funnel / lander URL | `[TO FILL]` |
| CRM login / pipeline URL | `[TO FILL]` |
| Calendar booking URL | `[TO FILL]` |
| Meta ads / Business Manager | `[TO FILL]` |
| Skool / training | `[TO FILL]` |
| Client Drive — Launch Kit folder | `[TO FILL]` |
| Who works new leads | LO / VA / call center / Laura |
| Speed standard (as sold) | `[TO FILL]` — do not invent a number |
| Market / geo | `[TO FILL]` |

## PDF section order (do not reorder)

Shared for RM and DSCR. Swap the appendix blocks only. **One section per page** — end each section with a `pagebreak` and trim copy until it fits. Never let a table or callout spill onto a mostly empty page.

0. **Welcome** — two short paragraphs, one callout (PDF is the conversation, Drive is the vault), "What's inside" table (01–07), one closing line
1. **01 What's live** — property + URL table, "Your account at a glance" table, one callout
2. **02 How the engine works** — six-stage table (stage / what the prospect experiences / what you do), one line on repetition, "What we do differently" table
3. **03 Week 1 operator checklist** — six numbered rules, If / then table, Daily rhythm table, speed-standard callout — product appendix
4. **04 Resource index** + **05 Creative and swipe files** — same page. Resource table (links only), folder table with the Drive link as row one, three bullets — product appendix
5. **06 First 30 days** — what you will feel / what it means table, Week by week table, four numbered jobs, one callout (same for both products)
6. **07 Who to ping** — situation / where / when table, Your team table, one line on weekly check-ins, welcome-aboard callout, divider, footer caption

Section headings carry the number: `"01  What's live"` (two spaces). Cover fields (client, company, product, go-live) come from build flags, not `content.json`.

## Product appendix — Week 1

### Reverse mortgage

- Who dials (LO / VA / call center as sold)
- Speed-to-lead: work the lead when it hits; do not batch until tonight
- Never hang up without the next step on the calendar (BAMFAM)
- Update the disposition after every live conversation
- The drip and bot support you — they do not replace the call

### Reverse mortgage — Waiz call center dials

- The Waiz call center works new leads and books the appointment. You own the appointment.
- Keep your calendar accurate — block time you cannot take before we book into it
- Show up to every booked appointment on time and prepared; read the notes first
- If we send a live transfer, pick up — that homeowner is on the line now
- Log the outcome after every appointment so the pipeline stays honest
- Do not call or text leads we are still working unless we hand them to you
- Resource index: Ads playbook, HQ Lead Acquisition, swipe folder — no nurture / BAMFAM playbooks (that is our job)

### DSCR — self-serve

- You or your VA are the system. Do not also run Laura as the daily owner.
- First 48 hours decide the file. Call when they text back.
- BAMFAM on every live conversation
- Drip is the safety net
- Point them at the self-serve playbook in the resource index — do not paste it

### DSCR — Laura

- Laura owns SMS and booking. You own the consult.
- Confirm calendar holds and show up prepared
- Do not hand them the self-serve playbook as the daily operating system
- Ping Slack if a lead needs the LO before Laura has booked

## Product appendix — Resource index

Link `paying-client` or `lo-course` docs only. Never link `internal-fulfillment`.

### Reverse mortgage

| Resource | Repo path (team) | Client sees |
|----------|------------------|-------------|
| Lead Nurture — Waiz Meta Stack | `docs/client-fulfillment/client-marketing/playbook-lead-nurture.md` | Portal / Drive copy, or “ask your CSM” if unpublished |
| RM High-Quality Lead Acquisition | `docs/client-fulfillment/client-marketing/rm-high-quality-lead-acquisition.md` | Same |
| Reverse Mortgage Ads Playbook | `docs/client-fulfillment/client-marketing/reverse-mortgage-ads-playbook.md` | Same |
| BAMFAM Playbook | `docs/client-fulfillment/client-sales/playbook-bamfam-rm.md` | Same |
| Fulfillment Lead Lifecycle | `docs/client-fulfillment/fulfillment-lead-lifecycle.md` | Already summarized in section 2 |

### DSCR — self-serve

| Resource | Repo path (team) |
|----------|------------------|
| DSCR Self-Serve Lead Response | `docs/client-fulfillment/dscr-dna/playbook-dscr-self-serve-lead-nurture.md` |
| Client PDF (if already rendered) | `docs/client-fulfillment/dscr-dna/assets/playbook-self-serve-nurture/DSCR-Self-Serve-Lead-Response.pdf` |

### DSCR — Laura

| Resource | Repo path (team) |
|----------|------------------|
| How Laura books (client language only) | Summarize from `docs/client-fulfillment/dscr-dna/dscr-nurture-and-booking-laura.md` — do not attach the sequence spec |

If a playbook has no client-safe PDF or portal URL yet, write “your CSM will send this” instead of a repo path.

## First 30 days (client language — both products)

Translate. Do not attach the phase blueprint.

- Weeks 1–4 are a test. We are collecting data across ads, audiences, and angles.
- Lead volume will be uneven. That is normal.
- Do not judge the system by ROI this month.
- Your job: work every lead, keep dispositions clean, stay in Slack, show up to the weekly check-in.
- Closings can happen. They are not the scoreboard yet.

## Generate

**Default: Mr. Waiz.** Client Roster → **Kit** → confirm variant → fill What's live → operator setup → Generate. The PDF is stored per version, logged on the client file, and posted to ops Slack; **Send to client** posts it to the client channel. See the [SOP](../client-fulfillment/onboarding/sop-client-launch-kit.md#process).

**Fallback (Mr. Waiz down, or copy not yet ported):**

1. Duplicate [sample `content.json`](../client-fulfillment/onboarding/assets/launch-kit-sample/content.json).
2. Replace sample names, URLs, and the product appendix. Keep the section order and page breaks.
3. Render from the repo root with the branded build script (wraps the minimax-pdf skill and applies Waiz tokens):

```bash
python3 scripts/build-launch-kit.py \
  --content /path/to/{slug}-content.json \
  --subtitle "{Client Name} · {Company}<br>{Reverse Mortgage | DSCR} · Go-live {D Month YYYY}" \
  --date "{Month YYYY}" \
  --out /tmp/{slug}-launch-kit.pdf
```

The script fixes the brand so nobody has to remember flags: navy `#061A4A` cover with dot grid, accent blue `#4FA3FF` rules / callouts / table headers, **Barlow Condensed** headings, **IBM Plex Sans** body, eyebrow `WELCOME PACKET · {date}`, running header `CLIENT LAUNCH KIT`. Fonts download once to `~/.cache/waiz-fonts/`. Requires the minimax-pdf skill at `~/.agents/skills/minimax-pdf` (or `MINIMAX_PDF_DIR`) plus Node + Playwright for the cover.

4. Rasterize and eyeball every page before sending — no orphan rows, no half-empty pages, every URL real.
5. Upload the PDF to `{Client Drive}/Launch Kit/01-Launch-PDF/`.
6. Do not commit the per-client PDF to git.

## `content.json` block types

Use only: `h1` `h2` `h3` `body` `bullet` `numbered` `callout` `table` `pagebreak` `spacer` `divider`.

`body` may use `<b>` and `<i>`. Put URLs in table cells as plain text.

## Shareability

This template is `paying-client`. Generated kits are `paying-client`.

Forbidden in any generated kit: onboarding A-Z, media-buying SOPs, CRM/bot specs, drip copy libraries, internal swipe research, campaign-phase numbers, pricing.

→ [Shareability Boundaries](../client-fulfillment/shareability-boundaries.md) · [Launch Kit SOP](../client-fulfillment/onboarding/sop-client-launch-kit.md)
