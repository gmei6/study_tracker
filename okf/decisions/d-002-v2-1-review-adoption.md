---
type: Decision
mutability: append-only
timestamp: 2026-06-11
---

# D-002: Accept the first external review's recommendations (v2.1), with two corrections

Decision: accept all 14 recommendations (D1–D14) of the 2026-06-11 external architecture review,
implementing D4/D12 with lazy file creation, and apply two corrections to the review's own
proposals: (1) single-source ID counters — next-ID is derived from each domain index, never stored
twice; (2) a queue admission gate — priority alone reorders but does not cap inflow (failure
mode C2).

Rationale: the review identified 12 weaknesses and 7 failure modes, led by missing research
infrastructure, non-reviewable proof techniques, ingest friction, and uncontrolled queue inflow.
Lazy creation avoids empty-file clutter at zero migration cost while the system is empty.

Full verbatim record: [s-002](../changes/s-002-v2-1-post-review-improvements.md).
