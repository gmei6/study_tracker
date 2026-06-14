# C-ANLY-003 — L'Hôpital's Rule (Indeterminate Forms)

- **Domain:** ANLY
- **Type:** theorem
- **Mastery:** 1/5 (1 = seen once, 3 = can use, 5 = can teach/prove cold)
- **Created:** S-2026-06-12-1 | **Last touched:** S-2026-06-12-1

## Statement

If $\lim_{x\to a}\frac{f(x)}{g(x)}$ is of the form $\frac{0}{0}$ or $\frac{\infty}{\infty}$, and $g'(x)\neq 0$ near $a$, then:

$$\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$$

provided the right-hand limit exists (or equals $\pm\infty$). Apply repeatedly if the form persists.

## Proof / Derivation

⚠ GAP: full proof via Cauchy's mean value theorem not yet derived.

## Intuition

Near an indeterminate point, the ratio $f/g$ behaves like the ratio of their linear approximations, which is $f'/g'$.

## Indeterminate Forms and Rewrites

| Form | Rewrite to apply L'Hôpital |
|---|---|
| $0/0$ or $\infty/\infty$ | Apply directly |
| $0 \cdot \infty$ | Rewrite as $f/(1/g)$ or $g/(1/f)$ to achieve $0/0$ or $\infty/\infty$ |
| $1^\infty,\ 0^0,\ \infty^0$ | Take ln, apply L'Hôpital, exponentiate result |

## Canonical Problems

1. $\lim_{x\to\infty}\frac{e^x}{x^2}$: form $\infty/\infty$. Apply twice: $\frac{e^x}{2x} \to \frac{e^x}{2} \to \infty$.
2. $\lim_{x\to 0^+} x^2\ln x$: form $0\cdot(-\infty)$. Rewrite as $\frac{\ln x}{x^{-2}}$ (form $-\infty/\infty$). L'Hôpital: $\frac{1/x}{-2x^{-3}} = \frac{x^3}{-2x} = \frac{-x^2}{2} \to 0$.

## Connections

*(No prereq edges to other C-IDs registered yet.)*

## Sources

- S-2026-06-12-1 (2026-06-12): limit 1 solved independently; limit 2 explained by book, not yet reproduced [NEEDS_RECALL].

## Review

- **Last review:** 2026-06-13 — fail. *(Full history: review/QUEUE.md Results column.)*
