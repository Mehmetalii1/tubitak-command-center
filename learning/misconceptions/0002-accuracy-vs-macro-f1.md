# Misconception: Accuracy vs Macro F1

## Wrong understanding

Accuracy alone is enough to evaluate a multi-label project.

## Correct understanding

Macro F1 and per-class F1 are needed to inspect label-level behavior, especially with imbalance.

## Why it matters in this project

The primary metric is macro F1 + per-class F1.

## How to detect this mistake again

Look for reports that hide weak per-class performance behind one aggregate score.

## Status

Open

