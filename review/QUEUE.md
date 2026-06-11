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

*Empty — populated from first session ingest.*

## Graduated (≥ 60d; never deleted)

| Item | Refers to | Graduated on | Results |
|---|---|---|---|

## Protocol

- Session start: pull `Next due ≤ today`, sorted by priority then age. Recall *before* opening the concept file. Cap 15/session; never skip days.
- Per review: update the queue row (rung, due, streak, append to Results) + the concept file's last-review line. Two touches, one history.
