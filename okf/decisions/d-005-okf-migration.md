---
type: Decision
mutability: append-only
timestamp: 2026-07-06
---

# D-005: Migrate structural memory into the okf/ knowledge bundle

Decision: migrate the repo's structural memory — `docs/ARCHITECTURE_CHANGELOG.md` (append-only
structural changelog, v2.0 → current) — into an OKF-style `okf/` knowledge bundle, mirroring the
`project_template` reference implementation, with zero information loss; then retire the changelog
to a short redirect stub (not deleted). Scaffold the OKF live files (`status.md`,
`next-actions.md`, `open-questions.md`, `identity.md`, `north-star.md`, `roadmap.md`, `risks.md`)
populated from what the repo already records, and add project skills (`edit-okf`, `session-start`,
`session-wrapup`) that enforce the bundle's conventions.

Scope boundary: `okf/` is the project's structural/meta memory layer only. It points at the
operational docs; it does not replace them. SYSTEM.md, README.md, GOALS.md, DASHBOARD.md and all
study data (study_logs/, knowledge/, review/, interview/, research/) stay where they are and
remain the operational system. Study sessions keep their `S-YYYY-MM-DD-n` IDs in `study_logs/`;
okf change files use the unrelated `s-NNN` sequence.

Rationale: one file per decision/change with explicit `mutability` frontmatter
(`frozen`/`live`/`append-only`) makes the append-only record tamper-evident (files locked
read-only, appended only via `append_okf.py`); `log.md` gives a one-line-per-session history
instead of an ever-growing narrative file; session context loads through the `session-start`
skill; going forward, structural changes are recorded as a paired `changes/s-NNN.md` +
`log.md` line (plus a `decisions/d-NNN.md` when a convention changes), preserving the changelog's
original contract.

Affects: `docs/ARCHITECTURE_CHANGELOG.md` (migrated → redirect stub), SYSTEM.md/README.md/
DASHBOARD.md/docs/USAGE.md (pointer updates), `.agents/skills/` and `.claude/skills` (created),
`AGENTS.md`/`CLAUDE.md` (created). Full record and entry-by-entry mapping:
[s-010](../changes/s-010-okf-migration.md).
