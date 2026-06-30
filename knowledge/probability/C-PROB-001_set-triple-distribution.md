# C-PROB-001 — Ordered Set k-Tuple Distribution

- **Domain:** PROB
- **Type:** counting argument
- **Mastery:** 1/5 (1 = seen once, 3 = can use, 5 = can teach/prove cold)
- **Created:** S-2026-06-14-1 | **Last touched:** S-2026-06-14-1

## Statement

The number of ordered triples (A1, A2, A3) with A1∪A2∪A3 = {1,...,n} and A1∩A2∩A3 = ∅ is **6^n**.

For Putnam A-1 (n=10): 6^10 = 2^10 · 3^10, so a=10, b=10, c=0, d=0.

**General form:** for k sets with k-fold intersection = ∅ and union = S (|S|=n):
- Each element must appear in 1, 2, ..., or k-1 sets (not 0, not k)
- Choices per element = C(k,1) + C(k,2) + ... + C(k,k-1) = 2^k − 2
- Total = (2^k − 2)^n

For k=3: 2^3 − 2 = 6. ✓

## Proof Sketch

Element-by-element (T-015): the global constraints decompose independently per element. Element x ∈ S must be in ≥1 set (union condition) and ≤2 sets (triple-intersection condition). The C(3,j) configurations for j=1,2 give 3+3=6 choices. Since elements are independent, multiply over all n elements.

## Canonical Problems

- Putnam A-1 (S-2026-06-14-1). Traps: (1) stars-and-bars assumes disjoint partition, doesn't allow overlap (M-013); (2) summing over total element-coverage y rather than multiplying per element (M-014); (3) element-by-element independence is the unlock.

## Connections

- → T-015 : technique — element-by-element independent counting

## Sources

- S-2026-06-14-1 (2026-06-14): framework explained, not yet reproduced independently [NEEDS_RECALL].

## Review

- **Last review:** 2026-06-30 — fail (needed element-by-element counting hint; see M-014). *(Full history: review/QUEUE.md Results column.)*
