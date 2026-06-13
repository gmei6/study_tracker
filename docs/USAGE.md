# USAGE.md — Exact Commands & Prompts

> Copy-paste playbook. Two kinds of "commands": **prompts** you give the AI (in a chat with the study_tracker folder selected) and **git commands** you run in Terminal. Nothing else is required.

## 1. Start a study session (new chat)

Select the study_tracker folder, then paste:

```
Read SYSTEM.md, GOALS.md, then DASHBOARD.md, due rows in review/QUEUE.md, and open
BLOCKERS. Run the session start protocol: give me my due recalls (priority
then age, cap 15), then a study recommendation.
```

Do the recalls *from memory* before opening any concept file. Report results in the same chat:

```
Recall results: {item} pass, {item} fail (what went wrong), ...
```

The AI updates QUEUE rows and last-review lines.

## 2. Ingest after studying (the core loop)

In the same chat (or a new one — include the session-start prompt first if new), paste raw notes:

```
Ingest this session.
Duration: {min} | Effort: {1–5} | Source: {book/site + chapter/problem ref}
{raw notes, verbatim — keep your confusion in, tag as you go:}
[STRUGGLE] [INSIGHT] [NEEDS_RECALL] [INTERVIEW]
```

The AI runs Full Ingest per SYSTEM.md (log → concepts/techniques → mistakes → queue → indexes → DASHBOARD/GOALS). It will ask before writing if anything is ambiguous — answer, don't let it guess.

**Short on time?** Say `Quick ingest` instead — notes get logged with `[PENDING_EXTRACT]`. Clear pending extractions within the week:

```
Process all pending extractions from DASHBOARD.
```

### 2b. Studying with a separate LLM? Make it your scribe

If you study alongside a different AI (tutoring, working problems), paste this **at the start** of that session. It makes that AI compile the ingest message for you, so nothing is lost in translation:

```
You are my study scribe. Alongside helping me study, track this session and
— when I say "generate the ingest message" — produce ONE copy-paste block in
EXACTLY this format:

Ingest this session.
Duration: {min} | Effort: {1–5} | Source: {book/site + chapter/problem ref}
{my notes}

Rules for {my notes}:
1. First person, my words. Reconstruct from what I actually said and did —
   lightly cleaned, never paraphrased into generic summaries. Mistakes, dead
   ends, and confusion MUST stay in: they are the most valuable data.
2. Append these tags inline where they apply:
   [STRUGGLE]     — anything I got wrong, blanked on, or fought with;
                    state specifically what went wrong
   [INSIGHT]      — a trick, intuition, or connection worth keeping
   [NEEDS_RECALL] — anything I failed or said I should re-drill
   [INTERVIEW]    — problems with quant-interview flavor; include the
                    full problem statement
3. Distinguish what I derived from what YOU explained to me. If you taught it
   and I only followed along, write "explained to me, not yet reproduced
   [NEEDS_RECALL]" — do not phrase your work as my understanding.
4. Exact references (chapter, page, problem #) when known. Never invent a
   reference, duration, time, or result — ask me for anything missing.
5. Before outputting, ask me three things: duration, effort (1–5), and any
   struggle I haven't mentioned. One ingest block per source; two sources =
   two blocks.
```

Then paste the generated block into a tracker chat (with the study_tracker folder selected) — it goes through the normal Full Ingest.

**Why rule 3 exists:** the tracker's mastery scores and queue admissions are built from what *you* can do. An LLM's clean explanation pasted as your own notes would inflate mastery and corrupt the review system at its source.

## 3. Commit after every ingest (Terminal)

```bash
cd ~/Downloads/study_tracker
git add -A && git commit -m "S-YYYY-MM-DD-n: {topic}" && git push
```

Architecture changes use `arch: {what}` as the message. Never force-push.

## 4. Periodic reviews

**Weekly** (end of study week):

```
Run the weekly review: append a snapshot to review/SNAPSHOTS.md, update the
DASHBOARD pointer and pace metrics, flag queue backlog trend, confirm pending
extractions are zero.
```

**Monthly** (due date in GOALS.md § Review Schedule):

```
Run the monthly review per SYSTEM.md: GOALS checklist + Progress Metrics vs
targets, DRILL_RESULTS trends, overdue contacts (next action date < today),
append a Milestone Review Log entry, set the next review date.
```

**Quarterly:** same prompt with "quarterly" — adds threshold/milestone recalibration and a CONNECTIONS.md pattern review.

Commit reviews too: `git commit -m "arch: monthly review YYYY-MM"`.

## 5. Other situations

| Situation | Prompt |
|---|---|
| Timed drill block done | `Log this drill block in DRILL_RESULTS: {type, Q-IDs, scores, times}` |
| Read a paper | `Ingest paper: {title, authors, takeaways, depth}` → P-ID |
| Research idea struck | `Log research idea: {one line, origin}` → R-ID |
| Met/emailed a contact | `Update CONTACTS: {name, what happened, next action + date}` |
| Queue feels overloaded | `Check overflow thresholds and tell me which mode we're in` |
| Changing the system itself | `Propose this as an architecture change` → changelog entry first |

## 6. Rules that keep the system honest

- Recalls before new material, every session. 41+ due = emergency: no new material.
- Never edit `study_logs/` history or delete mistakes — status changes only.
- Mastery scores honest (5 = prove cold). A fail is data.
- If the AI ever writes review history anywhere but QUEUE.md, or stores a counter, stop it — single-source rules are the integrity guarantee.
- A review that isn't logged didn't happen. A session that isn't committed isn't safe.
