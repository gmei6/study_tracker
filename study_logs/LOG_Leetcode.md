# Subject Log: Leetcode

> **Scope:** Python/C++ algorithms, applied logic, and exact failure points.
> **Protocol:** APPEND-ONLY. Add new entries to the bottom via file-system tools. Never delete or summarize past entries.

---

*Log initialized: 2026-06-11. Session entries are appended below in chronological order.*

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
