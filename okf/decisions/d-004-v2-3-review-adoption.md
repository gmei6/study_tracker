---
type: Decision
mutability: append-only
timestamp: 2026-06-11
---

# D-004: Accept the third external review's recommendations (v2.3); D2/D5 modified; pace floors set

Decision: accept all 6 recommendations of the third external review, two with modifications:
(1) D2 modified — technique pre-seeding is implemented as ID reservations in
`knowledge/techniques/INDEX_TECH.md` (T-001…T-011) rather than pre-seeded skeleton files, because
full skeletons would reverse v2.1's lazy-creation rule and put LLM-drafted content with false
mastery claims and no real S-ID into the knowledge layer; files are still created at the first
real encounter. (2) D5 modified — habit tracking is a "sessions in last 7 days" health indicator
plus a weekly pace streak assessed at weekly snapshots, not the review's harsher
"reset streak on any gap > 1 day". Pace floors set by Gary: ≥ 10 h/week and ≥ 5 sessions/week,
as independent floors (volume + frequency).

Rationale: the review identified 6 weaknesses and 6 failure modes; the modifications keep the
no-fabricated-data and lazy-creation invariants intact while still making the technique layer
linkable from session 1 and pace slippage diagnosable within 7 days.

Full verbatim record: [s-004](../changes/s-004-v2-3-third-external-review.md).
