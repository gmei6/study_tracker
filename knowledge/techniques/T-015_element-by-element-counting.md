# T-015 — Element-by-Element Independent Counting

- **Mastery:** 1/5 (5 = can construct the argument cold on a novel problem)
- **Created:** S-2026-06-14-1 | **Last touched:** S-2026-06-14-1

## Prerequisites

- Basic combinatorics (binomial coefficients)
- Set operations (union, intersection)

## When to Reach For It

Combinatorics problems assigning n elements to k sets/bins under global constraints. Key signal: the constraint on each element depends only on which sets contain *that* element, not on how other elements are assigned. If elements are interchangeable and independent under the constraint, this technique applies.

## The Technique

1. Verify that the global constraint separates element-wise (check independence).
2. Count valid assignments for a single generic element.
3. Multiply over all n elements: total = (choices per element)^n.

## Common Failure Modes

- **Stars-and-bars reflex:** assumes a disjoint partition (each element in exactly one bin). Wrong when elements can appear in multiple sets — undercounts valid configurations.
- **Summing over aggregate quantity:** enumerates by a global variable (e.g., total element-coverage y) rather than factoring over elements. Loses independence, produces intractable sums (e.g., prime factors that can't fit a given form).

## Worked Example (Putnam A-1)

Ordered triples (A1, A2, A3) with A1∪A2∪A3 = {1,...,10}, A1∩A2∩A3 = ∅.

- Each element x: must be in ≥1 set (union) and ≤2 sets (triple intersection forbidden).
- Valid membership patterns: {A1}, {A2}, {A3} (one set each) or {A1,A2}, {A1,A3}, {A2,A3} (two sets each).
- Choices per element: C(3,1) + C(3,2) = 3 + 3 = 6.
- Elements independent → total = 6^10 = 2^10 · 3^10.

## Used In

- C-PROB-001 : Ordered set k-tuple distribution (first use)

## Review

- **Last review:** 2026-06-29 — fail (described n!/ordering rather than (choices per element)^n; core mechanism wrong). *(Full history: review/QUEUE.md Results column.)*
