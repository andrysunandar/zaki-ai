# 🌍 KATALOG LENGKAP PROYEK AI LINGKUNGAN UNGGULAN
## Persiapan Kompetisi GENIUS Olympiad (St. John Fisher University, New York)

Katalog ini berisi kumpulan ide proyek riset **Artificial Intelligence (AI)** bertema **Lingkungan Hidup & Keberlanjutan** yang dirancang khusus untuk memiliki:
1. **Keunikan lokal Indonesia** (menjadi pembeda di panggung internasional).
2. **Relevansi ekologis global** (sesuai target *Sustainable Development Goals* / SDGs PBB).
3. **Kelayakan teknis** untuk dikerjakan oleh siswa SMP–SMA (Kelas 7–12).
4. **Faktor "WOW" di depan juri internasional di New York**.

---

## 📑 DAFTAR KATEGORI
- [Kategori A: Ekosistem Laut & Pesisir (Marine & Coastal)](#kategori-a-ekosistem-laut--pesisir)
- [Kategori B: Hutan Tropis, Lahan Gambut, & Satwa Liar (Forest & Wildlife)](#kategori-b-hutan-tropis-lahan-gambut--satwa-liar)
- [Kategori C: Sungai & Kualitas Air Bersih (Water & Rivers)](#kategori-c-sungai--kualitas-air-bersih)
- [Kategori D: Pengelolaan Sampah & Ekonomi Sirkular (Waste & Circular Economy)](#kategori-d-pengelolaan-sampah--ekonomi-sirkular)
- [Kategori E: Pertanian Berkelanjutan & Pangan (Sustainable Agriculture)](#kategori-e-pertanian-berkelanjutan--pangan)
- [Kategori F: Energi Terbarukan & Iklim Perkotaan (Clean Energy & Climate)](#kategori-f-energi-terbarukan--iklim-perkotaan)

---

## KATEGORI A: Ekosistem Laut & Pesisir

### 1. 🏆 MangroveGuard AI — Sentinel Kanopi & Deforestasi Mangrove
* **SDGs:** SDG 13 (Aksi Iklim) & SDG 14 (Ekosistem Laut)
* **Tingkat Kesulitan:** ⭐⭐⭐ (Menengah)
* **Masalah:** Indonesia memiliki 20%+ mangrove dunia yang menjadi penyerap karbon biru (*Blue Carbon*) terbesar bumi, namun terancam alih fungsi lahan ilegal dan serangan hama defoliasi.
* **Cara Kerja AI:** Menggunakan citra foto udara (drone/kamera) dengan model YOLOv8 / Segmentasi Citra untuk mengklasifikasi 3 kondisi kanopi: *Sehat Lebat*, *Stres/Meranggas (Terserang Hama)*, dan *Lahan Gundul (Penebangan Liar)*.
* **Nilai Jual di NY:** Sangat prestisius karena karbon biru adalah isu negosiasi iklim dunia paling hangat saat ini.

---

### 2. 🪸 Nusantara ReefWatch — Pemantau Pemutihan Karang & Hama COTS
* **SDGs:** SDG 14 (Ekosistem Laut)
* **Tingkat Kesulitan:** ⭐⭐⭐ (Menengah)
* **Masalah:** Terumbu karang di Segitiga Karang Dunia (Raja Ampat, Wakatobi) terancam gelombang panas laut (*bleaching*) dan ledakan populasi bintang laut berduri pemakan karang (*Crown-of-Thorns Starfish* / COTS).
* **Cara Kerja AI:** Model Computer Vision bawah air (*underwater object detection*) yang memproses rekaman kamera aksi (GoPro) untuk mendeteksi tingkat keparahan pemutihan karang dan menghitung kepadatan hama COTS secara otomatis.
* **Nilai Jual di NY:** Visual bawah air sangat memukau dan Indonesia adalah episentrum keanekaragaman hayati laut dunia.

---

### 3. 🔬 MicroDetect AI — Deteksi Mikroplastik Air Pesisir via Mikroskop Digital
* **SDGs:** SDG 14 (Ekosistem Laut) & SDG 6 (Air Bersih)
* **Tingkat Kesulitan:** ⭐⭐⭐⭐ (Menengah - Lanjut)
* **Masalah:** Mikroplastik (<5 mm) di perairan pesisir termakan ikan dan masuk ke rantai makanan manusia. Pengujian laboratorium biasanya mahal dan lama.
* **Cara Kerja AI:** Memasang lensa mikroskop portable murah pada kamera smartphone/webcam. AI dilatih mengenali serat (*fibers*), fragmen (*fragments*), dan pelet mikroplastik berdasarkan pola refraksi cahaya dan tepi objek.
* **Nilai Jual di NY:** Menawarkan solusi pengujian mikroplastik berbiaya murah untuk komunitas nelayan di negara berkembang.

---

### 4. 🐢 TurtleSafe AI — Deteksi & Perlindungan Sarang Penyu dari Predator
* **SDGs:** SDG 14 (Ekosistem Laut) & SDG 15 (Ekosistem Darat)
* **Tingkat Kesulitan:** ⭐⭐ (Mudah - Menengah)
* **Masalah:** Pantai peneluran penyu di Indonesia (Sukabumi, Bali, Kalimantan) sering diserang predator malam (anjing liar, biawak, kepiting) dan pencuri telur.
* **Cara Kerja AI:** Kamera malam inframerah bertenaga surya dengan model Edge AI mendeteksi keberadaan penyu bertelur serta membunyikan alarm/sinyal pengusir ketika ada predator mendekati sarang.
* **Nilai Jual di NY:** Proyek konservasi satwa karismatik yang sangat disukai juri internasional.

---

## KATEGORI B: Hutan Tropis, Lahan Gambut, & Satwa Liar

### 5. 🔥 PeatSense AI — Deteksi Dini Kebakaran Bawah Tanah Lahan Gambut (Smoldering)
* **SDGs:** SDG 13 (Aksi Iklim) & SDG 3 (Kesehatan yang Baik)
* **Tingkat Kesulitan:** ⭐⭐⭐ (Menengah)
* **Masalah:** Kebakaran gambut di Sumatera/Kalimantan membara di kedalaman 1 meter di bawah tanah (*smoldering*) tanpa api tampak, melepaskan kabut asap PM2.5 lintas negara.
* **Cara Kerja AI:** Menggabungkan data citra termal FLIR/inframerah dengan jaringan saraf tiruan (ANN) yang menganalisis penurunan drastis kelembaban tanah (*soil moisture*) untuk mendeteksi *hotspot* sebelum asap tebal keluar.
* **Nilai Jual di NY:** Isu otentik Indonesia yang menyumbang emisi gas rumah kaca global dan krisis kesehatan regional.

---

### 6. 🎧 BioAcoustics JungleGuard — Deteksi Suara Gergaji Mesin & Tembakan Liar
* **SDGs:** SDG 15 (Ekosistem Darat) & SDG 16 (Penegakan Hukum Lingkungan)
* **Tingkat Kesulitan:** ⭐⭐⭐ (Menengah)
* **Masalah:** Penjaga hutan Taman Nasional (Leuser, Lorentz) terbatas jumlah personilnya untuk memantau jutaan hektar hutan rimba dari pembalakan liar (*illegal logging*).
* **Cara Kerja AI:** Audio Spectrogram Classifier (CNN) yang dipasang pada mikrofon tenaga surya di atas pohon. Model mengenali suara khas gergaji mesin (*chainsaw*), tembakan senapan, dan mesin truk kayu, lalu mengirimkan SMS koordinat GPS kepada polisi hutan.
* **Nilai Jual di NY:** Proyek berbasis audio AI (*Bioacoustics*) sangat segar dan jarang dibuat dibanding proyek berbasis kamera biasa.

---

### 7. 🦧 WildTrack AI — Smart Camera Trap Satwa Kritis (Orangutan & Harimau Sumatera)
* **SDGs:** SDG 15 (Ekosistem Darat)
* **Tingkat Kesulitan:** ⭐⭐ (Mudah - Menengah)
* **Masalah:** *Camera trap* konvensional di hutan mengambil ribuan foto kosong (daun goyang) yang memboroskan baterai dan memakan waktu berbulan-bulan untuk disortir manual oleh peneliti.
* **Cara Kerja AI:** Kamera jebak pintar yang menggunakan Edge AI (YOLO nano) untuk langsung mengidentifikasi satwa langka (Orangutan, Badak Jawa, Harimau, Gajah) dan memfilter foto kosong secara otomatis.
* **Nilai Jual di NY:** Kolaborasi sains data dengan lembaga konservasi satwa dunia.

---

## KATEGORI C: Sungai & Kualitas Air Bersih

### 8. 🌊 RiverShield AI — Penghalang Otomatis & Pemilah Sampah Sungai Tropis
* **SDGs:** SDG 6 (Air Bersih) & SDG 14 (Ekosistem Laut)
* **Tingkat Kesulitan:** ⭐⭐⭐ (Menengah)
* **Masalah:** 80% plastik di laut berasal dari aliran sungai perkotaan seperti Sungai Citarum dan Kali Ciliwung.
* **Cara Kerja AI:** Kamera pemantau di jembatan mendeteksi kepadatan akumulasi sampah terapung (*plastic debris density*), memprediksi titik rawan penyumbatan pintu air, dan mengaktifkan lengan penangkap sampah mekanis otomatis.
* **Nilai Jual di NY:** Solusi langsung mencegah sampah daratan mencapai samudera pasifik.

---

### 9. 💧 AlgaeBloom Watch — Prediksi Ledakan Ganggang & Eutrofikasi Danau
* **SDGs:** SDG 6 (Air Bersih) & SDG 12 (Konsumsi Bertanggung Jawab)
* **Tingkat Kesulitan:** ⭐⭐ (Mudah - Menengah)
* **Masalah:** Limbah pupuk kimia dan pakan ikan di danau Indonesia (seperti Danau Toba, Rawa Pening) memicu ledakan populasi alga beracun (*blooming*) yang mematikan jutaan ikan.
* **Cara Kerja AI:** Analisis citra warna air danau (*water colorimetry*) + model regresi AI memprediksi konsentrasi klorofil-a dan kadar oksigen terlarut (*Dissolved Oxygen*) 48 jam sebelum kematian massal ikan terjadi.
* **Nilai Jual di NY:** Menjaga mata pencaharian petambak lokal dan ekosistem danau air tawar.

---

## KATEGORI D: Pengelolaan Sampah & Ekonomi Sirkular

### 10. ♻️ SmartSort Nusantara — Reverse Vending Machine (RVM) Pemilah Bank Sampah
* **SDGs:** SDG 12 (Konsumsi Bertanggung Jawab) & SDG 11 (Kota Berkelanjutan)
* **Tingkat Kesulitan:** ⭐⭐ (Mudah - Menengah)
* **Masalah:** Bank Sampah di pemukiman Indonesia kesulitan memilah kemasan sachet plastik multilayer dan gelas plastik karena harus diperiksa satu per satu secara manual.
* **Cara Kerja AI:** Kotak sampah pintar / konveyor mini dengan kamera webcam. Menggunakan YOLOv8 / MobileNet untuk membedakan botol PET bening, botol berwarna, kemasan sachet aluminium foil, dan kaleng minuman, lalu menjatuhkannya ke wadah pemilahan yang tepat. *(Didukung oleh Modul 4 dan 5 di repositori Zaki!)*
* **Nilai Jual di NY:** Proyek yang bisa didemokan secara langsung (*live demo prototype*) di meja pameran juri!

---

### 11. 🍎 FreshCheck AI — Deteksi Kelayakan Makanan & Pengurangan Food Waste Kantin
* **SDGs:** SDG 12 (Pengurangan Sampah Makanan) & SDG 2 (Tanpa Kelaparan)
* **Tingkat Kesulitan:** ⭐⭐ (Mudah)
* **Masalah:** Indonesia adalah salah satu penghasil sampah makanan (*food waste*) terbesar di dunia. Buah, sayuran, dan makanan siap saji sering dibuang karena salah estimasi masa simpan.
* **Cara Kerja AI:** Aplikasi kamera smartphone yang mendeteksi tingkat kematangan buah/sayur lokal (pisang, pepaya, cabai, tomat) dan bintik kebusukan mikro untuk menghitung sisa hari konsumsi optimal (*shelf-life estimator*).
* **Nilai Jual di NY:** Relevan dengan kehidupan sehari-hari siswa di sekolah.

---

### 12. 📱 E-Waste Lens — Pemilah Limbah Elektronik Ramah Lingkungan
* **SDGs:** SDG 12 (Pengelolaan Bahan Berbahaya & Beracun / B3)
* **Tingkat Kesulitan:** ⭐⭐⭐ (Menengah)
* **Masalah:** Baterai litium, kabel tembaga, dan PCB bekas dibuang sembarangan ke TPA bercampur sampah organik, menyebabkan logam berat mencemari air tanah.
* **Cara Kerja AI:** Computer Vision mendeteksi komponen limbah elektronik, memisahkan baterai berisiko meledak, serta memberikan petunjuk keselamatan pemilahan komponen bernilai daur ulang tinggi (*Urban Mining*).
* **Nilai Jual di NY:** Mendukung transisi sirkular ekonomi global.

---

## KATEGORI E: Pertanian Berkelanjutan & Ketahanan Pangan

### 13. 🌾 PaddyDoctor AI — Dokter Padi Cerdas untuk Petani Indonesia
* **SDGs:** SDG 2 (Ketahanan Pangan) & SDG 15 (Ekosistem Daratan)
* **Tingkat Kesulitan:** ⭐⭐ (Mudah - Menengah)
* **Masalah:** Petani padi sering gagal panen akibat penyakit Hawar Daun Bakteri (*Bacterial Leaf Blight*), Blas, atau hama Wereng Coklat, dan sering terlambat menyemprot pestisida.
* **Cara Kerja AI:** Klasifikasi citra daun padi dari kamera handphone (menggunakan arsitektur CNN / MobileNet) untuk mendiagnosis penyakit daun padi sejak gejala awal dan merekomendasikan takaran pestisida nabati alami.
* **Nilai Jual di NY:** Solusi langsung menjaga ketahanan pangan beras di negara agraris tropis.

---

### 14. 🌴 PalmEco AI — Optimalisasi Biomassa Limbah Kelapa Sawit (Janjang Kosong)
* **SDGs:** SDG 7 (Energi Bersih) & SDG 12 (Ekonomi Sirkular)
* **Tingkat Kesulitan:** ⭐⭐⭐ (Menengah)
* **Masalah:** Industri kelapa sawit menghasilkan jutaan ton Janjang Kosong Kelapa Sawit (JKKS) dan limbah cair POME yang mencemari lingkungan bila tidak diolah.
* **Cara Kerja AI:** Model AI memprediksi kualitas dekomposisi biomassa kelapa sawit menjadi biochar dan pupuk organik berdasarkan parameter kelembaban, rasio C/N, dan citra tekstur permukaan.
* **Nilai Jual di NY:** Mengubah limbah perkebunan kontroversial menjadi komoditas penyerap karbon (*Carbon Dioxide Removal / CDR*).

---

## KATEGORI F: Energi Terbarukan & Iklim Perkotaan

### 15. ☀️ SolarClean AI — Deteksi Debu & Penurunan Efisiensi Panel Surya
* **SDGs:** SDG 7 (Energi Bersih Terjangkau) & SDG 13 (Aksi Iklim)
* **Tingkat Kesulitan:** ⭐⭐ (Mudah - Menengah)
* **Masalah:** Di negara tropis berdebu dan berpolusi tinggi seperti Indonesia, lapisan debu (*soiling effect*) pada panel surya dapat menurunkan efisiensi pembangkit listrik hingga 25–40%.
* **Cara Kerja AI:** Kamera CCTV / drone memindai permukaan modul surya, lalu model segmentasi citra mendeteksi persentase tutupan debu/kotoran burung dan secara otomatis memicu semprotan air pembersih hanya pada panel yang kotor.
* **Nilai Jual di NY:** Langsung terhubung dengan efisiensi energi hijau dunia.

---

### 16. 🏙️ UrbanCool AI — Pemetaan Pulau Panas Perkotaan (Urban Heat Island)
* **SDGs:** SDG 11 (Kota Berkelanjutan) & SDG 13 (Aksi Iklim)
* **Tingkat Kesulitan:** ⭐⭐⭐ (Menengah)
* **Masalah:** Kota-kota besar di Indonesia (Jakarta, Surabaya, Medan) mengalami kenaikan suhu ekstrem akibat hilangnya ruang terbuka hijau dan masifnya aspal/beton (*Urban Heat Island*).
* **Cara Kerja AI:** Memadukan citra satelit termal Landsat/Sentinel dengan tutupan vegetasi (*NDVI*) untuk memprediksi koridor jalan mana yang paling membutuhkan penanaman pohon peneduh demi menurunkan suhu kota.
* **Nilai Jual di NY:** Isu adaptasi perubahan iklim di megapolitan Asia Tenggara.

---

## 📊 Matriks Perbandingan & Rekomendasi untuk Zaki

| No | Nama Proyek | Bidang | Kebutuhan Alat | Daya Saing di NY | Rekomendasi |
|:---:|---|---|---|:---:|:---:|
| **1** | **MangroveGuard AI** | Pesisir & Karbon | Foto Drone / Laptop | ⭐⭐⭐⭐⭐ (Sangat Tinggi) | 🥇 **Pilihan Terbaik #1** |
| **2** | **EcoSort Nusantara** | Sampah Sungai | Webcam / Mini PC | ⭐⭐⭐⭐⭐ (Sangat Tinggi) | 🥈 **Pilihan Terbaik #2 (Bisa Live Demo)** |
| **3** | **PeatSense AI** | Lahan Gambut | Sensor / Citra Termal | ⭐⭐⭐⭐⭐ (Sangat Tinggi) | 🥉 **Pilihan Riset Iklim** |
| **4** | **Nusantara ReefWatch** | Terumbu Karang | Kamera Aksi / Video | ⭐⭐⭐⭐⭐ (Sangat Tinggi) | 🌟 **Paling Menawan Visual** |
| **5** | **PaddyDoctor AI** | Pertanian Padi | Kamera HP / Dataset | ⭐⭐⭐⭐ (Tinggi) | 💡 **Paling Cepat Selesai** |
| **6** | **BioAcoustics Jungle**| Audio Hutan Tropis | Mikrofon / Laptop | ⭐⭐⭐⭐ (Tinggi) | 🎵 **Pendekatan Audio Unik** |

---

## 🎯 Tips Memilih untuk Zaki:
* **Jika ingin membuat prototipe fisik yang bisa didemokan langsung di depan juri Jakarta:**  
  👉 Pilih **`EcoSort Nusantara`** (karena kita sudah punya kode dasarnya di Modul 4 dan 5 di repositori ini, tinggal tambah kamera webcam!).
* **Jika ingin proyek yang paling prestisius secara sains internasional dan berbobot akademis tinggi:**  
  👉 Pilih **`MangroveGuard AI`** atau **`PeatSense AI`** (karena isu Karbon Biru dan Lahan Gambut Indonesia adalah magnet juara di ajang Amerika Serikat!).
