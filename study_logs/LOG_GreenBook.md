# Subject Log: Green Book

> **Scope:** Quant finance interview problems and mathematical insights.
> **Protocol:** APPEND-ONLY. Add new entries to the bottom via file-system tools. Never delete or summarize past entries.

---

*Log initialized: 2026-06-11. Session entries are appended below in chronological order.*

---

## S-2026-06-14-2 — Integration by parts (∫ln x dx) and ∫sec x dx via substitution + partial fractions
- Duration: 32 | Effort: 4
- Source: Green Book, Calculus section, Problems A & B

**Problem A [INTERVIEW]:** ∫ln(x) dx
Solved independently using IBP: u = ln(x), dv = dx → du = 1/x dx, v = x. Result: x·ln(x) - ∫1 dx = x·ln(x) - x + C. Verified by differentiation: d/dx(x·ln x - x) = ln x + 1 - 1 = ln x ✓. Clean.

**Problem B [INTERVIEW]:** ∫sec(x) dx from 0 to π/6
Initially recalled sec(x) = 1/sin(x) [STRUGGLE] — wrong (M-015). Correct: sec(x) = 1/cos(x). Guessed antiderivative behaves like ln(cos x) but couldn't handle chain rule factor of -sin(x) — stuck. Given hint: try u = sin(x) substitution, converting to ∫1/(1-u²) du. Set up partial fractions 1/(1-u²) = A/(1-u) + B/(1+u) correctly, but tried to arbitrarily set A = 1 instead of solving systematically [STRUGGLE] (M-016). Systematic method: multiply both sides by (1-u²), equate coefficients → A = B = 1/2. Explained, not yet reproduced [NEEDS_RECALL]. When integrating: factored constant 1/2 out as a 2 [STRUGGLE] (M-017), and applied FTC to -ln|1-u| in wrong order [STRUGGLE] (M-018). Once corrected: 1/2·[ln|1+u| - (-ln|1-u|)] from 0 to 1/2 = 1/2·[ln(3/2) - (-ln(1/2))] - 0 = 1/2·ln(3).

---

## S-2026-06-12-1 — Logarithmic differentiation, exponential comparison, L'Hôpital
- Duration: 43 | Effort: 2
- Source: Green Book, Calculus Section, ~p.50

**Problem 1 [INTERVIEW]:** Derivative of $y = (\ln x)^{\ln x}$.
Notation misread initially as $\ln(x^{\ln x})$ [STRUGGLE] — that interpretation gives $y = (\ln x)^2$,
derivative $2\ln x/x$, verified independently via product rule [INSIGHT]. Correct form requires
logarithmic differentiation: $\ln y = \ln x \cdot \ln(\ln x)$, differentiate implicitly. Got
stuck trying $e^{\ln y}$ on both sides in a circle [STRUGGLE]; forgot left side yields
$\frac{1}{y}\frac{dy}{dx}$ by chain rule [STRUGGLE]. Once corrected:
$\frac{dy}{dx} = (\ln x)^{\ln x} \cdot \frac{\ln(\ln x)+1}{x}$.

**Problem 2 [INTERVIEW]:** Which is larger, $e^\pi$ or $\pi^e$?
Misremembered $e \approx 1.2$ [STRUGGLE]. Integer approximation $e=2, \pi=3$ gives
$2^3=8 < 9=3^2$, suggesting $\pi^e > e^\pi$ — wrong [STRUGGLE]. Correct: define
$f(x)=x^{1/x}$, show $f$ maximized at $x=e$ via sign chart on $f'$ (product rule on
$x^{-1}\ln x$ gives $f'= x^{1/x}(1-\ln x)/x^2$) [INSIGHT]. Since $\pi>e$ and $f$
decreasing there, $f(e)>f(\pi)$, so $e^\pi > \pi^e$.

**Problem 3 [INTERVIEW]:** $\lim_{x\to\infty} e^x/x^2$ and $\lim_{x\to 0^+} x^2\ln x$.
First limit: recognized $\infty/\infty$, L'Hôpital twice → $\infty$. Second limit:
misremembered $\ln x \to +\infty$ near $0^+$ [STRUGGLE]; tried $x^2/\ln x$ as quotient form
(algebraic nonsense) [STRUGGLE]; arithmetic slip $2x/(1/x) = 2$ instead of $2x^2$ [STRUGGLE].
Correct: rewrite as $\ln x / x^{-2}$, L'Hôpital → $\frac{1/x}{-2x^{-3}} = -x^2/2 \to 0$.
Explained by book, not yet reproduced [NEEDS_RECALL].
