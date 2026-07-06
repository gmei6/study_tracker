# C-LINALG-001 — Complex Numbers (ℂ)

- **Domain:** LINALG
- **Type:** definition
- **Mastery:** 1/5 (1 = seen once, 3 = can use, 5 = can teach/prove cold)
- **Created:** S-2026-06-14-4 | **Last touched:** S-2026-06-14-4

## Statement

A **complex number** is $\alpha = a + bi$ where $a, b \in \mathbb{R}$ and $i = \sqrt{-1}$. $\mathbb{R} \subset \mathbb{C}$ (e.g., $3 = 3 + 0i$).

**Arithmetic:**
- Addition: $(a+bi)+(c+di) = (a+c)+(b+d)i$
- Multiplication: $(a+bi)(c+di) = (ac-bd)+(ad+bc)i$

**Properties (Definition 1.5):** commutativity (+ and ×), associativity (+ and ×), additive identity 0, multiplicative identity 1, additive inverse $-\alpha = (-a)+(-b)i$, multiplicative inverse $1/\alpha$ for $\alpha \neq 0$.

**Multiplicative inverse in standard form** (conjugate division — not yet reproduced; see T-019):
$$\frac{1}{a+bi} = \frac{a-bi}{a^2+b^2}$$

$\mathbb{F}$ denotes ℝ or ℂ throughout Axler (statements hold for both fields). Index variable $i \in \{1,\dots,n\}$ is distinct from imaginary unit $i = \sqrt{-1}$ — same letter, context-dependent; see M-026.

## Proof / Derivation

**Commutativity of multiplication (reproduced):**
$$\alpha\beta = (ac-bd)+(ad+bc)i, \qquad \beta\alpha = (ca-db)+(cb+da)i$$
Equal by commutativity of $\mathbb{R}$. ✓

**Additive inverse (reproduced):** $(a+bi)+(-a-bi) = 0+0i = 0$. ✓

**Associativity of multiplication:** ⚠ GAP — expand $(\alpha\beta)\gamma$ and $\alpha(\beta\gamma)$; equal by associativity of $\mathbb{R}$. Proof not yet reproduced [NEEDS_RECALL].

## Intuition

ℂ is ℝ extended by adjoining $\sqrt{-1}$. Multiplication rotates and scales in the plane. The conjugate $\bar\alpha = a-bi$ flips the imaginary part: $\alpha\bar\alpha = a^2+b^2 \in \mathbb{R}$, which is the key to computing inverses and dividing.

## Canonical Problems

- **Ex 1:** Commutativity of addition — reduce to real parts. ✓
- **Ex 9:** Coordinate-wise arithmetic in $\mathbb{F}^4$. ✓
- **Ex 7:** Show $\omega = -\frac{1}{2}+\frac{\sqrt{3}}{2}i$ satisfies $\omega^3=1$. Compute $\omega^2$ carefully then multiply by $\omega$. Trap: $\left(\frac{\sqrt{3}}{2}\right)^2 = \frac{3}{4}$ (not $\frac{3}{2}$) and $i^2=-1$ always. See M-028, M-029.
- **Ex 8:** Square roots of $i$ — set $(a+bi)^2=i$, match components. See T-020. Not reproduced.

## Connections

- → C-LINALG-002 : extends — $\mathbb{F}^n$ lists are built from elements of $\mathbb{F}=\mathbb{C}$ or $\mathbb{R}$
- → T-019 : technique — conjugate division for multiplicative inverse
- → T-020 : technique — component-wise root-finding for complex equations

## Sources

- S-2026-06-14-4 (2026-06-14): First encounter. Commutativity (× and +) and additive inverse reproduced. Multiplicative associativity and conjugate inverse not reproduced. Arithmetic errors in Ex 7–8 (M-028, M-029, M-030).

## Review

- **Last review:** 2026-07-05 — pass. *(Full history: review/QUEUE.md Results column.)*
