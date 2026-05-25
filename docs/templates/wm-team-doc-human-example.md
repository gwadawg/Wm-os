---
title: WM Team Doc — Human Example (Gold Standard)
domain: templates
owner: operations
status: active
last_updated: 2026-05-23
review_cycle: quarterly
artifact_type: reference
purpose: Visual mock of how every published team Google Doc should read. Compare to live reference Objection Handling doc.
---

# WM Team Doc — Human Example (Gold Standard)

> **This file is the layout contract.** When you publish any SOP or playbook to Drive, the output should read like this — not like raw repo markdown.
>
> **Live reference (colored):** [WM Objection Categories](https://docs.google.com/document/d/19creUTdx5cTwWJVjdX3qPUMY40v1z379bCNoieY_Q5Y/edit)

---

## How to read this mock

Each block below is labeled with what it becomes in Google Docs. Colors are described in [wm-team-doc-format-spec.md](wm-team-doc-format-spec.md).

---

## COVER (centered)

```
                    WAIZ MEDIA
              (26pt, bold, navy #1a365d)

           Setter No-Reply Bump — Scripts
              (20pt, blue #2b6cb0)

     Sales & Setting Team | Internal Use Only | 2026
              (11pt, gray italic)

────────────────────────────────────────────
         (light blue horizontal rule)
```

---

## OVERVIEW (HEADING_1 — navy)

LinkedIn outbound moves a loan officer from cold profile → real conversation → booked intro call. This page is **only** the setter bump and when to hand off — not the full LinkedIn process.

### 📌 NORTH STAR (shaded box — light blue fill, blue border)

**One sentence only. Never put Who/When/Questions inside this box.**

> 📌 **NORTH STAR**
>
> One bump only: add value with a single question — never pitch or re-send the opener.

### Meta (normal bullets, directly under the box)

- **Who:** Setter (Pedro / VA)
- **When:** 48–72 hours after opener if no reply

---

## QUICK START (HEADING_1 — navy)

Use this order every time:

1. Confirm the original opener topic in the tracker.
2. Pick **Option A or B** below (match the tone of their profile).
3. Log `setter_bump_sent = Y`.
4. If still no reply after the bump → stop; Gabriel runs ghost sequence.

---

## BUMP OPTIONS (HEADING_2 — navy)

**Rules (bold label, not a wall of text)**

- No pitch. One question. Max ~3 short lines on mobile.

### ✉️ COPY & PASTE — Option A (shaded template box, italic message)

> ✉️ **COPY & PASTE**
>
> Hey [Name] — no worries if timing’s off. Wondering if [original topic from opener] is still on your radar or if the market’s taken a back seat for now?

### ✉️ COPY & PASTE — Option B

> ✉️ **COPY & PASTE**
>
> Hey [Name] — bumping this once — you’d mentioned [their post topic / climate / volume]. Is that still the main headache on your end?

### ⚠️ IMPORTANT (shaded callout — same box style as NORTH STAR)

> ⚠️ **IMPORTANT**
>
> After one bump with no reply, do **not** send a second setter message. Hand off to Gabriel for ghost touches 1–3.

---

## WHEN TO USE WHICH OPTION (HEADING_2 — navy)

| Situation | Use |
| --------- | --- |
| Opener was about a **specific post or topic** | Option B (reference their topic) |
| Opener was **general / mutuals / group** | Option A (timing check) |
| They were **cold** (no strong signal) | Option A |

*(In Google Docs this is a real table: navy header row, white header text, bordered rows — not `\| pipe \|` bullets.)*

---

## GHOST SEQUENCE PREVIEW (HEADING_2 — navy)

Gabriel owns touches 1–3. Setter does not send these.

| Touch | Timing | What Gabriel sends |
| ----- | ------ | ------------------ |
| 1 | +3–4 days | Value tied to **their** pain — no ask |
| 2 | +7–10 days | Different insight or approved proof snippet |
| 3 | +12–14 days | Clean opt-out + door open |

---

## DONE RIGHT LOOKS LIKE (HEADING_2 — navy)

- Bump feels human, not automated.
- One question only; they can answer in one thumb tap.
- Tracker updated the same day.

---

## WHEN TO GET HELP (HEADING_2 — navy)

Pricing, exceptions, or angry replies → **Gabriel** immediately.

---

## 📌 REMEMBER (shaded callout at end)

> 📌 **REMEMBER**
>
> If this doc conflicts with what you heard elsewhere, follow this doc and tell Gabriel.

---

## FOOTER (centered, gray)

```
        Waiz Media  |  Internal Document  |  Confidential
```

---

## BAD vs GOOD (what we are fixing)

| Bad (old publish) | Good (this standard) |
| ----------------- | -------------------- |
| `\| Touch \| Template \|` as a bullet | Real 2-column table |
| `> Hey [Name]…` as plain bullet | ✉️ COPY & PASTE box |
| Who/When/Outcome crammed into NORTH STAR | One-sentence NORTH STAR + bullets below |
| Entire playbook under one “How to do it” | Section per H2 (Voice, Bump, Ghost, Angles…) |
| Black plain text, no hierarchy | Navy headings, colored cover, shaded boxes |

---

## Related

- [wm-team-doc-format-spec.md](wm-team-doc-format-spec.md)
- [team-doc-publish-template.md](team-doc-publish-template.md)
- Publish test: `python3 scripts/publish-team-doc.py docs/templates/wm-team-doc-human-example.md --force` (optional — add registry row first)
