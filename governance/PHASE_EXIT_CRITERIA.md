# PHASE_EXIT_CRITERIA.md

## Phase 0 Exit Criteria

- Command Center skeleton exists.
- Setup-safe tests pass.
- Scientific implementation has not started.
- Learning gates exist but none are passed.
- ADRs exist as Proposed only.
- Proposal files are placeholders only.
- Literature files contain no invented citations.

## Phase 1A Exit Criteria

Phase 1A is a readiness / scientific-preparation planning sub-phase between Phase 0 and Phase 1.

- Learning gates have a defined dependency order and a selected first gate.
- A conceptual prototype-shape note exists and is linked to gates and the prototype-preparation checklist.
- ADR 0001 is reduced to template shape, with evidence/discussion material relocated under `docs/decisions/data-source/`.
- ADR 0001 may record the conditional NMRShiftDB2 data-source decision after Mehmetali approval.
- NMRShiftDB2 blocker areas (license, attribution/share-alike obligations, usable measured 13C subset count, assignment quality, and export practicality) remain queued for separately approved verification.
- No data is downloaded, and the scientific pipeline has not started.
- ADR 0002 and ADR 0003 remain Proposed, and no learning gate is Passed.

## Decision-Stall Rule

When a must-answer count item stays `blocked` or `uncertain` only because of the no-download boundary:

- It is recorded as `blocked`/`uncertain` (a legitimate evidence outcome), not estimated.
- Source selection is not held hostage to that count. It proceeds on total-count sufficiency + license + narrative/scope.
- The exact post-filter usable count is deferred to Phase 1, Task 1 (first scientific-preparation task), after approval.
- The source-selection decision itself still requires Mehmetali approval (see `APPROVAL_REQUIRED.md`).

## Phase 1 Exit Criteria

To be completed later.

Must include:

- approved data source
- proposed label schema
- proposed feature strategy
- scaffold split rationale
- relevant learning gates reviewed or in progress

## Rule

A phase cannot be considered complete just because files exist.
Completion requires meeting the phase criteria.

