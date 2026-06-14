# Subject Log: Leetcode

> **Scope:** Python/C++ algorithms, applied logic, and exact failure points.
> **Protocol:** APPEND-ONLY. Add new entries to the bottom via file-system tools. Never delete or summarize past entries.

---

*Log initialized: 2026-06-11. Session entries are appended below in chronological order.*

---

## S-2026-06-14-3 — LeetCode 212: Word Search II (Trie + Grid DFS)
- Duration: 54 | Effort: 4
- Source: Leetcode — 212. Word Search II

[INTERVIEW] Given m×n board and list of words, return all words constructible from adjacent cells (H/V only, no reuse).

Attempted brute-force DFS per word. Bugs:

1. Grid boundary check: failed to check `0 <= i < m and 0 <= j < n` explicitly — Python's negative indexing means `board[-1]` wraps instead of raising IndexError [STRUGGLE] (M-019).
2. `enumerate[board]` syntax error — used [] for function call, causing TypeError (tuples as indices) [STRUGGLE] (M-020). Correct: `enumerate(board)`.
3. DFS structure wrong: recursed on same cell (i, j) instead of all 4 neighbors (i±1, j±1) [STRUGGLE] (M-021). Adjacent cells are the recursive targets, not the current cell.
4. Method call inside class missing `self.` prefix [STRUGGLE] (M-022).
5. Mutated board with '#' to mark visited but never restored after recursion — no backtracking [STRUGGLE] (M-023). Correct: set `board[i][j] = '#'`, recurse, then `board[i][j] = tmp` (restore).
6. Struggled to identify Trie as the optimization for TLE: per-word DFS is O(words × cells × 4^L); with Trie, all words are searched in a single DFS pass sharing prefix work [STRUGGLE] (M-024).

Clean grid DFS backtracking pattern (T-018) and Trie-integrated solution (C-ALGO-003) explained, not yet reproduced [NEEDS_RECALL].

---

## S-2026-06-13-1 — LeetCode 211: Trie Wildcard Search
- Duration: 47 | Effort: 4
- Source: Leetcode — 211. Design Add and Search Words Data Structure

Recognized immediately as a Trie variant (similar to LC 208 Implement Trie, done prior to tracker). addWord = standard insert — implemented cleanly with no issues.

Search twist: '.' can match any char. Approach: recursive `search(word, index, curr)` — at '.', loop all children and recurse into each; any True → return True. At letter, advance curr normally. Return `curr.word` when index reaches `len(word)`. [INSIGHT]

Bugs encountered [STRUGGLE]:
1. Python string slicing direction backwards — thought `temp[:3]` gets last 3 chars; it's first 3.
2. Non-dot else branch: updated curr + index, then fell through to `return True` without checking remaining chars. Explained, not reproduced. [NEEDS_RECALL]
3. Index + slice mismatch: passed `word[plus_one:]` (shorter string) but used `plus_one` as index into it — index past end. Should keep original word + advance index, or slice + reset index to 0. Explained, not reproduced. [NEEDS_RECALL]
4. Early `return True` at `index == len(word)-1` for dot-as-last-char skips checking `curr.word` — incorrectly matches incomplete paths. Explained, not reproduced. [NEEDS_RECALL]

Gave up; shown clean solution. Key takeaway not yet internalized: when mixing iteration and recursion on string traversal, pick one — advance an index, or slice the string — never both simultaneously. [NEEDS_RECALL]
