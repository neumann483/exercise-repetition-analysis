"""
mediapipe_pose.py

Performs pose estimation using MediaPipe's pose module.

Functions:
- detect_mediapipe_pose(): loads and processes a video frame-by-frame and extracts
keypoints.
Returns list of frames and structured keypoints.

Note:
- Produces 33 keypoints per frame with x, y, z and visibility
(confidence).
- No drawing or saving inside this script - handled externally.
"""
import cv2
import time
import numpy as np
import mediapipe as mp


def detect_mediapipe_pose(video_path: str) -> tuple[list[np.ndarray], list[dict]]:
    # Return list of frames, list of keypoints per frame
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False,
                        model_complexity=1,
                        enable_segmentation=False)

    cap = cv2.VideoCapture(video_path)

    frames, keypoints_data = [], []
    frame_count = 0
    t0 = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result_image = pose.process(rgb_image)
        if result_image.pose_landmarks:
            landmarks = []
            for l in result_image.pose_landmarks.landmark:
                landmarks. append({
                    'x': l.x,
                    'y': l.y,
                    'z': l.z,
                    'confidence': l.visibility
                })
            keypoints_data.append({
                'frame_index': frame_count,
                'keypoints': landmarks
            })
        else:
            keypoints_data.append({
                'frame_index': frame_count,
                'keypoints': []
            })
        frames.append(frame)
        frame_count += 1

    cap.release()
    print(f"FPS: {frame_count / (time.time()-t0):.2f}")

    return frames, keypoints_data

