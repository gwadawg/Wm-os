# Client Playbook Creator — Discovery Questions

Ask **one question at a time**. Skip any already answered in the thread or attached files.

## Sequence

### 1. Topic and north star

"What playbook are we creating? In one sentence, what outcome should a loan officer (or their team) achieve when they follow it?"

### 2. Audience

"Who is the primary user — the LO, their assistant/setter, Waiz CS, or a mix?"

### 3. Product lane

"Which product does this apply to — reverse mortgage (default), DSCR, or shared across products?"

### 4. Layer split

"Do you need:
- **A)** Canonical playbook only (system + rules),
- **B)** Canonical + execution doc (long copy / scripts / GHL steps),
- **C)** Canonical + course material (client education module),
- **D)** All three?"

Recommend **B** or **D** when the topic includes drip copy, ad scripts, or step-by-step GHL builds.

### 5. References and inspiration

"What should I read or use as input? (paste notes, repo paths, Drive `.docx` paths, URLs, or name an existing doc like `rm-ad-playbook.md`)"

If none: "Any frameworks, courses, or competitors you want this modeled after?"

### 6. Existing OS overlap

Agent runs catalog + grep silently, then asks:

"I found [doc A] and [doc B] on similar topics. Should I **update** one of those, **split** one, or **create new**?"

### 7. Core framework

"What is the mental model? (e.g. four pillars, funnel stages, TOF/MOF/BOF, phases, checklist) — even a rough list is fine."

### 8. Execution boundaries

"What must live in a separate execution doc vs the strategic playbook? (copy libraries, message sequences, Meta setup steps, etc.)"

### 9. Owner and trigger

"Who owns maintaining this — Client Success, Media Buying, Community/Education, or LO? What event triggers using this playbook?"

### 10. Quality bar and compliance

"Any compliance sensitivities, banned claims, or non-negotiable standards beyond [RM Compliance Guardrails](../../docs/client-fulfillment/reverse-mortgage-dna/rm-compliance-guardrails.md)?"

### 11. Confirm plan

Before writing, confirm verbatim structure:

```
Here's what I'll build:
- Canonical: [path] — [one line]
- Execution: [path or "none"] — [one line]
- Course material: [path or "none"] — [one line]
Reference format: playbook-lead-nurture.md
Proceed? (yes / adjust)
```

---

## Split-mode questions (legacy monolith)

Use when user points at an existing large file (e.g. `rm-ad-playbook.md`):

1. "What should stay as **strategy** (framework, angles, rules) in a new `playbook-{topic}.md`?"
2. "What stays as **execution** in the current file or a new `{topic}-execution.md`?"
3. "Do clients need a **course material** module for this topic?"
4. "Can we deprecate sections of the old file, or must it remain until you've reviewed the split?"

---

## After interview

Switch to **Build** mode → Phase 0–5 in [SKILL.md](SKILL.md).
