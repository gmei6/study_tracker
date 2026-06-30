# C-ALGO-002 — Trie Wildcard Search (Dot Matching)

- **Domain:** ALGO
- **Type:** pattern
- **Mastery:** 1/5 (1 = seen once, 3 = can use, 5 = can teach/prove cold)
- **Created:** S-2026-06-13-1 | **Last touched:** S-2026-06-13-1

## Statement

Extension of basic Trie search (C-ALGO-001) where '.' matches any single character. Uses recursive DFS: at a '.', branch into every child; at a letter, advance deterministically.

## Implementation

```python
def search(self, word):
    def recursive_search(word, index, curr):
        if index == len(word):
            return curr.word          # base case: exhausted word; check complete-word flag
        ch = word[index]
        if ch == '.':
            for child in curr.children.values():
                if recursive_search(word, index + 1, child):
                    return True
            return False
        else:
            if ch not in curr.children:
                return False
            return recursive_search(word, index + 1, curr.children[ch])
    return recursive_search(word, 0, self.root)
```

## Key Design Decisions

- **Index, not slice:** pass the original `word` with `index + 1`; do not slice and also pass an old index — that produces an off-end reference (see T-014, M-011).
- **Base case:** `index == len(word)` → return `curr.word`. Do NOT return True unconditionally — the node must mark a complete word (see M-012).
- **Dot handling:** iterate `curr.children.values()` (not keys); return True on any positive recursive call.

## Canonical Problems

- LC 211 — Design Add and Search Words Data Structure (S-2026-06-13-1). Trap 1: else-branch fall-through returning True without exhausting word (M-010). Trap 2: early return True at dot-as-last-char skipping `curr.word` check (M-012).

## Connections

- → C-ALGO-001 : prereq — basic Trie structure and insert
- → T-014 : technique — index vs. slice in recursive string traversal

## Sources

- S-2026-06-13-1 (2026-06-13): approach identified correctly; implementation had 4 bugs; clean solution shown. Not yet reproduced independently. [NEEDS_RECALL]

## Review

- **Last review:** 2026-06-30 — fail (mixed while loop with recursion, infinite loop risk, early base case check; see M-012, M-037; B-001). *(Full history: review/QUEUE.md Results column.)*
