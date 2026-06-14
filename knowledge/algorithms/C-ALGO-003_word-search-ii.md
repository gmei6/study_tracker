# C-ALGO-003 — Word Search II (LC 212): Trie + Grid DFS

- **Domain:** ALGO
- **Type:** algorithm
- **Mastery:** 1/5 (solution explained; not yet reproduced independently)
- **Created:** S-2026-06-14-3 | **Last touched:** S-2026-06-14-3

## Problem

Given an m×n character board and a list of words, return all words constructible from sequentially adjacent cells (H/V only, no cell reused within one word).

## Why Trie (not per-word DFS)

Brute force — DFS for each word separately: O(words × m×n × 4^L). With many words sharing prefixes, this retraces the same paths repeatedly → TLE.

**Trie optimization:** insert all words into a Trie, then do a single DFS pass over the board. At each cell, follow the Trie node corresponding to the current character — if no child exists, prune immediately. All words sharing a prefix are explored in one traversal. Overall: O(m×n × 4^L) regardless of word count.

## Clean Solution

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # stores complete word at terminal node

class Solution:
    def findWords(self, board, words):
        # Build Trie
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w

        m, n = len(board), len(board[0])
        result = []

        def dfs(node, i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            ch = board[i][j]
            if ch == '#' or ch not in node.children:
                return
            nxt = node.children[ch]
            if nxt.word:
                result.append(nxt.word)
                nxt.word = None   # de-duplicate: avoid adding same word twice

            tmp = board[i][j]
            board[i][j] = '#'
            for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                dfs(nxt, i + di, j + dj)
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                dfs(root, i, j)

        return result
```

## Key Design Decisions

- **`node.word = None` after match:** prevents adding same word multiple times if it appears at multiple board positions.
- **Prune on `ch not in node.children`:** avoids DFS into paths with no matching prefix — the core speedup.
- **Backtrack restore:** `board[i][j] = tmp` after recursion; marker `'#'` only persists during active path.
- **Explicit bounds first:** check before accessing `board[i][j]` (M-019).

## Connections

- → C-ALGO-001 : prereq — Trie structure and insert
- → C-ALGO-002 : relates — Trie DFS (single-word variant)
- → T-018 : technique — grid DFS with backtracking

## Sources

- S-2026-06-14-3 (2026-06-14): solution explained; not yet reproduced independently [NEEDS_RECALL].

## Review

- **Last review:** 2026-06-14 — fail (not yet reproduced). *(Full history: review/QUEUE.md Results column.)*
