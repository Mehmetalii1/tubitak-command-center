# Data Source - Decision Note (outcome recorded)

## Purpose

This note preserves the pre-decision framing that led to ADR 0001 and records the
outcome now accepted in the ADR.

## Outcome

Mehmetali selected NMRShiftDB2 as the first active data source. ADR 0001 is
`Accepted`.

This is reversible / conditional acceptance. It does not declare license
compatibility, attribution/share-alike obligations, usable measured 13C subset
count, assignment quality, or export practicality fully verified. Those remain
blocker areas for the first separately approved NMRShiftDB2 verification task.

NP-MRD is deferred as a secondary candidate, not rejected. HMDB remains fallback /
comparison.

## Boundary

- No new evidence is produced here; this only organizes evidence already recorded in
  `verification-and-evidence.md`, `candidate-research.md`, `literature/SOURCES.md`, and `literature/CLAIMS.md`.
- NMRShiftDB2 is selected as the first active data source, but this does not start
  data download, parser/loader work, processed data, split, modeling, evaluation, or run logging.
- License may still need advisor/institution input before derived datasets,
  software/notebooks, or public reuse are released.
- Per the decision-stall rule (`governance/PHASE_EXIT_CRITERIA.md`), the exact post-filter
  usable counts do **not** block the source-direction decision; they are deferred to the first approved NMRShiftDB2 verification task.

## Decision A - Is the NMRShiftDB2 license acceptable for this project? (yes / no)

What the license grants (per the official NMRShiftDB2 Database License, summarized in
`verification-and-evidence.md` -> "NMRShiftDB2 License Evidence Note"):

- Broad reuse rights, including commercial use, with no non-commercial-only restriction found.

What the license obligates, which is what the yes/no turns on:

- Public conveyance of the database / a derivative database requires license + URI notices.
- Public produced works require a "obtained from NMRShiftDB2" notice.
- A public **derivative database** is subject to share-alike terms and may trigger an
  obligation to offer the derivative database (or alteration/method file) in machine-readable form.
- Software that relies on the database for its intended functionality must be licensed
  under an **OSI-approved** license.

The pre-decision question for Mehmetali was:

> Are these obligations acceptable for the project's intended repository, a possibly
> published filtered/derived dataset, notebooks/software that load the data, and the
> TUBITAK proposal/publication path?

Contrast: NP-MRD's context is **CC BY-NC** (non-commercial), which is simpler but carries
its own non-commercial limitation.

Outcome: NMRShiftDB2 is accepted conditionally as the first active data source, while
license, attribution/share-alike, derivative-database, software-license, and public
reuse obligations remain blocker areas for separately approved verification.

## Decision B - Which narrative/scope does the project want? (NP-MRD vs NMRShiftDB2)

The repo's own decision-discussion frame (now in `candidate-research.md` -> "Data Source
Decision Discussion") already differentiates the two:

| | NP-MRD | NMRShiftDB2 |
| --- | --- | --- |
| Scope / story | Natural products - narrower, chemically coherent | Broad organic chemistry - wider functional-group diversity |
| Spectra | Experimental / simulated / predicted, separable | Measured / calculated, separable |
| License posture | CC BY-NC (clearer, but non-commercial) | Custom DB license (broader reuse, but obligations - see Decision A) |
| Audit characterization | "clearer but narrower" | "may be more reusable but needs compatibility review" |

The pre-decision question for Mehmetali was:

> Does the project prefer a focused, tightly-explainable natural-product 13C NMR story
> (NP-MRD), or a broader organic-chemistry story with more label diversity but more
> filtering and license complexity (NMRShiftDB2)?

This is a judgment about research narrative and scope, not an evidence gap.

Outcome: the project chooses the broader NMRShiftDB2 direction first. NP-MRD remains
a deferred secondary candidate if NMRShiftDB2 fails a blocker or becomes impractical.

## What this note deliberately does not do

- It does not reject NP-MRD.
- It does not declare the NMRShiftDB2 license compatible or incompatible.
- It does not estimate any post-filter count.
- It does not authorize data download, parser/loader work, processed data, split, modeling, evaluation, or run logging.
- HMDB stays fallback/comparison only, outside this two-way framing.
