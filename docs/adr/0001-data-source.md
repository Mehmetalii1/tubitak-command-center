# 0001. Data Source

> Freeze note: this ADR is a refactor target, not an append target. The detailed
> candidate research, verification plans, evidence notes, readiness summaries, and
> advisor material now live under `docs/decisions/data-source/`. Do not append new
> sections here; add evidence in that folder and keep this ADR at template shape.

## Status

Proposed

## Context

The data source for the 13C NMR functional group prediction project has not been approved yet.

This decision comes first because the selected data source will constrain the label set, 13C NMR representation strategy, leakage risk, scaffold split feasibility, and minimum evaluation protocol.

During Phase 1A, this ADR records working assumptions only. It does not select a specific data source, authorize data download, or start the scientific pipeline.

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

- Which candidate sources satisfy both 13C NMR availability and molecular structure availability?
- What license or access limitations apply to each candidate source?
- Does each source provide experimental spectra, calculated spectra, or mixed records?
- Are metadata fields sufficient to reproduce filtering and selection?
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

Pending Mehmetali approval. No specific source is selected.

## Consequences

No data download, processing, experiment, or run logging should start from this ADR.

The data source decision remains open until candidate sources are compared against the criteria above and Mehmetali approves a specific direction.

## Review Trigger

Review when candidate data sources are ready to compare, when source access/license details are known, or when Mehmetali is ready to approve a specific source direction.
