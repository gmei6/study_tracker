# Architecture Changelog

> Every structural modification to the Quant Tracker is recorded here: date, reason, files affected, expected benefit. Append-only.

---

## 2026-06-11 — v2.0: Two-Layer Knowledge Architecture

**Reason:** v1 (master hub + 5 chronological logs) conflated events with durable knowledge, had no retrieval layer, no functioning review system, and an overwrite-only dashboard that destroyed trajectory data. Redesign approved by Gary on 2026-06-11. Full review in session transcript; summary below.

**Files affected:**
- Created: `DASHBOARD.md`, `GOALS.md`, `SYSTEM.md`, `ARCHITECTURE_CHANGELOG.md`
- Created: `knowledge/INDEX.md`, `knowledge/_TEMPLATE_concept.md`
- Created: `review/QUEUE.md`, `review/MISTAKES.md`, `review/BLOCKERS.md`
- Created: `interview/QUESTION_BANK.md`, `interview/DRILL_RESULTS.md`
- Modified: `STUDY_MASTER.md` → deprecated pointer; its full v1 content preserved verbatim in `DASHBOARD.md` § History
- Unchanged: all 5 logs in `study_logs/` (append-only protocol retained; directory name kept — rename to `logs/` deferred, cosmetic only)

**Expected benefit:**
- O(1) retrieval via stable IDs + `knowledge/INDEX.md` instead of log scans
- Functioning spaced-repetition loop (`review/QUEUE.md`) instead of dead tags
- Mistake recurrence tracking with auto-escalation to blockers
- Interview-readiness layer (question bank + timed drill calibration)
- Longitudinal history preserved (dashboard snapshots appended, not overwritten)
- Goal layer (`GOALS.md`) tying daily work to Dec 2027 outcomes

**Reversibility:** All v1 content preserved verbatim. Reverting = restoring `STUDY_MASTER.md` from Appendix A below and deleting new files.

---

## 2026-06-11 — v2.1: Post-Review Improvements (D1–D14)

**Reason:** External architecture review (2026-06-11) identified 12 weaknesses and 7 failure modes. All 14 recommendations accepted; D4/D12 implemented with lazy file creation (avoids empty-file clutter; zero migration cost since system is empty), and two corrections applied: single-source ID counters (domain indexes only, next-ID derived not stored) and a queue admission gate (priority alone reorders but doesn't cap inflow — failure mode C2).

**Files affected:**
- Modified: `SYSTEM.md` (v2.1: log entry format w/ duration & effort, T- prefix, quick ingest, queue priority + admission gate, connection edge types, periodic reviews, study recommendation protocol, per-domain index rule)
- Modified: `DASHBOARD.md` (v1 history moved here → Appendix A; added Domain Mastery + Pending Extractions sections)
- Modified: `knowledge/INDEX.md` (now domain registry only; added STAT, OPT, NUMER, FINM; per-domain indexes created lazily; next-ID derived from domain index)
- Modified: `knowledge/_TEMPLATE_concept.md` (connection edge types: prereq / extends / relates)
- Modified: `review/QUEUE.md` (priority column, admission gate)
- Modified: `interview/QUESTION_BANK.md` (converted to registry; per-category files in interview/questions/ created lazily)
- Modified: `GOALS.md` (milestone review log)
- Created: `knowledge/techniques/_TEMPLATE_technique.md`, `knowledge/techniques/INDEX_TECH.md`
- Created: `research/READING_LOG.md`, `research/IDEAS.md`, `research/CONTACTS.md`
- Created: `interview/FIRM_PROFILES.md`

**Expected benefit:** Research readiness gets infrastructure (worst gap, C4); proof techniques become reviewable first-class entities (objectives #4–5); ingest overhead gets a low-friction path (C7); review queue gets prioritization + inflow control (C2); all anticipated domains have a home; index and question bank scale via per-domain/per-category files.

**Reversibility:** All changes additive or relocations with content preserved. Rollback = re-merge split files, delete new directories, restore v1 history block to DASHBOARD.

---

## 2026-06-11 — v2.2: Startup-Protocol Review Improvements (D1–D14; D15 deferred)

**Reason:** Second external review (v2.1 audit) identified 15 weaknesses, led by cold-start friction (no worked ingest example) and a dual-write consistency flaw in review tracking introduced in v2.1. 14/15 recommendations implemented with corrections: (1) worked example is **synthetic**, embedded in SYSTEM.md, consuming no IDs — creating real concept files with fabricated mastery data would corrupt the knowledge base; (2) review's single-write design would have silently destroyed review history (QUEUE rows update in place) — fixed by adding a `Results` sequence column to QUEUE, making it the true single source; (3) CONNECTIONS.md created now rather than at 100 concepts (capture from concept #1, never retrofit); (4) D15 (delete STUDY_MASTER.md pointer) deferred — shell unavailable; harmless 10-line file.

**Files affected:**
- Modified: `SYSTEM.md` (v2.2: worked example, domains-vs-sources section, single-write review protocol, overflow thresholds reference, maintenance triggers, version control conventions)
- Modified: `review/QUEUE.md` (overflow thresholds 20/40/41+, Results column, source-of-truth declaration)
- Modified: `knowledge/_TEMPLATE_concept.md` (Type field; Review History table → last-review line)
- Modified: `knowledge/techniques/_TEMPLATE_technique.md` (Prerequisites section; same review change)
- Modified: `DASHBOARD.md` (System Health panel w/ 🟢🟡🔴 thresholds; "Domain Status" → "Source Log Status"; snapshots → pointer)
- Modified: `GOALS.md` (Progress Metrics table; Review Schedule with concrete dates)
- Created: `knowledge/CONNECTIONS.md`, `review/SNAPSHOTS.md`, `.gitignore`

**Expected benefit:** First real ingest is pattern-matching, not protocol interpretation (C1, the fatal risk); review history desync impossible (C4); queue overflow has a decision tree (C2); dashboard readability bounded (C3); usage gaps visible (C5); milestones measurable (C6); synthesis captured from day one (C7).

**Reversibility:** All additive or content-preserving. Template Review History tables removed before any data existed in them — zero loss. Rollback per section via this entry.

**Outstanding:** D15 deletion pending shell access; `git init` is a manual one-time step (folder is not yet a git repo).

---

## 2026-06-11 — v2.3: Third External Review (D1–D6; D2/D5 modified)

**Reason:** Third external architecture review identified 6 weaknesses and 6 failure modes. All 6 recommendations accepted by Gary, two with modifications: (1) **D2 modified** — pre-seeding 10 full T-skeleton files would reverse v2.1's lazy-creation rule and put LLM-drafted content (with a false "seen once" mastery and no real S-ID) into the knowledge layer; implemented instead as **ID reservations** in INDEX_TECH.md (T-001…T-011, covering all 11 listed candidates) — linkable from session 1, files still created at first real encounter. (2) **D5 modified** — review's "reset streak on any gap > 1 day" is harsher than the system's own health thresholds; implemented as "sessions in last 7 days" health indicator + weekly pace streak assessed at weekly snapshots. Pace floors set by Gary: **≥ 10 h/week, ≥ 5 sessions/week** (independent floors: volume + frequency).

**Files affected:**
- Modified: `DASHBOARD.md` (D1: "Current position" column in Source Log Status; D5: "Sessions in last 7 days" health row + 🟡 legend extension; version bump)
- Modified: `GOALS.md` (D4/D5: weekly hours, sessions/week, pace-streak rows in Progress Metrics + floors note)
- Modified: `research/CONTACTS.md` (D3: explicit `next action date` column + overdue rule)
- Modified: `knowledge/techniques/INDEX_TECH.md` (D2-modified: T-001…T-011 reserved; next ID = 012)

**Expected benefit:** O(1) session resume at any log size (D1); technique layer linkable from first proof session without synthetic content (D2/C5); contacts file self-auditing on the longest-lead-time item — letters by Fall 2027 (D3/C2); pace slippage diagnosable in 7 days instead of 90 (D4); habit decay visible before queue emergencies (D5/C6).

**Reversibility:** All additive — rollback = delete added rows/columns per this entry.

**Outstanding:** D6 (`git init`) still blocked — sandbox shell cannot mount the folder. **Manual step for Gary:** `cd ~/Downloads/QUANT_TRACKER && git init && git add -A && git commit -m "arch: v2.3 initialized"`. D15 (delete STUDY_MASTER.md pointer) remains deferred for the same reason.

---

## 2026-06-11 — README.md added

**Reason:** Repo now synced to GitHub (github.com/gmei6/QUANT_TRACKER); README provides the entry-point overview and a Mermaid data-flow diagram (renders natively on GitHub). Documentation only — no protocol or structural changes. SYSTEM.md remains the operating manual.

**Files affected:** Created `README.md`.

**Reversibility:** Delete the file.

---

## 2026-06-11 — USAGE.md added; root folder renamed to study_tracker

**Reason:** USAGE.md is a copy-paste playbook of exact prompts (session start, ingest, reviews, edge cases) and git commands. Documentation only; protocols unchanged — SYSTEM.md remains authoritative. Separately, Gary renamed the root folder QUANT_TRACKER → study_tracker (cosmetic; git history and GitHub remote unaffected — remote repo name may still be QUANT_TRACKER).

**Files affected:** Created `USAGE.md`; `README.md` (title updated, Usage section links to USAGE.md).

**Reversibility:** Delete the file, revert README lines, rename folder back.

---

## 2026-06-11 — docs/ folder created; D15 completed

**Reason:** Repo cleanup (Gary's request): reference documentation separated from operational state. `docs/` holds files consulted occasionally (usage playbook, this changelog); root keeps `README.md` (GitHub convention), `SYSTEM.md` (every-session entry point), and all operational files — moving those was considered and rejected (DASHBOARD/GOALS/queue/logs are working state, not docs). D15 finally completed: deprecated `STUDY_MASTER.md` pointer deleted — its v1 content remains preserved verbatim in Appendix A below and in git history.

**Files affected:** Moved `USAGE.md` → `docs/USAGE.md` and `ARCHITECTURE_CHANGELOG.md` → `docs/ARCHITECTURE_CHANGELOG.md`; deleted `STUDY_MASTER.md`; path references updated in `SYSTEM.md`, `DASHBOARD.md`, `README.md`. Historical entries above retain original paths (append-only record — not rewritten).

**Reversibility:** Move files back to root; restore the pointer from git history or Appendix A.

---

## Appendix A — v1 STUDY_MASTER.md content (preserved verbatim)

# Quantitative Study Master Hub

> **Target:** Quantitative Research / MFE / Quant PhD Fall 2027
> **Protocol:** Overwrite this file during updates to reflect real-time status.

- **Last Updated:** 2026-06-11 (Session 00 — System Initialization)
- **Current Phase:** Foundations & Core Theory

---

## 🟢 Global Overview
Logging system initialized: master hub is live and all five subject logs are created and append-ready. No study sessions recorded yet — baselines and momentum will be established from the first set of raw session notes.

## 📊 Domain Status

* **Leetcode:** Not Started — log initialized
* **Linear Algebra:** Not Started — log initialized
* **Stochastics:** Not Started — log initialized
* **Green Book:** Not Started — log initialized
* **Putnam:** Not Started — log initialized

## 🛑 Active Blockers & Concept Gaps
*(Auto-aggregated from `[STRUGGLE]` and `[NEEDS_RECALL]` tags in the subject logs.)*

* None yet.

## 🎯 Next Session Focus

* 1. Submit first raw session notes to seed a baseline entry in at least one domain.
* 2. Confirm the primary source per domain (Leetcode problem list, LinAlg text, stochastics notes, Green Book edition, Putnam archive).
