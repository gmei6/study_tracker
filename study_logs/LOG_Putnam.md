# Subject Log: Putnam Competition

> **Scope:** Putnam competition frameworks and conceptual gaps.
> **Protocol:** APPEND-ONLY. Add new entries to the bottom via file-system tools. Never delete or summarize past entries.

---

*Log initialized: 2026-06-11. Session entries are appended below in chronological order.*

## S-2026-06-14-1 — Putnam A-1: ordered set triples (union + empty triple intersection)
- Duration: 38 | Effort: 5
- Source: Putnam Archive, A-1

Problem: count ordered triples (A1, A2, A3) with A1∪A2∪A3 = {1,...,10} and A1∩A2∩A3 = ∅. Express answer as 2^a 3^b 5^c 7^d. [INTERVIEW]

Started with stars-and-bars: 2 dividers + 10 elements → (12 choose 2)·10! [STRUGGLE]. Model assumes disjoint partition — doesn't allow elements to appear in multiple sets. Wrong (M-013).

Revised: sets can share elements as long as no element is in all three. Tried summing (y+2 choose 2)·y! for y = 10 to 20, but y=20 gives a factor of 19 (prime, doesn't fit target form) — dead end [STRUGGLE] (M-014). Root issue: aggregating over configurations instead of recognizing per-element independence.

Framework explained to me, not yet reproduced independently [NEEDS_RECALL]: each element must be in ≥1 and ≤2 sets. Choices per element: C(3,1)=3 (exactly 1 set) + C(3,2)=3 (exactly 2 sets) = 6. Elements are independent → total = 6^10 [INSIGHT]. Once framework was given, derived 6^10 = 2^10·3^10, so a=10, b=10, c=0, d=0.
