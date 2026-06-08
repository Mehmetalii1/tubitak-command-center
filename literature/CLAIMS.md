# CLAIMS.md

This file tracks evidence-scored claims for Phase 1A data source decision readiness.

Claims here are not final proposal language.

Phase 0 final proposal/literature language is still not written; this file now contains Phase 1A evidence-scored working claims only.

## Claim 1

## Claim

NP-MRD appears to be a strong candidate for continued verification because it has evidence for 13C NMR information and downloadable structure formats.

## Evidence

- NP-MRD downloads list SDF structures, SMILES structures, NMR peaklists, and NMR spectra files.
- NP-MRD article describes experimental 1H/13C chemical-shift assignments and structure metadata.

## Confidence

High

## Used in

- data source decision

## Needs verification?

Yes. Experimental vs predicted/simulated record filtering and natural-product scope suitability still need verification.

## Claim 2

## Claim

NMRShiftDB2 is close to the project topic, but exact license, export format, and SMILES/InChI availability must be verified before selection.

## Evidence

- Official site describes an NMR database for organic structures and NMR spectra with 13C/1H functionality.
- Official site states that data is under an open-content license.

## Confidence

Medium

## Used in

- data source decision

## Needs verification?

Yes. Exact license text and machine-readable export fields remain unresolved.

## Claim 3

## Claim

HMDB is strong on structure metadata and license clarity, but may be scope-limited because it focuses on human metabolites.

## Evidence

- HMDB About states that structure data is available in SMILES, SDF, MOL, InChI, InChIKey, and PDB formats.
- HMDB About states CC BY-NC 4.0 licensing.
- A concrete HMDB spectrum page shows an experimental 1H/13C HSQC example.

## Confidence

High

## Used in

- data source decision

## Needs verification?

Yes. Usable 13C record count and functional-group label diversity need verification.

## Claim 4

## Claim

SDBS has evidence for 13C NMR search and structure display, but reuse terms and machine-readable structure export are unclear.

## Evidence

- SDBS help documents 13C chemical-shift search.
- SDBS help mentions search results with chemical structures.

## Confidence

Medium

## Used in

- data source decision

## Needs verification?

Yes. License, redistribution, bulk export, and SMILES/InChI availability need verification.

## Claim 5

## Claim

BMRB Metabolomics may be useful for metabolite-focused 13C NMR records, but project fit and export/licensing details need more evidence.

## Evidence

- BMRB Metabolomics search supports 1D and 2D NMR searches.
- BMRB help describes 13C peak-list search and SMILES/InChI structure search.

## Confidence

Medium

## Used in

- data source decision

## Needs verification?

Yes. Bulk export, license coverage, and usable small-molecule record count need verification.

## Claim 6

## Claim

CH-NMR-NP and NAPROC-13 are relevant natural-product 13C NMR resources, but machine-readable structure access and reuse conditions may limit Phase 1A suitability.

## Evidence

- CH-NMR-NP states complete 13C NMR data was a strict inclusion precondition.
- NAPROC-13 official site identifies itself as a Natural Products 13C NMR Database.
- NAPROC-13 conditions allow academic, nonprofit, and personal use.

## Confidence

Medium

## Used in

- data source decision

## Needs verification?

Yes. Structure export, bulk access, and exact reuse permissions need verification.

## Claim 7

## Claim

Literature-extracted datasets such as NMRBank/NMRExtractor and NMRSI are potentially useful but carry higher provenance, extraction-error, and validation risks.

## Evidence

- NMRExtractor paper describes extracted 1H/13C records, SMILES subsets, and confidence metadata.
- NMRExtractor GitHub describes NMRBank files and SMILES counts.
- NMRSI Zenodo record describes a dataset containing 1H, 13C, and 19F entries from supporting information.

## Confidence

Medium

## Used in

- data source decision

## Needs verification?

Yes. Data license, structure fields, confidence filtering, and suitability as a main scientific source need verification.

## Focused Verification Claims

Recorded after focused verification on 2026-06-08.

These claims prepare a data source decision discussion only. They do not select a source.

## Claim FV-1

## Claim

NP-MRD appears ready for data source decision discussion because official downloads, statistics, and article evidence support 13C NMR availability, export paths, structure fields, and experimental/simulated/predicted distinctions.

## Evidence

- NP-MRD downloads list metadata exports, SDF structures, SMILES structures, NMR peaklists, nmrML/JCampDX spectra, experimental assignment CSV, and predicted spectra exports.
- NP-MRD statistics report experimental 1D 13C NMR spectra alongside simulated and predicted 13C NMR counts.
- The NP-MRD 2025 article documents data formats, structure identifiers, and CC BY-NC data-release context.

## Confidence

High

## Used in

- data source decision discussion readiness

## Needs verification?

Yes. Structure-linked usable experimental 1D 13C count still needs project-specific filtering before any source selection.

## Claim FV-2

## Claim

NMRShiftDB2 appears ready for data source decision discussion because official/help/download evidence supports organic structure records, 13C NMR data handling, measured/calculated distinction, and bulk export availability.

## Evidence

- The official site reports organic structures and NMR spectra, with measured and calculated top-level spectrum counts.
- The help page documents 1D 13C NMR storage and bulk data availability in NMReDATA, SDF, SDF-with-spectra, and CML/XML forms.
- The official data license is available and explicitly grants broad reuse, but includes notice, share-alike, derivative database, and OSI-approved software conditions.
- Technical documentation supports SMILES/chiral SMILES, atom/bond tables, and structure handling.

## Confidence

High for decision-discussion readiness; Medium for final license-compatibility certainty.

## Used in

- data source decision discussion readiness

## Needs verification?

Yes. Measured 13C-only subset count and custom database license compatibility must be checked separately before any source selection.

## Claim FV-3

## Claim

HMDB remains a strong fallback/comparison candidate because metadata, structure fields, license clarity, and 13C NMR statistics are strong, but one more check is needed for current experimental versus predicted 13C separation.

## Evidence

- HMDB About documents CC BY-NC 4.0 licensing, commercial permission requirements, citation expectations, NMR search support, and structure formats including SMILES, SDF, MOL, InChI, InChIKey, and PDB.
- HMDB Downloads lists structure downloads, metabolite XML/flat-file downloads, and NMR FID/peaklist/spectrum information downloads.
- HMDB Statistics reports NMR 1D 13C spectra and compounds with NMR spectra.
- An HMDB 1D 13C example spectrum confirms at least one concrete experimental record path.
- HMDB release notes show predicted NMR spectra are also present in newer releases.

## Confidence

Medium-High

## Used in

- fallback/comparison candidate tracking

## Needs verification?

Yes. Current experimental/predicted 13C split and clean structure linkage must be checked before treating HMDB as decision-ready.

## Claim FV-4

## Claim

NP-MRD, NMRShiftDB2, and HMDB do not remove the need for project-specific functional group label derivation; labels may be derived from structure, but that requires a separate ADR and audit.

## Evidence

- Focused verification confirmed structure fields or structure exports across the three shortlisted candidates.
- No focused verification source established a ready-to-use functional-group label set aligned with this project's multi-label classification target.
- ADR 0001 already treats functional group label extraction as a separate decision and audit topic.

## Confidence

High

## Used in

- label set decision planning
- data source decision discussion readiness

## Needs verification?

Yes. Label schema and rule-based derivation must be handled in a later ADR/audit, not in the data source verification step.
