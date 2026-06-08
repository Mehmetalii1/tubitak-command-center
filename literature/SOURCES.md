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

## Focused Verification Sources - Shortlisted Candidates

Recorded after focused verification on 2026-06-08.

This section does not select a data source and does not authorize data download.

| candidate | source name | source kind | what it supports | confidence | remaining evidence |
| --- | --- | --- | --- | --- | --- |
| NP-MRD | [NP-MRD downloads page](https://np-mrd.org/downloads) | Official download page | Supports bulk/download clarity for metadata in XML/JSON, 2D structures in SDF, structures in SMILES/CSV, NMR chemical-shift peaklists, nmrML spectra, JCampDX spectra, experimental assignment CSV, and predicted spectra exports. | Strong | Project-specific filter must confirm structure-linked usable experimental 1D 13C records before selection. |
| NP-MRD | [NP-MRD statistics page](https://np-mrd.org/statistics) | Official statistics page | Supports current counts for compounds, experimental/simulated/predicted NMR spectra, and a public count for experimental 1D 13C NMR spectra. | Strong | The public count is not yet the final usable count after structure linkage, deduplication, and project filters. |
| NP-MRD | [NP-MRD 2025 Nucleic Acids Research article](https://academic.oup.com/nar/article/53/D1/D700/7906838) | Peer-reviewed article | Supports NP-MRD scope, experimental/simulated/predicted distinction, data availability formats, structure identifiers including SMILES/SDF/MOL/PDB/InChI/InChIKey, and CC BY-NC data-release context. | Strong | Project-specific suitability still depends on filtering and label derivation audit. |
| NMRShiftDB2 | [NMRShiftDB2 official site](https://nmrshiftdb.nmr.uni-koeln.de/) | Official source | Supports database relevance for organic structures and NMR spectra, 13C/1H search/prediction, measured/calculated top-level counts, open-content statement, and peer-reviewed assigned spectra context. | Strong | Exact measured 13C-only subset count is not confirmed from top-level counts. |
| NMRShiftDB2 | [NMRShiftDB2 help page](https://nmrshiftdb.nmr.uni-koeln.de/nmrshiftdbhtml/t1.html) | Official documentation | Supports 1D 13C NMR storage, peak lists/raw data, and bulk data availability in NMReDATA, SDF, SDF with spectra, and CML/XML forms. | Strong | Field-level audit is still needed before any import plan. |
| NMRShiftDB2 | [NMRShiftDB2 data license](https://nmrshiftdb.nmr.uni-koeln.de/nmrshiftdbhtml/nmrshiftdb2datalicense.txt) | Official license text | Supports license clarity: reuse is allowed, commercial use is explicitly included, but notices, share-alike terms, derivative database obligations, and an OSI-approved software condition may apply. | Strong | Compatibility with project publication/release plans needs a separate license check before selection. |
| NMRShiftDB2 | [NMRShiftDB2 SourceForge data downloads](https://sourceforge.net/projects/nmrshiftdb2/files/data/) | Project download repository | Supports bulk export/download clarity for SDF, SDF-with-signals, NMReDATA SDF, XML/CML-like exports, 3D variants, and SQL dump availability. | Strong | No data was downloaded; field-level confirmation remains future work. |
| NMRShiftDB2 | [NMRShiftDB2 StructureDatabase wiki](https://sourceforge.net/p/nmrshiftdb2/wiki/StructureDatabase/) | Project technical documentation | Supports structure-field readiness through SMILES/chiral SMILES, atom/bond tables, fingerprints, and molecule-level structure handling. | Medium | Exported-file field names and scaffold split workflow still require audit after source selection. |
| HMDB | [HMDB About page](https://www.hmdb.ca/about) | Official source | Supports CC BY-NC 4.0 licensing, commercial permission requirement, citation expectation for significant downloads, NMR search support, downloadable data formats, and structure availability in SMILES/SDF/MOL/InChI/InChIKey/PDB. | Strong | Experimental versus predicted 13C NMR split needs one more check. |
| HMDB | [HMDB downloads page](https://www.hmdb.ca/downloads) | Official download page | Supports bulk/download clarity for metabolite structures in SDF, all metabolites in XML/MetaboCard-like formats, NMR FID files, NMR peaklists, spectrum information, and 13C/1H NMR download entries. | Strong | Must confirm clean linkage between downloadable 13C spectra and structures before any selection. |
| HMDB | [HMDB statistics page](https://www.hmdb.ca/statistics) | Official statistics page | Supports a public count for NMR 1D 13C spectra and compounds with NMR spectra. | Strong | Statistics do not by themselves resolve current experimental versus predicted 13C split. |
| HMDB | [HMDB 13C NMR example spectrum](https://hmdb.ca/spectra/nmr_one_d/3103) | Official record page | Supports existence of concrete experimental 1D 13C NMR spectrum metadata, nucleus/frequency/solvent fields, and a downloadable peak-list CSV for at least one record. | Medium | Single example does not establish dataset-wide usable count. |
| HMDB | [HMDB release notes](https://hmdb.ca/release-notes) | Official release notes | Supports that HMDB includes predicted NMR spectra in newer releases, creating a necessary experimental/predicted filtering check. | Medium | Current 13C-specific experimental/predicted split remains unresolved. |
