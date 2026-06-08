# DECISIONS_THIS_WEEK.md

## Phase 0

No scientific decisions were accepted during setup.

## Phase 1A - Governance / Architecture

These are governance and structure decisions only. No scientific truth is finalized and no source is selected.

### 2026-06-08 - Define Phase 1A and a decision-stall rule

Decision: Phase 1A ("readiness / scientific preparation planning") is formally defined in `ROADMAP.md`, and `governance/PHASE_EXIT_CRITERIA.md` now carries Phase 1A exit criteria plus a decision-stall rule.
Why: `STATE.md` already used "Phase 1A" but it was undefined in the roadmap, and there was no rule for what happens when a must-answer count stays blocked under the no-download boundary.
Rule: a blocked/uncertain count is recorded (not estimated); source selection proceeds on total-count sufficiency + license + narrative; the exact post-filter count is deferred to Phase 1 Task 1; source selection still requires Mehmetali approval.
Reversible: Yes.

### 2026-06-08 - Operationalize the learning gate system

Decision: the six learning gates now have a defined dependency order (GATE_01 -> 03 -> 02 -> 04 -> 05 -> 06) in `learning/PROJECT_CONCEPT_DEPENDENCIES.md`, GATE_01 is the selected first gate, `learning/GATE_STATUS.md` carries an order column, and `learning/learning_logs/README.md` defines the per-gate evidence format and location.
Why: the gate system was structurally sound but not operational (no order, no first gate, no evidence format), so it could not actually carry Mehmetali from no-knowledge to prototype-ready.
Boundary: all gates remain `Not started`; no gate is `Passed`; this is sequencing and evidence-format setup only.
Reversible: Yes.

### 2026-06-08 - Add a conceptual prototype-shape map

Decision: `learning/PROTOTYPE_SHAPE.md` describes the first prototype's concept-level stages in order (source -> experimental 13C subset -> structure-based labels -> multi-label baseline -> scaffold-aware split -> macro/per-class F1), each linked to a gate and a readiness item; `first-prototype-preparation.md` now points to it.
Why: the preparation track listed learning blocks but had no single picture connecting concepts to a concrete prototype shape, which the audit flagged as the missing bridge between gates and prototype-readiness.
Boundary: concept level only; no code, data, counts, metrics, or source selection; all underlying decisions remain pending and approval-gated.
Reversible: Yes.

### 2026-06-08 - Freeze and slim ADR 0001

Decision: `docs/adr/0001-data-source.md` is reduced from ~21 sections (~553 lines) to template shape (~74 lines): Status (still Proposed), Context, working assumptions, decision criteria, open questions, a relocation pointer, Decision, Consequences, Review Trigger. The 13 evidence/verification/advisor sections are moved verbatim to `docs/decisions/data-source/` (candidate-research.md, verification-and-evidence.md, advisor-discussion.md, README.md). A freeze note marks the ADR as a refactor target, not an append target.
Why: the ADR had become the repo's largest single-file drift risk and an "append" center of gravity; the audit identified it as a refactor target.
Boundary: content moved unchanged; no source selected; ADR stays Proposed; no ADR Accepted.
Reversible: Yes (content is preserved and tracked in git).

