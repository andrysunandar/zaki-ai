# 🍎 Modul 6: Pipeline Pengolahan Dataset FreshCheck AI

Modul ini mendemonstrasikan proses pengolahan dataset dari citra mentah (*raw image*) hingga menjadi fitur ilmiah dan prediksi kuantitatif **Remaining Shelf Life (RSL)** untuk mencegah sampah makanan (*food waste*).

---

## 🎯 Tahapan Pengolahan Dataset (Data Pipeline)

```
[ 1. Citra Buah Mentah (RGB/BGR) ]
                 │
                 ▼
[ 2. Konversi ke Ruang Warna HSV ]  --> Memisahkan intensitas cahaya dari krominansi warna
                 │
                 ▼
[ 3. Segmentasi Masking Warna ]     --> Menghitung Piksel Hijau, Kuning, dan Bintik Coklat
                 │
                 ▼
[ 4. Ekstraksi Fitur Ilmiah ]       --> Menghitung Brown Spot Area (BSA %)
                 │
                 ▼
[ 5. Augmentasi Citra ]             --> Flip, Brightness +/- 30, Gaussian Blur (simulasi kondisi nyata)
                 │
                 ▼
[ 6. Fusi Multimodal (Suhu Q10) ]   --> Menghitung Remaining Shelf Life (RSL dalam hari)
                 │
                 ▼
[ 7. Mesin Intervensi Pangan ]      --> Diskon Dinamis 50% & Resep Olahan Zero Food Waste
```

---

## 🚀 Cara Menjalankan

Buka terminal dan jalankan:
```bash
python main.py
```
atau dari root direktori proyek:
```bash
python 06_freshcheck_data_processing/main.py
```

Setelah script selesai dieksekusi, periksa visualisasi hasil olah data di folder `output/`:
1. `freshcheck_01_citra_asli.jpg` : Gambar asli buah pisang.
2. `freshcheck_02_segmentasi_warna.jpg` : 3 panel perbandingan masking tubuh buah, kulit kuning, dan bintik coklat (*BSA*).
3. `freshcheck_03_augmentasi.jpg` : Sampel hasil augmentasi cahaya dan rotasi.

---

## 🔬 Parameter Ilmiah yang Dihasilkan
1. **Brown Spot Area (BSA %):**
   $$\text{BSA (\%)} = \frac{\text{Jumlah Piksel Bintik Coklat}}{\text{Total Piksel Buah}} \times 100\%$$
2. **Kinetika Laju Kerusakan Suhu Tropis ($Q_{10}$):**
   Di iklim Indonesia (~30°C), laju respirasi dan kerusakan buah berlangsung **2x lebih cepat** dibandingkan penyimpanan ruang ber-AC (~20°C).
3. **Remaining Shelf Life (RSL):**
   Estimasi sisa hari layak konsumsi sebelum buah mengalami kebusukan total.
