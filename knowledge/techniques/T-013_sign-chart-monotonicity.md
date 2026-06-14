# T-013 — Sign-Chart / Monotonicity Analysis

- **Mastery:** 2/5 (5 = can construct the argument cold on a novel problem)
- **Created:** S-2026-06-12-1 | **Last touched:** S-2026-06-12-1

## Prerequisites

- Derivatives and critical points
- Ability to test sign of an expression in an interval

## When to Reach For It

- Locating where a function is increasing or decreasing.
- Proving a function achieves a global maximum or minimum.
- **Comparison problems:** to show $f(a) > f(b)$ without computing exact values, prove $f$ is monotone on $[a, b]$ in the right direction.

## Skeleton

1. Find $f'(x)$; solve $f'(x) = 0$ and note where $f'$ is undefined → critical points.
2. Draw a number line. Mark each critical point.
3. Pick a test value in each interval; determine sign of $f'$.
4. $f' > 0 \Rightarrow f$ increasing; $f' < 0 \Rightarrow f$ decreasing.
5. Sign change at $c$: local extremum. No sign change: saddle/inflection.

## Worked Example

$f(x) = x^{1/x}$ on $(0,\infty)$. $\ln f = \frac{\ln x}{x}$, so $\frac{f'}{f} = \frac{1-\ln x}{x^2}$.

Critical point: $\ln x = 1 \Rightarrow x = e$.
- $x < e$: $1 - \ln x > 0 \Rightarrow f' > 0$ (increasing)
- $x > e$: $1 - \ln x < 0 \Rightarrow f' < 0$ (decreasing)

Global maximum at $x = e$. Since $e < \pi$, $f(e) > f(\pi)$, i.e., $e^\pi > \pi^e$.

## Common Failure Modes

- Forgetting to check endpoints or behavior at $0$ and $\infty$.
- Missing a critical point (especially where $f'$ is undefined, not just zero).
- Conflating a sign change (extremum) with a zero of $f'$ without sign change (not an extremum).

## Used In

- C-ANLY-002 : $e^\pi$ vs $\pi^e$ comparison
- Q-002 : interview version of the same problem

## Review

- **Last review:** 2026-06-12 — pass. *(Full history: review/QUEUE.md Results column.)*
