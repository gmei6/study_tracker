# C-ANLY-004 — ∫ln(x) dx via Integration by Parts

- **Domain:** ANLY
- **Type:** canonical integral
- **Mastery:** 2/5 (solved independently on first attempt)
- **Created:** S-2026-06-14-2 | **Last touched:** S-2026-06-14-2

## Statement

$$\int \ln x \, dx = x \ln x - x + C$$

## Derivation

IBP with **u = ln(x), dv = dx** (LIATE: logarithm before algebraic):
- du = (1/x) dx, v = x
- ∫ln x dx = x·ln x − ∫x·(1/x) dx = x·ln x − ∫1 dx = x·ln x − x + C

**Verification:** d/dx(x·ln x − x) = ln x + x·(1/x) − 1 = ln x + 1 − 1 = ln x ✓

## Key Insight

The "trick" is recognizing ln(x) as the piece to differentiate (u), not to integrate — ln(x) has no clean antiderivative by inspection, but differentiates to 1/x, which cancels the introduced v = x.

## Canonical Problems

- Green Book Calculus Problem A (S-2026-06-14-2). Solved independently; verify by differentiating result.

## Connections

- → T-016 : technique — integration by parts

## Sources

- S-2026-06-14-2 (2026-06-14): solved cold and independently.

## Review

- **Last review:** 2026-06-14 — pass. *(Full history: review/QUEUE.md Results column.)*
