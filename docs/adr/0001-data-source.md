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

## Must-Answer Evidence Collection Plan

Prepared on 2026-06-08.

This section plans how to collect evidence for the must-answer items before source selection. It does not collect evidence, confirm counts, select a source, accept this ADR, authorize data download, start the scientific pipeline, create processed data, or produce experiment results.

The first verification target is the NP-MRD usable experimental 1D 13C subset count. This section only plans how that count should be verified later; it does not try to find, estimate, or confirm the count.

### Decision-readiness status vocabulary

- `clean`: acceptable evidence is strong enough to bring the item into a source-selection discussion without treating the source as selected.
- `blocked`: acceptable evidence cannot be obtained, access or license interpretation is blocked, or Mehmetali/advisor review is required before the item can support a source-selection discussion.
- `uncertain`: partial evidence exists, but a specific unresolved gap remains before the item can support a source-selection discussion.

### NP-MRD usable experimental 1D 13C subset count

- verification question: How will the project confirm the structure-linked, experimental, 1D 13C NP-MRD subset count after minimal pre-selection filters?
- why it matters: The source cannot be compared responsibly unless the usable experimental 13C subset is large enough and linked to molecular structure for later labels, scaffold split, and leakage audit.
- acceptable evidence: Official NP-MRD statistics, official NP-MRD download documentation, the NP-MRD peer-reviewed article, access date, filter assumptions, and a future count or count range with unresolved caveats.
- allowed method: Inspect official public pages and the already recorded literature sources; record exact source URLs, access date, filter assumptions, and whether each count is public, derived from public metadata, or still unavailable.
- forbidden method: Download NP-MRD data, open bulk exports, modify `data/raw/`, create processed data, run import scripts, estimate a count without evidence, or mark the count as verified in this planning step.
- expected output: A future short evidence note with source references, access date, filter assumptions, count or count range, caveats, and one status from `clean`, `blocked`, or `uncertain`.

### NMRShiftDB2 measured 13C-only subset count

- verification question: How will the project confirm the measured, not calculated, 13C-only NMRShiftDB2 subset count with molecule-structure linkage?
- why it matters: NMRShiftDB2 can only be compared to NP-MRD if the measured 13C subset is separable from calculated records and linked to molecular structures.
- acceptable evidence: Official NMRShiftDB2 site counts, official help or export documentation, public measured/calculated descriptions, access date, filter assumptions, and a future measured 13C-only count or count range with caveats.
- allowed method: Inspect official public pages and already recorded NMRShiftDB2 documentation; record whether the evidence is a direct 13C-only count, a defensible public query result, or an unresolved gap.
- forbidden method: Download SQL, SDF, SDF-with-signals, NMReDATA, or XML/CML exports; run import or parsing scripts; start the scientific pipeline; create a fake count; or treat top-level spectrum counts as a confirmed measured 13C-only subset.
- expected output: A future short evidence note with source references, access date, measured/calculated filter assumptions, molecule-linkage caveats, count or count range, and one status from `clean`, `blocked`, or `uncertain`.

### NMRShiftDB2 license compatibility

- verification question: How will the project check whether the NMRShiftDB2 custom database license is compatible with the intended repository, TUBITAK proposal/publication path, possible derived dataset notes, and possible future software release?
- why it matters: A source should not be selected if reuse obligations, share-alike terms, derivative database requirements, notices, or software-license conditions conflict with the project plan.
- acceptable evidence: Official NMRShiftDB2 license text, a concise obligation summary, a compatibility note for repository publication, proposal/publication, derived dataset notes, and future software release, plus any items requiring Mehmetali or advisor review.
- allowed method: Read and summarize the official license text; map each obligation to the intended project use cases without giving legal certainty; mark unresolved interpretation issues for Mehmetali/advisor review.
- forbidden method: Declare legal compatibility as final, ignore share-alike or derivative database obligations, treat license review as source selection, or publish derived data/software based on this planning note.
- expected output: A future license evidence note listing obligations, compatible-looking uses, blocked or uncertain uses, required review questions, and one status from `clean`, `blocked`, or `uncertain`.

### Minimum label, scaffold, and leakage feasibility

- verification question: How will the project minimally check whether NP-MRD and NMRShiftDB2 have enough structure identifiers for later label derivation, scaffold-aware splitting, molecule deduplication, and leakage audit?
- why it matters: Functional-group labels, scaffold split, and leakage control depend on reliable molecule structure identifiers, but those later decisions must not be implemented during source selection.
- acceptable evidence: Official documentation or article evidence for SMILES, SDF, MOL/PDB, InChI, InChIKey, structure tables, spectrum-to-compound linkage, and export metadata for NP-MRD and NMRShiftDB2.
- allowed method: Compare only the presence and clarity of structure identifiers and spectrum-to-molecule linkage using public documentation already recorded in `literature/SOURCES.md` and `literature/CLAIMS.md`.
- forbidden method: Define the label schema, derive functional-group labels, implement scaffold split code, deduplicate molecules, create processed data, or perform any leakage audit.
- expected output: A future two-candidate feasibility note that says whether later label derivation, scaffold split, deduplication, and leakage audit appear documentable, with one status from `clean`, `blocked`, or `uncertain` for each candidate.

### Decision-readiness note

- verification question: How will the project summarize readiness without selecting a source?
- why it matters: Mehmetali needs a compact readiness view before source selection, but the evidence collection step must not make the scientific decision.
- acceptable evidence: The future evidence notes for NP-MRD count, NMRShiftDB2 count, NMRShiftDB2 license, and minimum feasibility, each with source references and caveats.
- allowed method: Prepare a small readiness table with one row per must-answer item and one status from `clean`, `blocked`, or `uncertain`.
- forbidden method: Write that NP-MRD should be selected, write that NMRShiftDB2 should be selected, rank the candidates as a final choice, accept the ADR, or mark any must-answer item as resolved without evidence.
- expected output: A future pre-selection readiness note that lists statuses and remaining caveats only; HMDB remains fallback/comparison and is not treated as a main contender unless a later fallback task is approved.

## NP-MRD Subset Count Evidence Note

Prepared on 2026-06-08. Sources accessed on 2026-06-08.

This note addresses only how well official or primary NP-MRD sources support the NP-MRD structure-linked usable experimental 1D 13C subset count question. It does not select NP-MRD, accept this ADR, authorize data download, inspect bulk exports, run filters, create processed data, or start the scientific pipeline.

### Verification question

Can official NP-MRD sources directly verify the structure-linked usable experimental 1D 13C subset count needed before source selection?

### Sources inspected

- [NP-MRD Statistics](https://np-mrd.org/statistics): official statistics page. It reports a public total for experimental 1D 13C NMR spectra and separates experimental, simulated, and predicted NMR spectra at aggregate level.
- [NP-MRD Downloads](https://np-mrd.org/downloads): official downloads page. It shows metadata exports, 2D structures in SDF, structures in SMILES/CSV, NMR peaklist files, nmrML and JCampDX spectra files, and experimental assignment CSV availability.
- [NP-MRD 2025 Nucleic Acids Research article](https://academic.oup.com/nar/article/53/D1/D700/7906838): primary peer-reviewed article. It supports NP-MRD data availability, structure identifiers, NMR spectra formats, and the experimental/simulated/predicted data context.
- Existing repo notes in `literature/SOURCES.md` and `literature/CLAIMS.md`: Phase 1A notes already record these NP-MRD sources as strong evidence for decision-discussion readiness, but not for a final filtered subset count.

### Directly supported by sources

- The official statistics page directly reports `Number of Experimental 1D 13C NMR Spectra` as `4,864`.
- The same statistics page supports that NP-MRD distinguishes experimental, simulated, and predicted NMR spectra at aggregate level.
- The official downloads page supports that structure exports and spectra-related exports exist through documented public paths.
- The NP-MRD article supports that NP-MRD data can be accessed in structure formats such as SMILES, SDF, MOL, PDB, InChI, and InChIKey, and that NMR spectra are available in standard exchange formats.

### Still not directly verified

- The official `4,864` value is an aggregate experimental 1D 13C NMR spectra count, not a confirmed project-ready subset count.
- The official count does not by itself prove that every counted spectrum is linked to a usable molecular structure after project filters.
- The count does not resolve molecule-level deduplication, multiple spectra per compound, salts/mixtures, missing or ambiguous structure fields, assignment completeness, label derivation suitability, scaffold split readiness, or leakage-audit readiness.
- No bulk export was downloaded or inspected, so the structure-linked usable filtered subset remains unverified.

### Filter assumptions not applied in this task

- Include experimental records only; exclude simulated and predicted records.
- Include 1D 13C NMR records only.
- Require a link from spectrum or assignment record to a molecule with a usable structure identifier such as SMILES, InChI, InChIKey, or SDF.
- Leave deduplication, salt/mixture policy, label derivation, scaffold split, and leakage audit for later approved decisions.

### Decision readiness

`uncertain`

Reason: official NP-MRD sources directly support an experimental 1D 13C NMR spectra total and strongly support the existence of structure and spectra export paths, but they do not directly verify the structure-linked usable filtered subset count needed for source selection.

## NMRShiftDB2 Subset Count Evidence Note

Prepared on 2026-06-08. Sources accessed on 2026-06-08.

This note addresses only how well official or primary NMRShiftDB2 sources support the measured, not calculated, 13C-only subset count question. It does not select NMRShiftDB2, accept this ADR, authorize data download, inspect bulk exports, run filters, create processed data, or start the scientific pipeline.

### Verification question

Can official NMRShiftDB2 sources directly verify the measured, not calculated, 13C-only subset count needed before source selection?

### Sources inspected

- [NMRShiftDB2 official site](https://nmrshiftdb.nmr.uni-koeln.de/): official site. It reports current top-level usage counts for structures and spectra, including measured and calculated spectra.
- [NMRShiftDB2 Search page](https://nmrshiftdb.nmr.uni-koeln.de/portal/js_pane/P-Search): official search page. It lists `13C` among spectrum types and exposes expert-mode areas for measured/calculated and spectrum-type filtering.
- [Using NMRShiftDB2](https://nmrshiftdb.nmr.uni-koeln.de/nmrshiftdbhtml/using.html): official documentation. It states that searches can distinguish measured and theoretically calculated spectra and can be restricted by spectrum type.
- [NMRShiftDB2 Help/About page](https://nmrshiftdb.nmr.uni-koeln.de/nmrshiftdbhtml/t1.html): official documentation. It supports one-dimensional NMR shift data including 13C and documents public data availability in NMReDATA, SDF, SDF-with-spectra, and CML/XML-style forms.
- [NMRShiftDB2 SourceForge data page](https://sourceforge.net/projects/nmrshiftdb2/files/data/): project download repository. It shows bulk export files, but no file was downloaded or inspected.
- Existing repo notes in `literature/SOURCES.md` and `literature/CLAIMS.md`: Phase 1A notes already record NMRShiftDB2 as strong evidence for measured/calculated top-level counts and export availability, but not for a final measured 13C-only subset count.

### Directly supported by sources

- The official site directly reports top-level spectra counts: `Measured 70029, calculated 396583`.
- Official documentation supports that NMRShiftDB2 contains both measured and theoretically calculated spectra.
- Official search documentation supports filtering searches to measured-only, calculated-only, or both types of NMR data.
- Official search UI/documentation supports `13C` as a spectrum type.
- Official help/download documentation supports export availability for structure-linked spectral data in formats such as NMReDATA, SDF, SDF-with-spectra, and CML/XML-style exports.

### Still not directly verified

- The official `70029` measured spectra count is an aggregate measured spectra count, not a confirmed measured 13C-only subset count.
- The official sources inspected do not directly report the intersection of measured spectra and 13C-only spectra.
- The official sources do not directly resolve whether the measured 13C-only subset excludes 1H, 2D, 13C/1H correlation, calculated/predicted records, unreviewed records, duplicates, or records without project-usable molecule linkage.
- Official export paths exist, but the measured 13C-only filtered subset remains unverified without a future approved export/query/filter audit.
- No bulk export was downloaded or inspected.

### Filter assumptions not applied in this task

- Include measured records only; exclude calculated or predicted records.
- Include 13C spectrum type only; exclude 1H, other nuclei, 2D spectra, and 13C/1H correlation unless later approved.
- Require a molecule/spectrum linkage suitable for later label derivation, scaffold-aware split, deduplication, and leakage audit.
- Leave unreviewed-record policy, duplicate policy, field-level import schema, and license compatibility for later approved evidence notes or ADRs.

### Decision readiness

`uncertain`

Reason: official NMRShiftDB2 sources directly support top-level measured/calculated counts, 13C spectrum handling, measured/calculated filtering, and bulk export availability, but they do not directly verify the measured 13C-only filtered subset count needed for source selection.

## NMRShiftDB2 License Evidence Note

Prepared on 2026-06-08. Sources accessed on 2026-06-08.

This note addresses only how well official or primary NMRShiftDB2 sources support license-compatibility review for a TUBITAK 2209-A project, possible derived dataset notes, repository documentation, software/notebook sharing, and proposal/publication plans. It is not legal advice, does not make a final legal conclusion, does not select NMRShiftDB2, and does not accept this ADR.

### Verification question

Do official NMRShiftDB2 license sources provide enough evidence to treat NMRShiftDB2 as license-compatible for the intended project uses before source selection?

### Sources inspected

- [NMRShiftDB2 data license](https://nmrshiftdb.nmr.uni-koeln.de/nmrshiftdbhtml/nmrshiftdb2datalicense.txt): official database license text. It defines the licensed database, granted rights, notice requirements, share-alike terms, produced-work notices, derivative database obligations, and an OSI-approved software condition.
- [NMRShiftDB2 Help/About page](https://nmrshiftdb.nmr.uni-koeln.de/nmrshiftdbhtml/t1.html): official documentation. It states that the software is open source, the data is under an open-content license, and NMRShiftDB2 as a database is available under the NMRShiftDB2 Data License.
- [NMRShiftDB2 SourceForge project page](https://sourceforge.net/projects/nmrshiftdb2/): project page. It repeats that the software is open source and the data is under an open-content license.
- [NMRShiftDB2 SourceForge data page](https://sourceforge.net/projects/nmrshiftdb2/files/data/): project data page. It shows the presence of data export files, but no export was downloaded or inspected.
- Existing repo notes in `literature/SOURCES.md` and `literature/CLAIMS.md`: Phase 1A notes already record the official license as strong evidence but mark final compatibility as needing separate review.

### Directly supported by sources

- The official license is a custom NMRShiftDB2 Database License derived from the ODC Open Database License, with additional terms.
- The license explicitly covers the NMRShiftDB2 database of organic structures and assigned NMR spectra, including forms such as SDF, CML, and SQL files.
- The license grants broad use rights, including commercial use, subject to conditions.
- Publicly conveying the database, a derivative database, or the database as part of a collective database requires license/URI notices and preservation of relevant notices.
- Public produced works require a notice that the content was obtained from NMRShiftDB2 and is available under the NMRShiftDB2 Database License.
- Public derivative databases are subject to share-alike style requirements.
- Public use of a derivative database or produced work from a derivative database can trigger an obligation to offer the derivative database or alteration/method file in machine-readable form.
- Software that relies on the database, a derivative database, or a produced work for its intended functionality must be licensed under an Open Source Initiative-approved license.
- The database license says it does not apply to computer programs used in making or operating the database, so database-data obligations and software-code licensing need to be considered separately.

### License compatibility notes

- TUBITAK 2209-A academic use: no non-commercial-only restriction was found in the official data license; broad use is supported by the license text, but any public reuse still needs notices and license compliance.
- Repository documentation: documenting source identity, access date, license URL, and required attribution/notice appears necessary if NMRShiftDB2 remains a candidate or is later selected.
- Derived dataset sharing: public release of a filtered or transformed NMRShiftDB2-derived dataset may be treated as a derivative database and may need share-alike licensing plus a machine-readable derivative database or alteration/method file.
- Software/notebook sharing: notebooks or software that require NMRShiftDB2 data, a derivative database, or produced work for intended functionality may need an OSI-approved license; notebooks that only document methods without bundling or depending on data still need separate review before release.
- Publication/proposal use: small textual summaries, counts, or produced outputs may require a clear NMRShiftDB2 notice if they publicly use produced work; exact citation and notice wording should be drafted later, not in this note.

### Still unclear / risk areas

- Whether a future project-specific filtered subset would be legally treated as a derivative database, a produced work, a collective database component, or only documented filtering logic.
- Whether publishing only identifiers, labels, or derived functional-group annotations would trigger derivative database obligations.
- Whether project notebooks that demonstrate loading/filtering against NMRShiftDB2 exports would count as software relying on the database for intended functionality.
- Which repository license would be chosen if future software/notebooks must satisfy the OSI-approved software condition.
- Whether advisor, institution, or TUBITAK publication rules impose additional constraints beyond the NMRShiftDB2 license.
- Whether individual contents inside the database have any separate rights or constraints not covered by the database license.

### Decision readiness

`uncertain`

Reason: official NMRShiftDB2 license evidence is strong and supports broad reuse in principle, but public derived dataset release, repository packaging, software/notebook licensing, notice wording, and institutional/project constraints still need Mehmetali/advisor review before license compatibility can support source selection.

## Label, Scaffold, and Leakage Feasibility Evidence Note

Prepared on 2026-06-08.

This note records minimum feasibility evidence for later functional-group label derivation, scaffold-aware evaluation, and leakage audit for NP-MRD and NMRShiftDB2. It does not select a source, define a label schema, write SMARTS rules, implement scaffold split logic, perform leakage audit, download data, create processed data, or start the scientific pipeline.

Status vocabulary for this note:

- `supported`: existing official/primary evidence directly supports the minimum feasibility point.
- `plausible but unverified`: existing evidence makes the point plausible, but project-specific field-level or record-level checking is still needed.
- `risk / unclear`: existing evidence exposes a known risk or does not yet resolve the point.
- `not needed yet`: the item belongs to a later approved ADR/audit rather than this pre-selection evidence note.

### NP-MRD feasibility notes

| topic | status | note |
| --- | --- | --- |
| structure identifier availability | supported | Official NP-MRD download/article evidence supports SDF, SMILES/CSV, MOL, PDB, InChI, and InChIKey paths. This is enough to treat later structure-based label derivation and scaffold-aware evaluation as plausible. |
| structure-to-label derivation feasibility | plausible but unverified | Structure identifiers make later rule-based functional-group label derivation plausible, but no project label schema, SMARTS/rule set, or label coverage check exists yet. |
| molecule/spectrum linkage risk | plausible but unverified | Downloads and article evidence support spectra, peaklists, assignments, metadata, and structure exports, but the project has not verified record-level links between usable experimental 1D 13C spectra and molecule structures. |
| duplicate / near-duplicate risk | risk / unclear | Multiple spectra per compound, repeated records, stereochemistry variants, salts/mixtures, and natural-product analog series could affect molecule-level counting and split design. No deduplication policy is defined yet. |
| scaffold-aware split feasibility | plausible but unverified | Structure identifiers make scaffold-aware splitting feasible in principle, but no scaffold method, molecule standardization policy, or field-level audit has been approved. |
| spectrum-level vs molecule-level leakage risk | risk / unclear | If multiple spectra or assignments exist for the same molecule, splitting at spectrum level could leak molecule identity across train/test. Molecule-level grouping is a later audit requirement, not implemented here. |
| experimental vs predicted/calculated contamination risk | risk / unclear | Official evidence supports experimental, simulated, and predicted categories, but the usable project subset still needs filtering rules to prevent simulated/predicted contamination. |

### NMRShiftDB2 feasibility notes

| topic | status | note |
| --- | --- | --- |
| structure identifier availability | supported | Official/help/download/technical evidence supports organic structures, SDF/NMReDATA/CML-like exports, SMILES/chiral SMILES, atom/bond tables, and molecule-level structure handling. |
| structure-to-label derivation feasibility | plausible but unverified | Structure data makes later rule-based functional-group label derivation plausible, but no project label schema, SMARTS/rule set, or label coverage check exists yet. |
| molecule/spectrum linkage risk | plausible but unverified | NMRShiftDB2 is built around structures and assigned spectra, and exports can include spectral data, but the measured 13C-only subset and exact molecule/spectrum linkage still require field-level audit. |
| duplicate / near-duplicate risk | risk / unclear | General organic chemistry scope may include duplicates, stereochemical variants, repeated measurements, unreviewed entries, or multiple spectra per structure. No deduplication policy is defined yet. |
| scaffold-aware split feasibility | plausible but unverified | Structure fields make scaffold-aware splitting feasible in principle, but no scaffold method, molecule standardization policy, or field-level audit has been approved. |
| spectrum-level vs molecule-level leakage risk | risk / unclear | Assigned spectra tied to the same or closely related structures could leak if split by spectrum instead of molecule/scaffold. This must be handled by a later leakage audit. |
| experimental vs predicted/calculated contamination risk | risk / unclear | Official evidence supports measured/calculated distinction, but the measured 13C-only subset is not directly verified and needs later filtering rules to prevent calculated-record contamination. |

### Cross-candidate takeaway

Both NP-MRD and NMRShiftDB2 have enough documented structure-identifier evidence to keep later label derivation, scaffold-aware splitting, and leakage audit plausible. Neither candidate currently removes the need for a separate label-schema ADR, field-level molecule/spectrum linkage audit, deduplication policy, scaffold split decision, and leakage audit. NP-MRD's main feasibility risk is cleanly linking usable experimental 1D 13C spectra to structures after filtering; NMRShiftDB2's main feasibility risk is cleanly isolating measured 13C-only records and interpreting structure/spectrum linkage after export-field audit. This is not a source selection.

### Decision readiness

`uncertain`

Reason: minimum feasibility is plausible for both candidates because structure identifiers and spectra-related exports are documented, but project-specific label derivation, scaffold splitting, duplicate handling, leakage controls, and contamination filters are not yet verified or implemented.

## Compact Pre-Selection Readiness Summary

Prepared on 2026-06-08.

This summary collects the current must-answer evidence notes in one place before source selection. It does not select a source, accept this ADR, authorize data download, start the scientific pipeline, define labels, implement split/leakage logic, create coverage/count results, or make legal conclusions.

Source selection is not ready yet. The current evidence is useful for a decision discussion, but the must-answer items remain `uncertain` because key filtered counts, license interpretation, and field-level audit details are not fully closed.

### Readiness matrix

| item | current evidence | remaining uncertainty | decision-readiness |
| --- | --- | --- | --- |
| NP-MRD usable experimental 1D 13C subset count | Official NP-MRD statistics report `4,864` experimental 1D 13C NMR spectra; official downloads/article support structure and spectra export paths. | The official count is aggregate, not confirmed as structure-linked usable filtered subset after project filters, deduplication, and molecule/spectrum linkage checks. | `uncertain` |
| NMRShiftDB2 measured 13C-only subset count | Official NMRShiftDB2 site reports top-level `Measured 70029, calculated 396583`; official search/docs support measured/calculated distinction and `13C` spectrum type. | The measured count is aggregate; official sources do not directly report the measured 13C-only filtered subset or molecule-linkage quality. | `uncertain` |
| NMRShiftDB2 license compatibility | Official custom database license grants broad reuse in principle and documents notices, share-alike, derivative database, produced work, and OSI-approved software conditions. | Public derived dataset release, repository packaging, notebook/software licensing, notice wording, and institutional/TUBITAK constraints still need Mehmetali/advisor review. | `uncertain` |
| NP-MRD vs NMRShiftDB2 label/scaffold/leakage feasibility | Both candidates have documented structure identifiers and spectra-related export paths, making later label derivation, scaffold split, and leakage audit plausible. | Neither candidate has project-specific label schema, field-level molecule/spectrum linkage audit, deduplication policy, scaffold split decision, leakage audit, or contamination filters verified yet. | `uncertain` |

### Candidate posture

#### NP-MRD

- Strong side: Official evidence supports experimental 1D 13C NMR spectra, experimental/simulated/predicted distinction, and multiple structure identifier paths.
- Weak/risky side: The public `4,864` experimental 1D 13C count is not yet the structure-linked usable filtered subset count.
- Still needed before source selection: confirm usable structure-linked experimental 1D 13C subset after filters and clarify molecule/spectrum linkage, duplicates, and contamination controls.

#### NMRShiftDB2

- Strong side: Official evidence supports broad organic-structure coverage, measured/calculated distinction, 13C handling, export paths, and structure-field readiness.
- Weak/risky side: The official measured count is aggregate, not a measured 13C-only filtered subset; license obligations also need project-specific interpretation.
- Still needed before source selection: confirm measured 13C-only subset count/linkage and resolve license compatibility enough for the intended repository, derived dataset, notebook/software, and publication/proposal path.

#### HMDB

- Posture: HMDB remains fallback/comparison only. It is not part of the main NP-MRD vs NMRShiftDB2 pre-selection readiness summary unless a later fallback task is approved.

### Overall decision readiness

`uncertain`

Reason: evidence is now organized enough for a structured pre-selection discussion, but source selection is not ready yet because all must-answer items remain open or partially verified. No candidate is selected by this summary.

## Advisor / Owner Discussion Questions

Prepared on 2026-06-08.

These questions are for Mehmetali/advisor discussion before any source selection. They do not select a source, accept this ADR, authorize data download, define labels, implement split/leakage logic, create counts or coverage results, or make legal conclusions.

### Dataset viability

- For NP-MRD, is the official experimental 1D 13C total enough to justify one more verification pass, even though the structure-linked usable subset remains unverified?
- For NMRShiftDB2, is the aggregate measured spectra evidence enough to justify one more verification pass, even though the measured 13C-only subset remains unverified?
- What minimum usable subset size or count range would be acceptable before a source-selection discussion becomes meaningful?
- Should the project prefer a narrower but more coherent dataset story, or a broader dataset story with more filtering and license complexity, if both remain scientifically defensible?

### Legal / license / sharing constraints

- Are NMRShiftDB2 notice, share-alike, derivative database, and OSI-approved software conditions acceptable for the intended repository and future notebook/software sharing?
- Would publishing a filtered subset, identifiers, labels, or derived notes create a license obligation that should be reviewed before source selection?
- Does NP-MRD's CC BY-NC context fit the expected TUBITAK 2209-A dissemination, publication, and repository plans?
- Who should review the final license interpretation before any source is selected: Mehmetali, advisor, institution, or another reviewer?

### Label derivation feasibility

- Is structure-based functional-group label derivation acceptable in principle for this project if the source does not provide ready labels?
- What level of label coverage evidence is needed before selecting a data source, without designing the final label schema yet?
- Are natural-product-biased labels and broader organic-chemistry labels both acceptable project stories, or does one create a clearer learning/research scope?

### Leakage and split strategy

- Should source selection require clear molecule-level grouping evidence before any later scaffold-aware split design?
- What leakage risks would be unacceptable at source-selection time, even before implementing a split?
- Should duplicate, near-duplicate, stereochemistry, salts/mixtures, and multiple-spectra-per-molecule policies be drafted before or after source selection?
- How much confidence is needed that experimental versus predicted/calculated contamination can be filtered cleanly?

### Project scope / TUBITAK suitability

- Which unresolved uncertainty is most important for a TUBITAK 2209-A project: usable count, license clarity, label feasibility, scaffold/leakage auditability, or narrative explainability?
- Is a smaller, more explainable initial source acceptable if it keeps the first scientific scope auditable?
- What evidence would be sufficient to move from pre-selection readiness to a formal source-selection discussion without starting the scientific pipeline?

### Fallback decision path

- If NP-MRD and NMRShiftDB2 both remain uncertain after one more public verification pass, when should HMDB be revisited as fallback/comparison rather than a main contender?
- What condition would justify pausing source selection and asking for advisor input instead of collecting more public evidence?

## Decision

Pending Mehmetali approval. No specific source is selected.

## Consequences

No data download, processing, experiment, or run logging should start from this ADR.

The data source decision remains open until candidate sources are compared against the criteria above and Mehmetali approves a specific direction.

## Review Trigger

Review when candidate data sources are ready to compare, when source access/license details are known, or when Mehmetali is ready to approve a specific source direction.
