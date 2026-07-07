---
name: session-start
description: Use when starting a new study_tracker session (study, recall, ingest, or system work) to load context and run the SYSTEM.md Session Start Protocol - due recalls first, then a study recommendation.
---

# session-start Skill Instructions

Use this skill's logic at the beginning of a new session to load project context and run the
tracker's session-start protocol before doing any work.

## Steps

1. Run `python3 .agents/skills/session-start/scripts/get_context.py` to efficiently load
   `AGENTS.md`, `okf/index.md`, `okf/status.md`, `okf/next-actions.md`, `okf/open-questions.md`,
   `DASHBOARD.md`, `review/QUEUE.md`, and `review/BLOCKERS.md` in one call. **Do not** manually
   read these files with file-viewing tools — that wastes tokens.
2. Run the **Session Start Protocol** (SYSTEM.md is authoritative):
   - Check DASHBOARD health first (🟡/🔴 indicators drive what happens next).
   - List due QUEUE rows and open BLOCKERS. Due recalls come *before* any new material —
     priority then age, cap 15. Check overflow thresholds in `review/QUEUE.md`
     (41+ due = emergency: no new material).
   - The user does recalls *from memory* before opening any concept file; on results, update
     QUEUE rows (the `Results` column is the single source of review history) and the one-line
     last-review summary in each concept/technique file.
   - Then give a **study recommendation**: largest gap between DASHBOARD Domain Mastery and
     GOALS metrics; within a domain, next concept by prereq ordering. Bias against comfortable
     domains.
3. Read further files only as the task requires: `SYSTEM.md` for protocol details (read it first
   if this is your first session in this repo), `GOALS.md` for milestone context, specific
   `okf/decisions/`/`okf/changes/` files only when the task needs structural history. Do not
   read the whole okf/ bundle or any `study_logs/` history unasked (every update is O(new
   information)).
