# PHASE_RULES.md

## Phase 0 Rule

Phase 0 is Command Center setup only.

It may create:

- repository memory files
- governance files
- protocol templates
- ADR placeholders
- experiment tracking scaffolds
- placeholder scientific folders
- learning gates
- literature placeholders
- proposal placeholders
- audit checklists
- setup-safe tests and CI

It may not create scientific implementation or scientific results.

## Phase Boundary Rule

Moving from Phase 0 to Phase 1 requires Mehmetali approval.

## Project Invariants

- Topic: 13C NMR spectra -> functional group prediction
- Problem type: multi-label classification
- Main metric: macro F1 + per-class F1
- Evaluation must consider scaffold-aware splitting
- Repository role during setup: Command Center, not scientific experiment
- Data safety: do not modify `data/raw/`

