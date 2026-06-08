# 00 RDKit Projedeki Rolü Prompt Provenance

## Geriye dönük kayıt notu

- Bu prompt, `00_rdkit_projedeki_rolu.ipynb` için üretim niyetini belgelemek
  amacıyla geriye dönük eklenmiştir.
- Notebook daha önce `d11f3c0 docs: add rdkit introduction notebook` commit'iyle
  üretilmiştir.
- Bu dosya notebooku yeniden üretmez; yalnızca prompt provenance / üretim kaydı
  sağlar.
- RDKit Learning Module eğitim amaçlıdır; final dataset seçimi, modelleme,
  split, evaluation veya ADR kabulü değildir.

## Üretim promptu

RDKit Learning Module içinde ilk eğitim notebookunu üret:

`learning/rdkit/notebooks/00_rdkit_projedeki_rolu.ipynb`

Bu notebookun amacı RDKit'i "molekül yapısını Python'da temsil etme ve kimyasal
veriyi makine öğrenmesine hazırlanabilir hâle getirme aracı" olarak tanıtmaktır.

Notebook Türkçe yazılmalıdır. Teknik terimler Türkçe anlatılmalı, gerekiyorsa
İngilizcesi parantez içinde verilmelidir. Anlatım kimya öğrencisine uygun,
öğretici, sakin ve gereksiz akademik ağırlıktan uzak olmalıdır.

Notebookta özellikle şunlar yapılmalıdır:

- RDKit'in projedeki rolünü net biçimde tanıt.
- ¹³C NMR → fonksiyonel grup tahmini projesiyle bağlantı kur.
- SMILES kavramını giriş seviyesinde açıkla.
- RDKit `Mol` nesnesinin molekül yapısını Python içinde temsil ettiğini anlat.
- Descriptor kavramını, molekülün sayısal/kategorik özeti olarak tanıt.
- Fingerprint kavramını, molekül yapısının bit/vektör benzeri temsili olarak
  açıkla.
- SMARTS kavramını, alt yapı arama deseni olarak tanıt.
- Label matrix kavramını, çok etiketli fonksiyonel grup fikrine giriş olarak
  açıkla.
- Küçük ve kontrollü bir oyuncak molekül listesi kullan.
- Oyuncak örneklerin final proje dataset'i olmadığını açıkça belirt.
- `nmrshiftdb2rawdata.nmredata.sd` dosyasını bu ilk notebookta ana veri olarak
  kullanma; yalnızca ileride kullanılacak `learning sample / pilot example`
  olarak kısaca an.
- RDKit kurulu değilse notebookun tamamen çökmesini engelleyecek güvenli import
  mantığı kullan.
- RDKit yoksa kavramsal açıklamaların okunabilir kalmasını ve RDKit gerektiren
  kod hücrelerinin güvenli şekilde atlanmasını sağla.

Kod kuralları:

- Kodlar basit, okunabilir ve öğretici olmalı.
- Gerekli yerlerde kısa `#` açıklamaları kullanılmalı.
- Dosya indirme yapılmamalı.
- Dosya yazma yapılmamalı.
- Modelleme yapılmamalı.
- Train/test split yapılmamalı.
- Metric, Macro F1, accuracy, benchmark veya skor üretilmemeli.
- Sahte sonuç veya bilimsel sonuç üretilmemeli.
- Final dataset seçimi veya veri kaynağı seçimi yapılmamalı.
- ADR kabulü veya learning gate `Passed` statüsü verilmemeli.

Notebook sonunda bilinçli olarak yapılmayan işler kısa bir sınır kontrolüyle
özetlenmelidir: veri indirme yok, modelleme yok, split yok, evaluation yok, final
dataset seçimi yok, ADR kabulü yok.
