---
name: edit-okf
description: Use when reading, creating, or editing files within the okf/ knowledge bundle (e.g., "record an architecture change", "update okf", "make a decision") to enforce OKF structural conventions like mutability, index syncing, and changelog management.
---

# edit-okf Skill Instructions

Use this skill's logic anytime you are reading, creating, or editing files in the `okf/`
directory, to enforce the bundle's structural and mutability conventions.

**Scope reminder:** `okf/` is study_tracker's *structural/meta* memory layer — architecture
decisions, structural changes, project-level state. Study data never lives here: study sessions
go to `study_logs/` (IDs `S-YYYY-MM-DD-n`), concepts to `knowledge/`, review state to
`review/QUEUE.md`, per `SYSTEM.md`. OKF change files use the unrelated lowercase `s-NNN`
sequence — never confuse the two.

## Steps

1. **Observe Directory-Level Conventions**:
   - `okf/decisions/`: One file per architecture decision, named `d-NNN-short-slug.md`
     (sequential, never reused, never renumbered; next NNN = highest existing + 1). Frontmatter
     requires `type: Decision`, `mutability: append-only`, `timestamp` (ISO 8601 date decided),
     optional `tags`. Never edit a decision once written; instead, write a new decision that
     supersedes it, and make both files say so explicitly.
   - `okf/changes/`: One file per structural session/unit of work, named `s-NNN-short-slug.md`
     (sequential, never reused). Frontmatter requires `type: Session Change`,
     `mutability: append-only`, `timestamp`, optional `tags`. It holds the full narrative of the
     session's structural changes. (This is the successor of `docs/ARCHITECTURE_CHANGELOG.md`:
     date, reason, files affected, expected benefit — keep recording those.)
   - `okf/log.md`: Reserved changelog. One line per session, chronological (oldest first, newest
     appended at the bottom via `append_okf.py`), each linking to its `changes/s-NNN.md` file.
     Never holds full narrative text itself.

2. **Respect Mutability Frontmatter**:
   - `mutability: frozen`: Requires a decision file (`decisions/d-NNN.md`) explaining the change
     *before* editing. Then make a minimal edit and link the file to the decision (and vice
     versa). Do not silently edit frozen files.
   - `mutability: live`: Can be overwritten freely to reflect the current state — truthfully, from
     what the repo records (no fabricated data; that invariant applies here too).
   - `mutability: append-only`: Add new entries only at the bottom. **CRITICAL**: You are strictly
     forbidden from using text editing tools to directly edit append-only files (`okf/log.md`,
     `changes/`, `decisions/`). You MUST use the provided Python script to create or append:
     `python3 .agents/skills/edit-okf/scripts/append_okf.py <filepath> "<content>"` or pipe
     content into it. Never edit prior entries. The script re-locks files read-only (444) after
     each append.

3. **Keep index.md Synchronized**:
   - Every `index.md` follows the OKF spec exactly: one or more `#` section headings, each
     followed by a flat bullet list of `[Title](relative-path) - short description`. No prose
     outside the list items.
   - Update the respective `index.md` whenever a file in its directory is added, renamed, or
     removed.

4. **Maintain log.md and changes/ Pairing**:
   - When creating a `changes/s-NNN.md` file, add its corresponding one-line entry to
     `okf/log.md` in the same operation.
   - Flag and fix any mismatch (a `changes/` file missing a `log.md` entry, or vice versa).

5. **Follow the Session Workflow**:
   - **Start of session**: use the `session-start` skill (reads root `okf/index.md` and the live
     files alongside the operational session-start protocol). Read `decisions/`/`changes/` files
     only when the task actually needs that history.
   - **End of session**: use the `session-wrapup` skill (overwrite relevant `live` files; if the
     session changed the system structurally, append one `changes/s-NNN.md` + its `log.md` line
     and any new `decisions/d-NNN.md` entries; update any `index.md` that gained or lost entries).
