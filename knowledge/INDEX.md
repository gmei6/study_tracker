# Knowledge Index — Domain Registry

> Root registry only. Each domain's concept list lives in its own `INDEX_{DOM}.md`, created lazily with the domain's first concept. Next ID for any domain = highest ID in its index + 1 (001 if none). Counters are derived, never stored.

## Registered Domains

| Code | Domain | Folder | Domain index |
|---|---|---|---|
| PROB | Probability & Combinatorics | knowledge/probability/ | INDEX_PROB.md (on first concept) |
| LINALG | Linear Algebra | knowledge/linear-algebra/ | INDEX_LINALG.md (on first concept) |
| STOCH | Stochastic Processes & Calculus | knowledge/stochastics/ | INDEX_STOCH.md (on first concept) |
| ANLY | Real Analysis & Calculus | knowledge/analysis/ | INDEX_ANLY.md (on first concept) |
| ALGO | Algorithms & Data Structures | knowledge/algorithms/ | INDEX_ALGO.md (on first concept) |
| STAT | Statistics (inference, regression, estimation) | knowledge/statistics/ | INDEX_STAT.md (on first concept) |
| OPT | Optimization & Operations Research | knowledge/optimization/ | INDEX_OPT.md (on first concept) |
| NUMER | Numerical Methods (Monte Carlo, PDE, FD) | knowledge/numerical/ | INDEX_NUMER.md (on first concept) |
| FINM | Financial Mathematics (pricing, Greeks, no-arbitrage) | knowledge/financial-math/ | INDEX_FINM.md (on first concept) |
| — | Proof Techniques (cross-cutting, `T-` IDs) | knowledge/techniques/ | INDEX_TECH.md (exists) |

New domain: add a row here, then use it. Folders and domain indexes are created with the first concept file.

## Domain Index Template

```markdown
# INDEX_{DOM} — {Domain Name}

| ID | Concept | File | Mastery | Priority | Links |
|---|---|---|---|---|---|
| C-{DOM}-001 | {name} | C-{DOM}-001_{slug}.md | 2/5 | 1 | C-..., T-... |
```
