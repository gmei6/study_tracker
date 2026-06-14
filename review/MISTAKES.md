# Mistake Database

> Append-only registry of mistakes with root-cause analysis. Recurrence ≥ 3 ⇒ escalate to BLOCKERS.md. Mistakes are never deleted — they are data.

## Format

`M-{NNN}` | date | domain | what happened | **root cause** | recurrence count | sessions where it recurred | status (active / dormant ≥ 60d clean)

## Mistakes

| ID | Date | Domain | What happened | Root cause | Recurrence | Sessions | Status |
|---|---|---|---|---|---|---|---|
| M-001 | 2026-06-12 | ANLY | Misread $\ln x^{\ln x}$ as $\ln(x^{\ln x})$ instead of $(\ln x)^{\ln x}$ | Notation ambiguity / inattentive reading | 1 | S-2026-06-12-1 | active |
| M-002 | 2026-06-12 | ANLY | Forgot $\frac{1}{y}\frac{dy}{dx}$ on LHS during log diff; tried $e^{\ln y}$ in a circle | Incomplete implicit-diff setup — forgot chain rule on $\ln y$ | 1 | S-2026-06-12-1 | active |
| M-003 | 2026-06-12 | ANLY | Recalled $e \approx 1.2$ instead of $\approx 2.718$ | Weak constant recall | 1 | S-2026-06-12-1 | active |
| M-004 | 2026-06-12 | ANLY | Integer approx ($e=2, \pi=3$) gave wrong inequality $\pi^e > e^\pi$ | Approximation error larger than actual gap; misleading heuristic | 1 | S-2026-06-12-1 | active |
| M-005 | 2026-06-12 | ANLY | Drew $\ln x \to +\infty$ as $x \to 0^+$ (should be $-\infty$) | Wrong mental graph of $\ln x$ near zero | 1 | S-2026-06-12-1 | active |
| M-006 | 2026-06-12 | ANLY | Rewrote $x^2\ln x$ as $x^2/\ln x$ for L'Hôpital (should be $\ln x / x^{-2}$) | Confused which factor to invert in $0\cdot\infty \to \infty/\infty$ conversion | 1 | S-2026-06-12-1 | active |
| M-007 | 2026-06-12 | ANLY | Computed $\frac{2x}{1/x} = 2$ instead of $2x^2$ | Compound fraction arithmetic slip | 1 | S-2026-06-12-1 | active |
| M-008 | 2026-06-13 | ANLY | L'Hôpital recall: stated $0/0$ and $\infty/\infty$ cases correctly but did not cover form-rewrite table ($0\cdot\infty$, $1^\infty$, $0^0$, $\infty^0$) or reproduce canonical problem 2 ($\lim_{x\to0^+}x^2\ln x$) | Scope of recall too narrow — internalized theorem statement only, not the extended forms or canonical application | 1 | review-2026-06-13 | active |
| M-009 | 2026-06-13 | ALGO | Python string slicing direction backwards — thought `temp[:3]` gets last 3 chars; it's first 3 | Rusty Python slice semantics; `s[:k]` = first k chars, `s[k:]` = from index k onward | 1 | S-2026-06-13-1 | active |
| M-010 | 2026-06-13 | ALGO | Non-dot else branch in recursive Trie search fell through to `return True` after advancing curr/index, without processing remaining chars | Missing check — else branch must either recurse or loop; cannot fall through | 1 | S-2026-06-13-1 | active |
| M-011 | 2026-06-13 | ALGO | Passed `word[plus_one:]` (sliced string) AND `plus_one` as index into it — index was past the end of the shorter string | Mixed index advancement and slicing simultaneously; see T-014 | 2 | S-2026-06-13-1, review-2026-06-14 | active |
| M-012 | 2026-06-13 | ALGO | Early `return True` when dot is last char (`index == len(word)-1`) skips checking `curr.word` — incorrectly matches paths that aren't complete words | Incomplete base case; must check `curr.word` even at end of wildcard | 2 | S-2026-06-13-1, review-2026-06-14 | active |

| M-013 | 2026-06-14 | PROB | Applied stars-and-bars to a set-distribution problem where elements can appear in multiple sets — model assumes disjoint partition | Conflated "distributing elements into bins" with "partitioning" — stars-and-bars requires each element in exactly one bin | 1 | S-2026-06-14-1 | active |
| M-014 | 2026-06-14 | PROB | After recognizing overlap, summed (y+2 choose 2)·y! over y=10..20 — hit prime factor 19 dead end | Missed element-independence; tried aggregating over configurations instead of multiplying per-element choices; see T-015 | 1 | S-2026-06-14-1 | active |

## Recurrence Watchlist (count ≥ 2)

| ID | Domain | Root cause | Count |
|---|---|---|---|
| M-011 | ALGO | Mixed slice + index in recursive traversal; rule not internalized | 2 |
| M-012 | ALGO | Incomplete wildcard base case — forgetting `curr.word` check at end of dot | 2 |
