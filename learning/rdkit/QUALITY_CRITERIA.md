# RDKit Quality Criteria

## Amaç

Bu belge, RDKit öğrenme modülünde kullanılacak örneklerin ve notebookların güvenli
sınırlarını tanımlar. Kriterler öğrenme, kalite kontrol ve debugging içindir;
bilimsel pipeline başlatmaz.

## Learning sample usage rules

- `nmrshiftdb2rawdata.nmredata.sd` dosyası final dataset gibi
  adlandırılmayacak.
- Bu dosya üzerinden model eğitilmeyecek.
- Macro F1, accuracy, benchmark veya final sonuç üretilmeyecek.
- Dosya sadece öğrenme, parsing, kalite kontrol ve debugging amacıyla
  kullanılacak.
- Notebooklar bu dosyayı okurken hata toleranslı kod kullanacak.
- Notebooklar dosyadaki her property alanının bilimsel olarak doğru veya temiz
  olduğunu varsaymayacak.
- 13C verisi varsa bile bu doğrudan modelleme-ready kabul edilmeyecek.
- Duplicate, assignment, solvent, sıcaklık, measured/calculated ve metadata
  konuları öğrenme amaçlı tartışılacak.

## Notebook beklentileri

- Notebooklar örnek veriyi okurken başarısız kayıtlar, eksik property alanları ve
  beklenmeyen metadata için açıklayıcı kontroller içermelidir.
- Notebook anlatımı, kod yorumları ve insan-okur çıktıları UTF-8 Türkçe karakter
  bütünlüğünü korumalıdır; `?`e dönüşmüş mojibake bırakılmamalı, emin olunamayan
  yerler audit içinde açıkça raporlanmalıdır.
- Notebooklar örnek veriden çıkarılan gözlemleri bilimsel sonuç gibi
  sunmamalıdır.
- Notebooklar veri kaynağı seçimi, final label schema, split stratejisi veya
  evaluation protokolü kararı vermez.
