# Data Source - Advisor / Owner Discussion Material

> Relocated verbatim from `docs/adr/0001-data-source.md` during the ADR slim refactor (2026-06-08).
> Content is unchanged. The ADR stays at template shape; the detail lives here.
> This is working evidence, not final proposal/literature text, and it selects no source.

## Advisor / Owner Discussion Agenda

Prepared on 2026-06-08.

This agenda organizes a future Mehmetali/advisor discussion. It does not replace the detailed discussion questions below, select a source, accept this ADR, authorize data download, start the scientific pipeline, create new evidence, or record a real discussion outcome.

### Meeting purpose

Align on which uncertainties must be closed before a formal data source selection discussion can happen for NP-MRD and NMRShiftDB2.

### What is already known

- Phase 1A is still a readiness and scientific preparation phase.
- NP-MRD and NMRShiftDB2 are the main candidates for discussion.
- HMDB remains fallback/comparison only, not a main contender in this agenda.
- Current evidence supports 13C NMR relevance and structure-identifier plausibility for both main candidates.
- Overall decision readiness remains `uncertain`.

### What is still uncertain

- NP-MRD structure-linked usable experimental 1D 13C subset count after project filters.
- NMRShiftDB2 measured 13C-only filtered subset count and molecule linkage.
- NMRShiftDB2 license compatibility for repository, publication, derived dataset notes, and future software/notebook sharing.
- Whether later label derivation, scaffold split, duplicate handling, and leakage audit can be made clean enough after source-specific filtering.

### Questions to prioritize in the discussion

- What minimum usable subset size or count range would make source-selection discussion meaningful?
- Which uncertainty should be closed first: usable count, license compatibility, label feasibility, or leakage/split auditability?
- Is NP-MRD's narrower natural-product scope acceptable if its usable subset is defensible?
- Is NMRShiftDB2's broader chemistry scope acceptable if license and measured 13C filtering remain more complex?
- Who should review NMRShiftDB2 license obligations before they can support source selection?
- What evidence would be enough to move from pre-selection readiness to a formal source-selection discussion?

### What should NOT be decided in this meeting

- No source selection in this agenda.
- No ADR status change.
- No legal conclusion.
- No scientific pipeline start.
- No label schema or split strategy finalization.

### Expected output of the meeting

- A short list of evidence still required before source selection.
- A decision on which uncertainty to investigate next.
- Any Mehmetali/advisor concerns to record later in the blank discussion outcome template.
- No change to ADR status unless separately approved after the meeting.

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

## Discussion Outcome Template

This section is only a blank template for recording the outcome of a future Mehmetali/advisor discussion. It is not a source selection, does not change ADR status, and must not be treated as an accepted decision by itself.

- Discussion date: `TBD`
- Participants: `TBD`
- Main questions discussed: `TBD`
- Evidence accepted as sufficient: `TBD`
- Evidence still missing: `TBD`
- License / sharing concerns: `TBD`
- Dataset viability concerns: `TBD`
- Label / scaffold / leakage concerns: `TBD`
- Candidate source preference, if any: `TBD / non-decisional`
- Follow-up actions: `TBD`
- Decision impact: `No ADR status change recorded in this template`

