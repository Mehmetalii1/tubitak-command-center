# NMRShiftDB2 NMReDATA Learning Sample Policy Audit

## Kabul edilen statü

`learning/rdkit/examples/nmrshiftdb2rawdata.nmredata.sd` dosyasının kabul edilen
statüsü: `learning sample / pilot example`.

Bu dosya RDKit öğrenme modülünde gerçekçi ama kontrollü örnek veri olarak
kullanılabilir.

## Kabul edilmeyen statü

Bu dosya aşağıdaki statülerde kabul edilmez:

- final dataset
- source selection
- model dataset
- model-ready dataset
- benchmark dataset
- cleaned scientific dataset

## Kullanılabileceği notebooklar

- `04_kimyasal_veri_temizligi.ipynb`
- `05_smarts_substructure_search.ipynb`
- `06_fonksiyonel_grup_etiketleme.ipynb`
- `12_proje_koprusu_yapi_to_label_matrix.ipynb`
- `13_rdkit_debugging.ipynb`
- `14_rdkit_quality_control_checklist.ipynb`

## Kullanılamayacağı işler

- Final TUBITAK dataset'i ilan etmek.
- Veri kaynağı seçmek veya ADR 0001'i kapatmak.
- Model eğitmek.
- Train/test split üretmek.
- Macro F1, accuracy, benchmark veya final sonuç üretmek.
- Processed veri üretmek.
- Deney run kaydı oluşturmak.
- Learning gate statüsünü Passed yapmak.

## No-go listesi

- ADR 0001 `Accepted` yapılmayacak.
- Bu dosya `data/raw/` içine proje datası gibi taşınmayacak.
- `data/processed/` altında türetilmiş veri oluşturulmayacak.
- `experiments/runs.csv` içine gerçek veya sahte run eklenmeyecek.
- Parser, modelleme, split veya evaluation kodu bu karar kapsamında
  yazılmayacak.
- Dosyadaki property alanları temiz, doğru veya modelleme-ready varsayılmayacak.
- 13C alanı bulunması tek başına kullanılabilir bilimsel dataset kabulü
  sayılmayacak.

## ADR 0001 ilişkisi

Bu karar ADR 0001'i değiştirmez.

ADR 0001 hala `Proposed` durumundadır. Bu learning sample politikası, veri
kaynağı seçimi değildir ve TUBITAK final dataset kararını temsil etmez.
