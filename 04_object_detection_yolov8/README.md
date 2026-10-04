# 🎯 Modul 4: Object Detection dengan YOLOv8 & ONNX Runtime

Modul ini mengimplementasikan model deteksi objek mutakhir **YOLOv8 (You Only Look Once)** yang dioptimasi menggunakan **ONNX Runtime** berkecepatan tinggi.

---

## 🎯 Mengapa YOLOv8 Populer di Kompetisi Sains & AI?
* **Single-Stage Detector:** Tidak seperti detektor tradisional yang lambat, YOLO memprediksi seluruh kotak pembatas (*bounding boxes*) dan probabilitas kelas secara simultan dalam satu lintasan inferensi (*single pass*).
* **Super Cepat & Ringan:** Model YOLOv8 nano hanya berukuran ~6.4 MB dan mampu memproses satu frame gambar hanya dalam **~65 milidetik** di CPU laptop biasa.
* **COCO Dataset Pre-trained:** Mampu mengenali **80 kategori objek** dunia nyata (manusia, botol, tanaman, kursi, mobil, ransel, cangkir, dll.).

---

## 🚀 Cara Menjalankan

### 1. Mode Gambar Statis
Memproses gambar sampel dan menghasilkan deteksi dengan bounding box berwarna:
```bash
python main.py
```
atau dari root direktori proyek:
```bash
python 04_object_detection_yolov8/main.py
```

### 2. Mode Live Webcam (Interaktif)
Mendeteksi objek di sekitar meja belajar/kamar Zaki secara langsung:
```bash
python -c "from main import run_webcam_detection; run_webcam_detection()"
```
*(Tekan tombol **q** pada jendela kamera untuk keluar)*

---

## 🔬 Konsep Teknis yang Dipelajari
1. **Normalisasi Piksel:** Mengubah nilai integer `0 - 255` menjadi float `0.0 - 1.0`.
2. **Tensor NCHW:** Mentransposisi bentuk gambar dari `(Tinggi, Lebar, Channel)` ke `(Batch, Channel, Tinggi, Lebar)` sesuai standar Deep Learning.
3. **Non-Maximum Suppression (NMS):** Algoritma eliminasi kotak pembatas ganda yang menindih objek yang sama berdasarkan skor IoU (*Intersection over Union*).
