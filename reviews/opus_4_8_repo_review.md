# Opus 4.8 Repo Review Report

> **İnceleme kapsamı:** Bu rapor **`origin/master` (5ecfcdb)** durumunu inceler — yani GitHub'daki canlı repo. Yerelde checked-out olan `docs/data-source-decision-note` (caae193) dalında RDKit Learning Module bulunmuyor; o dal master'a PR #5 ile zaten merge edilmiş ve master'a sonradan RDKit modülünü ekleyen 4 commit daha gelmiş (3119911, d11f3c0, a3d5b3f, 5ecfcdb). Yerel `origin/master` ref'i bayattı (8957375); gerçek remote master'ı görmek için yalnızca salt-okunur `git fetch origin master` yapıldı (çalışma ağacına/dosyalara dokunulmadı, checkout yapılmadı). Rapordaki tüm dosya yolları **master** içeriğine göredir.
>
> **Notasyon:** **[Bulgu]** = repoda doğrudan gözlenen; **[Çıkarım]** = gözlemden türetilen yorum; **[Öneri]** = aksiyon önerisi.

## 1. Executive Summary

**Genel statü: PASS — hijyen tarafında WATCH.**

Repo, bir "bilimsel pipeline" değil; gerçekten bir **karar ve disiplin merkezi** gibi davranıyor ve bunu başarıyla yapıyor. No-go sınırları yalnızca metinle değil, **testlerle mekanik olarak** korunuyor (`tests/test_repository_structure.py` ADR'lerin `Proposed`, gate'lerin `Not started`, `runs.csv`'nin header-only olduğunu doğruluyor; CI her push/PR'da çalıştırıyor). Veri kaynağı kararı doğru biçimde **açık ve seçilmemiş** durumda; ADR 0001 `Proposed` ve template-shape'e dondurulmuş. RDKit Learning Module iyi izole edilmiş, sınırları net tarif edilmiş, audit'lenmiş ve eğitim amaçlı.

Tek somut **içerik kusuru**: iki RDKit notebook'unun (`.ipynb`) Türkçe karakterleri kayıtta `?`'e bozulmuş (mojibake). Bunun dışında bulgular küçük hijyen/tutarlılık sorunları: Phase 0 ↔ Phase 1A doküman kayması, STATE.md'de bir bullet'ın ASCII-Türkçe yazılması, RDKit modülünün yapı testiyle korunmaması, ve birkaç çapraz-referans/over-promise pürüzü.

Hiçbir no-go ihlali yok: veri indirme yok, modelleme yok, split yok, skor yok, sahte sonuç yok, ADR Accepted yok, gate Passed yok.

## 2. What This Repo Is Doing Well

- **[Bulgu] Karar disiplini örnek seviyede.** `docs/adr/0001-data-source.md` `Proposed` ve başına bir "freeze note" konmuş ("this ADR is a refactor target, not an append target"). Tüm kanıt/araştırma `docs/decisions/data-source/`'a taşınmış; `DECISION_NOTE.md` iki açık kararı (NMRShiftDB2 lisansı evet/hayır; NP-MRD vs NMRShiftDB2 anlatı/kapsam) **tarafsız, seçim yapmadan** çerçeveliyor.
- **[Bulgu] No-go sınırları test ile zorlanıyor.** `tests/test_repository_structure.py`: `test_adrs_are_proposed_not_accepted`, `test_learning_gates_not_passed`, `test_runs_csv_header_only`, `test_phase_zero_boundaries_are_documented`. `tests/test_no_scaffold_leak.py` ve `tests/test_f1_regression.py` bilinçli `pytest.mark.skip` placeholder. `.github/workflows/ci.yml` bunları her push/PR'da koşuyor. Bu, disiplinin sadece "söz" değil **mekanik** olduğunu gösteriyor.
- **[Bulgu] RDKit modülü doğru izole.** `learning/rdkit/README.md`, `CURRICULUM.md`, `QUALITY_CRITERIA.md` modülün bilimsel pipeline olmadığını ve `data/raw/` yerine geçmediğini açıkça yazıyor. Her iki notebook'ta da güvenli RDKit import'u (yoksa çökmüyor) ve sonda açık bir `notebook_boundary_check` hücresi var.
- **[Bulgu] Kanıt notlarında entelektüel dürüstlük.** `docs/decisions/data-source/verification-and-evidence.md` içindeki her kanıt notu `clean/blocked/uncertain` sözlüğüyle kapanıyor ve hepsi `uncertain` — gerçek sayılar (NP-MRD 4.864 deneysel 1D ¹³C; NMRShiftDB2 70.029 measured / 396.583 calculated) "aggregate, henüz filtrelenmiş usable subset değil" diye dürüstçe işaretlenmiş.
- **[Bulgu] Decision-stall kuralı olgun.** `governance/PHASE_EXIT_CRITERIA.md`, filtrelenmiş sayım belirsizliğinin kaynak seçimini **rehin almasını** engelliyor: sayım Phase 1 Task 1'e erteleniyor, karar total-count + lisans + anlatıya göre ilerliyor; seçim yine de Mehmetali onayına bağlı.
- **[Bulgu] Sorumluluk netliği.** `APPROVAL_REQUIRED.md`, `RESPONSIBILITY_MATRIX.md`, `governance/MODEL_OUTPUT_POLICY.md`, `governance/MODULE_ADMISSION_CRITERIA.md` (anti-fake-progress kuralı dahil) hep aynı yönde: Codex önerir/scaffold'lar, Mehmetali bilimsel gerçeği onaylar.
- **[Bulgu] Prompt provenance var.** Her iki notebook için `learning/rdkit/prompts/` altında üretim promptu kaydı tutulmuş.

## 3. Main Structural Observations

- **[Çıkarım] Evet, repo gerçekten Command Center mantığına uyuyor.** Katmanlar (governance / learning / audits / decisions / proposal / literature / experiments-scaffold / codex_protocol) proje yönetimi içindir; hiçbiri bilimsel hesap yapmıyor. `src/`, `models/`, `notebooks/`, `data/` yalnızca placeholder README içeriyor.
- **[Bulgu] Bilimsel pipeline ile yönetim ayrımı net.** Bilimsel iş için ayrılan tüm yüzeyler boş tutulmuş: `experiments/runs.csv` sadece header; `data/`, `data/raw/`, `data/processed/` placeholder; gerçek test mantığı yok.
- **[Bulgu] RDKit modülü doğru konumda.** `learning/` altında, `src/` veya `data/` altında değil — bu, "öğrenme modülü" niyetiyle tutarlı. Modül kendi README/CURRICULUM/QUALITY_CRITERIA/prompts/audits/examples alt-yapısına sahip; yani Command Center'ın geri kalanındaki "her şeyin bir politikası ve denetimi olur" desenini içeride de tekrarlıyor.
- **[Çıkarım] Tek yapısal pürüz:** RDKit modülü, reponun geri kalanını koruyan **mekanik yapı testinin dışında** (bkz. Bölüm 6 ve 7). Modülün disiplini tamamen prose + manuel audit'e dayanıyor.

## 4. RDKit Learning Module Review

İncelenen yollar: `learning/rdkit/README.md`, `CURRICULUM.md`, `QUALITY_CRITERIA.md`, `prompts/00…`, `prompts/01…`, `notebooks/00…`, `notebooks/01…`, `audits/00…`, `audits/01…`, `audits/nmrshiftdb2_nmredata_learning_sample_policy.md`, `examples/nmrshiftdb2rawdata.nmredata.sd`.

- **00 ve 01 sırası: [Bulgu] Doğru.** `00_rdkit_projedeki_rolu` kavramsal giriş (RDKit'in roldeki yeri, SMILES/descriptor/fingerprint/SMARTS/label-matrix tanıtımı, toy moleküller); `01_smiles_mol_nesnesi` ilk teknik adım (SMILES → `Mol` → canonical → görselleştirme). Pedagojik sıra mantıklı ve 01, 00'a açıkça referans veriyor.
- **NMReDATA sample ayrımı: [Bulgu] Çok iyi ayrılmış.** `examples/nmrshiftdb2rawdata.nmredata.sd` (gerçek nmrshiftdb2 SDF, **196 kayıt / 37.140 satır**) üç ayrı yerde (README, QUALITY_CRITERIA, audits/…policy) "learning sample / pilot example" olarak işaretlenmiş; "final dataset / source selection / model-ready / benchmark değildir" ve "ADR 0001'i değiştirmez, hâlâ `Proposed`" diye tekrarlanmış. Her iki notebook da bu dosyayı **ana veri olarak okumuyor**, yalnızca "ileride kullanılacak" diye anıyor.
- **Bilimsel pipeline'a kayma var mı: [Bulgu] Hayır.** Notebook'ların sonundaki boundary-check hücreleri (`downloads_data: False`, `trains_model: False`, `creates_train_test_split: False`, `computes_metrics_or_benchmark: False`, `selects_final_dataset: False`, `accepts_adr: False`) ve audit'lerdeki "No-go kontrolü" blokları bunu doğruluyor. Toy moleküller (etanol, aseton, asetik asit, benzen, anilin…) kullanılıyor; metrik/skor üretilmiyor.
- **Prompt provenance düzeni: [Bulgu] Yeterli ama 00'da retroaktif.** `prompts/00…` dosyası kendi içinde dürüstçe belirtiyor: notebook önce `d11f3c0` ile üretilmiş, prompt **geriye dönük** eklenmiş. `audits/00…` de aynı şeyi "prompt bu çalışma sırasında bulunamadı… düzeltme ile eklendi" diye kaydediyor. 01'de prompt+notebook+audit birlikte planlanmış. **[Çıkarım]** İdeal sıra prompt → notebook → audit; 00 bu sırayı sonradan kapatmış (kabul edilebilir, ama desenin tam oturmadığının işareti).
- **Audit dosyaları anlamlı mı: [Bulgu] Evet, ama 00 ve 01 şablonları biraz farklı.** Her iki audit da QUALITY_CRITERIA'ya karşı satır satır "Uygun" veriyor ve net "No-go kontrolü"/"Karar" blokları içeriyor. Ancak `audits/01…` başta ilgili prompt'u referans verirken `audits/00…` kontrol tablosunda "prompt provenance mevcut mu?" satırı yok. Küçük şablon tutarsızlığı.
- **[Bulgu] CURRICULUM ileri-vaat içeriyor.** `CURRICULUM.md` ve policy audit, sample'ın kullanılabileceği 6 notebook listeliyor (`04_…`, `05_…`, `06_…`, `12_…`, `13_…`, `14_…`) — bunların hiçbiri henüz yok. Ayrıca CURRICULUM "`00`, `01`, `02` ve `03` ile başlayan ilk teknik notebooklar" diyor ama **02 ve 03 mevcut değil**. Forward-looking olması sorun değil; "02, 03 var" iması hafif over-promise.
- **[Çıkarım] En ciddi RDKit bulgusu içerik tarafında, sınır tarafında değil:** notebook'ların Türkçe metni kayıtta bozulmuş (bkz. Bölüm 7, madde A). Audit'ler her satıra "Uygun" demiş ama bu encoding bozulmasını yakalamamış — `QUALITY_CRITERIA.md`'de bir encoding/karakter bütünlüğü kriteri yok.

## 5. Decision / ADR Hygiene

- **[Bulgu] Kaynak seçimi hâlâ açık ve unresolved.** `docs/adr/0001-data-source.md` `Status: Proposed`, `Decision: Pending Mehmetali approval. No specific source is selected.` `DECISION_BACKLOG.md`, `STATE.md`, `DECISION_NOTE.md` hepsi aynı şeyi söylüyor. ADR 0002 (scaffold split) ve 0003 (label set) de `Proposed`.
- **[Bulgu] NP-MRD / NMRShiftDB2 / HMDB ayrımı net.** `candidate-research.md` üçlüyü ayırıyor; NP-MRD ve NMRShiftDB2 "decision-ready" iki ana aday, **HMDB tutarlı biçimde fallback/comparison** (deneysel/predicted ¹³C ayrımı kontrolü beklemede). `DECISION_NOTE.md` ikiliyi lisans + anlatı/kapsam ekseninde karşılaştırıyor; karşılaştırma tablosu dengeli (NP-MRD: CC BY-NC, daha dar ama net; NMRShiftDB2: özel DB lisansı, daha geniş ama share-alike/derivative yükümlülükleri).
- **[Bulgu] Belirsizlikler doğru işaretlenmiş.** `verification-and-evidence.md`'deki her must-answer item `uncertain`; aggregate sayılar ("4.864", "70029/396583") "filtrelenmiş usable subset değil" uyarısıyla veriliyor. Lisans notu "legal advice değildir, final değildir, Mehmetali/danışman incelemesi gerekir" diyor.
- **[Bulgu] ADR gereksiz şişmiş değil — tersine, bilinçli olarak slim'lenmiş.** 0001 zaten ~74 satıra (template shape) indirilmiş; detay üç ayrı dosyaya taşınmış. STATE.md'de geçmişte "X ADR 0001'e eklendi" diyen birçok bullet var; bu, kanıtların **eskiden** ADR içinde biriktiğini ve sonradan dışarı alındığını gösteriyor.
- **[Öneri / Çıkarım] Bundan sonra ADR'ye ek YAPMA; ayrı karar notları daha doğru.** Mevcut yapı (ADR = donmuş template + `docs/decisions/data-source/` = canlı kanıt) zaten bu yöne karar vermiş ve doğru karar. Yeni kanıt/tartışma `docs/decisions/data-source/` altına eklenmeli; ADR 0001 yalnızca Mehmetali bir yön onayladığında ve `Accepted`'a geçeceği an dokunulmalı. ADR'yi tekrar append-target'a çevirmek, yapılan slim refactor'u geri alır.

## 6. No-Go Boundary Check

| Kontrol | Sonuç | Kanıt |
| --- | --- | --- |
| Veri indirme var mı? | **Hayır** | `STATE.md`: "Data downloaded: No". Hiçbir loader/fetch kodu yok. |
| `data/raw` yanlış kullanılmış mı? | **Hayır** | `data/raw/README.md` placeholder; "No raw data is added". |
| `data/processed` yanlış kullanılmış mı? | **Hayır** | `data/processed/README.md` placeholder; "No processed data is created". |
| Modelleme kodu var mı? | **Hayır** | `src/`, `models/` yalnızca README. Notebook'larda model yok. |
| Train/test split var mı? | **Hayır** | Yok; `test_no_scaffold_leak.py` bilinçli `skip` placeholder. |
| Evaluation / skor var mı? | **Hayır** | `test_f1_regression.py` bilinçli `skip`; metrik üretilmiyor. |
| Sahte sonuç var mı? | **Hayır** | `MODEL_OUTPUT_POLICY.md` + boundary-check hücreleri; hiçbir uydurma sayı yok. |
| `experiments/runs.csv` yanlış kullanılmış mı? | **Hayır** | Yalnızca header satırı; `test_runs_csv_header_only` bunu zorluyor. |
| Learning gate yanlışlıkla Passed mı? | **Hayır** | `learning/GATE_STATUS.md` 6 gate de `Not started`; `test_learning_gates_not_passed` "Passed" stringini yasaklıyor. |
| ADR Accepted mı? | **Hayır** | 0001/0002/0003 `Proposed`; `test_adrs_are_proposed_not_accepted` "Accepted"ı yasaklıyor. |
| NMReDATA sample modellemeye kaymış mı? | **Hayır** | Notebook'larda ana veri olarak okunmuyor; policy audit modelleme/split/skor yasağını tekrarlıyor. |

**Sonuç: [Bulgu] Tüm no-go sınırları korunuyor.** İhlal yok.

## 7. Small Hygiene Issues

Bu bölüm bilinçli olarak ayrıntılı.

**A. [Bulgu — en somut sorun] İki RDKit notebook'unda Türkçe karakter bozulması (mojibake).**
`learning/rdkit/notebooks/00_rdkit_projedeki_rolu.ipynb` ve `01_smiles_mol_nesnesi.ipynb` dosyalarında Türkçe karakterler kayıtta literal `?` (0x3F) ile değişmiş.
- Byte düzeyinde doğrulandı: 00 → 499 adet `?`, 01 → 682 adet `?`; her ikisinde de **sıfır** UTF-8 Türkçe dizisi (ör. `molek?lle ?al??man?n`).
- Karşılaştırma: aynı modüldeki `.md` dosyaları (`README.md`, `CURRICULUM.md`) temiz UTF-8 (proper ç/ö/ü/ş/ğ/ı, sıfır `?`). Yani sorun **yalnızca `.ipynb`'lere özgü**.
- **[Çıkarım]** Notebook'lar muhtemelen Türkçe karakterleri kodlayamayan bir encoding (ASCII/cp1252) ile yazılmış. Notebook'ların öğretici değeri büyük ölçüde **prose** olduğundan bu, modülün asıl çıktısını gözle görülür biçimde düşürüyor.
- **[Çıkarım]** Audit'ler her satıra "Uygun" verdi ama bunu kaçırdı; `QUALITY_CRITERIA.md`'de karakter-bütünlüğü kriteri yok. CI yalnızca `pytest` koşuyor (`requirements.txt` sadece `pytest>=8.0`; RDKit/Jupyter yok), notebook'ları çalıştırmıyor/lint'lemiyor → bozulma CI'a da görünmez.

**B. [Bulgu] Phase 0 ↔ Phase 1A doküman kayması.**
`STATE.md` "Phase 0 kapandı, güncel = Phase 1A" diyor. Ama şu dosyalar hâlâ şimdiki-zaman "Phase 0 / during setup" diliyle yazılı: `README.md`, `START_HERE.md`, `AGENTS.md`, `PROJECT_INVARIANTS.md`, `governance/NOW_LATER_FORBID.md` (başlık: "NOW - Phase 0"), `governance/STOP_DOING_LIST.md`, `data/README.md`, `data/raw/README.md`, `data/processed/README.md`, ve test skip-reason'ları ("Phase 0 placeholder only"). **[Çıkarım]** İronik nokta: Phase 1A'nın `ROADMAP.md`'deki amaçlarından biri "reduce document drift" — bu kayma tam da o hedefin konusu.

**C. [Bulgu] STATE.md'de ASCII-Türkçe bullet tutarsızlığı.**
İlk RDKit STATE bullet'ı diakritiksiz yazılmış ("dosyasinin", "kullanilmasina", "secimi degildir", "kabulu yapilmadi") iken hemen altındaki RDKit bullet'ları proper Türkçe ("üretildi ve audit edildi", "eğitim amaçlıdır"). Aynı dosyada iki farklı yazım.

**D. [Çıkarım/Bulgu] RDKit modülü mekanik yapı testinin dışında.**
`tests/test_repository_structure.py` içindeki `REQUIRED_FILES` listesinde hiçbir `learning/rdkit/` yolu yok ve modüle özgü bir invariant testi yok (ör. notebook'ların varlığı, içeride "Passed"/"Accepted" string'i bulunmaması). Reponun geri kalanını koruyan kapı bu modülü kapsamıyor; disiplin tamamen prose+manuel audit'e dayanıyor.

**E. [Bulgu] Var olmayan notebook'lara referans (over-promise).**
`CURRICULUM.md` "00, 01, 02, 03 ile başlayan ilk teknik notebooklar" diyor; 02/03 yok. CURRICULUM ve policy audit, sample'ın kullanılacağı 6 ileri notebook (04/05/06/12/13/14) listeliyor; hiçbiri yok. Numara atlaması (01 → 04) ileride boşluk olarak sorulabilir.

**F. [Çıkarım] PROTOTYPE_SHAPE.md'de sıra ifadesi yanıltıcı olabilir.**
`learning/PROTOTYPE_SHAPE.md` tablosu **pipeline sırasında** (Source → subset → labels → baseline → split → metric) ve gate etiketleri monoton değil (02, 02/04, 03, 01, 05, 06). Ama prose "The order matches the gate learning order" diyor. Gate öğrenme sırası (01 → 03 → 02 → 04 → 05 → 06) ile tablo satır sırası farklı; cümle, tablo sırasını gate sırasıyla aynıymış gibi okutabiliyor.

**G. [Bulgu] NMReDATA sample için dosya-düzeyi provenance eksik.**
`audits/nmrshiftdb2_nmredata_learning_sample_policy.md` statüyü (learning sample) net tanımlıyor ama dosyanın kendisinin provenance'ı (hangi URL'den, hangi nmrshiftdb2 export'undan, hangi tarihte, 196 kayıt) tek satırda kayıtlı değil. Veri-kaynağı kanıt notlarındaki titiz "source/access date/caveats" disiplini bu sample dosyaya uygulanmamış.

**H. [Bulgu — çok küçük] İsimlendirme.**
`nmrshiftdb2rawdata.nmredata.sd` adında "rawdata" birleşik yazımı biraz garip ama zararsız; notebook/prompt/audit adları (`00_rdkit_projedeki_rolu`, `01_smiles_mol_nesnesi`) tutarlı ve iyi.

**I. [Çıkarım — housekeeping] Merge edilmiş dallar duruyor.**
Remote'ta 5 feature dalı (governance/phase-1a-definition, learning/operationalize-gates, learning/prototype-shape, docs/slim-adr-0001, docs/data-source-decision-note) master'a merge edildikten sonra hâlâ duruyor. Ayrıca yerel checkout, master yerine merge edilmiş bir feature dalında. Bu, "GitHub reposu" ile yerel görüntü arasında kafa karışıklığı yaratabilir (nitekim bu incelemede RDKit modülü ilk bakışta "yok" göründü).

**J. [Bulgu] 37k satırlık örnek dosyanın ağırlığı.**
`examples/nmrshiftdb2rawdata.nmredata.sd` 37.140 satır. Doğru biçimde "learning sample" olarak çitlenmiş ve `.gitignore` dışı tutulması bilinçli; yine de bir "command center" reposunda en büyük dosya bu. Çit net olduğu sürece kabul edilebilir; not olarak bırakılıyor.

## 8. Recommended Next Small Steps

Hepsi yalnızca dokümantasyon/öğrenme/audit; veri indirme yok, modelleme yok, kaynak seçimi yok, ADR Accepted yok. Mümkün olduğunca tek-commit.

**Öneri 1 — Notebook encoding'ini düzelt (en yüksek değer).**
- **Amaç:** 00 ve 01 notebook'larındaki `?` mojibake'ini düzelterek Türkçe öğretici metni geri kazanmak.
- **Değiştirilecek dosyalar:** `learning/rdkit/notebooks/00_rdkit_projedeki_rolu.ipynb`, `learning/rdkit/notebooks/01_smiles_mol_nesnesi.ipynb` (UTF-8 olarak yeniden yazım; içerik/sınırlar aynı kalır).
- **Risk seviyesi:** Düşük (yalnızca metin/encoding; kod mantığı ve boundary-check'ler değişmez).
- **Neden şimdi:** Modülün asıl öğretici çıktısı şu an okunaksız; üzerine 02+ notebook üretmeden önce düzeltilmeli.

**Öneri 2 — QUALITY_CRITERIA'ya encoding/karakter-bütünlüğü kriteri ekle.**
- **Amaç:** Gelecekteki notebook'ların aynı mojibake'e düşmesini ve audit'lerin bunu kaçırmasını önlemek.
- **Değiştirilecek dosyalar:** `learning/rdkit/QUALITY_CRITERIA.md` (bir madde), ileride audit şablonuna bir satır.
- **Risk seviyesi:** Düşük.
- **Neden şimdi:** Öneri 1 ile aynı commit ailesinde mantıklı; kök-neden kapatma.

**Öneri 3 — STATE.md RDKit bullet'ını proper Türkçe'ye çevir.**
- **Amaç:** Tek dosya içi yazım tutarlılığı (madde C).
- **Değiştirilecek dosyalar:** `STATE.md` (tek bullet).
- **Risk seviyesi:** Çok düşük.
- **Neden şimdi:** Önemsiz ve anında.

**Öneri 4 — Phase 0 → Phase 1A dilini tek geçişte uyumla.**
- **Amaç:** Doküman kaymasını (madde B) kapatmak; ya metinleri güncellemek ya da her birine "Phase 0 kapandı; güncel faz için STATE.md" tek-satır pointer'ı eklemek.
- **Değiştirilecek dosyalar:** `README.md`, `START_HERE.md`, `AGENTS.md`, `PROJECT_INVARIANTS.md`, `governance/NOW_LATER_FORBID.md`, `governance/STOP_DOING_LIST.md`, `data/README.md`, `data/raw/README.md`, `data/processed/README.md`.
- **Risk seviyesi:** Düşük (yalnızca prose). **Not:** test `test_phase_zero_boundaries_are_documented` "Do not modify `data/raw/`", "Do not write model code", "Do not invent citations" string'lerini bekliyor; bu cümleler korunmalı.
- **Neden şimdi / neden sonra:** Phase 1A'nın deklare amacı bu; ama çok dosyaya dokunduğu için Öneri 1–3'ten sonra ayrı, odaklı bir commit olarak.

**Öneri 5 — Yapı testini RDKit modülünü kapsayacak şekilde genişlet.**
- **Amaç:** Modülü reponun geri kalanıyla aynı mekanik kapıya almak (madde D). Notebook/prompt/audit dosyalarının varlığı + modül içinde "Passed"/"Accepted" geçmemesi assert'lenebilir.
- **Değiştirilecek dosyalar:** `tests/test_repository_structure.py` (yeni assert/REQUIRED girişleri). Bu bir **test** değişikliğidir, bilimsel kod değil.
- **Risk seviyesi:** Düşük.
- **Neden sonra:** Önce encoding düzeltilmeli (aksi halde içerik testleri kırılgan olur).

**Öneri 6 — NMReDATA sample'a dosya-düzeyi provenance ekle.**
- **Amaç:** Sample'ın kaynak URL'i, export tipi, erişim tarihi ve kayıt sayısını (196) tek satırda kayıt altına almak (madde G).
- **Değiştirilecek dosyalar:** `learning/rdkit/audits/nmrshiftdb2_nmredata_learning_sample_policy.md` (veya `examples/` altına kısa bir `README`/`PROVENANCE` notu).
- **Risk seviyesi:** Düşük.
- **Neden sonra:** Disiplini güçlendirir ama acil değil.

**Öneri 7 — CURRICULUM'daki var-olmayan-notebook ifadelerini gerçekle hizala.**
- **Amaç:** "02, 03 var" imasını "planlanan" diline çevirmek (madde E).
- **Değiştirilecek dosyalar:** `learning/rdkit/CURRICULUM.md`.
- **Risk seviyesi:** Çok düşük.
- **Neden sonra:** Kozmetik.

## 9. What Not To Do Yet

Şu an **yapılmaması** gerekenler:

- **Final dataset seçimi** — NP-MRD/NMRShiftDB2/HMDB hiçbiri seçilmemeli; karar Mehmetali'de ve must-answer item'lar `uncertain`.
- **Parser pipeline** — `.sd`/NMReDATA için parser/loader yazılmamalı (sample bunun için bile değil; yalnızca okuma-farkındalığı için).
- **Modelleme** — hiçbir model/baseline kodu yok.
- **Train/test split** — scaffold dahil hiçbir split kodu.
- **Evaluation** — metrik/değerlendirme kodu yok.
- **Macro F1 raporu** — gerçek ya da örnek hiçbir skor üretilmemeli.
- **Proposal final text** — `proposal/` placeholder kalmalı; final TÜBİTAK dili yazılmamalı.
- **Learning gate Passed** — 6 gate de `Not started`; Passed yalnızca Mehmetali kanıtı + reviewer notu ile.
- **ADR Accepted** — 0001/0002/0003 `Proposed` kalmalı.
- **Ek:** `.sd` dosyası `data/raw/`'a taşınmamalı; `experiments/runs.csv`'ye satır eklenmemeli; veri indirilmemeli.

## 10. Final Verdict

**Repo doğru yönde.** Bir Command Center'dan beklenen disiplini hem doküman hem de **test/CI** seviyesinde gerçekten uyguluyor; veri kaynağı kararı olgun biçimde açık tutulmuş; RDKit modülü temiz izole edilmiş ve hiçbir no-go ihlali yok. Genel statü **PASS**, hijyen tarafında **WATCH**.

**Bir sonraki küçük adım:** önce **notebook encoding düzeltmesi** (Öneri 1) ve buna eşlik eden **QUALITY_CRITERIA encoding kriteri** (Öneri 2). Bu, hâlihazırda inşa edilmiş öğrenme içeriğinin asıl değerini geri kazandıran, ucuz ve sınır-dokunmayan bir iş.

**RDKit Learning Module devam etmeli mi, önce hijyen mi?** Modül kavramsal olarak doğru ilerliyor ve durdurulması gerekmiyor — ama **02+ notebook üretmeden önce mevcut 00/01'in encoding'i düzeltilmeli** ve QUALITY_CRITERIA'ya encoding kriteri eklenmeli. Yani: küçük hijyen düzeltmesi (Öneri 1–3) → sonra modüle devam. Phase 0/1A dil uyumlaması (Öneri 4) ve test genişletmesi (Öneri 5) paralelde, ayrı küçük commit'ler olarak ilerletilebilir.
