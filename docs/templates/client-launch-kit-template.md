---
title: Client Launch Kit Template
domain: templates
owner: client-success
status: draft
last_updated: 2026-09-12
review_cycle: quarterly
shareability: paying-client
artifact_type: template
audience:
  - team
content_layer: canonical
product: general
---

# Client Launch Kit Template

> **North star:** One branded PDF that hands the client **everything we built and every login they own**, plus the short training that makes them successful. Review-and-approve first (01–02), training second (03–04), aftercare last (05–07). Living files stay in Drive.

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
| **Reverse mortgage** | 04 = LO / VA dials; 05 index lists Nurture, HQ Lead, Ads, BAMFAM playbooks | 04 = Waiz call center dials + books, LO owns the appointment; index = Ads + HQ Lead + swipe folder |
| **DSCR** | 04 = self-serve (first 48 hours, BAMFAM, drip is the safety net); index = Prospecting Playbook + Cash-Out Drip; Drive `05-Playbooks/` required | 04 = Laura owns SMS + booking, LO owns the consult; index = swipe folder only (do not hand them the self-serve playbook or drip) |

Shared sections (Welcome, 01 Access, 02 What we built, 03 Engine, 05 change-request table, 06 First 30 days, 07 Who to ping) are the same for all four. "Your three jobs" in 03, the 04 table, and the "Owner / Your access" column in 01 swap wording when Waiz works the leads. Legacy Call Center clients prefill *Waiz works leads* and the CSM picks the product.

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
| **Owner per property** (01) | For each row above: `You` (client owns the account) \| `Waiz` \| `Shared`. Ad account + page are normally `You`; CRM sub-account and landing page normally `Waiz`. Do not guess. |
| **Client's access per property** (01) | One short phrase per row, e.g. "Full login", "Owner. Waiz is a partner", "View. Edits via Slack" |
| **Logins shared via** (01) | How credentials were handed over (Slack DM / password manager). **Never put a password in the PDF.** |
| **Performance review** (01) | Where and when the client sees numbers. Default: "Weekly check-in. Numbers walked live, summary posted in Slack after." |
| **Build inventory** (02) | Creative counts (`N video ads`, `N statics`), form filters (e.g. age, home, intent), anything not built → drop the row. Client language only, no specs. |
| Speed standard (as sold) | `[TO FILL]` — print the number in the 04 callout. If none was sold, the callout reads "confirmed on your launch call". Never expose the internal "we do not invent a number" rule to the client. |
| Market / geo | `[TO FILL]` |

## PDF section order (do not reorder)

Shared for RM and DSCR. Swap the appendix blocks only. **One section per page** — end each section with a `pagebreak` and trim copy until it fits. Never let a table or callout spill onto a mostly empty page. Target: cover + 8 pages. **Max one callout per section; four in the whole kit.**

Three acts: **review and approve** (01–02) → **training** (03–04) → **aftercare** (05–07).

0. **Welcome** — one paragraph (the kit's two jobs: hand over access, teach the short version), one callout (PDF is the conversation, Drive is the vault), "How to read this kit" (three bullets mapping 01–02 / 03–04 / 05–07), one closing line
1. **01 Your access** — intro (we click every link; bookmark CRM + calendar), **Access & ownership register** (Property / Link / Owner / Your access), "Your account at a glance" (client + product + market, go-live, who works leads, CSM + channel + cadence, performance review, logins shared via). No callout.
2. **02 What we built for you** — intro with **"What is yours"** ownership line, **build inventory** table (Piece / What it does / Where to see it — creatives, landing page + form, CRM pipeline, instant response + nurture, booking + reminders, tracking, ongoing media buying), "Your Drive folder" table (five folders)
3. **03 How the engine works** — intro, six-stage table (Stage / What the homeowner experiences — **no** "what you do" column), "Your three jobs" (one line on which stages run without them + three numbered habits: speed, BAMFAM, clean dispositions) — product appendix
4. **04 Working a lead** — one-line variant statement, **When / Do this** table (new lead, no answer, text back, will not book, books, no-show, CRM looks wrong), Daily rhythm table, speed-standard callout with the number printed — product appendix
5. **05 Playbooks and creative** — resource table (links only), "Using the creative" three bullets, **"Asking for a change"** table (landing-page wording, new ad angle, calendar/hours, budget) — product appendix
6. **06 First 30 days** — what you will feel / what it means table, Week by week table, one callout ("How we score Month 1") — same for both products
7. **07 Who to ping** — situation / where / when table, "Your team" as one paragraph (CSM is the single point of contact; media buying and tech sit behind them), one line on weekly check-ins, divider, footer caption

Removed on purpose (do not add back): "What's inside" TOC, "Most agencies…" positioning paragraph, "What we do differently" table, the six numbered Week 1 rules (now the When / Do this table), "Your job this month" list, "Your team" table with unnamed "Waiz team" rows, welcome-aboard closing callout, `02-Links` Drive folder.

Section headings carry the number: `"01  Your access"`. Cover fields (client, company, product, go-live) come from build flags, not `content.json`.

## Product appendix — 03 "Your three jobs" + 04 "Working a lead"

Section 03's three habits and section 04's When / Do this table swap per variant. The sample `content.json` is the RM / client-works-leads version.

### Reverse mortgage — LO / VA works leads (sample)

- Three jobs: speed · BAMFAM · clean dispositions
- 04 rows: new lead → call now · no answer → voicemail + text + disposition · text back → call · will not book → hold inside 72 h · books → confirm, reminders stay on · no-show → call at the slot, re-send link, disposition · CRM wrong → Slack same day
- The instant response and nurture support you; they do not replace the phone

### Reverse mortgage — Waiz call center dials

- Three jobs: keep the calendar accurate (block time you cannot take before we book into it) · show up on time and prepared, notes read · log the outcome after every appointment
- 04 rows: we book → confirm the hold · live transfer → pick up now · no-show → we re-book, you log it · a lead contacts you directly → tell us in Slack before you work it · CRM wrong → Slack same day
- Do not call or text leads we are still working unless we hand them to you
- 05 index: Ads playbook, HQ Lead Acquisition, swipe folder — no nurture / BAMFAM playbooks (that is our job)

### DSCR — self-serve

- Three jobs: first 48 hours decide the file · BAMFAM on every live conversation · clean dispositions (drip is the safety net)
- 04 rows: new lead → call inside the speed standard · text back → call now · will not book → hold inside 72 h · books → confirm · no-show → call at the slot, re-send link · CRM wrong → Slack same day
- You or your VA are the system. Do not also run Laura as the daily owner.
- 05 index: point at the Prospecting Playbook + Cash-Out Drip in Drive `05-Playbooks/` — do not paste either into the PDF
- Drive pack must include both client-delivery files before Send to client

### DSCR — Laura

- Three jobs: confirm calendar holds · show up prepared for the consult · log the consult outcome
- 04 rows: Laura books → confirm · lead needs the LO before Laura has booked → Slack · no-show → Laura re-books, you log · CRM wrong → Slack same day
- Laura owns SMS and booking. You own the consult.
- 05 index: swipe folder only — do not hand them the self-serve playbook or drip as the daily operating system

## Product appendix — 05 Resource index

Link `paying-client` or `lo-course` docs only. Never link `internal-fulfillment`. The "Asking for a change" table in 05 is shared across variants.

### Reverse mortgage

| Resource | Repo path (team) | Client sees |
|----------|------------------|-------------|
| Lead Nurture — Waiz Meta Stack | `docs/client-fulfillment/client-marketing/playbook-lead-nurture.md` | Portal / Drive copy, or “ask your CSM” if unpublished |
| RM High-Quality Lead Acquisition | `docs/client-fulfillment/client-marketing/rm-high-quality-lead-acquisition.md` | Same |
| Reverse Mortgage Ads Playbook | `docs/client-fulfillment/client-marketing/reverse-mortgage-ads-playbook.md` | Same |
| BAMFAM Playbook | `docs/client-fulfillment/client-sales/playbook-bamfam-rm.md` | Same |
| Fulfillment Lead Lifecycle | `docs/client-fulfillment/fulfillment-lead-lifecycle.md` | Already summarized in section 2 |

### DSCR — self-serve

| Resource | Repo path (team) | Drop into Drive |
|----------|------------------|-----------------|
| DSCR Prospecting Playbook | `docs/client-fulfillment/dscr-dna/playbook-dscr-self-serve-lead-nurture.md` | `05-Playbooks/DSCR-Prospecting-Playbook.pdf` |
| Client PDF | `docs/client-fulfillment/dscr-dna/assets/playbook-self-serve-nurture/DSCR-Prospecting-Playbook.pdf` | same |
| Cash-Out CRM Drip (12 touches + long tail) | `docs/client-fulfillment/dscr-dna/dscr-cash-out-self-serve-crm-drip.md` | `05-Playbooks/DSCR-Cash-Out-Drip.md` |
| Client drip file | `docs/client-fulfillment/dscr-dna/assets/playbook-self-serve-nurture/DSCR-Cash-Out-Drip.md` | same |

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
- How we score Month 1: engine live, every lead worked inside the speed standard, dispositions clean.
- Closings can happen. They are not the scoreboard yet.

## 01 Access & ownership register — rules

- One row per property that exists. Mark a property *Not part of this account* only if it truly does not exist; never leave a guessed link.
- `Owner` is who holds the account, not who uses it. The client normally owns the Meta ad account, page, calendar, and Drive folder; Waiz normally owns the CRM sub-account and landing page. Confirm from the build, do not assume.
- `Your access` is one phrase: what the client can do inside it and where to ask for changes.
- Credentials are never printed. The "Logins shared via" row says where they were sent.
- The "What is yours" line in 02 must match the `Owner` column in 01.

## 02 Build inventory — rules

- Client language only. "Pixel and conversion events" is fine; tag names, automation names, and workflow specs are not.
- Counts must be real (creatives, statics). If a piece was not built for this client, delete the row; do not leave a placeholder.
- Drive folder rows mirror the SOP **Drive pack** exactly.

## Generate

**Default: Mr. Waiz.** Client Roster → **Kit** → confirm variant → fill Your access + build inventory → operator setup → Generate. **Mr. Waiz copy constants must be re-ported to this structure and `TEMPLATE_VERSION` bumped before the next kit is generated there.** The PDF is stored per version, logged on the client file, and posted to ops Slack; **Send to client** posts it to the client channel. See the [SOP](../client-fulfillment/onboarding/sop-client-launch-kit.md#process).

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

The script fixes the brand so nobody has to remember flags: navy `#061A4A` cover with dot grid, accent blue `#4FA3FF` rules / callouts / table headers, **Barlow Condensed Black** headings, **Barlow Medium / Bold** body, eyebrow `WELCOME PACKET · {date}`, running header `CLIENT LAUNCH KIT`. Barlow has no arrow glyph — write `/` or `to`, never `→`. Fonts download once to `~/.cache/waiz-fonts/`. Requires the minimax-pdf skill at `~/.agents/skills/minimax-pdf` (or `MINIMAX_PDF_DIR`) plus Node + Playwright for the cover.

4. Rasterize and eyeball every page before sending — no orphan rows, no half-empty pages, every URL real.
5. Upload the PDF to `{Client Drive}/Launch Kit/01-Launch-Kit/`.
6. Do not commit the per-client PDF to git.

## `content.json` block types

Use only: `h1` `h2` `h3` `body` `bullet` `numbered` `callout` `table` `pagebreak` `spacer` `divider` `caption` (footer line only).

`body` may use `<b>` and `<i>`. Put URLs in table cells as plain text.

## Shareability

This template is `paying-client`. Generated kits are `paying-client`.

Forbidden in any generated kit: onboarding A-Z, media-buying SOPs, CRM/bot specs, drip copy libraries, internal swipe research, campaign-phase numbers, pricing, **passwords or credentials**, the sample footer "internal reference only".

→ [Shareability Boundaries](../client-fulfillment/shareability-boundaries.md) · [Launch Kit SOP](../client-fulfillment/onboarding/sop-client-launch-kit.md)
