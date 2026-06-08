# SOURCES.md

This file tracks sources reviewed for Phase 1A data source decision readiness.

These notes are not final literature summaries and do not select a data source.

Phase 0 final proposal/literature language is still not written; this file now contains Phase 1A evidence notes only.

## Phase 1A Data Source Candidate Research

| source name | source kind | what it supports | confidence | missing evidence |
| --- | --- | --- | --- | --- |
| NMRShiftDB2 official site | Official source | Supports NMR database relevance, organic structures, 13C/1H spectrum prediction/search, and open-content statement. | Medium | Exact data license text, bulk export format, SMILES/InChI fields. |
| NP-MRD downloads page | Official source | Shows downloadable natural product metadata, SDF structures, SMILES structures, NMR peaklists, spectra files, and release dates. | Strong | How to filter experimental vs predicted/simulated records without downloading. |
| NP-MRD Nucleic Acids Research article | Peer-reviewed article | Supports NP-MRD scope, experimental 1H/13C data, structure metadata, natural-product focus, and licensing context. | Strong | Project-specific suitability after label distribution and filtering. |
| HMDB About page | Official source | Supports SMILES, SDF, MOL, InChI, InChIKey, PDB availability, FAIR metadata, and CC BY-NC 4.0 license statement. | Strong | Exact count of usable 13C entries after filtering. |
| HMDB Downloads page | Official source | Supports structure downloads and reuse/citation requirements. | Strong | Whether the downloadable set cleanly links to 13C NMR records. |
| HMDB NMR spectrum example | Official source | Shows a concrete experimental 1H/13C HSQC record with metadata and shift file availability. | Medium | Whether enough 13C records exist for label-level evaluation. |
| SDBS official site and help page | Official source | Supports SDBS as a free AIST spectral database and confirms 13C chemical shift search. | Medium | Machine-readable SMILES/InChI availability, bulk export, reuse/redistribution terms. |
| BMRB Metabolomics search and help | Official source | Supports 1D/2D NMR search, 13C peak list search, and SMILES/InChI structure search. | Medium | Exact bulk export path, license terms for project reuse, usable metabolite count. |
| BMRBj Terms of Use | Official partner/mirror terms | Indicates public/free site content and citation expectation for BMRBj. | Medium | Whether these terms fully cover the relevant BMRB metabolomics data path. |
| CH-NMR-NP JEOL page | Official source | Supports complete 13C NMR as an inclusion precondition and describes structure/assignment fields. | Medium | Reuse license, machine-readable structure export, maintenance/access constraints. |
| NAPROC-13 official site | Official source | Supports NAPROC-13 as a Natural Products 13C NMR Database with name/substructure/shift/carbon type search. | Medium | Machine-readable export and structure access. |
| NAPROC-13 conditions page | Official source | Supports academic, nonprofit, and personal use without a license. | Medium | Bulk/data reuse terms and structure download limits. |
| NAPROC-13 2024 article | Peer-reviewed article | Supports 13C NMR + structural information and notes limitations around free structure download. | Medium | Practical export path for scaffold split and label derivation. |
| Chemotion repository docs | Official documentation | Supports repository purpose, compound data standards, and 1H/13C NMR handling in Chemotion workflows. | Medium | Whether a coherent reusable dataset can be extracted without per-record complexity. |
| NMRExtractor / NMRBank paper | Peer-reviewed article | Supports literature-extracted 1H/13C NMR entries, SMILES subset, and confidence-score caveats. | Medium | Dataset license/provenance suitability and extraction error risk for this project. |
| NMRExtractor GitHub repository | Project repository | Supports NMRBank availability, SMILES counts, and MIT-licensed code repository. | Medium | Whether the data itself is appropriate as a main source and how article provenance is handled. |
| NMRSI Zenodo record | Repository record | Supports the existence of a dataset with 1H, 13C, and 19F entries extracted from supporting information. | Weak | License, structure/SMILES/InChI fields, and validation quality. |
