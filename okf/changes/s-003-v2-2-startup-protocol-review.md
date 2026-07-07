---
type: Session Change
mutability: append-only
timestamp: 2026-06-11
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
