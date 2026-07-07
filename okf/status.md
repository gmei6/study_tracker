---
mutability: live
type: concept
---

# Status

Structural state of the system. Operational status (health lights, mastery, queue, resume
positions) lives in `DASHBOARD.md` and is not duplicated here.

- **Architecture:** v2.4 — two-layer system (v2.0) hardened by three external reviews
  (v2.1–v2.3), plus the okf/ structural-memory bundle and project skills (s-010, 2026-07-06).
- **Structural memory:** migrated from `docs/ARCHITECTURE_CHANGELOG.md` (now a redirect stub)
  into this bundle with zero information loss — decisions d-001–d-005, changes s-001–s-010.
- **Skills:** `.agents/skills/` — `edit-okf`, `session-start`, `session-wrapup` (Claude Code
  loads them via the `.claude/skills` symlink; other LLMs use the raw prompts in `docs/USAGE.md`).
- **System in active use** (per DASHBOARD, 2026-07-06): 10 sessions logged across 5 source logs;
  11 concepts, 9 techniques, 49 mistakes, 0 open blockers; review queue populated and being
  worked; no weekly snapshot appended yet.
