# 🌿 4 IDE PROYEK RISET AI KHAS INDONESIA
## Rekomendasi Unggulan untuk GENIUS Olympiad (St. John Fisher University, New York)

Semua proyek di bawah ini dirancang khusus untuk memenuhi kriteria mutlak dewan juri **GENIUS Olympiad**:
1. **Fokus Lingkungan & Keberlanjutan (SDGs)**
2. **Keunikan Lokal Indonesia dengan Signifikansi Global**
3. **Metodologi Ilmiah Terukur (Bukan sekadar membungkus API pihak ketiga)**
4. **Kelayakan Realisasi untuk Siswa SMP/SMA (Kelas 7–12)**

---

### 🏆 Pilihan 1 (Rekomendasi Utama): MangroveGuard AI
> **"Autonomous Aerial Computer Vision Sentinel for Mangrove Canopy Health & Deforestation Monitoring"**

* **Latar Belakang Ekologis:**
  Indonesia adalah rumah bagi **lebih dari 3,3 juta hektar mangrove** (~20-23% total luas mangrove di muka bumi). Hutan mangrove Indonesia merupakan penyerap karbon biru (*Blue Carbon Sink*) paling efektif di dunia (mampu menyerap karbon 4–5 kali lebih tinggi dibandingkan hutan hujan terestrial). Ancaman terbesarnya adalah pembalakan liar, konversi tambak ilegal, dan serangan hama penggerek batang pada bibit baru.
* **Solusi Berbasis AI:**
  Sistem Computer Vision berbasis YOLOv8 / Semantic Segmentation yang dilatih untuk mendeteksi 3 status kanopi hutan pesisir dari foto udara drone:
  1. *Healthy Mangrove Canopy* (Kanopi lebat hijau pekat)
  2. *Defoliated / Stressed Canopy* (Kanopi meranggas/terserang hama atau salinitas ekstrem)
  3. *Cleared Land / Illegal Logging* (Lahan gundul yang baru ditebang)
* **Kebutuhan Teknis:** Kamera drone / foto udara publik, model YOLOv8/Segmentasi, laptop untuk training.
* **Target SDGs:** SDG 13 (Climate Action), SDG 14 (Life Below Water), SDG 15 (Life on Land).

---

### 🔥 Pilihan 2: PeatSense AI
> **"Multimodal AI for Subsurface Smoldering Fire Early-Warning in Indonesian Tropical Peatlands"**

* **Latar Belakang Ekologis:**
  Lahan gambut tropis di Riau, Jambi, Kalimantan Tengah, dan Papua menyimpan cadangan karbon raksasa. Ketika musim kemarau ekstrem tiba, gambut mengalami fenomena *smoldering* (pembakaran membara lambat tanpa nyala api di kedalaman 0.5–2 meter di bawah tanah). Ketika asap muncul di permukaan, api bawah tanah sudah menyebar puluhan hektar dan sangat sulit dipadamkan.
* **Solusi Berbasis AI:**
  Sistem prediksi awal multimodal:
  1. Data citra termal inframerah jarak dekat / drone untuk mendeteksi anomali suhu tanah di atas 45°C.
  2. Jaringan saraf tiruan (ANN/Random Forest) yang menggabungkan sensor kelembaban tanah (*soil moisture*), kelembaban udara, dan gas VOC.
* **Nilai Jual di New York:** Isu kebakaran hutan gambut Indonesia adalah topik pembicaraan iklim global di COP PBB. Juri internasional sangat mengapresiasi inovasi deteksi *smoldering* bawah tanah.
* **Target SDGs:** SDG 13 (Climate Action), SDG 3 (Good Health and Well-being).

---

### 🪸 Pilihan 3: Nusantara ReefWatch AI
> **"Edge-AI Underwater Detection of Coral Bleaching and Crown-of-Thorns Outbreaks in the Coral Triangle"**

* **Latar Belakang Ekologis:**
  Perairan Indonesia (Raja Ampat, Wakatobi, Bunaken) terletak tepat di jantung *Coral Triangle* dengan keanekaragaman karang tertinggi di dunia. Pemanasan suhu permukaan laut memicu *coral bleaching* massal, diperparah oleh ledakan populasi bintang laut berduri pemakan karang (*Acanthaster planci* / Crown-of-Thorns Starfish - COTS).
* **Solusi Berbasis AI:**
  Model *Edge-AI* yang diintegrasikan dengan rekaman kamera bawah air (GoPro/ROV):
  1. Klasifikasi otomatis status pemutihan karang (*Healthy*, *Paling*, *Bleached*, *Dead Covered with Algae*).
  2. Object Detection untuk menandai lokasi hama *Crown-of-Thorns* agar tim penyelam konservasi lokal dapat melakukan penanganan terarah.
* **Nilai Jual di New York:** Visual bawah laut sangat memikat juri. Solusi ini memberikan data presisi untuk program rehabilitasi karang.
* **Target SDGs:** SDG 14 (Life Below Water).

---

### ♻️ Pilihan 4: EcoSort Nusantara
> **"Low-Cost Edge-AI Automated Sorter for River Plastic Debris and Multilayer Sachets at Local Waste Banks"**

* **Latar Belakang Ekologis:**
  Sungai Citarum, Ciliwung, dan sungai perkotaan lainnya di Indonesia membawa ribuan ton sampah plastik ke laut Jawa setiap tahun. Tantangan terbesar Bank Sampah lokal adalah memilah sampah kemasan sachet (multilayer plastic) yang nilainya rendah dan membutuhkan tenaga manual yang sangat banyak.
* **Solusi Berbasis AI:**
  Konveyor sortir cerdas berbasis Edge AI:
  1. Kamera webcam mendeteksi jenis sampah yang lewat: Botol PET, Tutup Botol HDPE, Kemasan Sachet Multilayer, Styrofoam, dan Sampah Organik.
  2. Model AI mengklasifikasikan bahan secara *real-time* dan memberikan sinyal mekanis pemilah.
* **Nilai Jual di New York:** Proyek yang sangat membumi, dapat dibuat prototipe fisiknya oleh siswa SMP/SMA dengan biaya murah, dan dampaknya terukur dalam satuan kilogram plastik per hari.
* **Target SDGs:** SDG 12 (Responsible Consumption and Production), SDG 14 (Life Below Water).
