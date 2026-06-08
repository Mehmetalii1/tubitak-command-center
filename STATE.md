# STATE.md

## Current Phase

Phase 1A - readiness / scientific preparation planning (now formally defined in ROADMAP.md and governance/PHASE_EXIT_CRITERIA.md)

## Repository Role

This repository is a Codex-based Command Center for the TUBITAK 2209-A 13C NMR functional group prediction project.

It manages memory, planning, learning gates, evidence, proposal scaffolding, audits, and governance.

It does not yet implement the scientific pipeline.

## Current Status

- Command Center setup: closed by initial Phase 0 commit
- Phase 1A: formally defined in ROADMAP.md and governance/PHASE_EXIT_CRITERIA.md, including a decision-stall rule for blocked/uncertain count items
- Phase 0 no-go and setup boundaries remain active during Phase 1A unless Mehmetali explicitly approves a later scientific task
- Scientific pipeline: Not started
- Learning gates: Created, all Not started, none Passed
- Experiment tracking: Header-only scaffold
- Proposal: Draft placeholders only
- Literature: Phase 1A evidence notes only; no final proposal/literature text
- ADRs: Proposed only; none Accepted
- Data source ADR: Proposed, slimmed to template shape (Status / Context / working assumptions / criteria / open questions / Decision / Consequences / Review Trigger); still Proposed, no source selected
- Data source evidence/discussion notes: relocated verbatim from ADR 0001 to docs/decisions/data-source/ (candidate-research, verification-and-evidence, advisor-discussion); content unchanged, location centralized
- Data source open decisions: framed neutrally in docs/decisions/data-source/DECISION_NOTE.md (NMRShiftDB2 license yes/no; NP-MRD vs NMRShiftDB2 narrative/scope); both pending Mehmetali; no source selected
- Data source candidate research: integrated into repo memory; shortlist recorded for further verification only
- Data source focused verification: completed for NP-MRD, NMRShiftDB2, and HMDB; no source selected
- Decision discussion readiness: NP-MRD and NMRShiftDB2 noted as ready for discussion; HMDB noted as fallback/comparison candidate needing one more experimental/predicted 13C check
- Data source decision discussion: prepared in ADR 0001 for NP-MRD vs NMRShiftDB2; no source selected
- Remaining data source verification checklist: prepared in ADR 0001 as a pre-selection plan only; no source selected
- Must-answer evidence collection plan: prepared in ADR 0001; no evidence collected, no counts confirmed, and no source selected
- NP-MRD subset count evidence note: official experimental 1D 13C total recorded in ADR 0001; structure-linked usable filtered subset remains uncertain; no source selected
- NMRShiftDB2 subset count evidence note: official measured/calculated aggregate counts recorded in ADR 0001; measured 13C-only filtered subset remains uncertain; no source selected
- NMRShiftDB2 license evidence note: official license obligations recorded in ADR 0001; compatibility remains uncertain pending Mehmetali/advisor review; no source selected
- Label/scaffold/leakage feasibility note: prepared in ADR 0001 for NP-MRD and NMRShiftDB2; feasibility remains uncertain; no label schema, split code, audit code, or source selection
- Compact pre-selection readiness summary: prepared in ADR 0001; all must-answer items remain uncertain; source selection is not ready yet
- Advisor/owner discussion agenda: prepared in ADR 0001 as a short non-decisional meeting flow; no source selected
- Advisor/owner discussion questions: prepared in ADR 0001 for non-decisional pre-selection discussion; no source selected
- Discussion outcome template: blank TBD template prepared in ADR 0001; no real discussion outcome recorded and no source selected
- First Prototype Preparation Track: created as a conceptual learning/preparation track for Mehmetali; no data download, source selection, learning gate pass, scientific implementation, or model code started
- Learning gate system: operationalized (dependency order set, GATE_01 selected first, evidence format defined in learning/learning_logs/README.md); gates remain Not started
- Conceptual prototype-shape map: learning/PROTOTYPE_SHAPE.md created (concept-level stages linked to gates); no code, data, counts, or source selection
- RDKit Learning Module: nmrshiftdb2rawdata.nmredata.sd dosyasının learning sample / pilot example olarak kullanılmasına karar verildi; bu karar final dataset seçimi değildir ve veri indirme, modelleme, train/test split, evaluation veya ADR kabulü yapılmadı
- RDKit Learning Module: NMReDATA learning sample için examples/README.md dosya-düzeyi provenance notu eklendi; bu not final dataset sayımı, source selection, model-ready subset count veya lisans sonucu değildir ve kaynak URL / erişim tarihi repo içinde henüz kayıtlı değildir
- RDKit Learning Module: 00_rdkit_projedeki_rolu.ipynb üretildi ve audit edildi; bu notebook eğitim amaçlıdır, veri indirme, modelleme, split, evaluation, final dataset seçimi veya ADR kabulü yapılmadı
- RDKit Learning Module: 00 notebook için eksik prompt provenance dosyası geriye dönük eklendi; notebook yeniden üretilmedi ve no-go sınırları değişmedi
- RDKit Learning Module: 01_smiles_mol_nesnesi.ipynb üretildi ve audit edildi; bu notebook eğitim amaçlıdır, veri indirme, modelleme, split, evaluation, final dataset seçimi veya ADR kabulü yapılmadı
- RDKit Learning Module: CURRICULUM.md mevcut 00/01 notebookları ile planlanan 02+ notebookları net ayıracak şekilde güncellendi; yeni notebook üretilmedi ve no-go sınırları değişmedi
- Data downloaded: No
- Raw data changed beyond README: No

## Next Step

Begin conceptual first-prototype preparation through learning notes and checklists while keeping source selection, data download, and scientific implementation blocked until separately approved. Continue using the advisor/owner discussion as a parallel uncertainty-reduction path, and record only real discussion results without changing ADR status unless separately approved.

## Pending User Decisions

- Confirm scientific pipeline start timing
- Confirm data source
- Confirm first learning gate to work on
- Confirm first scientific-preparation task
