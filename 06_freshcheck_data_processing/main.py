"""
=============================================================================
MODUL 6: PIPELINE PENGOLAHAN DATASET FRESHCHECK AI (FOOD WASTE PREDICTOR)
Topik Proyek : "FreshCheck AI: Computer Vision & Kinetika Suhu untuk Prediksi 
                Remaining Shelf Life (RSL) Buah & Pengurangan Food Waste"
Target Siswa : Zaki (SMP - SMA / Kelas 7 - 12)
=============================================================================

Pipeline ini mendemonstrasikan proses pengolahan data ilmiah dari A sampai Z:
1. Pemuatan Citra (Data Ingestion) & Standarisasi Ukuran
2. Konversi Ruang Warna (BGR ke HSV & LAB)
3. Segmentasi Warna: Memisahkan Kulit Hijau, Kulit Kuning, & Bintik Coklat
4. Ekstraksi Fitur Fisika-Kimia: Brown Spot Area (BSA %) & Ripeness Index
5. Augmentasi Data (Simulasi Variasi Cahaya Pasar & Kantin Indonesia)
6. Fusi Multimodal: Menghitung Remaining Shelf Life (RSL) berbasis Suhu Tropis (Q10)
7. Mesin Keputusan Intervensi: Diskon Dinamis & Rekomendasi Olahan Pangan
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
OUTPUT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "output"))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. PEMBUATAN SAMPEL CITRA BUAH SINTETIS (UNTUK DEMO PIPELINE)
# -----------------------------------------------------------------------------
def create_synthetic_banana_stage(stage=3):
    """
    Membuat citra pisang sintetis pada berbagai tahapan kematangan:
    Stage 1: Mentah (Hijau dominan)
    Stage 2: Matang Sempurna (Kuning cerah, bintik 0%)
    Stage 3: Matang Lanjut / Berbintik (Kuning dengan bintik coklat ~15%)
    Stage 4: Hampir Busuk / Overripe (Coklat dominan ~55%)
    """
    img = np.full((320, 480, 3), 245, dtype=np.uint8) # Background putih bersih
    center = (240, 160)
    axes = (170, 55)

    if stage == 1: # Hijau
        color = (50, 160, 40)
        num_spots = 0
    elif stage == 2: # Kuning cerah
        color = (30, 215, 235) # BGR: Kuning
        num_spots = 2
    elif stage == 3: # Kuning berbintik coklat
        color = (30, 195, 220)
        num_spots = 35
    else: # Coklat kehitaman
        color = (30, 90, 120)
        num_spots = 120

    # Gambar bentuk pisang melengkung sederhana
    cv2.ellipse(img, center, axes, 15, 10, 190, color, -1)
    cv2.ellipse(img, (center[0], center[1] + 15), (axes[0]-10, axes[1]-15), 15, 10, 190, (245, 245, 245), -1)

    # Tambahkan bintik-bintik coklat kebusukan (senescence brown spots)
    np.random.seed(42 + stage)
    for _ in range(num_spots):
        sx = int(center[0] + np.random.randint(-120, 120))
        sy = int(center[1] + np.random.randint(-20, 40))
        r = np.random.randint(2, 6)
        cv2.circle(img, (sx, sy), r, (20, 40, 60), -1) # Coklat tua

    return img


# -----------------------------------------------------------------------------
# 2. SEGMENTASI WARNA & PERHITUNGAN BROWN SPOT AREA (BSA %)
# -----------------------------------------------------------------------------
def analyze_fruit_ripeness_and_spots(image_bgr):
    """
    Menganalisis kematangan dan tingkat kebusukan menggunakan ruang warna HSV.
    Menghitung metrik ilmiah: Brown Spot Area (BSA %).
    """
    hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

    # 1. Masking Seluruh Tubuh Buah (Menghilangkan latar belakang putih)
    # Background mendekati putih (Saturasi rendah, Value sangat tinggi)
    mask_fruit = cv2.inRange(hsv, np.array([0, 40, 40]), np.array([180, 255, 255]))
    total_fruit_pixels = cv2.countNonZero(mask_fruit)

    if total_fruit_pixels == 0:
        total_fruit_pixels = 1 # Hindari division by zero

    # 2. Masking Warna Hijau (Klorofil mentah)
    # Hue hijau berkisar di antara 35 - 85
    mask_green = cv2.inRange(hsv, np.array([35, 50, 40]), np.array([85, 255, 255]))
    mask_green = cv2.bitwise_and(mask_green, mask_green, mask=mask_fruit)
    green_pixels = cv2.countNonZero(mask_green)

    # 3. Masking Warna Kuning (Karotenoid matang)
    # Hue kuning berkisar di antara 20 - 35
    mask_yellow = cv2.inRange(hsv, np.array([18, 80, 80]), np.array([34, 255, 255]))
    mask_yellow = cv2.bitwise_and(mask_yellow, mask_yellow, mask=mask_fruit)
    yellow_pixels = cv2.countNonZero(mask_yellow)

    # 4. Masking Bintik Coklat / Jamur Antraknosa (Senescence Brown Spots)
    # Hue coklat berkisar 8 - 18 dengan Value (Brightness) lebih rendah
    mask_brown = cv2.inRange(hsv, np.array([5, 50, 20]), np.array([18, 255, 120]))
    mask_brown = cv2.bitwise_and(mask_brown, mask_brown, mask=mask_fruit)
    brown_pixels = cv2.countNonZero(mask_brown)

    # 5. Kalkulasi Persentase Fitur Ilmiah
    green_ratio = (green_pixels / total_fruit_pixels) * 100.0
    yellow_ratio = (yellow_pixels / total_fruit_pixels) * 100.0
    bsa_percentage = (brown_pixels / total_fruit_pixels) * 100.0

    return {
        "total_pixels": total_fruit_pixels,
        "green_ratio": green_ratio,
        "yellow_ratio": yellow_ratio,
        "bsa_percentage": bsa_percentage,
        "masks": {
            "fruit": mask_fruit,
            "green": mask_green,
            "yellow": mask_yellow,
            "brown": mask_brown
        }
    }


# -----------------------------------------------------------------------------
# 3. AUGMENTASI CITRA (DATA AUGMENTATION)
# -----------------------------------------------------------------------------
def augment_image_pipeline(image_bgr):
    """
    Melakukan augmentasi untuk melatih model agar kebal terhadap:
    - Variasi pencahayaan di warung/kantin (Brightness Shift)
    - Sudut pandang kamera handphone (Random Flip & Rotation)
    - Gambar buram/gerak tangan (Motion Blur)
    """
    augmented_list = []

    # A. Flip Horizontal
    flipped = cv2.flip(image_bgr, 1)
    augmented_list.append(("Flip Horizontal", flipped))

    # B. Brightness +30 (Simulasi cahaya siang terang)
    bright = cv2.convertScaleAbs(image_bgr, alpha=1.0, beta=30)
    augmented_list.append(("Brightness +30", bright))

    # C. Brightness -30 (Simulasi cahaya redup sore/malam)
    dark = cv2.convertScaleAbs(image_bgr, alpha=1.0, beta=-30)
    augmented_list.append(("Brightness -30", dark))

    # D. Gaussian Blur (Simulasi kamera sedikit goyang)
    blurred = cv2.GaussianBlur(image_bgr, (5, 5), 0)
    augmented_list.append(("Gaussian Blur", blurred))

    return augmented_list


# -----------------------------------------------------------------------------
# 4. FUSI MULTIMODAL: MODEL KINETIKA PREDIKSI REMAINING SHELF LIFE (RSL)
# -----------------------------------------------------------------------------
def predict_remaining_shelf_life(bsa_percentage, yellow_ratio, green_ratio, ambient_temp_c=30.0):
    """
    Memadukan fitur citra visual (BSA %) dengan Kinetika Degradasi Suhu Tropis (Q10 Spoilage Rate).
    Di iklim tropis Indonesia (~30°C), respirasi buah 2x lebih cepat dibanding suhu ruang AC (~20°C).
    """
    # Faktor percepatan degradasi suhu berbasis aturan Q10:
    # Laju kerusakan berlipat ganda setiap kenaikan 10 derajat Celcius
    q10_factor = 2.0 ** ((ambient_temp_c - 20.0) / 10.0)

    # Laju pertambahan bintik coklat rata-rata per hari pada suhu standar 20°C (~3.5% per hari)
    daily_base_decay_rate = 3.5
    daily_actual_decay_rate = daily_base_decay_rate * q10_factor

    # Batas maksimum BSA sebelum buah dinyatakan tidak layak konsumsi (sekitar 35% bintik)
    max_tolerable_bsa = 35.0

    if green_ratio > 30.0:
        # Masih mentah
        estimated_rsl_days = (7.0 - (yellow_ratio / 20.0)) / q10_factor
        fase_kematangan = "Fase 1: Mentah (Unripe / Green)"
    elif bsa_percentage < 2.0:
        # Kuning mulus
        estimated_rsl_days = (5.0 - (bsa_percentage)) / q10_factor
        fase_kematangan = "Fase 2: Matang Sempurna (Prime Ripe)"
    elif bsa_percentage < max_tolerable_bsa:
        # Berbintik coklat (sangat manis)
        sisa_kapasitas_bsa = max_tolerable_bsa - bsa_percentage
        estimated_rsl_days = sisa_kapasitas_bsa / daily_actual_decay_rate
        fase_kematangan = "Fase 3: Matang Lanjut / Berbintik (Senescent Ripe)"
    else:
        # Lewat matang / busuk
        estimated_rsl_days = 0.0
        fase_kematangan = "Fase 4: Terlalu Matang / Busuk (Decayed)"

    estimated_rsl_days = max(0.0, round(estimated_rsl_days, 1))

    # Mesin Rekomendasi Aksi Penyelamat Makanan (Food Waste Action Engine)
    if estimated_rsl_days >= 4.0:
        status_aksi = "🏷️ JUAL HARGA NORMAL"
        rekomendasi = "Kualitas prima untuk display rak utama kantin/supermarket."
    elif estimated_rsl_days >= 2.0:
        status_aksi = "🟡 DISKON DINAMIS 30% - 50%"
        rekomendasi = "Terapkan promo 'Flash Sale Buah Matang' hari ini agar segera terjual."
    elif estimated_rsl_days > 0.5:
        status_aksi = "🔴 INTERVENSI ZERO FOOD WASTE (OLAH SEGERA)"
        rekomendasi = "Alihkan ke dapur kantin: Olah menjadi Pisang Goreng, Smoothies, atau Banana Cake!"
    else:
        status_aksi = "♻️ KOMPOS ORGANIK"
        rekomendasi = "Tidak layak makan segar. Alihkan ke tong vermikompos untuk pupuk tanaman sekolah."

    return {
        "fase": fase_kematangan,
        "rsl_hari": estimated_rsl_days,
        "q10_factor": q10_factor,
        "status_aksi": status_aksi,
        "rekomendasi": rekomendasi
    }


# -----------------------------------------------------------------------------
# 5. EKSEKUSI PIPELINE & VISUALISASI
# -----------------------------------------------------------------------------
def main():
    print("=" * 70)
    print("🍎 FRESHCHECK AI: PIPELINE PENGOLAHAN DATASET & PREDIKSI SHELF LIFE")
    print("=" * 70)

    # 1. Buat Sampel Citra Pisang Fase 3 (Matang Berbintik Manis)
    print("\n[Step 1] Memuat Citra Sampel Buah Pisang (Fase 3: Berbintik)...")
    sample_img = create_synthetic_banana_stage(stage=3)
    path_asli = os.path.join(OUTPUT_DIR, "freshcheck_01_citra_asli.jpg")
    cv2.imwrite(path_asli, sample_img)
    print(f" -> Citra tersimpan di: {path_asli}")

    # 2. Analisis Fitur & Segmentasi Warna
    print("\n[Step 2] Menjalankan Segmentasi Warna HSV & Deteksi Bintik Coklat...")
    analysis = analyze_fruit_ripeness_and_spots(sample_img)
    print(f"  • Total Luas Piksel Buah : {analysis['total_pixels']} px")
    print(f"  • Rasio Kulit Kuning     : {analysis['yellow_ratio']:.2f}%")
    print(f"  • Rasio Kulit Hijau      : {analysis['green_ratio']:.2f}%")
    print(f"  • Brown Spot Area (BSA)  : {analysis['bsa_percentage']:.2f}% (Bintik Kebusukan Mikro)")

    # Simpan Visualisasi Masking
    mask_vis = np.hstack([
        cv2.cvtColor(analysis["masks"]["fruit"], cv2.COLOR_GRAY2BGR),
        cv2.cvtColor(analysis["masks"]["yellow"], cv2.COLOR_GRAY2BGR),
        cv2.cvtColor(analysis["masks"]["brown"], cv2.COLOR_GRAY2BGR)
    ])
    cv2.putText(mask_vis, "Fruit Mask", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(mask_vis, "Yellow Skin", (500, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.putText(mask_vis, "Brown Spots (BSA)", (980, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    path_mask = os.path.join(OUTPUT_DIR, "freshcheck_02_segmentasi_warna.jpg")
    cv2.imwrite(path_mask, mask_vis)
    print(f" -> Visualisasi segmentasi tersimpan di: {path_mask}")

    # 3. Augmentasi Citra
    print("\n[Step 3] Melakukan Augmentasi Citra (Simulasi Variasi Cahaya Pasar/Kantin)...")
    augmented_results = augment_image_pipeline(sample_img)
    for name, aug_img in augmented_results:
        print(f"  ✓ Berhasil membuat varian: {name}")

    aug_canvas = np.hstack([augmented_results[0][1], augmented_results[1][1]])
    path_aug = os.path.join(OUTPUT_DIR, "freshcheck_03_augmentasi.jpg")
    cv2.imwrite(path_aug, aug_canvas)
    print(f" -> Sampel augmentasi tersimpan di: {path_aug}")

    # 4. Fusi Multimodal: Prediksi RSL pada Suhu Tropis Indonesia
    print("\n" + "=" * 70)
    print("🌡️ FUSI MULTIMODAL: PREDIKSI SHELF LIFE PADA IKLIM INDONESIA (30°C)")
    print("=" * 70)
    suhu_ruang_indonesia = 30.0 # Derajat Celcius
    hasil_prediksi = predict_remaining_shelf_life(
        bsa_percentage=analysis["bsa_percentage"],
        yellow_ratio=analysis["yellow_ratio"],
        green_ratio=analysis["green_ratio"],
        ambient_temp_c=suhu_ruang_indonesia
    )

    print(f"Kondisi Lingkungan : Suhu Ruang {suhu_ruang_indonesia}°C (Faktor Laju Q10: {hasil_prediksi['q10_factor']:.2f}x Lebih Cepat)")
    print(f"Fase Kematangan    : {hasil_prediksi['fase']}")
    print(f"Estimasi Sisa Umur : 👉 {hasil_prediksi['rsl_hari']} HARI LAGI (Remaining Shelf Life)")
    print(f"Keputusan Sistem   : {hasil_prediksi['status_aksi']}")
    print(f"Rekomendasi Tindak : {hasil_prediksi['rekomendasi']}")

    # 5. Simulasi Perbandingan Jika Buah Disimpan di Kulkas (10°C)
    print("-" * 70)
    hasil_kulkas = predict_remaining_shelf_life(
        bsa_percentage=analysis["bsa_percentage"],
        yellow_ratio=analysis["yellow_ratio"],
        green_ratio=analysis["green_ratio"],
        ambient_temp_c=10.0
    )
    print(f"💡 SIMULASI PERBANDINGAN: Jika disimpan di Kulkas (10°C):")
    print(f"   Sisa umur melonjak menjadi: 👉 {hasil_kulkas['rsl_hari']} HARI (Tahan {hasil_kulkas['rsl_hari']/hasil_prediksi['rsl_hari']:.1f}x Lebih Lama!)")

    print("\n" + "=" * 70)
    print("✅ PIPELINE PENGOLAHAN DATA BERHASIL!")
    print("Data visual + Suhu ➡️ Ekstraksi BSA% ➡️ Prediksi RSL ➡️ Aksi Zero Food Waste!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
