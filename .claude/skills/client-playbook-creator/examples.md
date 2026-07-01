# Client Playbook Creator — Examples

## Example 1: Lead nurture (gold standard)

**User:** "Create lead nurture playbook"

**Layers built:**

| Layer | Path |
|-------|------|
| Canonical | `docs/client-fulfillment/client-marketing/playbook-lead-nurture.md` |
| Execution | `docs/client-fulfillment/client-marketing/10-day-rm-drip-campaign.md` (pre-existing) |
| Course material | `docs/client-fulfillment/course-material/lead-nurture-playbook.md` |

**Why it works:** Canonical has four pillars + decision rules; execution holds 900+ lines of copy; course material is ~100 lines teaching + links.

---

## Example 2: RM ads (split candidate)

**User:** "Split rm-ad-playbook into proper format"

**Proposed split:**

| Layer | Path | Content |
|-------|------|---------|
| Canonical | `playbook-rm-meta-ads.md` (new) | TOF/MOF/BOF framework, angle system, quality bar, links |
| Execution | `rm-ad-playbook.md` (trim or rename) | Angle bank, script concepts, checklists |
| Course material | `course-material/rm-meta-ads-course-material.md` (optional) | LO education on creative strategy |

**Interview stops** until user approves split plan — do not delete `rm-ad-playbook.md` without approval.

---

## Example 3: References from Drive

**User:** "Build playbook from Bootcamp doc in archive"

**Flow:**

1. Locate row in [google-drive-inventory.md](../../docs/_inventory/google-drive-inventory.md)
2. Read `.docx` via [docx](../docx/SKILL.md) from `waiz-os-archive`
3. Extract framework → canonical; steps/copy → execution or link existing SOP
4. Check [duplicate-resolutions.md](../../docs/_inventory/duplicate-resolutions.md)
5. Sync catalog

---

## Example 4: Methodology propagation

**After build**, agent finds new "education-first objection sequence" pattern not in OS:

Ask:

> I used **education-first objection sequence** in this playbook, but it is not in the knowledge base yet. Should I update **docs/client-fulfillment/reverse-mortgage-dna/rm-borrower-objections.md**, add it to a methodology pool in `client-playbooks/catalog.yaml`, or keep it local to this playbook only? (update KB / pool only / local only)

---

## Anti-pattern: monolith playbook

**Bad:** 1000-line `playbook-*.md` with strategy + full ad scripts + GHL steps + client teaching.

**Fix:** Split mode — canonical ~150–300 lines, execution doc(s) for copy, course material for teaching.
