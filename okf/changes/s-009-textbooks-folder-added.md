---
type: Session Change
mutability: append-only
timestamp: 2026-06-14
---

## 2026-06-14 — docs/textbooks/ added; all three textbook sources confirmed and named

**Reason:** Three primary textbook sources confirmed on disk: Green Book (`a-practical-guide-to-quantitative-finance-interviews.pdf`), *Linear Algebra Done Right* 4th ed. (`Linear Algebra Done Right, 4th edition, by Sheldon Axler.pdf`), and *Introduction to Stochastic Processes* 2nd ed. — Gregory F. Lawler (`Introduction to stochastic process-lawler_text.pdf`). All three PDFs placed by Gary in `docs/textbooks/pdf_version/`. MD conversions folder `docs/textbooks/md_version/` established (all entries pending — created lazily). Source names updated throughout to full textbook titles. Note: an initial version of this change incorrectly used the singular path `docs/textbook/`; corrected to `docs/textbooks/` (plural) to match the folder Gary created. Stale INDEX files left at `docs/textbook/` as redirect stubs.

**Files affected:**
- Created: `docs/textbooks/pdf_version/INDEX.md`, `docs/textbooks/md_version/INDEX.md`
- Modified (redirect stubs): `docs/textbook/pdf_version/INDEX.md`, `docs/textbook/md_version/INDEX.md`
- Modified: `DASHBOARD.md` (source names → full textbook titles; corrected folder path)
- Modified: `SYSTEM.md` (docs/textbooks/ added to architecture description)
- Modified: `README.md` (docs/textbooks/ added to layout table; stochastics title filled in)
- Modified: `docs/USAGE.md` (textbook context: generic template → two specialized blocks; stochastics title filled in)

**Expected benefit:** Single authoritative location for source files; session context (source, domain, log) unambiguous per textbook; scribe prompts require only chapter/section fill-in.

**Reversibility:** Delete `docs/textbooks/`; revert name changes in DASHBOARD.md, SYSTEM.md, README.md; restore generic template in USAGE.md.
