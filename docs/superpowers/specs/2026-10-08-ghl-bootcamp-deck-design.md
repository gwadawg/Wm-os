---
title: GoHighLevel Bootcamp Deck Design
domain: client-fulfillment
owner: operations
status: draft
last_updated: 2026-10-08
review_cycle: as-needed
artifact_type: overview
related_docs:
  - docs/company/doctrine-brand-and-visual-identity-april-26.md
  - docs/client-fulfillment/course-material/README.md
---

# GoHighLevel Bootcamp Deck Design

## Purpose

A speaker-led slide deck for a 45–60 minute GoHighLevel (GHL)
foundations bootcamp for loan officers. The deck keeps the presenter's
thoughts in order while he drives GHL live on screen. It is not a
manual and not a handout.

## Audience And Outcome

- **Audience:** loan officers who have a GHL login but have not built
  anything yet.
- **Format:** presenter drives the whole hour. Attendees watch. No
  click-along.
- **Outcome when the hour ends:**
  - They can tell tags, custom fields, and custom values apart, and know
    where each lives.
  - They could set up the skeleton on their own: their own fields,
    their own tags, one calendar, one pipeline.
- **Out of scope:** having attendees copy the automation. That is a
  later session.

## Content Rules

- One idea per slide. Up to three short bullets. No paragraphs.
- Use HighLevel's product terms on slides: custom fields, custom
  values, tags, workflows. "Automation" is fine when spoken.
- Teach principles, not a standard. Examples are examples, not a list
  attendees must copy.
- The live automation build is freeflow. Slides never show its
  click-steps.
- Each slide carries short presenter notes (talking points) as HTML
  comments, not on screen.

## Run Of Show

| Block | Minutes | Slides |
|---|---|---|
| Blank canvas and proof stories | 5 | 1–5 |
| Account map and live tour | 8 | 6–7 |
| Tags, custom fields, custom values | 15 | 8–11 |
| Calendar and pipeline, shown in GHL | 8 | 12–13 |
| Freeflow automation build | 10 | 14 |
| Number health and homework | 5 | 15–16 |

## Slide Outline

1. **Title.** "GoHighLevel Bootcamp: Foundations." Waiz wordmark.
2. **A blank canvas.** Other CRMs make you fit their structure. GHL
   lets you build your own. Pro: full control. Con: more to learn.
3. **Section: Proof.** What this flexibility makes possible.
4. **Andy Zao.** Deal closes, then a handwritten thank-you letter goes
   to the borrower's home automatically. Every birthday, a handwritten
   card goes out on its own.
5. **Personalized video.** A pre-recorded video where AI speaks the
   lead's name. GHL sees when they watch it and sends a text X minutes
   later, so it feels coincidental.
6. **Section: The Basics.** What we cover today.
7. **The map.** Contacts, Calendars, Opportunities, Tags, Custom
   Fields, Custom Values. Line: organized now, or messy later. The
   presenter then tours GHL live in this order.
8. **Custom fields: facts about the person.** Loan purpose, birthday,
   property state. Used to filter for future reactivations and to keep
   workflows from messaging unqualified borrowers. Light note: a field
   belongs to a contact or to an opportunity, and that cannot be
   changed later.
9. **Tags: what happened.** Lead source, booked, no-show. Tags start
   workflows and let you filter by history and status.
10. **Custom values: your library.** Booking link, your name, NMLS.
    The same for every contact. Change it once and every message
    updates.
11. **Side by side.** Person = custom field. Event = tag.
    Library = custom value.
12. **Calendar.** Build your first calendar. Its booking link lives in
    a custom value so messages never hardcode it.
13. **Pipeline.** Stages tell the story of the file. Deal facts live on
    the opportunity. Person facts stay on the contact.
14. **Live build.** A bridge slide that stays up during the freeflow:
    new lead, then a source tag, then an opportunity, then one text
    using custom values. No click-steps.
15. **Keep your number healthy.** Registered to the real business.
    People opted in. Appointment and file updates, not promotional
    blasts. No bought lists.
16. **Your homework.** Choose your fields. Choose your tags. Build one
    calendar. Build one pipeline.

## Visual System

Source: `wm-csm-kit/brand/tokens.css` and the brand doctrine.

- **Colors:** navy `#061A4A`, royal `#0E2F73`, accent blue `#4FA3FF`,
  growth green `#7CFF7A` (payoff moments only), light `#F4F7FC`, dark
  text `#0B1220`, mid `#5B6475`.
- **Fonts:** Barlow Condensed (uppercase display headlines) and IBM
  Plex Sans (body), from Google Fonts.
- **Logo:** the official `waiz-wordmark.svg` (`currentColor` fill).
  White on navy slides, navy on light slides. A small wordmark and slide
  number in the corner of every slide.
- **Rhythm:** title and section slides are a full-bleed navy-to-royal
  gradient. Teaching slides are white or light with navy headlines.
  Accent blue marks the focal point.

## Graphics

Two kinds of graphics, split by one rule: anything with exact labels
the presenter points at is a coded diagram. Scene-setting moments are
GPT Image 2 illustrations.

### GPT Image 2 Illustrations

Generated with `gpt-image-2`, quality `high`, size `1536x1024`.
Every prompt starts with this style baseline:

> Premium isometric 3D illustration, clean fintech SaaS aesthetic,
> soft studio lighting, deep navy #061A4A and royal blue #0E2F73 forms,
> accent blue #4FA3FF highlights, a tiny touch of mint green #7CFF7A,
> white or very light background, generous negative space, no text,
> no logos, no close-up faces.

| Slide | Subject |
|---|---|
| 1 | Modular blocks assembling into a floating CRM workspace |
| 2 | Rigid pre-built box beside an open grid where blocks are placed |
| 4 | Handwritten envelope with wax seal at a home doorstep, birthday card beside it |
| 5 | Phone with a video play button, a soft "viewed" glow, a text bubble appearing |
| 7 | Half organized filing system, half messy drawer |
| 12 | Calendar card with a confirmed booking checkmark |
| 13 | Deal cards moving along a conveyor toward a house key |
| 14 | Gears and flow pipes connecting a lead card to a text message |
| 15 | Phone inside a shield with a green signal glow |

The title and blank-canvas illustrations are generated first as a
style test. The rest are generated only after the presenter approves
that look.

### Coded Diagrams

Built in HTML/CSS inside the slide so labels stay exact and editable:

- Slide 8: contact card with filled fields and a filter funnel.
- Slide 9: tag chips dropping onto a contact, lightning bolt starting a
  workflow.
- Slide 10: custom values library, one edit fanning out to several
  message bubbles.
- Slide 11: three-column comparison (Person, Event, Library).
- Slide 16: homework checklist.

## Build

- Built with the frontend-slides skill
  (`github.com/zarazhangrui/frontend-slides`): a single self-contained
  HTML file on a fixed 1920×1080 stage, keyboard navigation, inline
  text editing, `viewport-base.css` included in full.
- The skill's three-style picker is skipped because the brand is fixed.
  A title slide and one teaching slide are shown for sign-off before
  the full deck.
- Location: `docs/client-fulfillment/course-material/ghl-bootcamp/`
  with `index.html` and an `assets/` folder for the wordmark and
  illustrations. All asset paths are relative.

## Verification

- Every slide renders at 1280×720 without overflow or overlapping
  panels (screenshot check).
- No slide shows internal labels, file names, or design notes.
- Optional: export to PDF with the skill's `export-pdf.sh`.
