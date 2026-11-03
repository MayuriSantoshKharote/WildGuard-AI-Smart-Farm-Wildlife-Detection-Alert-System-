# WildGuard AI - External YOLOv8 Inference Module

This directory contains the Python microservice for integrating real-time YOLOv8 / YOLO11 and OpenCV deep learning inference with the **WildGuard AI** central engine.

## Features Added
- **Non-blocking Audio Alarm (`audio_alarm.py`)**: Uses Pygame Mixer with background threading so inference loops never lag or freeze.
- **Leopard Alert Class Verification**: Checks detected YOLO class names and COCO proxy mapping (`leopard`, `cat`, `dog`, `bird` -> `leopard`). If confidence $> 0.50$, sounds an acoustic siren alarm.
- **5-Second Cooldown**: Prevents audio alarm spamming with strict 5-second cooldown tracking and on-screen cooldown timer.
- **Tactical Visual Highlights**: High-contrast tactical corner bounding boxes, confidence badges, and prominent `'ALERT: LEOPARD DETECTED'` emergency HUD frame banner.
- **Synthetic Siren Wave Generator**: Automatically generates emergency siren waveform if no custom audio file is provided.

## Quick Start
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run edge inference on webcam (default)
python yolo_detector.py

# 3. Or test on a specific image/video file
python yolo_detector.py --source "../assets/leopard 1.jpg"

# 4. Run automated test suite
python test_alert_system.py
```

The detections are automatically ingested into the Node.js backend (`/api/ai/external-detection`), evaluated by the mathematical threat engine, and broadcast to the dashboard via WebSocket.
