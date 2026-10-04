# 👁️ Modul 2: Dasar Computer Vision (OpenCV & NumPy)

Modul ini mengajarkan bagaimana komputer "melihat" dan memproses data visual (gambar dan video).

---

## 🎯 Tujuan Pembelajaran
Setelah menyelesaikan modul ini, Zaki akan mampu:
1. Memahami representasi gambar digital sebagai **Matriks Angka (NumPy Array)**.
2. Memahami ruang warna **BGR vs RGB** dan konversi ke **Grayscale** untuk efisiensi komputasi AI.
3. Menerapkan **Gaussian Blur** untuk membersihkan *noise* (derau) pada foto lapangan.
4. Menggunakan algoritma **Canny Edge Detection** untuk mendeteksi garis tepi kontur objek.
5. Menemukan kontur objek dan menggambar **Bounding Box (Kotak Pembatas)** secara otomatis.

---

## 🚀 Cara Menjalankan
Buka terminal dan jalankan:

```bash
python main.py
```
atau dari root direktori proyek:
```bash
python 02_dasar_computer_vision/main.py
```

Setelah dijalankan, file hasil visualisasi langkah demi langkah akan tersimpan otomatis di folder `output/`.

---

## 🖼️ Alur Pemrosesan Visual AI (Pipeline)
```
[ Citra Asli (BGR) ]
         │
         ▼
[ Konversi Grayscale ]  --> Mengurangi beban komputasi 66%
         │
         ▼
[ Gaussian Blur ]       --> Menghilangkan bintik/derau (noise)
         │
         ▼
[ Canny Edges ]         --> Menemukan gradien dan garis kontur
         │
         ▼
[ Bounding Box ]        --> Menandai lokasi koordinat objek (X, Y, W, H)
```
