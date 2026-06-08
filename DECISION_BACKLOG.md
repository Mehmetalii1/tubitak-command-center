# DECISION_BACKLOG.md

This file lists unresolved decisions.

A decision listed here is not yet accepted.

## Pending Scientific Decisions

- Label set definition
- 13C NMR representation strategy
- Feature extraction strategy
- Scaffold split method
- Baseline model
- Minimum acceptable evaluation protocol
- Proposal scope

## Data Source Decision Note

- ADR 0001 is Accepted: NMRShiftDB2 is conditionally accepted as the first active data source.
- This is reversible / conditional acceptance, not a completed scientific pipeline.
- NP-MRD is deferred as a secondary candidate, not rejected.
- HMDB remains a fallback / comparison candidate.
- NMRShiftDB2 license, attribution/share-alike obligations, usable measured 13C subset count, assignment quality, and export practicality remain blocker areas for the first separately approved verification task.

## Pending Setup / Governance Decisions

- First learning gate to work on: resolved. GATE_01 (multi-label classification) is the selected first gate; full order in learning/PROJECT_CONCEPT_DEPENDENCIES.md. Gates remain Not started; this is sequencing, not passing.
- First scientific-preparation task
- Timing for Phase 1 start

## Rule

Do not treat backlog items as settled decisions.
Move important accepted decisions into ADRs only after Mehmetali approval.
