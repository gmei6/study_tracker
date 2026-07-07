---
type: Session Change
mutability: append-only
timestamp: 2026-06-11
---

## 2026-06-11 — docs/ folder created; D15 completed

**Reason:** Repo cleanup (Gary's request): reference documentation separated from operational state. `docs/` holds files consulted occasionally (usage playbook, this changelog); root keeps `README.md` (GitHub convention), `SYSTEM.md` (every-session entry point), and all operational files — moving those was considered and rejected (DASHBOARD/GOALS/queue/logs are working state, not docs). D15 finally completed: deprecated `STUDY_MASTER.md` pointer deleted — its v1 content remains preserved verbatim in Appendix A below and in git history.

**Files affected:** Moved `USAGE.md` → `docs/USAGE.md` and `ARCHITECTURE_CHANGELOG.md` → `docs/ARCHITECTURE_CHANGELOG.md`; deleted `STUDY_MASTER.md`; path references updated in `SYSTEM.md`, `DASHBOARD.md`, `README.md`. Historical entries above retain original paths (append-only record — not rewritten).

**Reversibility:** Move files back to root; restore the pointer from git history or Appendix A.
