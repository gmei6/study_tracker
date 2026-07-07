# AGENTS.md — study_tracker agent memory

Project-intrinsic knowledge for any AI agent working in this repo. `CLAUDE.md` is a symlink to
this file. **`SYSTEM.md` is the operating manual — read it first in any new session**; this file
only records what an agent needs beyond it.

## What this repo is

Gary's two-layer personal knowledge system for quant prep (QR roles / MFE / Quant PhD, Dec 2027).
Not a software project: there is no build, no tests, no CI — the "code" is markdown protocols and
the data is real study history. Correctness here means protocol fidelity and data integrity.

## Layer map (who owns what)

- **Operational system** (SYSTEM.md, README.md, GOALS.md, DASHBOARD.md, study_logs/, knowledge/,
  review/, interview/, research/, docs/) — the tracker itself. Follow SYSTEM.md's ingest and
  review protocols exactly.
- **Structural memory** (`okf/`) — architecture decisions (`d-NNN`), structural changes (`s-NNN`),
  one-line session log, and live project-level state. Successor of
  `docs/ARCHITECTURE_CHANGELOG.md` (now a redirect stub). Edit only via the `edit-okf` skill
  conventions; append-only files are locked 444 and appended with
  `.agents/skills/edit-okf/scripts/append_okf.py`.
- **Skills** (`.agents/skills/`; `.claude/skills` symlinks to it): `session-start`,
  `session-wrapup`, `edit-okf`. Claude Code loads these; other LLMs use the raw prompts kept in
  `docs/USAGE.md` (the scribe workflow there deliberately serves non-Claude AIs).

## Sharp edges

- **Two unrelated ID schemes look alike:** `S-YYYY-MM-DD-n` = study session in `study_logs/`
  (SYSTEM.md scheme); lowercase `s-NNN` = okf structural change file. Never mix them.
- **Append-only is sacred:** `study_logs/` entries, `review/MISTAKES.md` rows, `okf/log.md`,
  `okf/changes/`, `okf/decisions/`. Never edit or delete existing entries; status fields change,
  history does not.
- **No fabricated data:** metrics reflect logged work only; synthetic examples must be marked
  synthetic and consume no IDs (SYSTEM.md § Invariants). An LLM's own explanation must never be
  recorded as the user's mastery.
- **Single-source rules:** review history lives only in `review/QUEUE.md` (`Results` column);
  counters/next-IDs are derived (highest existing + 1), never stored.
- **Structural changes** (anything the old changelog would have recorded) require an
  `okf/changes/s-NNN.md` + `okf/log.md` line, and a `okf/decisions/d-NNN.md` when direction
  changes; commit message `arch: {what}`. Ingest commits use `S-YYYY-MM-DD-n: {topic}`.
- `docs/textbook/` (singular) contains two deliberate redirect stubs to `docs/textbooks/`
  (plural) — documented in okf/changes/s-009; do not "clean them up" without a decision.
- Textbook MD conversions live in folder-per-book form under `docs/textbooks/md_version/` with
  `_meta.json` ToC data; see its `INDEX.md`.
