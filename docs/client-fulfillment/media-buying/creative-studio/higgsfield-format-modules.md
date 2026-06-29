---
title: Higgsfield Format Modules (Testimonial + Educational)
domain: client-fulfillment
owner: media-buying-lead
status: draft
last_updated: 2026-06-10
review_cycle: monthly
artifact_type: playbook
---

# Higgsfield Format Modules (Testimonial + Educational)

Extends the [Higgsfield Prompt Builder](higgsfield-prompt-builder.md) beyond UGC
creator-to-camera with three more creative formats: **spoken testimonial**, **silent
text-overlay testimonial**, and **educational / explainer**. Powers the `prompt` command of
the [rm-creative-studio skill](../../../../.claude/skills/rm-creative-studio/SKILL.md) when
the concept's format is not UGC.

> **Shared mechanics live in the prompt builder — do not duplicate them.** Every module here
> reuses the builder's direction blocks (§3, incl. 3.5 Clean Frame + Audio), character lock
> (§4), asset tagging (§5), chunked skeleton (§6.2), camera/failure standards (§8), and
> compliance overlay (§10). This doc only defines what **changes** per format.

## Format selector (which module for which job)

| Format | Module | Runtime | Best stage | Talent | What Higgsfield renders |
|--------|--------|---------|------------|--------|--------------------------|
| UGC creator-to-camera | [prompt builder](higgsfield-prompt-builder.md) (unchanged) | 18–32s | TOF + MOF/BOF | Retired homeowner to camera | Everything |
| Spoken testimonial | T1 below | 25–40s | MOF/BOF (TOF possible, product unnamed) | Retired homeowner/couple telling their story | Everything |
| Silent text-overlay testimonial | T2 below | 45–60s | TOF + MOF | Couple/homeowner as proof — never addresses the lens | B-roll scenes only (captions = editor) |
| Educational / explainer | E1 below | 30–60s | MOF/BOF strongest; TOF myth-hook variant | Calm educator/advisor or "what I learned" homeowner | Talking-head + human b-roll only (data/text visuals = sourced or editor) |

Pick by the concept's format field ([ideation matrix](rm-ad-ideation-matrix.md)). If the
concept has no format, recommend one by stage and hook type, then confirm with the user.

---

## Module T1 — Spoken testimonial (AI creator tells their story)

A first-person, past-tense story told to camera: life before → doubt → discovery → life
after. It borrows UGC realism but the energy is **reflective, not explanatory** — "let me
tell you what happened to us," not "let me teach you something."

### The dramatization rule (hard, non-negotiable)

An AI-generated person "giving a testimonial" is a **fabricated testimonial** unless it is
clearly disclosed as a dramatization. So every spoken-testimonial output must:

1. **Carry the disclosure line**, documented in the **Editor Notes** (never rendered by the
   AI — the Clean Frame + Audio block forbids all rendered text):
   `Dramatization. Composite of real homeowner experiences. Individual results vary.`
   Burned in by the editor as a persistent small super, or at minimum on the first frame and
   the CTA frame.
2. **Never present the speaker as a real named client.** No real names, no "client of
   [LO]" framing. The story is a composite built from VOC (ICP §5) and real objection
   patterns (ICP §7).
3. **Keep numbers on the struggle side.** No result dollar figures ("we now get $X/month").
   A specific outcome number must be a real, approved client result marked `[TO FILL]` and
   routed to **HUMAN REVIEW**.
4. **Story type tag.** Every output is tagged `Story type: Composite (dramatization)` so the
   editor and media buyer know the disclosure is required.

### Beat structure (5 beats, 25–40s)

| Beat | Timing | Job |
|------|--------|-----|
| 1. Life before | 0:00–0:06 | Past-tense hook in the prospect's world: the specific squeeze, said the way they'd say it (VOC). "Our income hadn't changed since [year]. Everything else had." |
| 2. Doubt / failed attempts | 0:06–0:12 | What they tried in the Debt frame (cut back, downsize talk, dip into savings) and the skepticism — "we'd heard the horror stories." Honest midpoint conflict builds trust. |
| 3. Discovery + mechanism | 0:12–0:22 | How they found the idea, mechanism in plain language with the tactile analogy. **This is the reveal beat** — reveal-asset YES at MOF/BOF, product still unnamed at TOF. |
| 4. Life after | 0:22–0:32 | Concrete, dignified after-state — a paid bill, a visit to the grandkids, walking out the door unhurried. Feelings + specifics, never dollar amounts. |
| 5. Soft CTA | 0:32–0:38 | Peer-to-peer, from the approved bank: "If you're where we were, there's a free guide below." |

### Voiceover deltas (vs UGC rules in the builder §2)

- **Past tense, first person** ("I" / "we"). The UGC reframe pattern becomes lived
  experience: "We thought it was an income problem, so we kept cutting back. Turned out the
  money was already in the house."
- **Story cadence** — slightly slower, warmer; complete sentences, small pauses. Still no em
  dashes, no bolding in the voiceover.
- **The doubt beat is mandatory.** A testimonial without skepticism reads fake; the midpoint
  conflict is what makes the composite credible.
- All other voiceover rules (hook owns the first five words, plain mechanism + analogy, live
  compliance) carry over unchanged.

### Prompt build

- Reuse the builder's standard or chunked skeleton with the **character lock + all five
  direction blocks** in every chunk.
- **UGC Realism block tone adjustment** (append after pasting it):
  > The energy is reflective and warm — someone recounting what happened to them, with small
  > natural pauses and genuine remembering expressions. Never salesy, never scripted-sounding.
- Couple variant: lock **both** characters in the character lock; one leads the story, the
  other reacts naturally (nods, small smiles, finishing a gesture). Never both talking over
  each other.
- Chunk mapping (5 chunks): Life before / Doubt / Discovery + Reveal / Life after / CTA.
  Reveal-asset pattern per builder §5 — `NO, NO, YES, NO, NO` at MOF/BOF; **all NO at TOF**.
- **Editor Notes (always output with the prompt):** disclosure line + placement, captions,
  CTA text, music direction. None of these go inside the prompt itself.

---

## Module T2 — Silent text-overlay testimonial (story told in captions)

Formalized from the validated outputs
[rm-testimonial-inflation-hedge.md](outputs/rm-testimonial-inflation-hedge.md) and
[rm-testimonial-trapped-asset.md](outputs/rm-testimonial-trapped-asset.md). The story is told
entirely through burned-in captions over dignified b-roll. **Works on mute. The text is the
content; the people are the proof, not presenters.** Strong at TOF because the soft mechanism
reveal never needs the product name.

> **Canonical playbook (2026-06+):** [silent-story-ad-playbook.md](silent-story-ad-playbook.md) —
> punchy caption engine (6–12 words/frame, 2–2.5s), three story layers (emotional + secret +
> proof), multi-hook pack workflow, B-roll REAL/AI/STILL matrix, lead-quality hook rules, and
> story spine library. Use that doc for brainstorm → script → editor handoff; this module covers
> Higgsfield prompt chunks and dramatization rules.

### What Higgsfield does and does not render

- Higgsfield renders **only the b-roll scenes** — no dialogue, no speaking to camera, and
  (per Clean Frame + Audio) **no rendered text and no music**.
- Captions, music, and the disclosure are **editor items**, delivered as a caption table in
  the Editor Notes.

### Structure (the caption engine)

- **16–19 caption frames** (~2–2.5s each, ~42–56s total) is the **preferred punchy standard**
  (see [silent-story-ad-playbook.md](silent-story-ad-playbook.md)). Legacy outputs may use
  **12–14 frames** (~3–4s each, 45–60s).
- Both map onto the 5-beat arc: Hook (1–2) → Empathy (3–5) → Frame Shift (6–8) → Proof (9–14)
  → Payoff + CTA (15–19).
- **Ellipsis open-loop engine:** captions that continue end with `…` to force the next
  frame; resolution beats end clean.
- **Hook frame (0:00–0:02) is the most important 2 seconds:** bold ALL-CAPS line +
  a specific anchor (a year, a receipt, a split-screen) that stops the scroll on mute.
- **Midpoint conflict is mandatory** ("we almost didn't look into it…") — it pre-handles the
  distrust objection.
- **Numbers on the struggle side only.** Specific years/prices in the pain; the payoff is
  feeling prepared, never a promised amount.
- **Disclosure** (dramatization rule above applies): persistent small super or on frames 1 +
  end card.

### Prompt build (one scene = one prompt chunk)

Each caption frame gets a short b-roll scene prompt. Every scene chunk carries the
**character lock + Subject/Setting Realism + Concept-Reveal + Clean Frame + Audio blocks**
(B-Roll Sequencing and UGC Realism are replaced by the rule below, since no one talks).

> Important silent-story direction: The people never address the camera and never speak.
> Every scene is an observed, candid moment — natural movement, genuine micro-expressions,
> documentary feel. The emotional arc moves from quiet strain to calm relief across the
> scenes, always dignified, never distressed.

Per scene chunk, output: scene number + beat label, the caption it sits under (for the
editor — **not** in the prompt), b-roll description (action, framing, light), reveal-asset
YES/NO, continuity notes. Reveal asset (document/guide prop) only at the frame-shift beat,
MOF only — at TOF the shift is carried by a soft visual (a friend showing a phone, a calmer
expression), no program visual at all.

### Editor Notes (always output)

Caption table (frame # / time / caption / ellipsis or clean), caption style (bold,
high-contrast, legible for an older audience, one short line at a time), music direction
(slow, melancholic → bittersweet, low volume), disclosure placement, end-card CTA.

---

## Module E1 — Educational / explainer (teach the mechanism)

A calm, credible **educator** ad: myth → why it persists → mechanism → nuance → soft CTA.
Denser than UGC is allowed — this format earns attention by actually teaching — but every
sentence stays plain enough for a 12-year-old, and it never crosses into advice.

### Talent and stance

- Default: a **calm educator/advisor figure** (45–65, warm, credible — think trusted
  financial educator, not a pitchman) in a clean home office or kitchen-table setting.
- Variant: a credible retired homeowner in "what I learned researching this" stance — keeps
  the educator structure with peer trust.
- **No advice.** The script explains how something works; it never says what the viewer
  should do. Close with "talk to a qualified professional" framing where relevant.

### Beat structure (30–60s)

| Beat | Timing | Job |
|------|--------|-----|
| 1. Myth hook | 0:00–0:05 | Name the misconception the audience already holds: "Most retired homeowners think the only way to use home equity is to sell or borrow against it with a new monthly payment." |
| 2. Why the myth persists | 0:05–0:12 | One honest sentence — old programs, horror stories, confusing jargon. Builds credibility by validating the skepticism. |
| 3. Mechanism | 0:12–0:30 | The actual how-it-works, one concept at a time, with the tactile analogy. This format may take two passes at the mechanism (plain version, then the analogy). Reveal beat lives here. |
| 4. Nuance / honesty | 0:30–0:40 | "It's not for everyone" — one real condition or trade-off, stated plainly (e.g. you keep up taxes and insurance). Honesty is the proof in this format. |
| 5. Soft CTA | 0:40–0:50 | Info-access close: the free guide / the explainer link. BOF: "book a quick call with [TO FILL]." |

Stage rules unchanged: at TOF the mechanism is explained **without naming the product**;
MOF can name the category and bust myths; BOF positions the LO.

### B-roll sourcing matrix (the smart part)

Higgsfield is excellent at consistent humans and terrible at legible text, real data, and
real places. So every educational scene is tagged with one of three sources:

| Tag | What goes here | Why |
|-----|----------------|-----|
| **GENERATE** (Higgsfield) | Talking-head continuity chunks (character lock), in-home human moments, character-locked cutaways (hands on a coffee mug, walking to the porch) | Character continuity across chunks; no licensing needed; AI renders warm human scenes well |
| **SOURCE** (stock/online) | Charts, graphs, data visuals, archival/news-style footage, aerial or real-location shots, document close-ups where text must be legible, anything with numbers on screen | AI renders text/data badly (warped, misspelled); real data needs real visuals; license via a stock library |
| **EDITOR** (post) | Captions, CTA cards, disclosure supers, simple text cards/lower-thirds, music | Clean Frame + Audio rule: the model never renders text or music |

**Decision rule of thumb:** needs a consistent human → GENERATE. Needs legible text, real
data, or a real place → SOURCE. Is text or a graphic overlay → EDITOR.

**Licensing rule:** every SOURCE item must come from a licensed stock library (or be
client-approved footage) and is flagged for a licensing check in the compliance gate. Never
"grab it from YouTube/Google."

### B-Roll Sourcing Plan (required output for every educational ad)

Output this table next to the prompt chunks:

```
| # | Beat | What's on screen | Source | Detail |
|---|------|------------------|--------|--------|
| 1 | Myth hook | Educator to camera, home office | GENERATE | Chunk 1 prompt below |
| 2 | Why it persists | 90s-era news-style footage of housing headlines | SOURCE | Stock search: "archival news housing 1990s"; license check |
| 3 | Mechanism | Educator + analogy gesture | GENERATE | Chunk 2 prompt below |
| 3b | Mechanism insert | Simple equity diagram | EDITOR | Editor builds graphic; spec in Editor Notes |
| ... | | | | |
```

For GENERATE rows → a prompt chunk. For SOURCE rows → 2–3 stock search terms + a licensing
flag. For EDITOR rows → a one-line spec in the Editor Notes.

### Prompt build

- Reuse the builder's chunked skeleton: character lock + all five direction blocks in every
  GENERATE chunk. Talking-head chunks follow the builder's camera standards (natural
  movement, motivated cuts, no locked-off shots).
- **Subject/Setting Realism block swap:** replace "retired homeowner" with the educator
  character ("a credible, warm financial educator, calm teaching energy, never salesy or
  hyped") when using the educator talent.
- Scene discipline: max 3 talking-head scenes; SOURCE/EDITOR inserts carry the visual
  variety, so the human chunks stay simple and consistent.
- Reveal-asset pattern per builder §5 applies to GENERATE chunks (TOF = all NO).

---

## Output templates

Use the builder's §11 template with these additions:

- **All modules:** add a `Format:` line naming the module (Spoken testimonial / Silent
  text-overlay / Educational) and an **Editor Notes** section (captions, CTA text, music,
  disclosure where required).
- **T1 + T2:** add `Story type: Composite (dramatization)` and the disclosure line +
  placement in Editor Notes.
- **T2:** prompt section is the per-scene chunk list; Editor Notes carries the full caption
  table.
- **E1:** add the **B-Roll Sourcing Plan** table before the prompt chunks; SOURCE rows carry
  stock search terms + `licensing check` flag.

## Compliance overlay additions

These sit on top of the builder §10 mapping and the
[compliance gate](compliance-gate-checklist.md) (see its Part E):

| Gate item | Where it lives |
|-----------|----------------|
| Dramatization disclosure (T1/T2) | Editor Notes, with placement; never AI-rendered |
| No fabricated result figures (T1/T2) | Numbers on the struggle side; results = `[TO FILL]` → HUMAN REVIEW |
| Speaker never a real named client (T1/T2) | Character lock + story tagged Composite |
| No advice claims (E1) | Nuance beat + "qualified professional" framing |
| Sourced b-roll licensed (E1) | B-Roll Sourcing Plan `licensing check` flag on every SOURCE row |

## Related

- Shared mechanics + UGC format: [higgsfield-prompt-builder.md](higgsfield-prompt-builder.md)
- Concept generation: [rm-ad-ideation-matrix.md](rm-ad-ideation-matrix.md)
- The gate: [compliance-gate-checklist.md](compliance-gate-checklist.md)
- Validated silent-testimonial examples: [outputs/rm-testimonial-inflation-hedge.md](outputs/rm-testimonial-inflation-hedge.md) · [outputs/rm-testimonial-trapped-asset.md](outputs/rm-testimonial-trapped-asset.md)
- Long-form real-talent scripts: [rm-script-generator.md](rm-script-generator.md)
