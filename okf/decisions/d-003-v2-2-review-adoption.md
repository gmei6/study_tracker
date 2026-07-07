---
type: Decision
mutability: append-only
timestamp: 2026-06-11
---

# D-003: Accept the second external review's recommendations (v2.2), with corrections; D15 deferred

Decision: implement 14 of 15 recommendations of the second external review (the v2.1 audit), with
corrections: (1) the worked ingest example is synthetic, embedded in SYSTEM.md, and consumes no IDs
— creating real concept files with fabricated mastery data would corrupt the knowledge base;
(2) review tracking becomes single-source by adding a `Results` sequence column to
`review/QUEUE.md` (the review's own single-write design would have silently destroyed review
history); (3) `knowledge/CONNECTIONS.md` is created immediately rather than at 100 concepts —
capture cross-domain synthesis from concept #1, never retrofit. D15 (delete the deprecated
`STUDY_MASTER.md` pointer) deferred for lack of shell access.

Rationale: the review identified 15 weaknesses, led by cold-start friction (no worked ingest
example) and a dual-write consistency flaw introduced in v2.1.

Full verbatim record: [s-003](../changes/s-003-v2-2-startup-protocol-review.md).
