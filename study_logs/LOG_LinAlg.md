# Subject Log: Linear Algebra

> **Scope:** Linear Algebra concepts, proofs, and theorems.
> **Protocol:** APPEND-ONLY. Add new entries to the bottom via file-system tools. Never delete or summarize past entries.

---

*Log initialized: 2026-06-11. Session entries are appended below in chronological order.*

---

## S-2026-06-14-4 — Complex numbers & lists (LADR 1A)
- Duration: 53 | Effort: 2
- Source: Axler, Linear Algebra Done Right, 4th ed., Ch 1, Section 1A

Complex number $a+bi$, $a,b \in \mathbb{R}$, $i=\sqrt{-1}$. Real numbers are a subset of ℂ (technically $3 = 3+0i$). My example: $3+2i$. Non-example: $3$ alone — we call it real in practice even though it is $3+0i$.

Copied multiplication definition as addition instead [STRUGGLE → M-025].

Complex arithmetic properties — commutativity, associativity, additive/multiplicative inverses. Proved multiplication commutativity: let $\alpha=a+bi$, $\beta=c+di$; then $\alpha\beta=(ac-bd)+(ad+bc)i$ and $\beta\alpha=(ca-db)+(cb+da)i$, equal by real commutativity [reproduced]. Multiplicative associativity not shown in book; proof not reproduced [NEEDS_RECALL]. Verified additive inverse $\alpha+(-\alpha)=0$ coordinate-wise [reproduced]. Wrote $\alpha\cdot\frac{1}{\alpha}=1$ for multiplicative inverse but did not reduce to standard $a+bi$ form — conjugate division method explained, not reproduced [NEEDS_RECALL → T-019].

Notation 1.6: wrote $i \in \mathbb{F}$ thinking imaginary unit rather than index variable [STRUGGLE → M-026]. Index $i \in \{1,\dots,n\}$ ≠ $i=\sqrt{-1}$ — same letter, different context.

Definition 1.8 (lists): sets don't care about order, lists do [INSIGHT — relates to CS visited sets in DFS; see C-ALGO-003]. Notation 1.10/1.11 ($\mathbb{F}^n$): wrote $n \in \mathbb{R}^+$ instead of $n \in \mathbb{Z}^+$ — list length must be a positive integer [STRUGGLE → M-027].

Exercises:
- Ex 1: Addition commutativity — $(a+bi)+(c+di)=(a+c)+(b+d)i=(c+a)+(d+b)i=\beta+\alpha$ [reproduced].
- Ex 9: $(4,-3,1,7)+2x=(5,9,-6,8)$ coordinate-wise → $x=(1/2,6,-7/2,1/2)$ [reproduced].
- Ex 7: Verify $\omega^3=1$ for $\omega=-\frac{1}{2}+\frac{\sqrt{3}}{2}i$. First attempt: wrote $3/2$ instead of $(\sqrt{3}/2)^2=3/4$ [STRUGGLE → M-028]. Second attempt: got 1 but via two cancelling sign errors — forgot $i^2=-1$ when computing $\omega^2$, then sign error in final multiply [STRUGGLE → M-029]. Shortcut $\omega^3=\omega^2\cdot\omega$ via difference of squares explained, not reproduced [NEEDS_RECALL].
- Ex 8: Square roots of $i$. Left as $\pm\sqrt{i}$, $\pm(-1)^{1/4}$ — did not find standard form [STRUGGLE → M-030]. Derivation: set $(a+bi)^2=i$, match real and imaginary parts to get $a^2-b^2=0$ and $2ab=1$, yielding $\pm(\frac{1}{\sqrt{2}}+\frac{1}{\sqrt{2}}i)$ — explained, not reproduced [NEEDS_RECALL → T-020].
