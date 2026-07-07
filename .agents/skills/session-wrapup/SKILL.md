---
name: session-wrapup
description: Use when ending a study_tracker session - after an ingest, review, or system change - to run the ingest protocol, update OKF live state, record structural changes, and commit.
---

# session-wrapup Skill Instructions

Use this skill's logic at the end of a session so nothing the session produced is lost and the
repo is committed in a consistent state.

## Steps

1. **Ingest any un-ingested study work** per SYSTEM.md (authoritative; ask before writing if
   anything is ambiguous):
   - **Full Ingest** (default): append the log entry to the source's `study_logs/LOG_*.md`
     (append-only — never edit existing entries); extract concepts/techniques into `knowledge/`
     with typed edges (cross-domain `relates` edges also into `knowledge/CONNECTIONS.md`);
     extract mistakes into `review/MISTAKES.md` (same root cause ⇒ increment recurrence; ≥ 3 ⇒
     escalate to `review/BLOCKERS.md`); apply queue admissions (gate: failed recall OR priority
     1–2; respect overflow thresholds); register interview problems; update the domain index;
     update `DASHBOARD.md` (status, Domain Mastery, System Health) and `GOALS.md` Progress
     Metrics for touched domains.
   - **Quick Ingest** (time-pressed): log entry with `[PENDING_EXTRACT]`, bump DASHBOARD session
     count + health, add to DASHBOARD § Pending Extractions.
   - Weekly boundary ⇒ append a snapshot to `review/SNAPSHOTS.md` and update the DASHBOARD
     pointer.
2. **Update OKF live files** to stay truthful: `okf/status.md`, `okf/next-actions.md`,
   `okf/open-questions.md` (and `okf/risks.md`/`okf/roadmap.md` if the session moved them).
   Routine study sessions usually change nothing here — okf/ is structural memory; do not mirror
   study content into it.
3. **If the session changed the system structurally** (protocols, layout, templates, thresholds,
   docs architecture — anything the old ARCHITECTURE_CHANGELOG would have recorded):
   - Append one `okf/changes/s-NNN-short-slug.md` (next sequential NNN) with the narrative:
     date, reason, files affected, expected benefit, reversibility. Frontmatter
     `type: Session Change`, `mutability: append-only`, `timestamp`.
   - Add its one-line entry to `okf/log.md` (newest first).
   - If a direction-setting decision was made, also append `okf/decisions/d-NNN-short-slug.md`
     and link it from the affected files.
   - **CRITICAL**: never use text-editing tools on append-only files; create/append them only
     via `python3 .agents/skills/edit-okf/scripts/append_okf.py <filepath>` (arg or stdin).
     Update `okf/changes/index.md` / `okf/decisions/index.md` (these are live).
4. **Check integrity before committing**: review history only in `review/QUEUE.md`; counters
   derived, never stored; no fabricated data or metrics; every `changes/` file has its `log.md`
   line.
5. **Commit** (per `docs/USAGE.md` § 3): `git add -A && git commit && git push`. Message
   `S-YYYY-MM-DD-n: {topic}` for an ingest, `arch: {what}` for a structural change. Never
   force-push. A session that isn't committed isn't safe.
