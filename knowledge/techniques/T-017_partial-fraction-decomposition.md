# T-017 — Partial Fraction Decomposition (PFD)

- **Mastery:** 1/5 (setup correct; coefficient-solving method not yet reproduced)
- **Created:** S-2026-06-14-2 | **Last touched:** S-2026-06-14-2

## Prerequisites

- Polynomial long division (degree of numerator ≥ denominator → divide first)
- Factoring denominators over ℝ

## When to Reach For It

Integrating a rational function P(x)/Q(x) where deg(P) < deg(Q) and Q factors. Also appears in Laplace transforms and solving linear ODEs.

## The Method

**Step 1 — Factor denominator** into irreducible linear and quadratic factors.

**Step 2 — Write the decomposition.** For each factor:
- Linear factor (ax+b)^n → terms A₁/(ax+b) + A₂/(ax+b)² + ... + Aₙ/(ax+b)ⁿ
- Irreducible quadratic (ax²+bx+c)^n → terms (B₁x+C₁)/(ax²+bx+c) + ...

**Step 3 — Solve for coefficients** (never guess):
- Multiply both sides by the full denominator.
- **Cover-up method** (fastest for distinct linear factors): to find Aᵢ for factor (x−rᵢ), set x=rᵢ — all other terms vanish.
- Alternatively: expand and equate coefficients of each power of x; solve the linear system.

## Worked Example (from C-ANLY-005)

$$\frac{1}{1-u^2} = \frac{A}{1-u} + \frac{B}{1+u}$$

Multiply both sides by $(1-u^2) = (1-u)(1+u)$:

$$1 = A(1+u) + B(1-u)$$

Cover-up: set u=1 → 1 = 2A → **A = 1/2**; set u=−1 → 1 = 2B → **B = 1/2**.

$$\int \frac{du}{1-u^2} = \frac{1}{2}\ln|1+u| - \frac{1}{2}\ln|1-u| + C$$

## Common Failure Modes

- Guessing coefficients (M-016) instead of solving — only works by accident.
- Forgetting to divide first when deg(P) ≥ deg(Q).
- Sign errors when integrating linear factors: ∫du/(a−u) = −(1/a)·ln|a−u| (note the negative from chain rule).

## Used In

- C-ANLY-005 : ∫sec(x) dx

## Review

- **Last review:** 2026-06-30 — fail (failed conceptual rules: degree condition check and repeated linear factor representation; see M-039, M-040). *(Full history: review/QUEUE.md Results column.)*
