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

## Data Source Decision Discussion

This section prepares a decision discussion only. It does not select a source, does not change this ADR from `Proposed`, and does not authorize data download, processing, experiments, or run logging.

HMDB is not treated as a main contender in this discussion. It remains a fallback/comparison candidate until its current experimental/predicted 13C split and clean structure linkage are checked.

| criterion | NP-MRD | NMRShiftDB2 | discussion note |
| --- | --- | --- | --- |
| 13C NMR suitability | Strong if the structure-linked usable experimental 1D 13C subset remains large enough after filtering. | Strong if the measured 13C-only subset is large enough after filtering. | Both are suitable for discussion; neither is approved without subset-count verification. |
| Experimental/predicted distinction | Public evidence supports experimental, simulated, and predicted categories. | Public evidence supports measured and calculated categories. | Both appear filterable in principle; exact project filter rules still need audit. |
| Structure-linked data availability | Public evidence supports SDF, SMILES, MOL/PDB, InChI, and InChIKey paths. | Public evidence supports SDF/NMReDATA/CML-like exports plus SMILES/chiral SMILES and structure tables. | Both appear compatible with scaffold-aware evaluation, pending field-level audit. |
| Bulk export and reproducibility | Strong download/documentation evidence for structured exports and spectra-related files. | Strong download/documentation evidence for SDF-with-signals, NMReDATA, XML/CML-like, and SQL paths. | Both are reproducible candidates if version, access date, filters, and identifiers are documented. |
| License/citation/reuse risk | Clear CC BY-NC context; non-commercial limitation must fit project dissemination plans. | Broader reuse appears possible, but custom database license obligations may affect derivative datasets/software. | NP-MRD is clearer but narrower; NMRShiftDB2 may be more reusable but needs compatibility review. |
| Functional group label derivation | No ready project-specific label set confirmed; labels would likely be derived from molecular structure. | No ready project-specific label set confirmed; labels would likely be derived from molecular structure. | Same blocker for both: label schema and derivation require a later ADR/audit. |
| Scaffold-aware evaluation readiness | Appears ready in principle because structure identifiers are available. | Appears ready in principle because structure data and SMILES paths are available. | Both require a later scaffold split decision and leakage audit. |
| Data cleaning and starting practicality | Natural-product scope may be chemically coherent but could require careful filtering of simulated/predicted and duplicate records. | General organic scope may align well with functional-group diversity but could require careful measured/calculated and assignment-quality filtering. | NP-MRD may be narratively cleaner; NMRShiftDB2 may be broader but license/filtering details matter. |
| TUBITAK 2209-A defensibility | Strong if framed as a focused natural-product 13C NMR dataset with clear non-commercial academic use. | Strong if license compatibility is resolved and measured 13C subset is defensible. | Both can be defended at student-project scale if the selected subset is explainable and auditable. |
| Future ML pipeline transition risk | Main risks: exact usable experimental 1D 13C count, natural-product distribution bias, and label coverage after filtering. | Main risks: measured 13C-only subset count, custom license obligations, and export-field audit. | The lower-risk choice depends on which unresolved check closes cleaner. |

Preliminary discussion frame:

- NP-MRD looks stronger if the project prioritizes a coherent natural-product story, clear experimental/simulated/predicted separation, and a tightly explainable academic dataset, assuming the structure-linked experimental 1D 13C count is sufficient.
- NMRShiftDB2 looks stronger if the project prioritizes broader organic-chemistry coverage, measured spectra with assigned structures, and potentially more flexible reuse, assuming the measured 13C-only subset count and license compatibility are acceptable.
- HMDB should remain outside the main NP-MRD vs NMRShiftDB2 comparison for now. It is useful as a fallback/comparison candidate because its metadata and structure fields are strong, but it still needs the experimental/predicted 13C split check before it can be treated as equally decision-ready.

Remaining open questions before any source can be selected:

- What is the structure-linked usable experimental 1D 13C record count for NP-MRD after project filters?
- What is the measured 13C-only subset count for NMRShiftDB2 after project filters?
- Are NMRShiftDB2 license obligations compatible with the intended project repository, publication, and any future derived dataset or software release?
- Which candidate gives enough functional-group label coverage after rule-based label derivation?
- Which candidate supports the cleanest scaffold-aware split and leakage audit after molecule deduplication?
- Which candidate is easiest to explain without overstating scientific certainty in the TUBITAK 2209-A context?

## Remaining Data Source Verification Checklist

Prepared on 2026-06-08.

This is the smallest remaining verification plan before any source selection. It does not select a source, accept this ADR, authorize data download, start a scientific pipeline, create processed data, or produce experiment results.

### Must answer before source selection

- NP-MRD usable subset count: confirm whether the structure-linked, experimental, 1D 13C subset remains large enough after minimal project filters. Record the evidence source, access date, filter assumptions, count or count range, and unresolved caveats.
- NMRShiftDB2 measured subset count: confirm whether the measured, not calculated, 13C-only subset remains large enough after minimal project filters and has a clear molecule-structure linkage. Record the evidence source, access date, filter assumptions, count or count range, and unresolved caveats.
- NMRShiftDB2 license compatibility: check the custom database license against the intended project repository, TUBITAK proposal/publication path, possible derived dataset notes, and possible future software release. Record obligations, blockers, and whether Mehmetali or advisor review is needed.
- Minimal feasibility comparison: for NP-MRD and NMRShiftDB2 only, check whether the available structure identifiers appear sufficient for later label derivation, scaffold-aware split, deduplication, and leakage audit. Do not define labels, implement split code, or derive labels in this step.
- Decision readiness note: summarize each must-answer item as clean, blocked, or still uncertain before asking Mehmetali to choose a source.

### Nice to answer later

- Detailed per-class functional-group label coverage after a future approved label-schema ADR.
- Field-level import schema for the selected export format after a source is approved.
- Duplicate handling details, stereochemistry policy, salt/mixture policy, and molecule-standardization rules.
- HMDB current experimental versus predicted 13C separation and clean structure linkage, only if a fallback/comparison source becomes necessary.
- Citation wording, final literature summary text, and TUBITAK proposal language after source approval.

### Not needed yet

- Selecting NP-MRD, NMRShiftDB2, or HMDB.
- Treating HMDB as a main contender before its fallback/comparison checks are needed.
- Downloading data, modifying `data/raw/`, or creating processed data.
- Writing data loaders, model, training, evaluation, feature extraction, or scaffold-split code.
- Creating real or fake experiment results, adding real rows to `experiments/runs.csv`, or reporting performance.
- Marking this ADR as `Accepted` or marking any learning gate as `Passed`.

## Decision

Pending Mehmetali approval. No specific source is selected.

## Consequences

No data download, processing, experiment, or run logging should start from this ADR.

The data source decision remains open until candidate sources are compared against the criteria above and Mehmetali approves a specific direction.

## Review Trigger

Review when candidate data sources are ready to compare, when source access/license details are known, or when Mehmetali is ready to approve a specific source direction.
