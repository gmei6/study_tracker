# C-ANLY-001 — Logarithmic Differentiation

- **Domain:** ANLY
- **Type:** technique
- **Mastery:** 2/5 (1 = seen once, 3 = can use, 5 = can teach/prove cold)
- **Created:** S-2026-06-12-1 | **Last touched:** S-2026-06-12-1

## Statement

For $y = f(x)^{g(x)}$ — variable base and variable exponent — direct differentiation is intractable. Take the natural log of both sides, differentiate implicitly, then solve for $dy/dx$:

$$\ln y = g(x)\,\ln f(x)$$
$$\frac{1}{y}\frac{dy}{dx} = g'(x)\ln f(x) + g(x)\frac{f'(x)}{f(x)}$$
$$\frac{dy}{dx} = y\left[g'(x)\ln f(x) + g(x)\frac{f'(x)}{f(x)}\right]$$

## Proof / Derivation

Take ln of both sides (valid for $y > 0$), differentiate both sides w.r.t. $x$. Left side: $\frac{d}{dx}[\ln y] = \frac{1}{y}\frac{dy}{dx}$ by the chain rule. Right side: product rule on $g(x)\ln f(x)$. Multiply through by $y$.

## Intuition

The log converts a "tower" exponent into a product, which the product rule can handle. The implicit differentiation on the left side is the step that surprises people — $\ln y$ is not constant, so its derivative is $(1/y)(dy/dx)$, not zero.

## Canonical Problems

- $y = (\ln x)^{\ln x}$: set $\ln y = \ln x \cdot \ln(\ln x)$, RHS product rule gives $\frac{\ln(\ln x)+1}{x}$, multiply back by $y$: $\frac{dy}{dx} = (\ln x)^{\ln x}\cdot\frac{\ln(\ln x)+1}{x}$. (S-2026-06-12-1; trap: see Key Traps below)
- Also applies to products of many factors: take log to convert the product into a sum before differentiating.

## Connections

- → T-012 : technique — logarithmic differentiation
- → C-ANLY-002 : relates — same log-then-differentiate setup used for $f(x)=x^{1/x}$

## Sources

- S-2026-06-12-1 (2026-06-12): first encounter; got answer for $\ln(x^{\ln x})$ interpretation correctly via product rule [INSIGHT]; failed key implicit-diff step for $(\ln x)^{\ln x}$ form [STRUGGLE].

## Review

- **Last review:** 2026-06-29 — fail (set y = d/dx[x^x] instead of y = x^x; missed chain rule on ln y; see M-002, M-033). *(Full history: review/QUEUE.md Results column.)*
