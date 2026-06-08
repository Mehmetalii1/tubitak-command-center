# First Prototype Preparation Track

## Purpose

This track prepares Mehmetali to build the first prototype himself at a later approved step.

It is a learning and readiness track only. It does not start the scientific pipeline, select a data source, define final labels, download data, write model code, or produce results.

## Why this exists

The advisor discussion remains important because it helps reduce uncertainty around data-source choice, licensing, label feasibility, and leakage risk.

However, the Command Center should not wait in advisor-only mode. It should also support safe conceptual preparation so Mehmetali can understand the first prototype before any scientific implementation begins.

## Boundary

- This is preparation, not implementation.
- No data download.
- No source selection.
- No model training.
- No evaluation result.
- No final label schema.
- No scientific claim.
- No ADR acceptance.
- No learning gate passing.

## What "first prototype" means here

In this track, "first prototype" means a future small, inspectable, teaching-oriented starting point that Mehmetali understands before it is implemented.

The concept-level shape of that prototype (its stages, in order, each linked to a gate and a readiness item) is mapped in `learning/PROTOTYPE_SHAPE.md`.

Before implementation, Mehmetali should conceptually understand:

- how a 13C NMR input might be represented;
- how functional-group labels could relate to molecular structure;
- why this is a multi-label classification problem;
- how macro F1 and per-class F1 would be interpreted;
- why leakage-aware thinking matters before any split or evaluation;
- what makes a prototype small, auditable, and useful for learning.

This section does not define code, data, model architecture, label rules, split logic, metrics output, or experiment results.

## Required learning blocks before prototype

- 13C NMR chemical shift basics
- functional groups and structure-to-label reasoning
- spectrum representation options
- multi-label classification basics
- macro F1 / per-class F1 interpretation
- train / validation / test split logic
- leakage and duplicate risk
- dataset license and reproducibility basics
- notebook discipline and experiment logging discipline

## Allowed preparation tasks

- Take conceptual notes.
- Build a term glossary.
- Write small non-code explanation exercises.
- Compare representation options without selecting a data source.
- Explain evaluation metric logic in plain language.
- Think through leakage risks with examples.
- Prepare a checklist before prototype approval.
- Make advisor-discussion technical questions easier to understand.

## Forbidden tasks until separately approved

- Download real data.
- Modify `data/raw/`.
- Write a data loader.
- Write a parser.
- Write feature extraction code.
- Write model, training, or evaluation code.
- Write a label schema or SMARTS rule set.
- Write scaffold split code.
- Write leakage audit code.
- Create fake metric, result, count, or coverage values.
- Add a real run row to `experiments/runs.csv`.
- Mark an ADR as `Accepted`.
- Mark a learning gate as `Passed`.
- Select a source.
- Write final proposal or literature text.

## Prototype readiness checklist

Allowed checklist statuses:

- `not started`
- `in progress`
- `ready for review`
- `approved`

No item is `approved` in this task.

| readiness item | current status | note |
| --- | --- | --- |
| 13C NMR input representation concept | `not started` | Mehmetali should be able to explain possible representations before implementation. |
| Functional group label reasoning concept | `not started` | Mehmetali should understand structure-to-label reasoning before any label schema is drafted. |
| Multi-label classification concept | `not started` | Mehmetali should explain why one molecule can have multiple labels. |
| Macro F1 / per-class F1 concept | `not started` | Mehmetali should understand both project-level and class-level interpretation. |
| Leakage and duplicate risk concept | `not started` | Mehmetali should explain why molecule/scaffold leakage can invalidate evaluation. |
| Dataset-source decision readiness | `not started` | Source selection remains separate and requires approval. |
| License/reproducibility awareness | `not started` | Mehmetali should know why source, version, access date, and license notes matter. |
| Notebook/run logging discipline | `not started` | Mehmetali should understand how future work will be recorded before real runs begin. |
| Advisor/owner uncertainty review | `not started` | Advisor discussion can support uncertainty reduction without selecting a source here. |

## Relation to advisor discussion

- Advisor discussion helps reduce uncertainty.
- It is not the only next step.
- Prototype preparation can continue at conceptual and learning level.
- Source selection still requires separate approval.
- Scientific implementation still requires a separate explicit approval step.

## Next smallest actions

- Read `learning/PROTOTYPE_SHAPE.md` and map each checklist item above to its stage and gate.
- Create a glossary for 13C NMR and ML terms.
- Prepare a non-code explanation of spectrum representation options.
- Prepare a learning-gate checklist for macro F1 / per-class F1.
- Prepare a leakage-risk explanation note.
- Prepare a prototype approval checklist.
