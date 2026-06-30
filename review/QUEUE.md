# Spaced Repetition Queue — Source of Truth for All Review State

> Ladder: 1d → 3d → 7d → 21d → 60d. Pass = advance; fail = reset to 1d (+ MISTAKES.md if root cause emerges). The `Results` column preserves the full result sequence (`F·P·P`) — review history lives HERE and only here; concept files carry a one-line last-review summary.

## Admission Gate

Enter only if (a) failed active recall, or (b) priority 1–2. Priority: **1** = interview-critical, **2** = core curriculum, **3** = enrichment (concept files only, never queued).

## Overflow Thresholds (initial values — recalibrate at first quarterly review)

| Due count | Mode |
|---|---|
| ≤ 20 | Normal operation |
| 21–40 | Pause priority-2 admissions until back ≤ 20 |
| 41+ | **QUEUE EMERGENCY** — no new admissions, no new material; clear backlog first; log the emergency in DASHBOARD § System Health |

## Due / Active

| Item | Refers to | Priority | Added | Rung | Next due | Streak | Results |
|---|---|---|---|---|---|---|---|
| L'Hôpital's rule — indeterminate forms | C-ANLY-003 | 1 | 2026-06-12 | 1d | 2026-07-01 | 0 | F·F·P·F |
| Logarithmic differentiation (technique) | T-012 | 1 | 2026-06-12 | 7d | 2026-07-07 | 2 | F·P·P |
| Logarithmic differentiation | C-ANLY-001 | 1 | 2026-06-12 | 3d | 2026-07-03 | 1 | F·P·F·P |
| $e^\pi$ vs $\pi^e$ via $f(x)=x^{1/x}$ | C-ANLY-002 | 1 | 2026-06-12 | 7d | 2026-07-06 | 2 | F·P·P |
| Trie — basic structure + addWord | C-ALGO-001 | 1 | 2026-06-13 | 7d | 2026-07-06 | 2 | P·P |
| Trie wildcard search — recursive_search | C-ALGO-002 | 1 | 2026-06-13 | 1d | 2026-07-01 | 0 | F·F·F·F |
| Index vs. slice in recursive traversal | T-014 | 1 | 2026-06-13 | 3d | 2026-07-03 | 1 | F·F·F·P |
| ∫ln(x) dx — IBP setup and result | C-ANLY-004 | 1 | 2026-06-14 | 7d | 2026-07-07 | 2 | P·P |
| ∫sec(x) dx — substitution + partial fractions | C-ANLY-005 | 1 | 2026-06-14 | 1d | 2026-07-01 | 0 | F·F·F |
| Integration by parts (IBP) | T-016 | 1 | 2026-06-14 | 1d | 2026-07-01 | 0 | P·F |
| Partial fraction decomposition | T-017 | 1 | 2026-06-14 | 1d | 2026-07-01 | 0 | F·F·F |
| Ordered set k-tuple distribution | C-PROB-001 | 1 | 2026-06-14 | 1d | 2026-07-01 | 0 | F·F·F |
| Element-by-element independent counting | T-015 | 1 | 2026-06-14 | 1d | 2026-07-03 | 1 | F·F·P |
| Word Search II — Trie + Grid DFS | C-ALGO-003 | 1 | 2026-06-14 | 3d | 2026-07-03 | 1 | F·F·P |
| Grid DFS with backtracking | T-018 | 1 | 2026-06-14 | 1d | 2026-07-01 | 0 | F·F·F |
| Conjugate division — $(a+bi)^{-1}$ to standard form | T-019 | 1 | 2026-06-14 | 1d | 2026-07-01 | 0 | F·F·F |
| Complex root-finding — solve $(a+bi)^n = z$ componentwise | T-020 | 1 | 2026-06-14 | 3d | 2026-07-03 | 1 | F·F·P |
| Complex numbers — multiplicative inverse & associativity proof | C-LINALG-001 | 1 | 2026-06-14 | 1d | 2026-06-30 | 0 | F·F |
| Lists and $\mathbb{F}^n$ — definition, integer dimension | C-LINALG-002 | 1 | 2026-06-14 | 1d | 2026-06-30 | 0 | F·F |

## Graduated (≥ 60d; never deleted)

| Item | Refers to | Graduated on | Results |
|---|---|---|---|

## Protocol

- Session start: pull `Next due ≤ today`, sorted by priority then age. Recall *before* opening the concept file. Cap 15/session; never skip days.
- Per review: update the queue row (rung, due, streak, append to Results) + the concept file's last-review line. Two touches, one history.
