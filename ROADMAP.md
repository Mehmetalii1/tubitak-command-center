# ROADMAP.md

## Phase 0 - Command Center Setup

Goal:
Create the repository-native project operating system.

Done-when:
- 18-layer skeleton exists
- setup-safe tests pass
- scientific implementation has not started

## Phase 1A - Readiness / Scientific Preparation Planning

Goal:
Move the Command Center into readiness mode: mature the pending decisions and prepare Mehmetali conceptually for the first prototype, without starting the scientific pipeline.

Scope:
- conceptual learning-gate progress
- conditional data-source decision tracking without scientific pipeline start
- governance and structure refactors that reduce document drift

Done-when:
- learning gates have a defined dependency order and a selected first gate
- a conceptual prototype-shape note exists and is linked to the gates
- ADR 0001 is reduced to template shape with evidence relocated
- the decision-stall rule (governance/PHASE_EXIT_CRITERIA.md) is documented

Boundary:
- no data download
- no unapproved data-source change beyond ADR 0001
- no model / split / label / feature code
- ADR 0001 may be Accepted as the conditional data-source decision; ADR 0002 and ADR 0003 remain Proposed
- no learning gate Passed

## Phase 1 - Scientific Baseline Preparation

Goal:
Prepare data loading, labels, features, and scaffold split.

Requires:
- relevant learning gates in progress or reviewed
- data source decision approved
- ADRs reviewed
- no unsupported scientific claims

## Phase 2 - Baseline Modeling

Goal:
Train first baseline and evaluate with macro F1 + per-class F1.

Requires:
- scaffold split validated
- label schema validated
- experiment logging ready

## Phase 3 - Analysis and Iteration

Goal:
Interpret errors, improve features/modeling, maintain scientific honesty.

## Phase 4 - TUBITAK Proposal Consolidation

Goal:
Turn evidence, decisions, risks, and results into proposal-ready material.

## Task Size Rule

One task = one coherent unit of work.

GitHub Issues, labels, and milestones are later setup items and are not created during Phase 0 unless Mehmetali explicitly asks for them.

