# 00 RDKit Projedeki Rolü Audit

## Kapsam

Denetlenen notebook:
`learning/rdkit/notebooks/00_rdkit_projedeki_rolu.ipynb`

Bu audit, notebookun RDKit Learning Module sınırlarına ve
`QUALITY_CRITERIA.md` kurallarına uygunluğunu kontrol eder.

Not: `learning/rdkit/prompts/00_rdkit_projedeki_rolu_prompt.md` dosyası bu
çalışma sırasında repo içinde bulunamadı. Notebook, kullanıcı görev metni ve
mevcut RDKit Learning Module politika dosyaları esas alınarak üretildi.

Düzeltme notu: Daha önce eksik olduğu belirtilen prompt provenance dosyası bu
düzeltme ile eklendi. Notebook yeniden üretilmedi.

## Kontrol sonuçları

| Kontrol | Sonuç | Not |
| --- | --- | --- |
| Notebook RDKit'in projedeki rolünü net anlatıyor mu? | Uygun | RDKit, molekül yapısını Python'da temsil etme ve kimyasal veriyi öğrenme amaçlı hazırlama aracı olarak tanıtıldı. |
| ¹³C NMR projesiyle bağlantı kurulmuş mu? | Uygun | ¹³C NMR → fonksiyonel grup tahmini bağlamı açıklandı; RDKit'in yapı tarafındaki yardımcı rolü belirtildi. |
| Başlangıç seviyesindeki kimya öğrencisi için anlaşılır mı? | Uygun | Anlatım Türkçe, sakin ve kavram odaklı tutuldu; teknik terimler gerektiğinde İngilizce karşılıklarıyla verildi. |
| Gereksiz modelleme/veri indirme/sahte sonuç var mı? | Uygun | Veri indirme, modelleme, train/test split, metric, benchmark veya bilimsel sonuç üretilmedi. |
| RDKit yoksa notebook tamamen çöküyor mu? | Uygun | Güvenli import mantığı kullanıldı; RDKit yoksa kavramsal okuma devam ediyor ve RDKit gerektiren hücreler güvenli şekilde atlanıyor. |
| Notebook `QUALITY_CRITERIA.md` kurallarına uyuyor mu? | Uygun | Oyuncak molekül listesi kullanıldı; NMReDATA dosyası ana veri yapılmadı ve final dataset gibi adlandırılmadı. |
| Notebook final dataset seçimi veya bilimsel pipeline başlatıyor mu? | Uygun | Final dataset seçimi, source selection, ADR kabulü, processed veri, modelleme veya evaluation yok. |

## Encoding kontrolü

Notebook JSON geçerliliği korunarak Türkçe karakter bütünlüğü ayrıca kontrol
edildi. Bozuk `?` mojibake'i yalnızca prose, yorum ve insan-okur stringlerinde
düzeltildi; notebook yeniden çalıştırılmadı. Bu not bilimsel karar, ADR kabulü
veya learning gate geçişi anlamına gelmez.

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

Notebook eğitim amaçlı RDKit giriş notebooku olarak kabul edilebilir.

Bu kabul, bilimsel veri kaynağı seçimi veya pipeline başlangıcı anlamına gelmez.
