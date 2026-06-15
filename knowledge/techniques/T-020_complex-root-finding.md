# T-020 — Complex Root-Finding via Component Equations

- **Mastery:** 1/5 (explained, not yet reproduced)
- **Created:** S-2026-06-14-4 | **Last touched:** S-2026-06-14-4

## Prerequisites

- Complex number multiplication formula (C-LINALG-001)
- Ability to solve 2×2 real systems (substitution)

## When to Reach For It

Asked to find $w \in \mathbb{C}$ such that $w^n = z$ and the answer must be in standard $a+bi$ form. Signal: "find all square/cube/nth roots of $z$," or "express $z^{1/n}$ in standard form."

## The Method

1. Write $w = a + bi$ with $a, b \in \mathbb{R}$ unknown.
2. Expand $w^n$ and collect real and imaginary parts.
3. Set $\text{Re}(w^n) = \text{Re}(z)$ and $\text{Im}(w^n) = \text{Im}(z)$.
4. Solve the resulting real system for $a$ and $b$.

## Canonical Application — Square Roots of $i$

Find $w = a+bi$ with $w^2 = i$:

**Expand:** $(a+bi)^2 = a^2 - b^2 + 2abi$

**Match:** $a^2 - b^2 = 0$ (real) and $2ab = 1$ (imaginary)

**Solve:** $a^2 = b^2 \Rightarrow a = \pm b$. From $2ab = 1$: if $a = b$ then $2a^2 = 1 \Rightarrow a = \frac{1}{\sqrt{2}}$; if $a = -b$ then $-2a^2 = 1$ (no real solution).

**Result:** $\sqrt{i} = \pm\left(\dfrac{1}{\sqrt{2}} + \dfrac{1}{\sqrt{2}}i\right)$

## Common Failure Modes

- Leaving the answer in exponential or radical form ($\pm\sqrt{i}$) instead of completing the $a, b$ solve.
- Forgetting $i^2 = -1$ when expanding — every $b^2i^2$ term flips sign.
- Missing the $\pm$ (both solutions): if $a=b$ gives a solution, $a=-b=-b$ gives the other.

## Used In

- C-LINALG-001 : Ex 8 (square roots of $i$), Ex 7 (cube root of unity approach)

## Review

- **Last review:** 2026-06-14 — fail (not reproduced). *(Full history: review/QUEUE.md Results column.)*
