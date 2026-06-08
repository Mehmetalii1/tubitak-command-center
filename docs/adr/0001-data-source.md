# 0001. Data Source

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

## Candidate Research Summary

Phase 1A concrete candidate research has been recorded in `literature/SOURCES.md` and `literature/CLAIMS.md`.

No data source has been selected.

This ADR remains `Proposed`.

The current shortlist is only a recommendation for further verification, not a decision:

- NP-MRD
- NMRShiftDB2
- HMDB

The shortlist is based on currently available evidence about 13C NMR relevance, molecular structure availability, license/reuse clarity, reproducibility, and scaffold-aware evaluation suitability. Each candidate still has unresolved verification questions before any source can be approved.

## Focused Verification Summary

Focused verification for NP-MRD, NMRShiftDB2, and HMDB was completed on 2026-06-08 and recorded in `literature/SOURCES.md` and `literature/CLAIMS.md`.

No data source has been selected.

This ADR remains `Proposed`.

The verification summary is preparation for decision discussion only, not a decision and not authorization to download data or start the scientific pipeline.

- NP-MRD appears ready for decision discussion. Public evidence supports bulk exports, structure fields, experimental/simulated/predicted distinction, and experimental 1D 13C presence. Remaining check: structure-linked usable experimental 1D 13C count after project filtering.
- NMRShiftDB2 appears ready for decision discussion. Public evidence supports 13C NMR handling, measured/calculated distinction, structure fields, and bulk exports. Remaining checks: measured 13C-only subset count and custom database license compatibility.
- HMDB remains promising but needs one more check. Public evidence supports metadata, structure fields, license clarity, and 13C NMR availability. Remaining check: current experimental versus predicted 13C separation and clean structure linkage.
- None of the three candidates currently provides a ready functional-group label set for this project. Structure-based label derivation remains a separate ADR/audit topic.

## Decision

Pending Mehmetali approval. No specific source is selected.

## Consequences

No data download, processing, experiment, or run logging should start from this ADR.

The data source decision remains open until candidate sources are compared against the criteria above and Mehmetali approves a specific direction.

## Review Trigger

Review when candidate data sources are ready to compare, when source access/license details are known, or when Mehmetali is ready to approve a specific source direction.
