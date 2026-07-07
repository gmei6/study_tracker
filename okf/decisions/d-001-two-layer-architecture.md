---
type: Decision
mutability: append-only
timestamp: 2026-06-11
---

# D-001: Adopt the v2.0 two-layer knowledge architecture

Decision: replace the v1 scheme (master hub `STUDY_MASTER.md` + 5 chronological logs) with a
two-layer architecture — an append-only event layer (`study_logs/`) separated from an editable
knowledge layer (`knowledge/`), with a spaced-repetition review loop (`review/QUEUE.md`), mistake
recurrence tracking with auto-escalation to blockers, an interview-readiness layer, and a goal
layer (`GOALS.md`) tying daily work to the Dec 2027 outcomes. Redesign approved by Gary on
2026-06-11.

Rationale: v1 conflated events with durable knowledge, had no retrieval layer, no functioning
review system, and an overwrite-only dashboard that destroyed trajectory data. The redesign gives
O(1) retrieval via stable IDs, a functioning retention loop, and longitudinal history that is
appended, not overwritten.

Full verbatim record (files affected, expected benefit, reversibility, and the preserved v1
`STUDY_MASTER.md` content): [s-001](../changes/s-001-v2-0-two-layer-architecture.md).
