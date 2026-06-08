# STATE.md

## Current Phase

Phase 1A - readiness / scientific preparation planning (now formally defined in ROADMAP.md and governance/PHASE_EXIT_CRITERIA.md)

## Repository Role

This repository is a Codex-based Command Center for the TUBITAK 2209-A 13C NMR functional group prediction project.

It manages memory, planning, learning gates, evidence, proposal scaffolding, audits, and governance.

It does not yet implement the scientific pipeline.

## Current Status

- Command Center setup: closed by initial Phase 0 commit
- Phase 1A: formally defined in ROADMAP.md and governance/PHASE_EXIT_CRITERIA.md, including a decision-stall rule for blocked/uncertain count items and a now-approved data-source direction
- Phase 0 no-go and setup boundaries remain active during Phase 1A unless Mehmetali explicitly approves a later scientific task
- Scientific pipeline: Not started
- Learning gates: Created, all Not started, none Passed
- Experiment tracking: Header-only scaffold
- Proposal: Draft placeholders only
- Literature: Phase 1A evidence notes only; no final proposal/literature text
- ADRs: ADR 0001 Accepted; ADR 0002 and ADR 0003 Proposed
- Data source: NMRShiftDB2 is conditionally accepted as the first active data source in ADR 0001; NP-MRD is deferred as a secondary candidate, and HMDB remains fallback / comparison
- Data source acceptance boundary: this does not authorize data download, parser/loader work, processed data, notebook creation, split implementation, model implementation, evaluation, benchmark, score reporting, or run logging
- Minimal notebook-support Codex skills installed in repo-local `.agents/skills`: `rdkit`, `scikit-learn`, `matplotlib`, and `markdown-mermaid-writing`; this does not authorize data download, notebook creation, preprocessing, feature extraction, modeling, evaluation, new source selection, new planning, or governance expansion
- NMRShiftDB2 blocker areas: license, attribution/share-alike obligations, usable measured 13C subset count, assignment quality, and export practicality remain to be verified in separately approved first real notebook or verification tasks
- Data source evidence/discussion notes: docs/decisions/data-source/ remains the centralized historical/pre-decision evidence folder; older notes remain useful context but do not start the scientific pipeline
- First Prototype Preparation Track: created as a conceptual learning/preparation track for Mehmetali; no data download, learning gate pass, scientific implementation, or model code started
- Learning gate system: operationalized (dependency order set, GATE_01 selected first, evidence format defined in learning/learning_logs/README.md); gates remain Not started
- Conceptual prototype-shape map: learning/PROTOTYPE_SHAPE.md created (concept-level stages linked to gates); no code, data, counts, labels, split, model, or evaluation
- RDKit Learning Module: the existing NMRShiftDB2 NMReDATA example remains a learning sample / pilot example only; it is not the final dataset, model-ready subset, benchmark, or evidence that pipeline work has started
- RDKit Learning Module: existing 00/01 notebooks are educational and audited; this decision creates no new notebook and changes no notebook outputs
- Data downloaded: No
- Raw data changed beyond README: No

## Next Step

Plan the first NMRShiftDB2 blocker verification task while keeping data download, parser/loader work, processed data, notebooks, split, modeling, evaluation, and run logging blocked until separately approved.

## Pending User Decisions

- Confirm scientific pipeline start timing
- Confirm first NMRShiftDB2 verification task
- Confirm first learning gate to work on
- Confirm first scientific-preparation task
