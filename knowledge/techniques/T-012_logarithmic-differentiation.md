# T-012 — Logarithmic Differentiation

- **Mastery:** 1/5 (5 = can construct the argument cold on a novel problem)
- **Created:** S-2026-06-12-1 | **Last touched:** S-2026-06-12-1

## Prerequisites

- Chain rule and product rule (basic calculus)
- Implicit differentiation ($\frac{d}{dx}[\ln y] = \frac{1}{y}\frac{dy}{dx}$)

## When to Reach For It

The function has the form $y = f(x)^{g(x)}$ — **both** base and exponent depend on $x$. Also useful when $y$ is a product/quotient of many factors and direct differentiation is messy.

## Skeleton

1. Ensure $y > 0$ (or split into cases). Take $\ln$ of both sides: $\ln y = g(x)\ln f(x)$.
2. Differentiate both sides w.r.t. $x$.
3. **Left side always:** $\dfrac{1}{y}\dfrac{dy}{dx}$ — this is the chain rule on $\ln y$ and is the most common failure point.
4. **Right side:** product rule + chain rule as needed.
5. Multiply both sides by $y$ to isolate $\dfrac{dy}{dx}$. Substitute back $y = f(x)^{g(x)}$.

## Worked Example

$y = (\ln x)^{\ln x}$

1. $\ln y = \ln x \cdot \ln(\ln x)$
2–3. $\dfrac{1}{y}\dfrac{dy}{dx} = \dfrac{d}{dx}[\ln x \cdot \ln(\ln x)]$
4. Product rule: $\dfrac{1}{x}\cdot\ln(\ln x) + \ln x \cdot \dfrac{1}{x\ln x} = \dfrac{\ln(\ln x)+1}{x}$
5. $\dfrac{dy}{dx} = (\ln x)^{\ln x}\cdot\dfrac{\ln(\ln x)+1}{x}$ ← **hard step marked: step 3**

## Common Failure Modes

- **Forgetting step 3:** treating $\ln y$ as a constant or trying $e^{\ln y} = y$ on both sides (circular — you're back to the original equation).
- Dropping the chain rule on $\ln f(x)$ in step 4.
- Forgetting to multiply back by $y$ in step 5.

## Used In

- C-ANLY-001 : logarithmic differentiation concept
- C-ANLY-002 : deriving $f'$ for $f(x) = x^{1/x}$
- Q-001 : $(\ln x)^{\ln x}$ derivative

## Review

- **Last review:** 2026-06-13 — pass. *(Full history: review/QUEUE.md Results column.)*
