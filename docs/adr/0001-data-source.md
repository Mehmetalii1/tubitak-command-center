# 0001. Data Source

> Freeze note: this ADR is a refactor target, not an append target. The detailed
> candidate research, verification plans, evidence notes, readiness summaries, and
> advisor material now live under `docs/decisions/data-source/`. Do not append new
> sections here; add evidence in that folder and keep this ADR at template shape.

## Status

Accepted

## Context

The first active data source for the 13C NMR functional group prediction project has now been conditionally approved.

This decision comes first because the selected data source will constrain the label set, 13C NMR representation strategy, leakage risk, scaffold split feasibility, and minimum evaluation protocol.

During Phase 1A, this ADR selects the data-source direction only. It does not authorize data download, parser/loader work, processed data creation, split implementation, modeling, evaluation, or experiment run logging.

## Current working assumptions

- Real experimental 13C NMR data is preferred. Calculated or simulated data may be considered only as fallback, prototype material, or auxiliary comparison.
- The source should be as open, accessible, and reproducible as possible. Source identity, access date, version, filtering steps, and selection rationale must be documentable.
- Functional group labels do not have to be provided directly. Rule-based and documented label extraction from molecular structure may be acceptable, but label extraction must be handled as a separate decision and audit topic later.
- A small or medium-sized source that is explainable and defensible is preferred over a large but noisy or unclear source. Scale can be increased later.
- TUBITAK defensibility priority is: explainability, reproducibility, chemical defensibility, scaffold-aware evaluation suitability, then scale.
- Molecular structure information is required. Without SMILES, InChI, or an equivalent structural representation, scaffold split and leakage control become weak.

## Decision criteria

- Contains usable 13C NMR information.
- Contains molecule identity and preferably structure representation.
- Supports direct or defensible functional group label extraction.
- Has clear license, access, and academic-use conditions.
- Can be reproduced through documented source, version, access date, and filtering steps.
- Supports scaffold-aware evaluation and leakage analysis.
- Is explainable in a TUBITAK context without overstating scientific certainty.
- Keeps initial Phase 1A work small enough to review and audit.

## Open questions

- Are NMRShiftDB2 license, attribution, share-alike, derivative-database, and software-license obligations acceptable for the intended repository, notebooks, publication path, and any future derived dataset?
- What is the usable measured 13C NMR subset count after approved project filters?
- Is assignment quality sufficient for the first defensible project subset?
- Are NMRShiftDB2 exports practical enough for a small, auditable first pipeline?
- Can functional group labels be derived consistently from the available structure representation?
- Is the source large enough for meaningful per-class evaluation after label filtering?

## Relocated evidence and discussion

The detailed candidate research, verification plans, evidence notes, readiness
summaries, and advisor material that previously lived in this ADR now sit under
`docs/decisions/data-source/`:

- `candidate-research.md` - candidate shortlist, focused verification, and the NP-MRD vs NMRShiftDB2 decision-discussion comparison.
- `verification-and-evidence.md` - remaining verification checklist, must-answer evidence collection plan, per-candidate evidence notes, feasibility note, and compact readiness summary.
- `advisor-discussion.md` - advisor/owner discussion agenda, questions, and the blank discussion outcome template.

This ADR stays at template shape. New evidence and discussion go in those files, not here.

## Decision

Accepted: NMRShiftDB2 is the first active data source for the project.

This is a reversible / conditional acceptance. It resolves the first data-source direction enough to focus the next approved verification work, but it does not claim that all project-ready subset, license, attribution, assignment-quality, or export-practicality blockers are closed.

NP-MRD is not rejected. It is deferred as a secondary candidate if NMRShiftDB2 fails a blocker or becomes impractical.

HMDB remains a fallback / comparison candidate, not the primary source.

## Consequences

No data download, parser/loader work, processed data creation, notebook creation, split implementation, model implementation, evaluation, benchmark, score reporting, or run logging should start from this ADR.

ADR 0002 (scaffold split) and ADR 0003 (label set) remain Proposed. Learning gates remain evidence-gated and must not be marked Passed from this decision.

The first real approved NMRShiftDB2 notebook or verification task must explicitly check license/attribution/share-alike obligations, usable measured 13C subset count, assignment quality, and export practicality before scientific claims or pipeline work are made.

## Review Trigger

Review this ADR if NMRShiftDB2 fails a blocker, if its license or share-alike obligations conflict with the project plan, if the measured 13C subset is not usable enough after approved filtering, or if NP-MRD/HMDB needs to be reconsidered.
