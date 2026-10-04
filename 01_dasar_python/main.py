"""
=============================================================================
MODUL 1: DASAR-DASAR PEMROGRAMAN PYTHON UNTUK AI
Dibuat untuk: Persiapan Lomba AI (GENIUS Olympiad / Competzy Indonesia)
Target Siswa: Zaki (SMP - SMA / Kelas 7 - 12)
=============================================================================

AI (Kecerdasan Buatan) dibangun di atas dasar logika pemrograman.
Python adalah bahasa #1 di dunia untuk AI karena mudah dipahami dan punya ribuan
library canggih (seperti OpenCV, NumPy, PyTorch, Scikit-Learn).

Mari kita pelajari 5 pondasi utama Python:
1. Variabel dan Tipe Data
2. Kondisional (If - Else)
3. Perulangan (Looping)
4. List & Dictionary (Struktur Data)
5. Fungsi (Functions) & Logika AI Sederhana
=============================================================================
"""

import sys

# Memastikan output Windows terminal mendukung karakter UTF-8
if sys.platform.startswith("win"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def print_separator(judul):
    print("\n" + "=" * 60)
    print(f"👉 {judul.upper()}")
    print("=" * 60)


def main():
    print("🚀 SELAMAT DATANG DI KELAS DASAR PYTHON UNTUK AI - ZAKI!")
    print(f"Python Version yang digunakan: {sys.version.split()[0]}")

    # -------------------------------------------------------------------------
    # 1. VARIABEL & TIPE DATA
    # -------------------------------------------------------------------------
    print_separator("1. Variabel & Tipe Data")
    
    nama_proyek = "MangroveGuard AI"     # String (Teks)
    tahun_lomba = 2026                   # Integer (Bilangan Bulat)
    akurasi_model = 94.75                # Float (Desimal)
    is_ready_for_final = True            # Boolean (True/False)

    print(f"Nama Proyek      : {nama_proyek} (Tipe: {type(nama_proyek).__name__})")
    print(f"Tahun Lomba      : {tahun_lomba} (Tipe: {type(tahun_lomba).__name__})")
    print(f"Akurasi Model    : {akurasi_model}% (Tipe: {type(akurasi_model).__name__})")
    print(f"Siap ke Final NY : {is_ready_for_final} (Tipe: {type(is_ready_for_final).__name__})")

    # -------------------------------------------------------------------------
    # 2. LOGIKA KONDISIONAL (IF - ELIF - ELSE)
    # -------------------------------------------------------------------------
    print_separator("2. Logika Keputusan (Kondisional)")
    
    # Studi Kasus Lingkungan: Deteksi Kualitas Indeks Udara (AQI / Air Quality Index)
    aqi_jakarta = 155
    print(f"Indeks Kualitas Udara (AQI): {aqi_jakarta}")
    
    if aqi_jakarta <= 50:
        status_udara = "Baik (Sehat)"
        rekomendasi = "Aman beraktivitas di luar ruangan tanpa masker."
    elif aqi_jakarta <= 100:
        status_udara = "Sedang"
        rekomendasi = "Kelompok sensitif sebaiknya mengurangi aktivitas fisik berat."
    elif aqi_jakarta <= 150:
        status_udara = "Tidak Sehat untuk Kelompok Sensitif"
        rekomendasi = "Gunakan masker medis jika beraktivitas lama di luar."
    else:
        status_udara = "TIDAK SEHAT (Bahaya Polusi Tinggi)"
        rekomendasi = "Peringatan AI: Wajib masker respirator (KN95/N95) dan nyalakan air purifier!"
        
    print(f"Status Menurut AI : {status_udara}")
    print(f"Rekomendasi Tindakan: {rekomendasi}")

    # -------------------------------------------------------------------------
    # 3. LIST & DICTIONARY (STRUKTUR DATA PENYIMPAN DATASET AI)
    # -------------------------------------------------------------------------
    print_separator("3. List & Dictionary (Dasar Dataset AI)")
    
    # List: Kumpulan label kelas sampah lingkungan
    label_sampah = ["Botol Plastik PET", "Kantong Kresek", "Daun Kering", "Kaleng Aluminium", "Kardus"]
    print(f"Daftar Kategori Sampah ({len(label_sampah)} kelas):")
    for index, nama in enumerate(label_sampah, start=1):
        print(f"  [{index}] {nama}")

    # Dictionary: Menyimpan metadata sampel data
    sampel_data = {
        "id_sampel": "SMPL-001",
        "kategori": "Botol Plastik PET",
        "tingkat_degradasi": "Rendah",
        "waktu_urai_tahun": 450,
        "dapat_didaur_ulang": True
    }
    print("\nDetail Sampel Lingkungan (Format Data Dictionary):")
    for key, value in sampel_data.items():
        print(f"  • {key.replace('_', ' ').capitalize()}: {value}")

    # -------------------------------------------------------------------------
    # 4. PERULANGAN & KALKULASI STATISTIK DASAR AI
    # -------------------------------------------------------------------------
    print_separator("4. Perulangan (Menghitung Metrik Evaluasi Model)")
    
    # Skor akurasi model dalam 5 kali uji coba (fold validation)
    skor_evaluasi = [0.91, 0.94, 0.89, 0.96, 0.93]
    print(f"Hasil 5 kali pengujian: {skor_evaluasi}")
    
    total_skor = 0
    for skor in skor_evaluasi:
        total_skor += skor
        
    rata_rata = total_skor / len(skor_evaluasi)
    print(f"Rata-rata Akurasi AI: {rata_rata * 100:.2f}%")
    print(f"Skor Tertinggi      : {max(skor_evaluasi) * 100:.2f}%")
    print(f"Skor Terendah       : {min(skor_evaluasi) * 100:.2f}%")

    # -------------------------------------------------------------------------
    # 5. FUNGSI & SIMULASI PREDIKSI AI (INFERENCE)
    # -------------------------------------------------------------------------
    print_separator("5. Fungsi: Simulasi Klasifikasi AI")
    
    def prediksi_jenis_ekosistem(suhu_air_c, ph_air, salinitas_ppt):
        """
        Fungsi sederhana yang meniru logika model rule-based/decision tree
        untuk menentukan kesehatan terumbu karang / mangrove Indonesia.
        """
        # Standar parameter terumbu karang tropis sehat
        # Suhu optimal: 26 - 30 C, pH: 8.1 - 8.4, Salinitas: 32 - 35 ppt
        skor_kesehatan = 0
        if 26 <= suhu_air_c <= 30:
            skor_kesehatan += 1
        if 8.0 <= ph_air <= 8.5:
            skor_kesehatan += 1
        if 30 <= salinitas_ppt <= 36:
            skor_kesehatan += 1
            
        if skor_kesehatan == 3:
            return "KONDISI PRIMA (Ekosistem Sangat Sehat)"
        elif skor_kesehatan == 2:
            return "WASPADA (Terdapat Tekanan Lingkungan / Indikasi Awal Bleaching)"
        else:
            return "BAHAYA KRITIS (Ekosistem Mengalami Kerusakan Berat!)"

    # Uji Coba Fungsi
    hasil_uji_1 = prediksi_jenis_ekosistem(28.5, 8.2, 34)
    hasil_uji_2 = prediksi_jenis_ekosistem(32.8, 7.4, 25)

    print("Hasil Uji Coba 1 (Raja Ampat Normal):")
    print(f"  -> Prediksi: {hasil_uji_1}")
    print("Hasil Uji Coba 2 (Wilayah Terdampak Polusi & Gelombang Panas Laut):")
    print(f"  -> Prediksi: {hasil_uji_2}")

    print("\n✅ SELESAI MODUL 1! Zaki sekarang sudah memahami dasar sintaks Python.")
    print("Lanjut ke Modul 2: Memahami bagaimana Komputer 'Melihat' Gambar (Computer Vision)!\n")

if __name__ == "__main__":
    main()
