# T-014 — Index vs. Slice in Recursive String Traversal

- **Mastery:** 1/5 (5 = can construct the argument cold on a novel problem)
- **Created:** S-2026-06-13-1 | **Last touched:** S-2026-06-13-1

## Prerequisites

- Basic recursion
- Python string slicing semantics (`s[:k]` = first k chars; `s[k:]` = chars from index k onward)

## When to Reach For It

Any recursive function that traverses a string character by character, especially when mixing a while loop (for non-branching characters) with recursion (for branching characters, e.g. wildcards).

## The Rule

**Pick one. Never both. At interview, always pick index.**

| Approach | How to pass remaining string | How to advance | Per-call cost |
|---|---|---|---|
| Index | Pass original `word` unchanged | Pass `index + 1` | O(1) |
| Slice | Pass `word[1:]` (or `word[k:]`) | Index resets to 0 in recursive call | O(n) — new string allocated each call |

Mixing them — e.g. passing `word[plus_one:]` AND using `plus_one` as the index into the shorter string — produces an index that is off the end of the sliced string.

**Why index is interview-preferred:** slice creates a new string of length n − k on each recursive call. Over a DFS with depth L and branching factor b (e.g. 26 for dots), that's O(n·b^L) total string allocation. Index adds zero allocation overhead. State this tradeoff explicitly when explaining your choice.

## Common Failure Mode

```python
# WRONG: mixed slice + old index
return recursive_search(word[plus_one:], plus_one, child)
# 'word[plus_one:]' has length len(word) - plus_one
# but 'plus_one' as an index into it is past the end

# CORRECT (index approach):
return recursive_search(word, index + 1, child)

# CORRECT (slice approach):
return recursive_search(word[1:], 0, child)
```

## Used In

- C-ALGO-002 : Trie wildcard search (the concrete case where this came up)

## Review

- **Last review:** 2026-06-29 — fail (got the rule but not the WHY; recommended slice; missed that slice is O(n) per call vs. index O(1); content gap now fixed). *(Full history: review/QUEUE.md Results column.)*
