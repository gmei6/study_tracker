# T-018 — Grid DFS with Backtracking

- **Mastery:** 1/5 (pattern explained; not yet reproduced independently)
- **Created:** S-2026-06-14-3 | **Last touched:** S-2026-06-14-3

## Prerequisites

- Basic DFS / recursion
- Python list indexing and mutation
- Trie structure (C-ALGO-001) when used with multi-word search

## When to Reach For It

Any grid traversal problem requiring path exploration with state restoration: word search, island counting, path finding. Key signal: "adjacent cells" + "same cell may not be used more than once."

## The Pattern

```python
def dfs(board, i, j, ...):
    # 1. Boundary + validity check (MUST be explicit — no negative index tricks)
    if i < 0 or i >= m or j < 0 or j >= n:
        return
    if board[i][j] == '#':   # already visited this path
        return

    # 2. Mark visited
    tmp = board[i][j]
    board[i][j] = '#'

    # 3. Recurse on all 4 neighbors (not the current cell)
    for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
        dfs(board, i + di, j + dj, ...)

    # 4. Backtrack — ALWAYS restore before returning
    board[i][j] = tmp
```

## Critical Rules

- **Explicit bounds:** `0 <= i < m and 0 <= j < n` — never rely on IndexError because Python's negative indices wrap silently (`board[-1]` is valid).
- **Neighbors, not self:** recurse on `(i+di, j+dj)`, not on `(i, j)` again.
- **Backtrack:** restore `board[i][j] = tmp` after the recursive block, every time. Permanent mutation corrupts other DFS paths.
- **`self.` in class:** method calls within a class require `self.dfs(...)`, not bare `dfs(...)`.

## Common Failure Modes

- Missing or implicit boundary check → wrapping / wrong-cell access (M-019)
- `enumerate[board]` → TypeError; must use `enumerate(board)` (M-020)
- Recurring on `(i, j)` instead of neighbors (M-021)
- Missing `self.` for recursive call inside class method (M-022)
- Forgetting backtrack restore → permanent '#' corruption (M-023)

## Used In

- C-ALGO-003 : Word Search II (LC 212)

## Review

- **Last review:** 2026-06-29 — fail (unmark timing wrong — "after moving to next node" not "after recursive call returns"; why-unmark explanation too vague). *(Full history: review/QUEUE.md Results column.)*
