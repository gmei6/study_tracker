# T-019 — Conjugate Division (Complex Multiplicative Inverse)

- **Mastery:** 1/5 (explained, not yet reproduced)
- **Created:** S-2026-06-14-4 | **Last touched:** S-2026-06-14-4

## Prerequisites

- Complex number definition and multiplication formula (C-LINALG-001)
- Difference of squares: $(a+b)(a-b) = a^2 - b^2$

## When to Reach For It

Any time a complex number appears in a denominator, or you need $\alpha^{-1}$ or $\alpha/\beta$ in standard $a+bi$ form. Signal: task says "find the multiplicative inverse" or "write in standard form."

## The Method

Multiply numerator and denominator by the **conjugate** $\bar\alpha = a - bi$:
$$\frac{1}{a+bi} \cdot \frac{a-bi}{a-bi} = \frac{a-bi}{(a+bi)(a-bi)} = \frac{a-bi}{a^2+b^2}$$

Key: $(a+bi)(a-bi) = a^2 - (bi)^2 = a^2 + b^2 \in \mathbb{R}$ — imaginary parts cancel via $i^2 = -1$.

Standard form result: $\dfrac{a}{a^2+b^2} - \dfrac{b}{a^2+b^2}\,i$

For general division $\alpha/\beta$: multiply both by $\bar\beta$.

## Canonical Applications

| Task | Apply |
|---|---|
| $1/(2+3i)$ | Multiply by $(2-3i)/(2-3i)$: result $(2-3i)/13$ |
| $(1+i)/(1-i)$ | Multiply by $(1+i)/(1+i)$: result $i$ |
| Verify $\alpha \cdot \frac{1}{\alpha} = 1$ in standard form | Conjugate divide, confirm product = 1 |

## Common Failure Modes

- Forgetting to apply $i^2 = -1$ when expanding $(a+bi)(a-bi)$ — the whole cancellation depends on this.
- Applying the conjugate to the numerator only, not both.

## Used In

- C-LINALG-001 : multiplicative inverse property

## Review

- **Last review:** 2026-07-06 — Pass
