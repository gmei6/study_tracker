# Subject Log: Green Book

> **Scope:** Quant finance interview problems and mathematical insights.
> **Protocol:** APPEND-ONLY. Add new entries to the bottom via file-system tools. Never delete or summarize past entries.

---

*Log initialized: 2026-06-11. Session entries are appended below in chronological order.*

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
