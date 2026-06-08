# 01 SMILES Mol Nesnesi Audit

## Kapsam

Denetlenen notebook:
`learning/rdkit/notebooks/01_smiles_mol_nesnesi.ipynb`

İlgili prompt provenance:
`learning/rdkit/prompts/01_smiles_mol_nesnesi_prompt.md`

Bu audit, notebookun RDKit Learning Module sınırlarına ve
`QUALITY_CRITERIA.md` kurallarına uygunluğunu kontrol eder.

## Kontrol sonuçları

| Kontrol | Sonuç | Not |
| --- | --- | --- |
| Notebook SMILES kavramını anlaşılır anlatıyor mu? | Uygun | SMILES, bilgisayarın okuyabileceği kompakt molekül temsili olarak açıklandı. |
| Mol nesnesinin string olmadığı net anlatılmış mı? | Uygun | `Mol` nesnesinin atom, bağ, halka ve yapı bilgisi taşıyan hesaplanabilir temsil olduğu vurgulandı. |
| Geçerli/geçersiz SMILES farkı gösterilmiş mi? | Uygun | Oyuncak listede `C1CC` geçersiz kapanmamış halka örneği olarak kullanıldı ve `None` davranışı açıklandı. |
| Canonical SMILES duplicate farkındalığına bağlanmış mı? | Uygun | Farklı SMILES yazımlarının canonical forma çevrilebileceği, bunun duplicate farkındalığına yardım ettiği belirtildi. |
| RDKit yoksa notebook çökmeden davranıyor mu? | Uygun | Güvenli import mantığı kullanıldı; RDKit yoksa teknik hücreler açıklama vererek atlanıyor. |
| NMReDATA learning sample ana veri gibi kullanılmamış mı? | Uygun | `nmrshiftdb2rawdata.nmredata.sd` okunmadı; yalnızca ilerideki learning sample / pilot example olarak anıldı. |
| Modelleme, split, metric, benchmark veya sahte sonuç yok mu? | Uygun | Notebook yalnızca oyuncak molekül temsili ve kavramsal RDKit akışı içeriyor. |
| `QUALITY_CRITERIA.md` kurallarına uyuyor mu? | Uygun | Final dataset, model-ready veri, benchmark veya evaluation üretilmedi. |
| Bu notebook final dataset seçimi veya bilimsel pipeline başlatıyor mu? | Uygun | Veri kaynağı seçimi, ADR kabulü, processed veri, modelleme veya evaluation yok. |

## No-go kontrolü

- ADR 0001 değiştirilmedi.
- Kaynak seçimi yapılmadı.
- Final dataset ilan edilmedi.
- `data/raw/` veya `data/processed/` içine dosya eklenmedi.
- `experiments/runs.csv` değiştirilmedi.
- Modelleme kodu yazılmadı.
- Train/test split yazılmadı.
- Macro F1, accuracy, benchmark veya skor üretilmedi.
- Learning gate `Passed` yapılmadı.

## Karar

Notebook eğitim amaçlı SMILES → RDKit `Mol` giriş notebooku olarak kabul
edilebilir.

Bu kabul, bilimsel veri kaynağı seçimi veya pipeline başlangıcı anlamına gelmez.
