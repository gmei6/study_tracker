---
type: Session Change
mutability: append-only
timestamp: 2026-06-11
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
