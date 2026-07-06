# C-ANLY-002 — Comparing $e^\pi$ vs $\pi^e$ via $f(x) = x^{1/x}$

- **Domain:** ANLY
- **Type:** pattern
- **Mastery:** 2/5 (1 = seen once, 3 = can use, 5 = can teach/prove cold)
- **Created:** S-2026-06-12-1 | **Last touched:** S-2026-06-12-1

## Statement

$e^\pi > \pi^e$.

More generally: to compare $a^b$ vs $b^a$ for $a, b > 0$, study $f(x) = x^{1/x}$, which is maximized at $x = e$.

## Proof / Derivation

Let $f(x) = x^{1/x}$. Taking ln: $\ln f(x) = \frac{\ln x}{x}$. Differentiate (using product rule on $x^{-1}\ln x$):

$$\frac{f'(x)}{f(x)} = \frac{1 - \ln x}{x^2} \implies f'(x) = \frac{x^{1/x}(1-\ln x)}{x^2}$$

Sign chart: $f'(x) > 0$ for $x < e$, $f'(x) = 0$ at $x = e$, $f'(x) < 0$ for $x > e$. So $f$ is uniquely maximized at $x = e$.

Since $e < \pi$, we have $f(e) > f(\pi)$, i.e., $e^{1/e} > \pi^{1/\pi}$. Raise both sides to the power $e\pi > 0$:

$$e^\pi > \pi^e. \quad \square$$

## Intuition

The function $x^{1/x}$ measures how "efficient" $x$ is as a base when raised to a power that normalizes for its size. $e$ is the uniquely efficient base — this is a deep fact that permeates all of analysis.

## Canonical Problems

- "Without calculating, which is larger: $e^\pi$ or $\pi^e$?" — Green Book ~p.50, S-2026-06-12-1. Trap: integer approximation ($e\approx2$, $\pi\approx3$) gives wrong answer $8 < 9$. Must use the analysis.

## Connections

- → C-ANLY-001 : prereq — logarithmic differentiation (to find $f'$)
- → T-013 : technique — sign-chart / monotonicity analysis

## Sources

- S-2026-06-12-1 (2026-06-12): integer approx failed [STRUGGLE]; looked at book's approach; reproduced sign chart correctly [partial pass].

## Review

- **Last review:** 2026-07-06 — Fail
