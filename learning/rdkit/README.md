# RDKit Learning Module

## Amaç

Bu klasör, TUBITAK 2209-A 13C NMR fonksiyonel grup tahmini projesi için RDKit
öğrenme notlarını, kontrollü örnekleri, kalite kurallarını ve audit kayıtlarını
tutar.

Bu modül bilimsel pipeline değildir. Buradaki içerik, Mehmetali'nin RDKit,
SDF/NMReDATA okuma, molekül-property ilişkisi, kalite kontrol ve debugging
konularını öğrenmesi için hazırlanır.

## NMReDATA learning sample

`examples/nmrshiftdb2rawdata.nmredata.sd` dosyasının kabul edilen statüsü:
`learning sample / pilot example`.

Bu dosya:

- RDKit/NMReDATA öğrenimi için gerçekçi ama kontrollü bir örnektir.
- SDF okuma, NMReDATA property alanlarını inceleme, 13C NMR alanlarını tanıma,
  molecule/property bağlantısını anlama, duplicate farkındalığı ve ileride
  parser/debugging öğrenimi için kullanılabilir.
- Final TUBITAK dataset'i değildir.
- Veri kaynağı seçimi anlamına gelmez.
- Modelleme veya evaluation için kullanılmayacaktır.
- Model-ready, clean, final veya benchmark dataset olarak adlandırılmayacaktır.

## Sınırlar

- Bu modül `data/raw/` yerine geçmez.
- Bu modülde processed veri üretilmez.
- Bu modülde train/test split, benchmark, Macro F1, accuracy veya final sonuç
  üretilmez.
- Bu modül ADR 0001'i değiştirmez; veri kaynağı kararı hala ayrıdır ve Mehmetali
  onayı gerektirir.
