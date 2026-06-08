# Learning Logs

This folder holds gate evidence and reflections. It defines the format and location
of the evidence a learning gate needs before it can be reviewed.

No learning gate is Passed during Phase 0.

## Where evidence lives

One file per gate, named after the gate:

- `learning/learning_logs/GATE_01_log.md`
- `learning/learning_logs/GATE_02_log.md`
- ... and so on through `GATE_06_log.md`

## Evidence template

Each log file should contain:

```
# GATE_<NN> Log - <gate name>

## Date

YYYY-MM-DD

## Plain-language explanation

3-5 sentences, in your own words, answering the gate's "Minimum understanding required".

## Worked conceptual example

One small example worked by hand and described in prose. Numbers and reasoning are
allowed; code is not. (Example: describe one molecule with two functional groups and
explain why it has two labels, not one.)

## Self-check against the gate

- Restate the gate's "Common mistakes" and say how this example avoids each one.

## Open questions

Anything still unclear, for advisor discussion or a later gate.
```

## Rules

- Writing a log is safe preparation and is allowed now.
- Producing a log does **not** pass the gate. Marking a gate `Passed` is a separate
  human decision: it requires Mehmetali's evidence plus a reviewer note, and is never
  done autonomously by Codex.
- No code, no real data, no invented metrics or counts in these logs.
