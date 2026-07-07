# C-LINALG-002 — Lists and $\mathbb{F}^n$

- **Domain:** LINALG
- **Type:** definition
- **Mastery:** 1/5 (1 = seen once, 3 = can use, 5 = can teach/prove cold)
- **Created:** S-2026-06-14-4 | **Last touched:** S-2026-06-14-4

## Statement

A **list** of length $n$ is an ordered sequence of $n$ elements. Order matters: $(1,2) \neq (2,1)$ as lists.

**Key constraint:** $n \in \mathbb{Z}^+$ — list length is a count (positive integer), not a real number. [M-027 trap: $n \notin \mathbb{R}^+$]

$\mathbb{F}^n$ is the set of all lists of length $n$ with entries in $\mathbb{F}$:
$$\mathbb{F}^n = \{(x_1, \dots, x_n) : x_j \in \mathbb{F},\; j = 1,\dots,n\}$$

Two elements of $\mathbb{F}^n$ are equal iff every corresponding coordinate is equal.

## Proof / Derivation

Type = definition — omitted.

## Intuition

A list is what CS calls an array or tuple. The key distinction: **sets ignore order; lists preserve it.** This matters in linear algebra because vectors in $\mathbb{F}^n$ carry coordinate positions — swapping entries gives a different vector.

## Canonical Problems

- **Notation 1.6 trap:** index $i \in \{1,\dots,n\}$ vs. imaginary unit $i = \sqrt{-1}$ — same symbol, different meaning by context. See M-026.
- **Ex 9:** Coordinate-wise solve in $\mathbb{F}^4$: $(4,-3,1,7)+2x=(5,9,-6,8)$ → $x=(\tfrac{1}{2},6,-\tfrac{7}{2},\tfrac{1}{2})$. ✓

## Connections

- → C-LINALG-001 : prereq — $\mathbb{F}$ (ℝ or ℂ) defined there; entries of $\mathbb{F}^n$ live in $\mathbb{F}$
- → C-ALGO-003 : relates — ordered lists (arrays) vs. unordered visited sets in DFS; same ordered/unordered distinction (see CONNECTIONS.md)

## Sources

- S-2026-06-14-4 (2026-06-14): First encounter. Integer dimension error (M-027). Key insight: list vs. set distinction maps directly to CS arrays vs. sets.

## Review

- **Last review:** 2026-07-06 — Pass
