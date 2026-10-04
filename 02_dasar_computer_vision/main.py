"""
=============================================================================
MODUL 2: BAGAIMANA AI "MELIHAT" GAMBAR (COMPUTER VISION DENGAN OPENCV & NUMPY)
Dibuat untuk: Persiapan Lomba AI (GENIUS Olympiad / Competzy Indonesia)
Target Siswa: Zaki (SMP - SMA / Kelas 7 - 12)
=============================================================================
"""

import sys
import os

# Memastikan output Windows terminal mendukung karakter UTF-8
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import cv2
import numpy as np

def main():
    print("=" * 65)
    print("👁️ MODUL 2: DASAR COMPUTER VISION UNTUK AI")
    print("=" * 65)

    # Direktori output utama di root proyek atau lokal
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "output"))
    os.makedirs(output_dir, exist_ok=True)

    # 1. MEMBUAT GAMBAR DARI ANGKA (NUMPY ARRAY)
    print("\n[Step 1] Membuat Gambar Digital Sintetis Ukuran 400x500 piksel...")
    tinggi, lebar = 400, 500
    citra = np.zeros((tinggi, lebar, 3), dtype=np.uint8)
    citra[:] = [40, 70, 30]  # Warna background hijau tua (B=40, G=70, R=30)

    # Simulasi objek lingkungan
    cv2.circle(citra, (150, 200), 80, (200, 150, 30), -1)  # Danau air bersih
    cv2.rectangle(citra, (300, 120), (450, 280), (50, 180, 50), -1) # Kotak sampah/sensor

    cv2.putText(citra, "ZAKI AI - ECO VISION LAB", (30, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
    cv2.putText(citra, "Danau (Air)", (100, 205), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.putText(citra, "Bank Sampah", (320, 205), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    path_asli = os.path.join(output_dir, "01_citra_asli.jpg")
    cv2.imwrite(path_asli, citra)
    print(f" -> Gambar asli tersimpan di: {path_asli}")

    # 2. KONVERSI KE GRAYSCALE
    print("\n[Step 2] Mengubah BGR (3 Channel Warna) menjadi Grayscale (1 Channel)...")
    citra_gray = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
    path_gray = os.path.join(output_dir, "02_citra_grayscale.jpg")
    cv2.imwrite(path_gray, citra_gray)
    print(f" -> Dimensi asli      : {citra.shape} (Tinggi, Lebar, B-G-R)")
    print(f" -> Dimensi grayscale : {citra_gray.shape} (Tinggi, Lebar saja)")
    print(f" -> Gambar grayscale tersimpan di: {path_gray}")

    # 3. GAUSSIAN BLUR
    print("\n[Step 3] Mereduksi Noise menggunakan Gaussian Blur...")
    citra_blurred = cv2.GaussianBlur(citra_gray, (5, 5), 0)
    path_blur = os.path.join(output_dir, "03_citra_blur.jpg")
    cv2.imwrite(path_blur, citra_blurred)
    print(f" -> Gambar blur tersimpan di: {path_blur}")

    # 4. EDGE DETECTION (CANNY)
    print("\n[Step 4] Deteksi Garis Tepi Objek dengan Algoritma Canny...")
    edges = cv2.Canny(citra_blurred, threshold1=50, threshold2=150)
    path_edges = os.path.join(output_dir, "04_citra_edges.jpg")
    cv2.imwrite(path_edges, edges)
    print(f" -> Gambar tepi (edges) tersimpan di: {path_edges}")

    # 5. MENEMUKAN KONTUR & BOUNDING BOX
    print("\n[Step 5] Menemukan Kontur Objek & Memasang Bounding Box...")
    kontur, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(f" -> Ditemukan {len(kontur)} objek terpisah!")

    citra_deteksi = citra.copy()
    for i, c in enumerate(kontur):
        x, y, w, h = cv2.boundingRect(c)
        luas_area = cv2.contourArea(c)

        cv2.rectangle(citra_deteksi, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(citra_deteksi, f"Objek #{i+1} (Area: {int(luas_area)})", 
                    (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 1)

    path_deteksi = os.path.join(output_dir, "05_hasil_deteksi_kontur.jpg")
    cv2.imwrite(path_deteksi, citra_deteksi)
    print(f" -> Hasil bounding box tersimpan di: {path_deteksi}")

    print("\n" + "=" * 65)
    print("✅ BERHASIL! Zaki telah menguasai pipeline computer vision.")
    print(f"Buka folder '{output_dir}' untuk melihat file hasil olah citra!")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    main()
