# T-016 — Integration by Parts (IBP)

- **Mastery:** 2/5 (applied correctly on first attempt; not yet tested on harder variants)
- **Created:** S-2026-06-14-2 | **Last touched:** S-2026-06-14-2

## Prerequisites

- Product rule for differentiation
- Basic antiderivatives (polynomials, exponentials, trig)

## When to Reach For It

Integrals of the form ∫f(x)g(x)dx where one factor becomes simpler under differentiation (ln, inverse trig, polynomials) and the other is easy to integrate (trig, exponentials, constants). Key signal: integrand is a *product* and no substitution simplifies it.

## The Formula

$$\int u \, dv = uv - \int v \, du$$

**Choosing u — LIATE priority (differentiate this one):**
Logarithmic → Inverse trig → Algebraic → Trigonometric → Exponential

## Canonical Applications

| Integral | u | dv | Result |
|---|---|---|---|
| ∫ln(x) dx | ln(x) | dx | x·ln(x) − x + C |
| ∫x·eˣ dx | x | eˣ dx | x·eˣ − eˣ + C |
| ∫x·sin(x) dx | x | sin(x) dx | −x·cos(x) + sin(x) + C |

**Always verify by differentiating the result.**

## Common Failure Modes

- Choosing dv = ln(x) dx — ln(x) has no elementary antiderivative by inspection; always put it in u.
- Forgetting the minus sign in uv − ∫v du.
- Not simplifying ∫v du before integrating (the whole point is that ∫v du should be easier).

## Used In

- C-ANLY-004 : ∫ln(x) dx

## Review

- **Last review:** 2026-07-06 — Fail
