# C-ANLY-005 — ∫sec(x) dx and definite integral from 0 to π/6

- **Domain:** ANLY
- **Type:** canonical integral
- **Mastery:** 1/5 (method explained; not yet reproduced independently)
- **Created:** S-2026-06-14-2 | **Last touched:** S-2026-06-14-2

## Statement

$$\int \sec x \, dx = \ln|\sec x + \tan x| + C$$

**Definite integral (0 to π/6):** $\dfrac{1}{2}\ln 3$

## Derivation via u-substitution + partial fractions

Let **u = sin(x)**, du = cos(x) dx. Since sec(x) = 1/cos(x):

$$\int \sec x \, dx = \int \frac{1}{\cos^2 x} \cos x \, dx = \int \frac{1}{1 - \sin^2 x} du = \int \frac{1}{1-u^2} du$$

Partial fractions (T-017): $\dfrac{1}{1-u^2} = \dfrac{A}{1-u} + \dfrac{B}{1+u}$

Multiply both sides by $(1-u^2)$: $1 = A(1+u) + B(1-u)$. Setting u=1: A = 1/2; u=−1: B = 1/2.

$$\int \frac{1}{1-u^2} du = \frac{1}{2}\int\frac{du}{1-u} + \frac{1}{2}\int\frac{du}{1+u} = \frac{1}{2}\left(-\ln|1-u| + \ln|1+u|\right) + C = \frac{1}{2}\ln\left|\frac{1+\sin x}{1-\sin x}\right| + C$$

**Definite from 0 to π/6** (sin(π/6) = 1/2, sin(0) = 0):

$$\frac{1}{2}\ln\frac{3/2}{1/2} - \frac{1}{2}\ln\frac{1}{1} = \frac{1}{2}\ln 3$$

## Common Traps

- sec(x) = 1/cos(x), NOT 1/sin(x) (M-015)
- PFD coefficients: solve systematically, never guess (M-016)
- The 1/2 factor in ∫du/(1−u) is from the coefficient, not a separate step — factor it out correctly (M-017)
- FTC on −ln|1−u|: the negative sign is part of the antiderivative; evaluate F(b)−F(a) on the whole expression (M-018)

## Connections

- → T-016 : technique — integration by parts (alternate derivation path)
- → T-017 : technique — partial fraction decomposition (used here)

## Sources

- S-2026-06-14-2 (2026-06-14): method explained by scribe; not yet reproduced independently [NEEDS_RECALL].

## Review

- **Last review:** 2026-06-14 — fail (not yet reproduced). *(Full history: review/QUEUE.md Results column.)*
