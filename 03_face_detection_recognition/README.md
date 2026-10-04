# 👤 Modul 3: Deep Learning Face Detection & Recognition

Modul ini mengimplementasikan dua arsitektur Deep Learning modern berbasis Neural Network yang terintegrasi di OpenCV 5: **YuNet** dan **SFace**.

---

## 🎯 Perbedaan Utama (Penting Dipahami!)
1. **Face Detection (YuNet):**
   * Menjawab pertanyaan: *"Di mana posisi wajah di dalam frame gambar?"*
   * Menghasilkan: **Bounding Box** (koordinat X, Y, Lebar, Tinggi) dan **5 Landmark Wajah** (mata kanan, mata kiri, hidung, sudut mulut kanan, sudut mulut kiri).
2. **Face Recognition (SFace):**
   * Menjawab pertanyaan: *"Wajah siapakah ini?"*
   * Menghasilkan: **Vektor Fitur (128-D Embedding)** dan menghitung skor kemiripan (*Cosine Similarity*) dengan database identitas yang terdaftar.

---

## 🚀 Cara Menjalankan

### 1. Mode Gambar Statis
Memproses gambar sampel dan menghasilkan file visualisasi di folder `output/`:
```bash
python main.py
```
atau dari root direktori proyek:
```bash
python 03_face_detection_recognition/main.py
```

### 2. Mode Live Webcam (Interaktif)
Mendeteksi wajah secara *real-time* menggunakan kamera laptop/PC:
```bash
python -c "from main import run_webcam_detection; run_webcam_detection()"
```
*(Tekan tombol **q** pada jendela kamera untuk keluar)*

---

## 🧠 Model yang Digunakan
* **YuNet** (`models/face_detection_yunet_2023mar.onnx`): Detektor wajah ultra-ringan (~232 KB) dengan kecepatan inferensi tinggi.
* **SFace** (`models/face_recognition_sface_2021dec.onnx`): Deep CNN untuk ekstraksi representasi identitas biometrik 128 dimensi.
