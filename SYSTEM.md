# SYSTEM.md — How the Quant Tracker Works (v2.2)

> Read this first in any new session. Architecture, ID scheme, ingest protocols, worked example, periodic reviews.

## Architecture

Two layers plus supporting systems:

1. **Event layer** — `study_logs/` — append-only chronological logs per *source*. What happened. Never edited, never summarized, never deleted.
2. **Knowledge layer** — `knowledge/` — one file per concept (by *domain*) and per proof technique (`knowledge/techniques/`). What's true. Updated in place.

Supporting: `review/` (queue, mistakes, blockers, snapshots), `interview/` (question bank, drills, firm profiles), `research/` (papers, ideas, contacts), `docs/textbooks/` (source textbooks: `pdf_version/` for PDFs, `md_version/` for converted MD versions created lazily), `DASHBOARD.md` (status + health), `GOALS.md` (milestones + metrics), `knowledge/CONNECTIONS.md` (cross-domain registry).

**Core rule:** every update is O(new information). Never reread entire logs to update state.

## Domains vs. Source Logs

A **source log** tracks where you studied (book, site, competition): Green Book, Leetcode, etc. A **domain** is where a concept *lives*: PROB, STOCH, etc. The mapping is **many-to-many** — one Green Book session may yield PROB, STOCH, and FINM concepts. Rule: log entry → the source's log; each extracted concept → its own domain. Never hesitate over this: source = where it came from, domain = what it is.

## ID Scheme

| Prefix | Entity | Lives in |
|---|---|---|
| `S-YYYY-MM-DD-n` | Study session | study_logs/ entries |
| `C-{DOM}-{NNN}` | Concept | knowledge/{domain}/ |
| `T-{NNN}` | Proof technique | knowledge/techniques/ |
| `M-{NNN}` | Mistake | review/MISTAKES.md |
| `B-{NNN}` | Blocker | review/BLOCKERS.md |
| `Q-{NNN}` | Interview question | interview/questions/ |
| `P-{NNN}` | Paper | research/READING_LOG.md |
| `R-{NNN}` | Research idea | research/IDEAS.md |

Domain codes: `PROB`, `LINALG`, `STOCH`, `ANLY`, `ALGO`, `STAT`, `OPT`, `NUMER`, `FINM`. Register new domains in `knowledge/INDEX.md` before use.

**ID rule:** next ID = highest existing in the entity's own index + 1. Counters derived, never stored twice. Per-domain indexes (`INDEX_{DOM}.md`) created lazily with first concept; root `INDEX.md` is registry only.

## Session Log Entry Format

```
## S-YYYY-MM-DD-n — {topic}
- Duration: {min} | Effort: {1–5} (optional but encouraged)
- Source: {book/site/lecture + ref}
{raw notes, verbatim where possible, with tags}
```

## Ingest Protocols

### Full Ingest (default)

1. **Clarify first** — ambiguity ⇒ ask before writing anything.
2. **Append log entry** to the source's `study_logs/LOG_*.md`.
3. **Extract concepts/techniques** → new or updated `C-`/`T-` files; typed edges (prereq/extends/relates); cross-domain `relates` edges also registered in `knowledge/CONNECTIONS.md`.
4. **Extract mistakes** → `review/MISTAKES.md`; same root cause ⇒ increment recurrence; ≥ 3 ⇒ escalate to `review/BLOCKERS.md`.
5. **Queue admissions** (gate: failed recall OR priority 1–2; respect overflow thresholds in QUEUE.md).
6. **Interview problems** → `interview/questions/QBank_*.md` (lazy), register Q-ID.
7. **Update domain index** (+ root registry if new domain).
8. **Update DASHBOARD** (status, Domain Mastery, **System Health**) and **GOALS.md Progress Metrics** for touched domains. Weekly boundary ⇒ append snapshot to `review/SNAPSHOTS.md`, update DASHBOARD one-line pointer.

### Quick Ingest (time-pressed)

1. Append log entry with `[PENDING_EXTRACT]`.
2. Increment DASHBOARD session count + health panel.
3. Add to DASHBOARD § Pending Extractions. Clear before each new week.

## Worked Example (synthetic — illustrative only, consumes no IDs)

**Raw notes:** *"45 min Green Book ch.4. Bayes: P(A|B)=P(B|A)P(A)/P(B). Solved the false-positive disease problem — got 0.5 first try [STRUGGLE], forgot base rate. Redid via odds form, much faster [INSIGHT]. Need to redrill [NEEDS_RECALL]."*

**1 — Log entry** (`study_logs/LOG_GreenBook.md`):
```
## S-2026-06-15-1 — Bayes & base rates (GB ch.4)
- Duration: 45 | Effort: 3
- Source: Green Book ch.4
Bayes via odds form. False-positive problem failed first attempt [STRUGGLE]:
ignored base rate. Odds form: posterior odds = prior odds × LR [INSIGHT].
Redrill the disease problem [NEEDS_RECALL].
```
**2 — Concept** `knowledge/probability/C-PROB-001_bayes-theorem.md`: Type: theorem; Mastery 2/5; Statement, odds-form intuition ("posterior odds = prior odds × likelihood ratio"); Canonical Problems: disease test (trap: base-rate neglect); edge `→ C-PROB-xxx : prereq — conditional probability`; Source S-2026-06-15-1.
**3 — Domain index** `INDEX_PROB.md` created (first PROB concept), row added.
**4 — Mistake** `M-001 | 2026-06-15 | PROB | answered 0.5 on disease problem | root cause: base-rate neglect | recurrence 1 | active`.
**5 — Queue row** `Bayes disease problem | C-PROB-001 | P1 | added 06-15 | rung 1d | due 06-16 | results: F`.
**6 — Dashboard:** sessions 0→1; PROB mastery row appears; health panel refreshed. **GOALS:** no metric touched.

First real session: do exactly this.

## Session Start Protocol

1. Read `DASHBOARD.md` (health first), due QUEUE rows, open BLOCKERS.
2. Due recalls *before* new material — priority then age, cap 15. Check overflow thresholds (QUEUE.md): 41+ due = emergency, no new material.
3. **Study recommendation:** largest gap between Domain Mastery and GOALS metrics; within domain, next concept by prereq ordering. Bias against comfortable domains.

## Review Tracking — Single Source of Truth

`review/QUEUE.md` owns all scheduling state (rung, due, streak) **and** the full result sequence (`Results` column, e.g. `F·P·P`). Concept/technique files carry only: `**Last review:** {date} — {pass/fail}`. One write per review (queue row), one summary-line touch. Never maintain parallel history tables.

## Connection Edge Types

`prereq` (requires) | `extends` (builds on) | `relates` (lateral) | `technique` (proof method, → T-ID). Prereq edges form the study-order graph. Cross-domain `relates` edges are additionally registered in `knowledge/CONNECTIONS.md` at ingest — synthesis is captured from concept #1, never retrofitted.

## Periodic Reviews

- **Weekly:** snapshot → `review/SNAPSHOTS.md`; queue backlog trend; clear Pending Extractions.
- **Monthly:** GOALS checklist + Progress Metrics vs targets; DRILL_RESULTS trends; Milestone Review Log entry; set next review date in GOALS.md.
- **Quarterly:** mini architecture review; recalibrate thresholds and milestones.

Concrete next-due dates live in GOALS.md § Review Schedule. A review that isn't logged didn't happen.

## Maintenance Triggers (act when fired, not before)

- `LOG_*.md` > 500 entries ⇒ yearly split (`LOG_X_2027.md`); newest file is the append target; old files untouched.
- `MISTAKES.md` > 50 entries ⇒ reorganize under domain headings (content unchanged).
- DASHBOARD unreadable in 2 min ⇒ structural review.

## Version Control

Repo should be a git repo (`git init` once, manually). Commit after every ingest: `S-YYYY-MM-DD-n: {topic}`; architecture changes: `arch: {what}`. Never force-push. `.gitignore` covers OS noise. Git is the real reversibility guarantee; the changelog is the human-readable layer.

## Tag Vocabulary

`[STRUGGLE]` → mistake/blocker | `[NEEDS_RECALL]` → queue (gated) | `[INSIGHT]` → concept note | `[INTERVIEW]` → question bank | `[PENDING_EXTRACT]` → DASHBOARD pending list.

## Invariants

- `study_logs/` append-only. Historical knowledge is sacred.
- Mistakes/blockers never deleted — status changes only.
- Structural changes → `docs/ARCHITECTURE_CHANGELOG.md`, reversible.
- One concept, one file; reference by ID everywhere else.
- Counters derived, never stored twice. Review state lives in QUEUE.md only.
- No fabricated data: examples are marked synthetic; metrics reflect logged work only.
