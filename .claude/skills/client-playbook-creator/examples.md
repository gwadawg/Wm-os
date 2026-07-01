# Client Playbook Creator — Examples

## Example 1: Conceptual beliefs (default — single client playbook)

**User:** "Build playbook on conceptual beliefs for RM LO sales calls"

**Built:**

| Artifact | Path |
|----------|------|
| Team framework | `docs/acquisition/sales/conceptual-beliefs-framework.md` — universal seven beliefs |
| Client playbook | `docs/client-fulfillment/client-sales/playbook-rm-conceptual-beliefs.md` — RM lines, worksheet, decision rules **in one file** |

**Why it works:** One doc for LOs to train and run calls from. Universal model lives in acquisition for team + other products. No question bank, no course-material wrapper.

---

## Example 2: Lead nurture (legacy multi-doc stack)

**User:** "Create lead nurture playbook"

**Existing stack** (pre-dates single-playbook default):

| Layer | Path |
|-------|------|
| Framework | `playbook-nurture-framework.md` |
| Application | `playbook-lead-nurture.md` — Waiz Meta stack |
| Long script | `10-day-rm-drip-campaign.md` — drip copy justifies separate doc |
| Course material | `course-material/lead-nurture-playbook.md` |

**Link rule:** Course material links **framework only** in lessons 1–4. Waiz stack + drip → gated appendix (*Waiz DFY clients only*). Never link `internal-fulfillment` paths in prospect course body.

**Why split here:** Drip is 200+ lines of copy; Waiz GHL stack is a separate application layer. **New topics** should not copy this pattern unless similar length/script needs exist.

---

## Example 3: Long sales script (split justified)

**User:** "Add full RM discovery call script"

**Built:**

| Artifact | Path |
|----------|------|
| Playbook | `playbook-rm-conceptual-beliefs.md` — beliefs + short lines (link to script) |
| Long script | `script-rm-discovery-call.md` — full word-for-word call flow |

**Rule:** Playbook keeps mental model + key lines; standalone script doc when the call script is long enough to run independently.

---

## Example 4: RM ads (split candidate)

**User:** "Split rm-ad-playbook into proper format"

**Proposed split:**

| Layer | Path | Content |
|-------|------|---------|
| Playbook | `playbook-rm-meta-ads.md` | Strategy, angles, quality bar, links |
| Execution | `rm-ad-playbook.md` (trim) | Angle bank, long script concepts |

**Interview stops** until user approves — do not delete original without approval.

---

## Example 5: References from Drive

**User:** "Build playbook from Bootcamp doc in archive"

**Flow:**

1. Locate row in [google-drive-inventory.md](../../docs/_inventory/google-drive-inventory.md)
2. Read `.docx` via [docx](../docx/SKILL.md) from `waiz-os-archive`
3. Write **one client playbook** with inline lines; split only if source contains a full long script
4. Check [duplicate-resolutions.md](../../docs/_inventory/duplicate-resolutions.md)
5. Sync catalog

---

## Anti-patterns

**Bad:** Three files for one training topic — `playbook-x.md` + `x-question-bank.md` + `course-material/x-education.md`

**Fix:** Merge into one client playbook. Link team framework in acquisition if reusable.

**Bad:** 1000-line playbook with full drip + GHL steps + strategy

**Fix:** Playbook stays strategy + key lines; drip/GHL in dedicated script/SOP doc.

**Bad:** LO course or framework links internal fulfillment — `playbook-lead-nurture.md`, `10-day-rm-drip-campaign.md`, `crm-architecture/`, `media-buying/`, `how-wm-ai-bot-works.md` in main lesson body

**Fix:** Link `playbook-*-framework.md` only. Waiz DFY context → gated appendix (`paying-client`). Grep blocked paths before sync. See **No internal process links** in [SKILL.md](SKILL.md).

---

## Methodology propagation

**After build**, if a reusable technique is new:

> I used **[technique]** in this playbook, but it is not in the knowledge base yet. Should I update **[candidate doc(s)]**, add it to a methodology pool in `client-playbooks/catalog.yaml`, or keep it local to this playbook only? (update KB / pool only / local only)
