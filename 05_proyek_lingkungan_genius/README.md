# 🏆 Modul 5: Starter Blueprint Proyek Lomba GENIUS Olympiad

Modul ini adalah **templat metodologi ilmiah** yang dirancang khusus untuk memenuhi standar penilaian kategori **Artificial Intelligence (AI)** pada ajang **GENIUS Olympiad**.

---

## 🚨 Syarat Mutlak GENIUS Olympiad
Di kompetisi ini, juri **tidak** mencari aplikasi biasa. Juri mencari:
1. **Environmental Focus:** Memecahkan masalah lingkungan hidup yang nyata.
2. **Karya Otentik:** Bukan sekadar memanggil API pihak ketiga atau sekadar chatbot siap pakai.
3. **Evaluasi Kuantitatif:** Menyajikan metrik ilmiah yang diakui dunia akademik: *Akurasi, Confusion Matrix, Precision, Recall, dan F1-Score*.
4. **Measurable Environmental Impact:** Menghitung estimasi dampak positif (kg sampah tersortir, reduksi emisi karbon $kg\text{ }CO_2e$, atau luas hutan terselamatkan).

---

## 🎯 Studi Kasus: "EcoSort Nusantara"
Proyek ini mensimulasikan pemilahan 4 kategori sampah perairan sungai/pesisir khas Indonesia:
* **Kelas 1:** Plastik PET (Botol Minuman Bening)
* **Kelas 2:** Plastik Multilayer Sachet (Bungkus Kopi/Snack - masalah terbesar Bank Sampah)
* **Kelas 3:** Styrofoam (Polistirena)
* **Kelas 4:** Sampah Organik (Daun, Ranting)

---

## 🚀 Cara Menjalankan
Buka terminal dan jalankan:

```bash
python main.py
```
atau dari root direktori proyek:
```bash
python 05_proyek_lingkungan_genius/main.py
```

---

## 📊 Output Ilmiah yang Dihasilkan
1. **Laporan Confusion Matrix:** Menunjukkan ketepatan prediksi tiap kategori sampah.
2. **Tabel Evaluasi (Precision, Recall, F1-Score):** Komponen wajib di bab hasil dan pembahasan proposal.
3. **SDGs Impact Calculator:** Mengonversi jumlah sampah ke dalam estimasi reduksi jejak karbon ($CO_2e$) dan relevansi ke target PBB (SDG 12, 13, 14).
