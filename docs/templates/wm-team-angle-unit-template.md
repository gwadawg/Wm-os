---
title: WM Team Angle Unit Template
domain: templates
owner: operations
status: active
last_updated: 2026-05-28
review_cycle: quarterly
---

# WM Team Angle Unit Template

**Use when:** Team drafts that are script/angle libraries (e.g. LinkedIn copy-angles).  
**Registry:** Set `team_doc_type: angle_library` on the publish registry row and in `*.team.meta.yaml`.

Every angle is one repeating unit. Do not improvise section order or labels per angle.

## Rigid unit skeleton (copy per angle)

```markdown
## Angle {N} — {Short title}

**Signal:**

{One short paragraph: what you see on profile/feed that qualifies this angle.}

**{Variant name} opener**  
*(Repeat this opener block for each voice variant: Professional, Peer LO, Casual, etc.)*

**✉️ COPY & PASTE**

```
{Paste-ready message. Brackets for manual fill only.}
```

**Avoid:**

{1–3 bullets: what not to say or do in message 1.}

**Note for Gabriel handoff:**  
*(Optional — only when handoff context matters. Omit line entirely if N/A.)*
```

### Opener block rules

- Every pasteable message uses **`✉️ COPY & PASTE`** immediately above a fenced code block.
- Never put paste text in a table cell, plain paragraph, or bullet without the banner.
- Variant label is always `**{Name} opener**` on its own line (not a table row).

### Shared sections (outside angles)

Keep non-angle sections in doc-level structure only:

| Section | Placement |
|---------|-----------|
| Cover stack | Top (WAIZ MEDIA → title → purpose → internal-use) |
| `# 1. Overview` + `📌 NORTH STAR` | Once |
| Quick Start, Voice Variants, Connect/Bump/Ghost | Before angle index |
| `## 3. Angle Index` table | Once, before first angle |
| Footer | **Once**, last line of doc |

## FORBIDDEN (do not ship)

| Failure mode | Why it breaks the doc |
|--------------|------------------------|
| Angle missing **Signal:** | Operators cannot qualify when to use it |
| Paste without **✉️ COPY & PASTE** + fence | Inconsistent blocks in Google Docs |
| Some angles have **Avoid:**, some do not | Training drift; looks unfinished |
| Paste living in table cells | Unstyled, hard to copy on mobile |
| Second `📌 NORTH STAR` or duplicate footer | Looks like unreviewed one-pass generation |
| Renaming labels (`Copy block`, `Template`, `Example only`) | Parser and team muscle memory break |
| Pitch, pricing, or “what we do” in message 1 | Violates outreach doctrine |
| Generic praise (“great post”, “loved your content”) | Fails signal-specific standard |

## Angle index table (required once)

| # | Bucket | Track | Signal |
| --- | --- | --- | --- |
| 1 | … | A, B | … |

Angle sections in the body should follow index order (`## Angle 1`, then `## Angle 2`, …). Reordering only after updating the index table.

## Related

- [wm-team-doc-format-spec.md](wm-team-doc-format-spec.md) — global WM layout
- [wm-team-doc-review-checklist.md](wm-team-doc-review-checklist.md) — second-pass review before approve/publish
- Canonical source example: [copy-angles.team.md](../team-drafts/copy-angles.team.md) (normalize to this template before publish)
