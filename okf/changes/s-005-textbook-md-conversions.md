---
type: Session Change
mutability: append-only
timestamp: 2026-06-15
---

## 2026-06-15 — Textbook MD conversions: folder-per-book structure

**Reason:** All three planned textbooks were converted from PDF to MD ahead of use (not lazily). The conversion tool produced a folder-per-book layout rather than single flat files, which also accommodates extracted images and ToC metadata.

**Files affected:**
- Created: `docs/textbooks/md_version/a-practical-guide-to-quantitative-finance-interviews/` (Green Book — full MD text, `_meta.json`, `_page_*.jpeg`)
- Created: `docs/textbooks/md_version/Linear Algebra Done Right, 4th edition, by Sheldon Axler/` (LADR 4e — full MD text, `_meta.json`, `_page_*.jpeg`)
- Created: `docs/textbooks/md_version/Introduction to stochastic process-lawler_text/` (Lawler — full MD text, `_meta.json`, `_page_*.jpeg`)
- Modified: `docs/textbooks/md_version/INDEX.md` (paths updated to folder names; status → Created for all 3; header updated to describe folder-per-book format)
- Modified: `SYSTEM.md` (Architecture section: md_version description updated to folder-per-book format with `_meta.json` and image files)
- Modified: `DASHBOARD.md` (Source Log Status footnote: "created lazily" → "all 3 converted; each in its own subfolder")

**Expected benefit:** All textbooks immediately referenceable in-chat without PDF upload. `_meta.json` per book provides structured ToC with page-level polygons for precise section lookup. Images rendered inline via relative paths in the MD.

**Reversibility:** Delete the three created folders; restore INDEX.md, SYSTEM.md, DASHBOARD.md lines from this entry.
