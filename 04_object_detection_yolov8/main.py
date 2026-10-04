"""
=============================================================================
MODUL 4: OBJECT DETECTION DENGAN DEEP LEARNING (YOLOv8 & ONNX RUNTIME)
Dibuat untuk: Persiapan Lomba AI (GENIUS Olympiad / Competzy Indonesia)
Target Siswa: Zaki (SMP - SMA / Kelas 7 - 12)
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
import onnxruntime as ort

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Resolusi direktori models dan output fleksibel
if os.path.exists(os.path.join(BASE_DIR, "models")):
    MODELS_DIR = os.path.join(BASE_DIR, "models")
else:
    MODELS_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "models"))

OUTPUT_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "output"))
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

MODEL_PATH = os.path.join(MODELS_DIR, "yolov8n.onnx")
SAMPLE_IMAGE = os.path.join(MODELS_DIR, "sample_face.jpg")

COCO_CLASSES = [
    "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
    "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
    "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
    "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
    "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
    "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
    "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair",
    "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop", "mouse",
    "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
    "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
]

np.random.seed(42)
COLORS = np.random.randint(0, 255, size=(len(COCO_CLASSES), 3), dtype=np.uint8)

def ensure_yolo_model():
    """Mengunduh model YOLOv8 ONNX jika belum ada."""
    if not os.path.exists(MODEL_PATH):
        print(f"📥 Mengunduh bobot model YOLOv8 ONNX...")
        try:
            from huggingface_hub import hf_hub_download
            import shutil
            downloaded = hf_hub_download(repo_id="unity/inference-engine-yolo", filename="models/yolov8n.onnx")
            shutil.copy(downloaded, MODEL_PATH)
            print(f"   Model tersimpan di: {MODEL_PATH}")
        except Exception as e:
            print(f"   Peringatan: Gagal unduh otomatis ({e}). Pastikan file {MODEL_PATH} ada.")

class YOLOv8Detector:
    def __init__(self, model_path=MODEL_PATH, conf_thresh=0.35, nms_thresh=0.45):
        ensure_yolo_model()
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model {model_path} tidak ditemukan!")
        
        self.session = ort.InferenceSession(model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.conf_thresh = conf_thresh
        self.nms_thresh = nms_thresh
        self.input_size = (640, 640)

    def detect(self, image):
        orig_h, orig_w = image.shape[:2]

        resized = cv2.resize(image, self.input_size)
        rgb_img = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        normalized = (rgb_img.astype(np.float16) / 255.0)
        input_tensor = np.transpose(normalized, (2, 0, 1))[np.newaxis, ...]

        outputs = self.session.run(None, {self.input_name: input_tensor})[0]
        predictions = np.squeeze(outputs).T

        scores = predictions[:, 4:]
        class_ids = np.argmax(scores, axis=1)
        confidences = np.max(scores, axis=1)

        mask = confidences > self.conf_thresh
        filtered_boxes = predictions[mask, 0:4]
        filtered_confs = confidences[mask].astype(float).tolist()
        filtered_ids = class_ids[mask].tolist()

        boxes = []
        for box in filtered_boxes:
            cx, cy, bw, bh = box
            x = int((cx - bw / 2) * (orig_w / float(self.input_size[0])))
            y = int((cy - bh / 2) * (orig_h / float(self.input_size[1])))
            w = int(bw * (orig_w / float(self.input_size[0])))
            h = int(bh * (orig_h / float(self.input_size[1])))
            boxes.append([x, y, w, h])

        indices = cv2.dnn.NMSBoxes(boxes, filtered_confs, self.conf_thresh, self.nms_thresh)

        results = []
        if len(indices) > 0:
            for idx in indices:
                cid = filtered_ids[idx]
                cname = COCO_CLASSES[cid] if cid < len(COCO_CLASSES) else f"Class_{cid}"
                results.append({
                    "box": boxes[idx],
                    "confidence": filtered_confs[idx],
                    "class_id": cid,
                    "class_name": cname
                })
        return results

    def draw_detections(self, image, detections):
        annotated = image.copy()
        for det in detections:
            x, y, w, h = det["box"]
            conf = det["confidence"]
            cname = det["class_name"]
            cid = det["class_id"]

            color = [int(c) for c in COLORS[cid % len(COLORS)]]

            cv2.rectangle(annotated, (x, y), (x + w, y + h), color, 2)
            label = f"{cname}: {conf * 100:.1f}%"
            (tw, th), baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
            cv2.rectangle(annotated, (x, y - th - 6), (x + tw + 6, y), color, -1)
            cv2.putText(annotated, label, (x + 3, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        return annotated

def run_detection_on_image():
    print("\n🖼️ Menjalankan Deteksi Objek pada Gambar...")
    detector = YOLOv8Detector(MODEL_PATH)
    
    img = cv2.imread(SAMPLE_IMAGE)
    if img is None:
        print(f"File {SAMPLE_IMAGE} tidak ditemukan.")
        return

    start_time = time.time()
    detections = detector.detect(img)
    duration_ms = (time.time() - start_time) * 1000

    print(f"⚡ Waktu Pemrosesan AI: {duration_ms:.1f} milidetik")
    print(f"📦 Total Objek Ditemukan: {len(detections)}")
    for i, d in enumerate(detections, 1):
        x, y, w, h = d["box"]
        print(f"  [{i}] {d['class_name'].upper()} (Confidence: {d['confidence']*100:.1f}%) | Posisi: (X={x}, Y={y}, {w}x{h})")

    result_img = detector.draw_detections(img, detections)
    output_file = os.path.join(OUTPUT_DIR, "hasil_object_detection_yolov8.jpg")
    cv2.imwrite(output_file, result_img)
    print(f"💾 Hasil visual disimpan ke: {output_file}")

def run_webcam_detection():
    detector = YOLOv8Detector(MODEL_PATH)
    print("\n🎥 Mengaktifkan Webcam untuk Live Object Detection... Tekan 'q' untuk keluar.")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("⚠️ Webcam tidak terdeteksi atau tidak memiliki izin akses.")
        return

    prev_time = time.time()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        annotated = detector.draw_detections(frame, detections)

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        cv2.putText(annotated, f"ZAKI AI LAB | FPS: {int(fps)} | Objek: {len(detections)}", (20, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Zaki AI - Live YOLOv8 Object Detection (Tekan 'q' untuk keluar)", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    print("=" * 65)
    print("🎯 MODUL 4: OBJECT DETECTION DENGAN YOLOV8 & ONNX RUNTIME")
    print("=" * 65)
    run_detection_on_image()
    print("\n💡 TIPS UNTUK ZAKI:")
    print("Untuk mencoba deteksi benda-benda di sekitar meja belajarmu secara langsung:")
    print("Panggil fungsi `run_webcam_detection()` di script ini!")
    print("=" * 65)

if __name__ == "__main__":
    main()
