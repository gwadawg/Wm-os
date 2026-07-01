# Shareability Checklist — LO Course Modules

Run before publishing course material for **non-client LOs** (prospect course, community, lead magnets).

## Doc metadata

- [ ] Course material frontmatter includes `shareability: lo-course`
- [ ] `canonical_parent` points to a **`lo-course`** framework doc (not an application or internal SOP)

## Link audit (main lesson body)

Every link in sections 1–4 (before any DFY appendix):

- [ ] Target doc has `shareability: lo-course` OR is acquisition marketing for selling Waiz
- [ ] **No links** to paths under:
  - `crm-architecture/`
  - `onboarding/a-z`
  - `media-buying/` (unless explicitly tagged `lo-course` — rare)
  - `10-day-rm-drip`, `rm-imessage-intent-drip` (execution copy)
  - `how-wm-ai-bot-works`
- [ ] **No links** to `playbook-*` application docs unless appendix is labeled **paying-client only**

## Content audit

- [ ] No GHL workflow steps, tag names, or Waiz bot conversation logic in prose
- [ ] No drip message copy pasted inline
- [ ] No internal KPI targets or CS constraint troubleshooting
- [ ] Frameworks taught in plain language; Waiz automation mentioned generically (*"a system can handle speed-to-lead"*) unless appendix is gated

## DFY appendix (optional)

If module includes *"For Waiz DFY clients"* section:

- [ ] Section is clearly separated (heading + warning)
- [ ] Links only `paying-client` docs — never `internal-fulfillment` in a prospect-facing export
- [ ] Prospect course export **omits** this section entirely when publishing publicly

## After changes

```bash
python scripts/sync-client-playbooks.py
```

Verify shareability column in [catalog.md](catalog.md).

## Related

- [Shareability boundaries](../shareability-boundaries.md)
- [client-playbook-creator skill](../../.claude/skills/client-playbook-creator/SKILL.md)
