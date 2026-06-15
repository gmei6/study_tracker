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

| M-019 | 2026-06-14 | ALGO | Grid boundary check relied on implicit IndexError — Python negative indices wrap silently (`board[-1]` valid), so boundary violations went undetected | Must always check `0 <= i < m and 0 <= j < n` explicitly; see T-018 | 1 | S-2026-06-14-3 | active |
| M-020 | 2026-06-14 | ALGO | `enumerate[board]` instead of `enumerate(board)` — used [] (indexing) instead of () (function call), causing TypeError | Syntax confusion: function calls use (), not [] | 1 | S-2026-06-14-3 | active |
| M-021 | 2026-06-14 | ALGO | Grid DFS recursed on same cell (i, j) instead of neighbors (i±1, j±1) | Wrong recursive targets — DFS explores neighbors, not current cell | 1 | S-2026-06-14-3 | active |
| M-022 | 2026-06-14 | ALGO | Missing `self.` prefix for recursive DFS method call inside class | Forgot Python class method call syntax in recursive context | 1 | S-2026-06-14-3 | active |
| M-023 | 2026-06-14 | ALGO | Permanently mutated board with '#' without restoring after recursion — no backtracking | Missing backtrack step: must restore `board[i][j] = tmp` after recursive block; see T-018 | 1 | S-2026-06-14-3 | active |
| M-024 | 2026-06-14 | ALGO | Couldn't identify Trie as optimization for multi-word grid search — proposed per-word DFS (TLE) | Didn't recognize that shared prefixes across many words map to a single Trie-guided DFS pass; see C-ALGO-003 | 1 | S-2026-06-14-3 | active |
| M-015 | 2026-06-14 | ANLY | Recalled sec(x) = 1/sin(x) instead of 1/cos(x) | Weak recall of reciprocal trig functions (sec/csc confusion) | 1 | S-2026-06-14-2 | active |
| M-016 | 2026-06-14 | ANLY | Set A=1 arbitrarily in partial fractions instead of solving for coefficients | Skipped systematic coefficient-solving; see T-017 | 1 | S-2026-06-14-2 | active |
| M-017 | 2026-06-14 | ANLY | Factored the constant 1/2 out of ∫du/(1−u) as 2 instead of 1/2 | Reciprocal constant arithmetic slip | 1 | S-2026-06-14-2 | active |
| M-018 | 2026-06-14 | ANLY | Wrong evaluation order for FTC on −ln\|1−u\| term (sign/bound error) | Applied F(a)−F(b) instead of F(b)−F(a); negative from antiderivative compounded the confusion | 1 | S-2026-06-14-2 | active |
| M-013 | 2026-06-14 | PROB | Applied stars-and-bars to a set-distribution problem where elements can appear in multiple sets — model assumes disjoint partition | Conflated "distributing elements into bins" with "partitioning" — stars-and-bars requires each element in exactly one bin | 1 | S-2026-06-14-1 | active |
| M-014 | 2026-06-14 | PROB | After recognizing overlap, summed (y+2 choose 2)·y! over y=10..20 — hit prime factor 19 dead end | Missed element-independence; tried aggregating over configurations instead of multiplying per-element choices; see T-015 | 1 | S-2026-06-14-1 | active |
| M-025 | 2026-06-14 | LINALG | Wrote addition formula $(a+bi)+(c+di)$ instead of multiplication $(a+bi)(c+di)$ when copying Definition 1.3 | Inattentive formula transcription — read "multiplication" but wrote the addition pattern | 1 | S-2026-06-14-4 | active |
| M-026 | 2026-06-14 | LINALG | Wrote $i \in \mathbb{F}$ conflating imaginary unit $i=\sqrt{-1}$ with index variable $i \in \{1,\dots,n\}$ (Notation 1.6) | Symbol overloading — same letter $i$ carries two meanings; must read surrounding context to disambiguate | 1 | S-2026-06-14-4 | active |
| M-027 | 2026-06-14 | LINALG | Wrote $n \in \mathbb{R}^+$ instead of $n \in \mathbb{Z}^+$ for list length in $\mathbb{F}^n$ | Type error — list length is a count (integer), not a measure (real); see C-LINALG-002 | 1 | S-2026-06-14-4 | active |
| M-028 | 2026-06-14 | LINALG | Squaring $\omega=-\frac{1}{2}+\frac{\sqrt{3}}{2}i$: wrote $3/2$ for $\left(\frac{\sqrt{3}}{2}\right)^2$ instead of $3/4$ | Arithmetic slip squaring a fractional coefficient; $\left(\frac{\sqrt{3}}{2}\right)^2 = \frac{3}{4}$, not $\frac{3}{2}$ | 1 | S-2026-06-14-4 | active |
| M-029 | 2026-06-14 | LINALG | Second cube-root attempt: two sign errors cancelled — forgot $i^2=-1$ when computing $\omega^2$ (wrote $1/4+3/4=1$ instead of $1/4-3/4=-1/2$), then sign error in final multiply masked the first | Failed to apply $i^2=-1$; complex arithmetic sign tracking; getting the right answer via cancelling errors is a false pass | 1 | S-2026-06-14-4 | active |
| M-030 | 2026-06-14 | LINALG | Square roots of $i$: left answer as $\pm\sqrt{i}$ and $\pm(-1)^{1/4}$ rather than standard $a+bi$ form | Stopped too early — task requires standard form; should apply T-020 (component equations) to complete; see T-020 | 1 | S-2026-06-14-4 | active |

## Recurrence Watchlist (count ≥ 2)

| ID | Domain | Root cause | Count |
|---|---|---|---|
| M-011 | ALGO | Mixed slice + index in recursive traversal; rule not internalized | 2 |
| M-012 | ALGO | Incomplete wildcard base case — forgetting `curr.word` check at end of dot | 2 |
