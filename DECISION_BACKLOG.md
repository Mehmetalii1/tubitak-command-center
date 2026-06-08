# DECISION_BACKLOG.md

This file lists unresolved decisions.

A decision listed here is not yet accepted.

## Pending Scientific Decisions

- Data source (pending; working assumptions drafted in ADR 0001; candidate research completed; focused verification completed; decision discussion prepared for NP-MRD vs NMRShiftDB2; final decision not approved)
- Label set definition
- 13C NMR representation strategy
- Feature extraction strategy
- Scaffold split method
- Baseline model
- Minimum acceptable evaluation protocol
- Proposal scope

## Data Source Backlog Note

- Focused verification completed for NP-MRD, NMRShiftDB2, and HMDB.
- Decision discussion prepared for NP-MRD vs NMRShiftDB2.
- The two real open decisions (NMRShiftDB2 license yes/no; NP-MRD vs NMRShiftDB2 narrative/scope) are framed neutrally for Mehmetali in docs/decisions/data-source/DECISION_NOTE.md.
- HMDB remains a fallback/comparison candidate until the experimental/predicted 13C split is checked.
- This is not a source selection.

## Pending Setup / Governance Decisions

- First learning gate to work on: resolved. GATE_01 (multi-label classification) is the selected first gate; full order in learning/PROJECT_CONCEPT_DEPENDENCIES.md. Gates remain Not started; this is sequencing, not passing.
- First scientific-preparation task
- Timing for Phase 1 start

## Rule

Do not treat backlog items as settled decisions.
Move important accepted decisions into ADRs only after Mehmetali approval.
