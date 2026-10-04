"""
=============================================================================
MODUL 5: STARTER PROTOTYPE PROYEK LOMBA GENIUS OLYMPIAD (JALUR INDONESIA)
Topik Proyek : "EcoSort Nusantara: Edge-AI Marine Debris & River Plastic Classifier"
Kategori     : Artificial Intelligence (AI) - Environmental Focus
Target Siswa : Zaki (SMP - SMA / Kelas 7 - 12)
=============================================================================

SYARAT MUTLAK GENIUS OLYMPIAD:
Semua proyek AI WAJIB bertema LINGKUNGAN HIDUP & KEBERLANJUTAN (Environmental).
Juri internasional di New York menilai:
1. Literature Review (Masalah nyata lingkungan di Indonesia & dunia)
2. Architecture & Algoritma (Bagaimana AI memproses data)
3. Quantitative Evaluation (Akurasi, Precision, Recall, F1-Score, Confusion Matrix)
4. Measurable Environmental Impact (Berapa kilogram plastik/emisi karbon yang dihemat)

Script ini menyediakan pipeline lengkap yang siap dijadikan dasar proposal & eksperimen!
=============================================================================
"""

import sys
import os
import time

# Memastikan terminal Windows mendukung karakter UTF-8
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
DATASET_DIR = os.path.join(BASE_DIR, "dataset_simulasi")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DATASET_DIR, exist_ok=True)

# 4 Kategori Sampah Khas Sungai & Pesisir Indonesia
KELAS_SAMPAH = [
    "Plastik PET (Botol Minuman)",
    "Plastik Sachet / Multilayer (Kemasan Snack/Kopi)",
    "Styrofoam / Polistirena",
    "Organik / Sampah Daun & Ranting"
]

def generate_synthetic_environmental_dataset(num_samples_per_class=25):
    """
    Membuat dataset citra sintetis untuk simulasi training dan testing AI,
    sehingga Zaki dapat langsung menguji pipeline sains tanpa harus menunggu data lapangan.
    """
    print(f"\n🌱 Menyiapkan Dataset Lingkungan ({num_samples_per_class * len(KELAS_SAMPAH)} total sampel)...")
    dataset = []

    for class_id, class_name in enumerate(KELAS_SAMPAH):
        for s in range(num_samples_per_class):
            img = np.zeros((100, 100, 3), dtype=np.uint8)
            # Karakteristik warna & tekstur sesuai jenis sampah
            if class_id == 0:  # PET: Dominan Transparan / Biru muda keperakan
                base_color = [180 + np.random.randint(-20, 20), 120 + np.random.randint(-15, 15), 50]
                noise = np.random.randint(0, 30, (100, 100, 3), dtype=np.uint8)
            elif class_id == 1: # Sachet: Warna-warni mengkilap / kontras tinggi
                base_color = [np.random.randint(20, 220), np.random.randint(20, 220), np.random.randint(180, 255)]
                noise = np.random.randint(0, 80, (100, 100, 3), dtype=np.uint8)
            elif class_id == 2: # Styrofoam: Putih terang dengan pori-pori halus
                base_color = [230 + np.random.randint(-10, 15), 230 + np.random.randint(-10, 15), 230 + np.random.randint(-10, 15)]
                noise = np.random.randint(0, 20, (100, 100, 3), dtype=np.uint8)
            else: # Organik: Coklat / Hijau tua tanah dan dedaunan
                base_color = [20 + np.random.randint(-10, 10), 80 + np.random.randint(-20, 20), 40 + np.random.randint(-15, 15)]
                noise = np.random.randint(0, 40, (100, 100, 3), dtype=np.uint8)

            img[:] = np.clip(base_color, 0, 255)
            img = cv2.add(img, noise)

            dataset.append({
                "image": img,
                "label_id": class_id,
                "label_name": class_name
            })
    print("✅ Dataset lingkungan siap digunakan!")
    return dataset


def extract_features(image):
    """
    Ekstraksi Fitur Citra (Feature Engineering):
    Menghitung statistik HSV (Hue, Saturation, Value) dan Kontras Grayscale.
    Ini adalah representasi matematika yang dipelajari algoritma AI.
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    mean_hsv = np.mean(hsv, axis=(0, 1)) # Rata-rata warna Hue, Saturasi, Brightness
    std_hsv = np.std(hsv, axis=(0, 1))   # Variasi warna
    std_gray = np.std(gray)               # Tingkat tekstur / kekasaran permukaan

    fitur = np.hstack([mean_hsv, std_hsv, std_gray])
    return fitur


class SimpleEnvironmentalClassifier:
    """
    Model AI Klasifikasi Cepat berbasis K-Nearest Neighbors (KNN)
    Cocok untuk Edge-Device (Raspberry Pi / Arduino Portenta / Mini PC)
    """
    def __init__(self, k=3):
        self.k = k
        self.x_train = []
        self.y_train = []

    def fit(self, x, y):
        self.x_train = np.array(x)
        self.y_train = np.array(y)

    def predict_one(self, x_sample):
        # Hitung jarak Euclidean ke seluruh sampel data latih
        distances = np.linalg.norm(self.x_train - x_sample, axis=1)
        # Ambil k tetangga terdekat
        k_indices = np.argsort(distances)[:self.k]
        k_labels = self.y_train[k_indices]
        # Voting mayoritas
        vals, counts = np.unique(k_labels, return_counts=True)
        return vals[np.argmax(counts)]

    def predict(self, x_list):
        return [self.predict_one(x) for x in x_list]


def evaluate_model(y_true, y_pred):
    """
    Menghitung Metrik Standar Penilaian Lomba Sains & AI:
    - Akurasi Total
    - Confusion Matrix (Matriks Kesalahan Prediksi)
    - Precision, Recall, F1-Score per Kategori
    """
    total = len(y_true)
    correct = sum([1 for t, p in zip(y_true, y_pred) if t == p])
    akurasi = (correct / total) * 100

    print("\n" + "=" * 65)
    print("📊 LAPORAN EVALUASI MODEL AI (UNTUK PAPER LOMBA)")
    print("=" * 65)
    print(f"Total Sampel Uji : {total}")
    print(f"Akurasi Keseluruhan: {akurasi:.2f}%\n")

    # Confusion Matrix
    n_classes = len(KELAS_SAMPAH)
    matrix = np.zeros((n_classes, n_classes), dtype=int)
    for t, p in zip(y_true, y_pred):
        matrix[t, p] += 1

    print("Confusion Matrix (Baris: Data Sebenarnya, Kolom: Prediksi AI):")
    print(f"{'':35} | " + " | ".join([f"K{i+1}" for i in range(n_classes)]))
    print("-" * 65)
    for i, row in enumerate(matrix):
        print(f"K{i+1}: {KELAS_SAMPAH[i][:30]:30} | " + " | ".join([f"{val:3d}" for val in row]))

    print("-" * 65)
    print("\nMetrik Per Kelas (Precision, Recall, F1-Score):")
    for i in range(n_classes):
        tp = matrix[i, i]
        fp = np.sum(matrix[:, i]) - tp
        fn = np.sum(matrix[i, :]) - tp

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

        print(f"• {KELAS_SAMPAH[i]}:")
        print(f"    Precision: {precision*100:.1f}% | Recall: {recall*100:.1f}% | F1-Score: {f1*100:.1f}%")


def calculate_environmental_impact(predictions):
    """
    Bagian Kunci Proposal GENIUS Olympiad:
    Menghitung Estimasi Dampak Lingkungan Terukur (Measurable Environmental Impact)!
    """
    print("\n" + "=" * 65)
    print("🌍 ESTIMASI DAMPAK LINGKUNGAN TERUKUR (SDGs IMPACT METRIC)")
    print("=" * 65)

    # Bobot rata-rata per item sampah (kg)
    berat_rata_rata = {
        0: 0.025, # Botol PET: 25 gram
        1: 0.005, # Kemasan Sachet: 5 gram
        2: 0.015, # Wadah Styrofoam: 15 gram
        3: 0.050  # Sampah Organik: 50 gram
    }

    # Faktor emisi karbon yang dicegah bila didaur ulang (kg CO2e per kg bahan)
    co2_saved_factor = {
        0: 1.5,  # PET recycle saves ~1.5 kg CO2e / kg
        1: 0.8,  # Sachet upcycling
        2: 2.1,  # Styrofoam recovery
        3: 0.5   # Kompos vs TPA metana
    }

    total_sampah_kg = 0
    total_co2_dicegah_kg = 0

    for pred in predictions:
        kg = berat_rata_rata[pred]
        total_sampah_kg += kg
        total_co2_dicegah_kg += kg * co2_saved_factor[pred]

    print(f"Dalam simulasi penyortiran {len(predictions)} item sampah:")
    print(f"  • Estimasi Volume Sampah Terselamatkan : {total_sampah_kg:.2f} Kilogram")
    print(f"  • Potensi Reduksi Emisi Gas Rumah Kaca : {total_co2_dicegah_kg:.2f} kg CO2e")
    print("  • Target SDGs Relevan                 : SDG 12 (Konsumsi Bertanggung Jawab),")
    print("                                          SDG 13 (Aksi Iklim), & SDG 14 (Ekosistem Laut)")
    print("=" * 65)


def main():
    print("=" * 65)
    print("🏆 PROYEK CONTOH: ECOSORT NUSANTARA (GENIUS OLYMPIAD TRACK)")
    print("=" * 65)

    # 1. Siapkan Dataset
    dataset = generate_synthetic_environmental_dataset(num_samples_per_class=30)
    
    # 2. Ekstraksi Fitur
    X = [extract_features(d["image"]) for d in dataset]
    y = [d["label_id"] for d in dataset]

    # 3. Bagi Data Latih (70%) dan Data Uji (30%)
    indices = np.arange(len(dataset))
    np.random.seed(42)
    np.random.shuffle(indices)

    split = int(0.7 * len(dataset))
    train_idx, test_idx = indices[:split], indices[split:]

    x_train = [X[i] for i in train_idx]
    y_train = [y[i] for i in train_idx]
    x_test = [X[i] for i in test_idx]
    y_test = [y[i] for i in test_idx]

    # 4. Latih Model AI
    print(f"\n⚙️ Melatih Model AI dengan {len(x_train)} sampel data latih...")
    start_time = time.time()
    classifier = SimpleEnvironmentalClassifier(k=3)
    classifier.fit(x_train, y_train)
    print(f"Training selesai dalam {(time.time() - start_time)*1000:.2f} ms!")

    # 5. Prediksi Data Uji
    y_pred = classifier.predict(x_test)

    # 6. Evaluasi Metrik Lomba
    evaluate_model(y_test, y_pred)

    # 7. Hitung Dampak Ekologis Nyata
    calculate_environmental_impact(y_pred)

    print("\n🎯 KESIMPULAN UNTUK ZAKI:")
    print("Pipeline kode ini membuktikan bahwa proyek Zaki memiliki fondasi ilmiah:")
    print("Data Input ➡️ Feature Extraction ➡️ AI Model ➡️ Precision/Recall ➡️ Environmental Impact!")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
