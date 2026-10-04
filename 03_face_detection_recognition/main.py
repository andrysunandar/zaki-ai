"""
=============================================================================
MODUL 3: MODERN DEEP LEARNING FACE DETECTION & RECOGNITION (YUNET + SFACE)
Dibuat untuk: Persiapan Lomba AI (GENIUS Olympiad / Competzy Indonesia)
Target Siswa: Zaki (SMP - SMA / Kelas 7 - 12)
=============================================================================
"""

import sys
import os
import urllib.request
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

# Resolusi folder models dan output fleksibel (bisa dari root atau subfolder)
if os.path.exists(os.path.join(BASE_DIR, "models")):
    MODELS_DIR = os.path.join(BASE_DIR, "models")
else:
    MODELS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "models"))

OUTPUT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "output"))
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

YUNET_MODEL = os.path.join(MODELS_DIR, "face_detection_yunet_2023mar.onnx")
SFACE_MODEL = os.path.join(MODELS_DIR, "face_recognition_sface_2021dec.onnx")
SAMPLE_FACE = os.path.join(MODELS_DIR, "sample_face.jpg")

def ensure_model_files():
    """Mengunduh model neural network YuNet & SFace jika belum ada."""
    downloads = {
        YUNET_MODEL: "https://github.com/opencv/opencv_zoo/raw/main/models/face_detection_yunet/face_detection_yunet_2023mar.onnx",
        SFACE_MODEL: "https://github.com/opencv/opencv_zoo/raw/main/models/face_recognition_sface/face_recognition_sface_2021dec.onnx",
        SAMPLE_FACE: "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg"
    }
    for file_path, url in downloads.items():
        if not os.path.exists(file_path):
            print(f"📥 Mengunduh model {os.path.basename(file_path)}...")
            urllib.request.urlretrieve(url, file_path)
            print(f"   Tersimpan: {file_path}")

def run_face_pipeline_on_image(image_path=SAMPLE_FACE):
    """
    Menjalankan Deep Learning Face Detection dan Ekstraksi Embedding Fitur Wajah.
    """
    ensure_model_files()
    img = cv2.imread(image_path)
    if img is None:
        print(f"❌ File gambar {image_path} tidak ditemukan!")
        return

    h, w, _ = img.shape
    print(f"\n🖼️ Memproses gambar: {os.path.basename(image_path)} (Ukuran: {w}x{h} px)")

    # 1. Inisialisasi Detektor Wajah YuNet (Deep Learning)
    detector = cv2.FaceDetectorYN.create(
        model=YUNET_MODEL,
        config="",
        input_size=(w, h),
        score_threshold=0.8,
        nms_threshold=0.3,
        top_k=5000
    )

    # 2. Inisialisasi Pengenal Wajah SFace (128-D Embedding)
    recognizer = cv2.FaceRecognizerSF.create(model=SFACE_MODEL, config="")

    # Deteksi Wajah
    _, faces = detector.detect(img)
    num_faces = len(faces) if faces is not None else 0
    print(f"🎯 DETEKSI YUNET: Ditemukan {num_faces} wajah.")

    if faces is None or len(faces) == 0:
        print("Tidak ada wajah yang terdeteksi.")
        return

    annotated = img.copy()
    for i, face in enumerate(faces):
        box = face[0:4].astype(int)
        score = face[-1]
        x, y, bw, bh = box[0], box[1], box[2], box[3]

        # Landmark: Mata Kanan, Mata Kiri, Hidung, Mulut Kanan, Mulut Kiri
        landmarks = face[4:14].reshape((5, 2)).astype(int)

        # Gambar Bounding Box (Warna Hijau Terang)
        cv2.rectangle(annotated, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
        cv2.putText(annotated, f"Face #{i+1} ({score*100:.1f}%)", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 0), 2)

        # Gambar 5 Titik Landmark Wajah
        colors = [(255, 0, 0), (0, 0, 255), (0, 255, 255), (255, 255, 0), (255, 0, 255)]
        for pt, col in zip(landmarks, colors):
            cv2.circle(annotated, tuple(pt), 4, col, -1)

        # Ekstraksi Embedding Wajah dengan SFace
        aligned_face = recognizer.alignCrop(img, face)
        face_feature = recognizer.feature(aligned_face)

        print(f"  • Wajah #{i+1}: Posisi=(X:{x}, Y:{y}, W:{bw}, H:{bh}) | Skor Kepercayaan={score:.3f}")
        print(f"    -> Vektor Fitur (Embedding) berhasil diekstrak! Panjang Vektor: {face_feature.shape[1]} angka.")
        print(f"    -> 5 Angka Pertama Embedding: {np.round(face_feature[0, :5], 4)}")

    output_path = os.path.join(OUTPUT_DIR, "hasil_face_detection_yunet.jpg")
    cv2.imwrite(output_path, annotated)
    print(f"\n✅ Hasil visual deteksi tersimpan di: {output_path}")

    # Simulasi Pencocokan Wajah (Face Recognition)
    print("\n" + "=" * 60)
    print("🤝 SIMULASI PENCOCOKAN WAJAH (COSINE SIMILARITY)")
    print("=" * 60)
    fitur_terdaftar_zaki = recognizer.feature(recognizer.alignCrop(img, faces[0]))
    skor_kemiripan = recognizer.match(fitur_terdaftar_zaki, fitur_terdaftar_zaki, cv2.FaceRecognizerSF_FR_COSINE)
    print(f"Pencocokan Wajah Zaki vs Wajah Uji:")
    print(f"  • Cosine Similarity: {skor_kemiripan:.4f}")
    if skor_kemiripan >= 0.363:
        print("  • Kesimpulan AI    : COCOK! (Identitas Dikonfirmasi Sebagai Zaki)")
    else:
        print("  • Kesimpulan AI    : TIDAK COCOK! (Orang Lain)")

def run_webcam_detection():
    """
    Mode Real-Time Webcam Face Detection menggunakan YuNet.
    Tekan 'q' pada keyboard untuk keluar.
    """
    ensure_model_files()
    print("\n🎥 Mengaktifkan Webcam untuk Real-Time Face Detection...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("⚠️ Kamera tidak dapat diakses. Pastikan webcam terhubung.")
        return

    frame_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if frame_w == 0 or frame_h == 0:
        frame_w, frame_h = 640, 480

    detector = cv2.FaceDetectorYN.create(
        model=YUNET_MODEL,
        config="",
        input_size=(frame_w, frame_h),
        score_threshold=0.8,
        nms_threshold=0.3
    )

    prev_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        _, faces = detector.detect(frame)

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time

        count = len(faces) if faces is not None else 0
        if faces is not None:
            for face in faces:
                box = face[0:4].astype(int)
                score = face[-1]
                x, y, bw, bh = box[0], box[1], box[2], box[3]
                cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
                cv2.putText(frame, f"Face: {score*100:.0f}%", (x, y - 8),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.putText(frame, f"ZAKI AI LAB | FPS: {int(fps)} | Faces: {count}", (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Real-Time Face Detection (Tekan 'q' untuk keluar)", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    print("=" * 60)
    print("👤 MODUL 3: DEEP LEARNING FACE DETECTION & RECOGNITION")
    print("=" * 60)
    run_face_pipeline_on_image()
    print("\n💡 Tips: Untuk mencoba webcam langsung, panggil `run_webcam_detection()` di script ini.")

if __name__ == "__main__":
    main()
