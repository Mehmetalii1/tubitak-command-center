from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "AGENTS.md",
    "START_HERE.md",
    "STATE.md",
    "ROADMAP.md",
    "README.md",
    "PROJECT_INVARIANTS.md",
    "DECISION_BACKLOG.md",
    "CODEX_COMMAND_CENTER_SETUP_GUIDE.md",
    "requirements.txt",
    "codex_protocol/SESSION_START.md",
    "codex_protocol/SESSION_END.md",
    "codex_protocol/TASK_TEMPLATE.md",
    "codex_protocol/DEBUG_TEMPLATE.md",
    "codex_protocol/REVIEW_TEMPLATE.md",
    "codex_protocol/HANDOFF_TEMPLATE.md",
    "governance/NOW_LATER_FORBID.md",
    "governance/PHASE_RULES.md",
    "governance/PHASE_EXIT_CRITERIA.md",
    "governance/MODULE_ADMISSION_CRITERIA.md",
    "governance/STOP_DOING_LIST.md",
    "governance/CHANGE_CONTROL.md",
    "governance/EVIDENCE_POLICY.md",
    "governance/MODEL_OUTPUT_POLICY.md",
    "docs/adr/ADR_TEMPLATE.md",
    "docs/adr/0001-data-source.md",
    "docs/adr/0002-scaffold-split.md",
    "docs/adr/0003-label-set.md",
    "experiments/runs.csv",
    "experiments/RUN_SCHEMA.md",
    "experiments/notes/README.md",
    "data/README.md",
    "data/raw/README.md",
    "data/processed/README.md",
    "src/README.md",
    "notebooks/README.md",
    "models/README.md",
    "reports/README.md",
    "reports/figures/README.md",
    "learning/LEARNING_MAP.md",
    "learning/CONCEPT_GLOSSARY.md",
    "learning/CHECKPOINTS.md",
    "learning/MASTERED_CONCEPTS.md",
    "learning/GATE_STATUS.md",
    "learning/CONCEPT_GRAPH.md",
    "learning/CHEMISTRY_TO_ML_MAP.md",
    "learning/PROJECT_CONCEPT_DEPENDENCIES.md",
    "learning/gates/GATE_01_MULTI_LABEL_CLASSIFICATION.md",
    "learning/gates/GATE_02_NMR_BASICS.md",
    "learning/gates/GATE_03_FUNCTIONAL_GROUPS.md",
    "learning/gates/GATE_04_DATA_LEAKAGE.md",
    "learning/gates/GATE_05_SCAFFOLD_SPLIT.md",
    "learning/gates/GATE_06_MACRO_F1.md",
    "learning/misconceptions/MISCONCEPTIONS_INDEX.md",
    "learning/misconceptions/0001-random-split-vs-scaffold-split.md",
    "learning/misconceptions/0002-accuracy-vs-macro-f1.md",
    "learning/misconceptions/0003-multiclass-vs-multilabel.md",
    "learning/learning_logs/README.md",
    "literature/SOURCES.md",
    "literature/CLAIMS.md",
    "literature/CITATION_MAP.md",
    "literature/OPEN_QUESTIONS.md",
    "literature/PAPER_NOTES/README.md",
    "proposal/PROBLEM_STATEMENT.md",
    "proposal/OBJECTIVES.md",
    "proposal/METHOD.md",
    "proposal/WORK_PACKAGES.md",
    "proposal/RISK_PLAN.md",
    "proposal/EXPECTED_OUTPUTS.md",
    "proposal/AI_USAGE_DECLARATION.md",
    "proposal/PROPOSAL_STATUS.md",
    "research_journal/WEEKLY_LOG.md",
    "research_journal/DECISIONS_THIS_WEEK.md",
    "research_journal/FAILED_ATTEMPTS.md",
    "research_journal/QUESTIONS_FOR_ADVISOR.md",
    "research_journal/MONTHLY_SUMMARY.md",
    "audits/CODE_REVIEW_CHECKLIST.md",
    "audits/SCIENTIFIC_REVIEW_CHECKLIST.md",
    "audits/CHANGE_SCOPE_CHECKLIST.md",
    "audits/RED_TEAM_CHECKLIST.md",
    "audits/OVERKILL_AUDIT.md",
    "audits/SCIENTIFIC_VALIDITY_AUDIT.md",
    "audits/LEAKAGE_AUDIT.md",
    "audits/USER_UNDERSTANDING_AUDIT.md",
    "audits/TUBITAK_READINESS_AUDIT.md",
    "HUMAN_ROLE.md",
    "RESPONSIBILITY_MATRIX.md",
    "APPROVAL_REQUIRED.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/workflows/ci.yml",
]


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_required_files_exist():
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    assert missing == []


def test_runs_csv_header_only():
    lines = read_text("experiments/runs.csv").splitlines()
    assert lines == [
        "run_id,date,git_commit,seed,data_version,model,hyperparams,split_type,macro_f1,per_class_f1,notes"
    ]


def test_phase_zero_boundaries_are_documented():
    state = read_text("STATE.md")
    invariants = read_text("PROJECT_INVARIANTS.md")
    forbid = read_text("governance/NOW_LATER_FORBID.md")

    assert "Scientific pipeline: Not started" in state
    assert "Do not modify `data/raw/`" in invariants
    assert "Do not write model code" in forbid
    assert "Do not invent citations" in forbid


def test_learning_gates_not_passed():
    gate_files = sorted((ROOT / "learning" / "gates").glob("GATE_*.md"))
    assert gate_files
    for gate_file in gate_files:
        text = gate_file.read_text(encoding="utf-8")
        assert "## Status\n\nNot started" in text
        assert "## Status\n\nPassed" not in text


def test_adrs_are_proposed_not_accepted():
    adr_files = sorted((ROOT / "docs" / "adr").glob("000*.md"))
    assert adr_files
    for adr_file in adr_files:
        text = adr_file.read_text(encoding="utf-8")
        assert "## Status\n\nProposed" in text
        assert "## Status\n\nAccepted" not in text


def test_literature_and_proposal_are_placeholders():
    for path in [
        "literature/SOURCES.md",
        "literature/CLAIMS.md",
        "literature/CITATION_MAP.md",
        "proposal/PROBLEM_STATEMENT.md",
        "proposal/METHOD.md",
    ]:
        text = read_text(path)
        assert "Phase 0" in text
