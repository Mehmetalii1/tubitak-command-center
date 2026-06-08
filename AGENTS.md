# Codex Instructions

## Setup

```bash
pip install -r requirements.txt
```

## Test

```bash
pytest -q
```

## Repository Role

This repository is the Command Center for the TUBITAK 2209-A 13C NMR functional group prediction project.

It supervises project memory, task discipline, learning gates, evidence, proposal structure, and audits.

It does not execute the scientific experiment during initial setup.

## Required Session Start

1. Read `START_HERE.md`.
2. Read `STATE.md`.
3. Read `PROJECT_INVARIANTS.md`.
4. Read `governance/NOW_LATER_FORBID.md`.
5. Read the relevant task file or issue.
6. Produce a short plan.
7. Ask for approval before modifying files.

## Core Rules

- Do not modify `data/raw/`.
- Do not implement scientific model code during setup.
- Do not mark knowledge gates as passed without Mehmetali's evidence.
- Do not mark scientific ADRs as accepted without approval.
- Do not invent citations.
- Use small scoped changes.
- Update `STATE.md` after meaningful changes.

