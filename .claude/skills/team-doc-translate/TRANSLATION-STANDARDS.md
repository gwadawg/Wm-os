# Team Doc Translation Standards

## At a glance (required)

Place immediately under the title. Template:

```markdown
AT A GLANCE
• Who: [Role]
• When: [Trigger in plain English]
• Outcome: [What "done" looks like in one line]
• Time: [Rough read or execution time if known]
• Questions: Escalate to Gabriel
```

Pull `When` from Trigger / When To Use. Pull `Outcome` from Purpose or Outputs.

## Heading map (repo → team)

| Repo section | Team heading |
|--------------|--------------|
| Purpose | What this is for |
| When To Use / Trigger | (fold into At a glance; expand in Before you start if needed) |
| Inputs / Tools | Before you start |
| Process / Operating Content | How to do it |
| Quality Bar | Done right looks like |
| Escalation | When to get help |
| Related Docs | Related procedures |

Never publish headings: Scope, Owner, Metrics, Open Questions, Operating Content.

## How to do it — phase pattern

Group long processes into 2–5 phases. Example:

```markdown
How to do it

Phase 1 — Prep (first 30 min)
1. Review notes from yesterday.
2. Open the priority list in [tool].

Phase 2 — Work the priority list
1. ...
```

Rules:

- Max 7 numbered steps per phase; split into a new phase if longer.
- Schedule tables: summarize mode (Hunt vs Normal Day) in 2–3 bullets; do not paste 40 time rows.
- Scripts: use blockquote-style lead-in: `Say:` / `Ask:` / `Do not:`

## Callouts

Use sparingly for non-negotiables:

```markdown
▸ IMPORTANT: Do not change campaign budgets without manager approval.
▸ TIP: If they text back, call immediately.
```

## Related procedures

- Link label = human title from registry `team_title`, not filename.
- If target not published: `Title (coming soon)` — never dead link to GitHub.
- Max 6 related links; prefer same role folder first.

## Sensitive content

- Money model / pricing: overview only; no numbers; "Gabriel approves deal structure."
- Identity / doctrine: plain language; avoid internal codenames unless team already uses them.

## Footer

Single line:

`Published: YYYY-MM-DD | Owner: Setter | Ref: setter-daily-ops`

`Ref` is slug for ops tracking only — team can ignore.
