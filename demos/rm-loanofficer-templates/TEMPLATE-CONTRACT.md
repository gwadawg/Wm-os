---
title: RM Virtual Card + Educate Template Contract
domain: client-fulfillment
owner: founder
status: draft
last_updated: 2026-09-21
review_cycle: quarterly
artifact_type: template-contract
product: reverse-mortgage
related:
  - demos/rm-loanofficer-templates/index.html
  - demos/rm-loanofficer-templates/packs.json
  - docs/client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md
---

# RM Virtual Card + Educate Template Contract

Frozen 2026-09-21. Layouts and section jobs are locked. Style packs swap CSS tokens only.

## URLs

| Surface | Pattern |
|---------|---------|
| Card | `loanofficer.me/[slug]` |
| Educate | `loanofficer.me/[slug]/learn` |

Waiz never appears in URL or UI. Card is fully LO-branded.

## Mr. Waiz form fields (collect)

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `slug` | string | yes | kebab-case, unique |
| `fullName` | string | yes | |
| `title` | string | no | Default: `Loan Officer` |
| `company` | string | yes | |
| `nmls` | string | yes | Digits only in storage; display with `NMLS #` |
| `statesLicensed` | string[] | yes | Joined for display (`CA`, `CA, AZ`) |
| `phone` | string | yes | E.164 preferred; drive `tel:` / `sms:` |
| `email` | string | yes | |
| `headshotUrl` | url | yes | Public HTTPS |
| `valueLine` | string | no | ≤ 20 words; falls back to pack `sample_value_line` |
| `product` | enum | yes | `rm` for this contract |
| `stylePackId` | enum | yes | One of pack_ids below (or `accentColor` override later) |
| `secondaryLinks` | `{label, href, sublabel?}[]` | no | Card renders **exactly one**. Default label: `How a reverse mortgage can help` → `/[slug]/learn` |
| `loNote` | string | no | Educate soft note; default stock line |
| `bookingUrl` | url | no | Calendar link (Calendly, Google, GHL, etc.). If empty, Book CTAs hide. |
| `bookingLabel` | string | no | Card button label. Default: `Book a call` |

### Generated (not collected)

- vCard download from name / title / company / phone / email / card URL
- Compliance footer strings from `nmls` + `statesLicensed`

---

## Section IDs

### Card (`#card`)

| ID | Job | Content source |
|----|-----|----------------|
| `#card-company` | Brand strip | `company` |
| `#card-headshot` | Identity | `headshotUrl` (initials fallback) |
| `#card-name` | Name | `fullName` |
| `#card-title` | Role | `title` |
| `#card-value` | Outcome line | `valueLine` or pack default |
| `#card-actions` | Reach / save | Call · Text · Save contact |
| `#card-details` | Below-fold facts | phone, email, nmls, states |
| `#card-secondary` | One educate link | `secondaryLinks[0]` or default |
| `#card-compliance` | Legal footer | Fixed sentence + tokens |

Above fold: company → headshot → name/title → value line → Call | Text | Save contact.  
Below fold: details → one secondary link → compliance.  
No social icons. No Waiz mark. No sticky bar.

### Educate (`#educate`)

| ID | Job | Content source |
|----|-----|----------------|
| `#edu-chrome` | Back + soft LO | back link, firstName, headshot |
| `#edu-hero` | BOF product frame | eyebrow + H1 + promise + image |
| `#edu-myths` | Belief: stigma → truth | Waiz stock (3 myths) |
| `#edu-outcomes` | Belief: life outcomes | Waiz stock (3 vignettes + hedge) |
| `#edu-steps` | Belief: process / control | Waiz stock (3 steps) |
| `#edu-lo-note` | Soft LO presence | `loNote` or default |
| `#edu-footer` | Education disclaimer | Fixed + nmls / states |

Locked hero copy:

- Eyebrow: `What a reverse mortgage actually is`
- H1: `Reverse mortgage basics: what changes, what stays the same.`
- Promise: `You keep the home. There is no required monthly mortgage payment. Here is how the equity you already built can support life in retirement, without the jargon.`

No sticky Call/Text bar. Program name allowed in eyebrow/H1 (BOF educate). No urgency. No age in copy.

---

## CSS variables (per pack)

```css
:root {
  --paper: /* hex */;
  --paper-deep: /* hex */;
  --ink: /* hex */;
  --ink-soft: /* hex */;
  --muted: /* hex */;
  --faint: /* hex */;
  --line: /* rgba */;
  --accent: /* hex */;
  --accent-deep: /* hex */;
  --accent-wash: /* rgba */;
  --on-accent: /* hex */;
  --display: /* font family */;
  --body: /* font family */;
  --radius: 14px;
}
```

Packs set tokens only. Shared layout components for card + educate.

---

## Style packs (frozen set)

Four packs only. Each owns a different axis (paper × accent × type × mode). Dropped Ink (too close to Coastal) and Ledger (too close to Heritage).

| pack_id | display_name | Axis | Mode |
|---------|--------------|------|------|
| `forest` | Forest | Green × soft-neutral paper × modern sans | light |
| `coastal` | Coastal | Blue × cool paper × soft sans | light |
| `heritage` | Heritage | Burgundy × warm cream × serif display | light |
| `night-desk` | Night Desk | Brass × charcoal × geometric sans | dark |

Canonical hex + fonts: [`demos/rm-loanofficer-templates/packs.json`](../../../demos/rm-loanofficer-templates/packs.json).

---

## Compliance (non-negotiable)

- Say **retired homeowners**, never age
- No financial / tax / legal advice; point to qualified pros in educate footer
- No guaranteed outcomes; outcome vignettes carry hedge line
- Property obligations (taxes, insurance, maintenance) stated when myths require it
- Education before pressure; no scarcity / “book now” as design center
- Equal Housing + NMLS + not a commitment to lend on both surfaces

---

## Implementation note

Demo reference: [`demos/rm-loanofficer-templates/index.html`](../../../demos/rm-loanofficer-templates/index.html).  
Production target: Next.js + CSS modules (or CSS variables theme), mobile-first ~390px.
