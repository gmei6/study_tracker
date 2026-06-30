# C-ALGO-001 — Trie (Prefix Tree)

- **Domain:** ALGO
- **Type:** data structure
- **Mastery:** 3/5 (1 = seen once, 3 = can use, 5 = can teach/prove cold)
- **Created:** S-2026-06-13-1 | **Last touched:** S-2026-06-13-1

## Statement

A Trie is a tree where each node represents a character. Paths from root to a marked node spell out stored words. Supports O(m) insert and search (m = word length), independent of number of stored words.

## Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}   # char → TrieNode
        self.word = False    # True iff a complete word ends here
```

## addWord / Insert

```python
def addWord(self, word):
    curr = self.root
    for ch in word:
        if ch not in curr.children:
            curr.children[ch] = TrieNode()
        curr = curr.children[ch]
    curr.word = True
```

Walk the path, creating nodes as needed; mark the terminal node.

## Basic Search (exact match)

```python
def search(self, word):
    curr = self.root
    for ch in word:
        if ch not in curr.children:
            return False
        curr = curr.children[ch]
    return curr.word   # must be a complete word, not just a prefix
```

## Connections

- → C-ALGO-002 : extends — wildcard search adds '.' handling on top of this
- → T-014 : technique — index vs. slice applies when adapting search to recursion

## Sources

- LC 208 (Implement Trie): prior encounter, not logged in tracker.
- S-2026-06-13-1 (2026-06-13): implemented addWord cleanly without issues.

## Review

- **Last review:** 2026-06-29 — pass (clean). *(Full history: review/QUEUE.md Results column.)*
