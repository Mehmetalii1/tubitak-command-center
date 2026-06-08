# RDKit Curriculum

## Amaç

Bu curriculum, RDKit öğrenme notebooklarının hangi tür veriyle çalışacağını
belirler. Erken teknik notebooklar küçük oyuncak molekül listeleriyle başlar;
gerçekçi ama kontrollü örnek gerektiğinde NMReDATA learning sample devreye girer.

## Veri kullanım düzeni

Mevcut `00` ve `01` notebooklarında küçük oyuncak molekül listeleri
kullanılır. Bu aşamada amaç RDKit nesnelerini, basit molekül okuma işlemlerini
ve temel kavramları öğrenmektir.

`02` ve sonraki teknik notebooklar henüz planlanan statüdedir. Bu curriculum
onları üretmez ve mevcut dosya olarak kabul etmez.

`examples/nmrshiftdb2rawdata.nmredata.sd` dosyası yalnızca daha gerçekçi örnek
gereken notebooklarda kullanılabilir. Bu kullanım, final dataset seçimi veya
modelleme hazırlığı anlamına gelmez.

## NMReDATA sample kullanılabilecek planlanan notebooklar

Aşağıdaki liste ileri RDKit öğrenme hattı için planlanan kullanımları gösterir;
bu notebookların üretildiği veya tamamlandığı anlamına gelmez.

- `04_kimyasal_veri_temizligi.ipynb`
- `05_smarts_substructure_search.ipynb`
- `06_fonksiyonel_grup_etiketleme.ipynb`
- `12_proje_koprusu_yapi_to_label_matrix.ipynb`
- `13_rdkit_debugging.ipynb`
- `14_rdkit_quality_control_checklist.ipynb`

## Kullanım amacı

Bu dosya şu öğrenme hedefleri için kullanılabilir:

- SDF dosyasını RDKit ile hata toleranslı okumayı görmek.
- NMReDATA property alanlarını listelemek ve yorumlamayı öğrenmek.
- 13C NMR ile ilişkili alanları tanımak.
- Molekül yapısı ile property metadata arasındaki bağlantıyı anlamak.
- Duplicate, assignment, solvent, sıcaklık, measured/calculated ve metadata
  sorunlarını öğrenme amacıyla tartışmak.
- Parser ve debugging disiplinine hazırlık yapmak.

## Kullanım sınırı

Bu curriculum kapsamında NMReDATA sample üzerinden model eğitimi, train/test
split, evaluation, Macro F1, accuracy, benchmark veya final bilimsel sonuç
üretilmez.
