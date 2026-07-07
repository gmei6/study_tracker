---
mutability: live
type: concept
---

# Identity

- **What:** study_tracker — a two-layer personal knowledge system for quant preparation. An
  append-only event layer (`study_logs/`) is separated from an editable knowledge graph
  (`knowledge/`), with control loops for retention (`review/`), interview readiness
  (`interview/`), and research pipeline (`research/`) wired between them.
- **Whose:** Gary's personal system. One user, LLM-operated: Gary studies and pastes raw notes;
  an AI runs the ingest/review protocols.
- **Core rule:** every update costs O(new information) — the system never rereads its own history
  to function.
- **Operating manual:** `SYSTEM.md` (read first in any new session). Overview: `README.md`.
  Playbook of exact prompts: `docs/USAGE.md`.
- **This bundle:** `okf/` is the structural/meta memory layer — architecture decisions, structural
  changes, and project-level state. It points at the operational docs and never re-homes study
  data.
