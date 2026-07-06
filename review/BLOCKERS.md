# Blocker Database

> Open conceptual obstacles. A blocker = something actively preventing progress (repeated mistake ≥ 3, a `[STRUGGLE]` with no resolution path, a prerequisite gap). Never deleted — status moves open → resolved, with the resolution recorded.

## Open

| ID | Opened | Domain | Description | Origin (M-/S- ID) | Unblock plan |
|---|---|---|---|---|---|

## Resolved

| ID | Opened | Resolved | Description | What resolved it |
|---|---|---|---|---|
| B-001 | 2026-06-30 | 2026-07-05 | Early return True in wildcard search base case (index == len(word)-1) skips complete-word check; mixing iterative while-loop with recursion | Implemented clean recursive approach without while loop. Base case correctly hits `index == len(word)` and checks `isWord`. |
