# Data Source - Decision Note (two open decisions)

## Purpose

A one-page, neutral framing of the two real decisions that stand between the project
and a data-source choice, per the second-pass audit. It does **not** select a source,
make the license judgment, or pick the narrative. It lays out the trade-offs so
Mehmetali can decide.

## Boundary

- No new evidence is produced here; this only organizes evidence already recorded in
  `verification-and-evidence.md`, `candidate-research.md`, `literature/SOURCES.md`, and `literature/CLAIMS.md`.
- No source is selected. No recommendation is given. ADR 0001 stays `Proposed`.
- Both decisions below are **pending - Mehmetali decides** (license may also need advisor/institution input).
- Per the decision-stall rule (`governance/PHASE_EXIT_CRITERIA.md`), the exact post-filter
  usable counts do **not** block these decisions; they are deferred to Phase 1, Task 1.

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

The open question for Mehmetali:

> Are these obligations acceptable for the project's intended repository, a possibly
> published filtered/derived dataset, notebooks/software that load the data, and the
> TUBITAK proposal/publication path?

Contrast: NP-MRD's context is **CC BY-NC** (non-commercial), which is simpler but carries
its own non-commercial limitation. **Decision: pending - Mehmetali (advisor/institution review may be needed).**

## Decision B - Which narrative/scope does the project want? (NP-MRD vs NMRShiftDB2)

The repo's own decision-discussion frame (now in `candidate-research.md` -> "Data Source
Decision Discussion") already differentiates the two:

| | NP-MRD | NMRShiftDB2 |
| --- | --- | --- |
| Scope / story | Natural products - narrower, chemically coherent | Broad organic chemistry - wider functional-group diversity |
| Spectra | Experimental / simulated / predicted, separable | Measured / calculated, separable |
| License posture | CC BY-NC (clearer, but non-commercial) | Custom DB license (broader reuse, but obligations - see Decision A) |
| Audit characterization | "clearer but narrower" | "may be more reusable but needs compatibility review" |

The open question for Mehmetali:

> Does the project prefer a focused, tightly-explainable natural-product 13C NMR story
> (NP-MRD), or a broader organic-chemistry story with more label diversity but more
> filtering and license complexity (NMRShiftDB2)?

This is a judgment about research narrative and scope, not an evidence gap.
**Decision: pending - Mehmetali.**

## What this note deliberately does not do

- It does not select NP-MRD or NMRShiftDB2.
- It does not declare the NMRShiftDB2 license compatible or incompatible.
- It does not estimate any post-filter count.
- It does not change ADR 0001's status (still `Proposed`) or accept any decision.
- HMDB stays fallback/comparison only, outside this two-way framing.
