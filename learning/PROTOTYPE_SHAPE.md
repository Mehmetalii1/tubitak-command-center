# PROTOTYPE_SHAPE.md

## What this is

A one-page, concept-level picture of the first prototype's *shape*: the stages it
would have, in order, and what each stage is for. It is a map for learning and
discussion, linked to the knowledge gates and the prototype-readiness checklist.

It is **not** an implementation. There is no code, no data, no counts, no metrics,
and no source selection here.

## Boundary

- Preparation only (see `first-prototype-preparation.md`).
- No data download, no source selection, no model/split/label/feature code.
- No ADR Accepted, no learning gate Passed.
- Every concrete decision below (which source, which labels, which split, which model)
  stays pending and requires separate Mehmetali approval.

## The shape (concept level only)

| # | Stage | What it means conceptually | Gate | Readiness item |
| --- | --- | --- | --- | --- |
| 1 | **Source** | A documented experimental 13C NMR source with molecular structure (SMILES/InChI). Identity, version, access date, license recorded. | GATE_02 | Dataset-source decision readiness; License/reproducibility awareness |
| 2 | **Experimental 13C subset** | Keep only real measured 13C records (not predicted/simulated), linked to a structure. Filtering rationale is documented; the exact count is deferred, not estimated. | GATE_02, GATE_04 | 13C NMR input representation concept |
| 3 | **Structure-based labels** | Derive functional-group presence/absence labels from molecular structure by a documented rule, audited separately. The label *approach*, not a final schema. | GATE_03 | Functional group label reasoning concept |
| 4 | **Multi-label baseline** | A small, inspectable model that predicts a vector of functional-group labels (each label independent), not a single class. | GATE_01 | Multi-label classification concept |
| 5 | **Scaffold-aware split** | Train/validation/test split that separates molecular scaffolds so near-duplicate structures do not leak across splits. | GATE_05 (needs GATE_04) | Leakage and duplicate risk concept |
| 6 | **Macro F1 / per-class F1** | Evaluate with macro F1 plus per-class precision/recall/F1, then close each number with a chemical interpretation. | GATE_06 | Macro F1 / per-class F1 concept |

## How to read this map

- The order matches the gate learning order in `PROJECT_CONCEPT_DEPENDENCIES.md`:
  understand the task and labels and input first, then leakage, then the split, then the metric.
- A stage is "understood" when its gate has accepted evidence and its readiness item is
  no longer `not started`. This file does not change any of those statuses.
- Stages 5 and 6 exist specifically to prevent the two classic mistakes recorded in
  `learning/misconceptions/` (random-vs-scaffold split, accuracy-vs-macro-F1).

## What this map deliberately leaves open

- Which source (NP-MRD vs NMRShiftDB2 vs fallback) — pending, see the data-source decision note.
- The exact representation of a 13C spectrum as model input.
- The exact functional-group label list and derivation rules.
- The exact baseline model and split method.

These are prototype *decisions*, made later with approval — not part of this shape.
