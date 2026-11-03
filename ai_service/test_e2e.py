import base64
import json
import os
import sys
import cv2

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from yolo_detector import process_cv_frame

def main():
    img_path = os.path.join(os.path.dirname(CURRENT_DIR), "assets", "leopard 5.jpg")
    img = cv2.imread(img_path)
    assert img is not None, "Failed to load test image"

    _, buf = cv2.imencode(".jpg", img)
    b64_str = base64.b64encode(buf).decode("utf-8")

    # Decode from base64
    import numpy as np
    raw_bytes = base64.b64decode(b64_str)
    frame = cv2.imdecode(np.frombuffer(raw_bytes, np.uint8), cv2.IMREAD_COLOR)

    detections, alert, fired = process_cv_frame(frame, notify_backend=False)

    print("=== Integration Test Successful ===")
    print("Detections count:", len(detections))
    print("Top Detection:", detections[0])
    print("Leopard Alert:", alert)
    print("Acoustic Alarm Fired:", fired)

if __name__ == "__main__":
    main()
