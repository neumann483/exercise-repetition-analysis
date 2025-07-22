"""
yolo_pose.py

Performs pose estimation using YOLOv8-pose model (Ultralytics).

Functiions:
- detect_yolo_pose(): processes video input, extracts 17 keypoints
per frame (x, y only).

Note:
- Does not return z or confidence - dummy values are added,
can be altered if needed.
"""
from ultralytics import YOLO
import cv2
import numpy as np
import time


def detect_yolo_pose(video_path: str) -> tuple[list[np.ndarray], list[dict]]:
    model = YOLO("yolov8n-pose.pt")
    cap = cv2.VideoCapture(video_path)

    frames, keypoints_data = [], []
    frame_count = 0

    print("[INFO] Started yolo pose detection...")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame.copy())
        out = model(frame, verbose=False)[0]
        kps = out.keypoints.xy.cpu().numpy()    # shape: (N, 17, 2)

        if len(kps):
            keypoints = []
            for x, y in kps[0]:     # first detected person only
                keypoints.append({
                    "x": float(x),
                    "y": float(y),
                    "z": 0.0,
                    "confidence": 1.0
                })
        else:
            keypoints = []

        keypoints_data.append({
            "frame_index": frame_count,
            "keypoints": keypoints
        })

        frame_count += 1

    cap.release()
    print("[INFO] Finished yolo pose detection...")

    return frames, keypoints_data
