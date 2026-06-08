# PROJECT_INVARIANTS.md

These are non-negotiable project invariants.

## Scientific Core

- Topic: 13C NMR spectra -> functional group prediction
- Problem type: multi-label classification
- Main metric: macro F1 + per-class F1
- Evaluation must consider scaffold-aware splitting

## Repository Core

- Phase 0 setup is closed; this repository remains a Command Center during Phase 1A.
- It does not implement the scientific pipeline during Phase 1A without explicit approval.
- It manages memory, planning, learning, evidence, proposal scaffolding, and audits.

## Responsibility Core

- Codex may assist, scaffold, draft, and propose.
- Codex may not finalize scientific truth alone.
- Mehmetali must understand and approve major scientific decisions.

## Safety Core

- Do not modify `data/raw/`.
- Do not invent citations.
- Do not mark gates as passed without evidence.
- Do not report fake experiment results.
