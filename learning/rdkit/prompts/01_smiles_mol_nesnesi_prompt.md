# 01 SMILES Mol Nesnesi Prompt Provenance

## Üretim kayıt notu

- Bu prompt, `01_smiles_mol_nesnesi.ipynb` notebookunun üretim niyetini ve
  sınırlarını belgelemek için eklenmiştir.
- RDKit Learning Module eğitim amaçlıdır; final dataset seçimi, kaynak seçimi,
  modelleme, split, evaluation, metric, benchmark veya ADR kabulü değildir.
- Bu prompt, küçük oyuncak molekül listesiyle güvenli bir SMILES → RDKit `Mol`
  giriş notebooku üretilmesini ister.

## Üretim promptu

RDKit Learning Module içinde ikinci eğitim notebookunu üret:

`learning/rdkit/notebooks/01_smiles_mol_nesnesi.ipynb`

Ayrıca bu notebookun üretim promptunu ve audit dosyasını oluştur:

- `learning/rdkit/prompts/01_smiles_mol_nesnesi_prompt.md`
- `learning/rdkit/audits/01_smiles_mol_nesnesi_audit.md`

Notebook amacı:

Öğrenci RDKit'te temel iş akışını öğrenmeli:

`SMILES metni → RDKit Mol nesnesi → temel molekül kontrolü → canonical SMILES → basit görselleştirme`

Notebook sonunda öğrenci şunu anlamalı:

> RDKit'te molekülle çalışmanın başlangıç noktası çoğu zaman SMILES metnini Mol
> nesnesine çevirmektir. Mol nesnesi yalnızca bir string değildir; atom, bağ,
> halka ve kimyasal yapı bilgisini taşıyan hesaplanabilir bir temsildir.

Notebook dili:

- Türkçe yaz.
- Teknik terimlerin İngilizcesini gerektiğinde parantez içinde ver.
- Kimya öğrencisine uygun, öğretici, sakin ve adım adım anlat.
- Çok basitleştirme ama gereksiz akademik ağırlaştırma da yapma.
- Kod bloklarında önemli satırlara kısa `#` açıklamaları ekle.

Notebook bölümleri:

1. Başlık, amaç ve yapılmayanlar.
2. Önceki notebookla bağlantı.
3. SMILES nedir?
4. RDKit `Mol` nesnesi nedir?
5. Güvenli RDKit import.
6. Küçük oyuncak molekül listesi.
7. SMILES → Mol dönüşümü.
8. Canonical SMILES.
9. Temel molekül bilgileri.
10. Basit görselleştirme.
11. ¹³C NMR projesi bağlantısı.
12. Mini alıştırmalar.
13. Kapanış özeti.

İçerik beklentileri:

- Ethanol, acetone, acetic acid, benzene, ethyl acetate, aniline ve cyclohexane
  gibi 6-10 basit molekül kullan.
- `molecule_name`, `smiles`, `expected_note` alanlarıyla küçük bir oyuncak tablo
  oluştur.
- Geçerli ve geçersiz SMILES farkını göster; geçersiz örnek olarak kapanmamış
  halka gibi `C1CC` kullanılabilir.
- `Chem.MolFromSmiles()` mantığını açıkla.
- `None` dönen Mol nesnesinin veri kontrolü açısından ne anlama geldiğini
  belirt.
- Aynı molekülün farklı SMILES yazımları olabileceğini ve RDKit'in canonical
  SMILES üretebildiğini göster.
- Canonical SMILES'ın duplicate farkındalığında yararlı olduğunu, ancak tek
  başına bilimsel veri temizliği anlamına gelmediğini açıkla.
- Atom sayısı, bağ sayısı, ağır atom sayısı, molekül formülü ve molekül ağırlığı
  gibi temel bilgileri göster.
- Basit molekül çizimi veya grid çizimi yap; RDKit yoksa hücre güvenli açıklama
  versin.
- `nmrshiftdb2rawdata.nmredata.sd` dosyasını bu ilk teknik notebookta ana veri
  olarak kullanma; yalnızca ileride kullanılacak `learning sample / pilot
  example` olarak an.
- ¹³C NMR projesinde SMILES/Mol nesnesinin ileride SMARTS ile fonksiyonel grup
  arama, descriptor/fingerprint üretme ve kalite kontrol için temel olacağını
  anlat.

Kod ve güvenlik kuralları:

- Basit ve okunabilir kod yaz.
- RDKit kuruluysa teknik hücreler çalışsın.
- RDKit kurulu değilse notebook tamamen çökmesin; güvenli import mantığı kullan.
- Dosya indirme yok.
- Dosya yazma yok.
- Modelleme yok.
- Train/test split yok.
- Metric, Macro F1, accuracy, benchmark veya skor yok.
- Sahte sonuç yok.
- Final dataset seçimi veya veri kaynağı seçimi yok.
- `data/raw`, `data/processed`, `experiments/runs.csv` değişmeyecek.
- ADR kabulü veya learning gate `Passed` statüsü yok.
