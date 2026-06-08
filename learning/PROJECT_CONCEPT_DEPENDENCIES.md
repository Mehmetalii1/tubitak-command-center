# PROJECT_CONCEPT_DEPENDENCIES.md

## Project Concept Dependencies

This is a conceptual learning order for the six knowledge gates. It is a study
sequence, not a scientific decision and not a claim of mastery. All gates remain
`Not started` and none is `Passed` here.

## Gate dependency order

1. **GATE_01 - Multi-label classification** — frame the problem: one molecule can carry several functional-group labels at once.
2. **GATE_03 - Functional groups** — understand what the labels *are* (the chemistry the model predicts).
3. **GATE_02 - NMR basics** — understand what the input *is* (13C chemical-shift information).
4. **GATE_04 - Data leakage** — understand why naive splits can invalidate evaluation.
5. **GATE_05 - Scaffold split** — the mitigation for leakage in this structural setting.
6. **GATE_06 - Macro F1 / per-class F1** — how to read evaluation under multi-label, class-imbalanced conditions.

## Why this order

- Problem framing (1) comes before labels (2) and input (3): you cannot judge labels or input without knowing the prediction task.
- Labels (2) before input (3): the project goal is functional groups; NMR is the evidence used to predict them.
- Leakage (4) is the motivation that makes scaffold split (5) meaningful, so it comes first.
- The metric (6) is last because it interprets results produced under the earlier concepts.

## First gate

GATE_01 (multi-label classification) is the selected starting gate. See `GATE_STATUS.md`.

## Boundary

- This is a learning sequence only.
- It does not pass any gate, select a data source, or start scientific implementation.
- Gate evidence format and location are defined in `learning/learning_logs/README.md`.
