import cv2
import mediapipe as mp

# YOLOv8 COCO keypoint skeleton (17 points)
YOLO_CONNECTIONS = [
    (5, 7), (7, 9), (6, 8), (8, 10),    # arms
    (11, 13), (13, 15), (12, 14), (14, 16),      # legs
    (5, 6), (11, 12), (5, 11), (6, 12)      # torso
]

# MediaPipe has built-in connections
MP_DRAWING = mp.solutions.drawing_utils
MP_POSE_CONNECTIONS = mp.solutions.pose.POSE_CONNECTIONS


def draw_skeleton(frame, keypoints, model_type):
    if model_type == "mediapipe":
        # Convert normalized coords to pixel coords
        height, width, _ = frame.shape
        points = [(int(l['x'] * width), int(l['y'] * height)) for l in keypoints]
        for connection in MP_POSE_CONNECTIONS:
            start_idx, end_idx = connection
            if start_idx < len(points) and end_idx < len(points):
                cv2.line(frame, points[start_idx], points[end_idx], (0, 255, 0), 2)
        for x, y in points:
            cv2.circle(frame, (x,y), 3, (0, 0, 255), -1)

    elif model_type == "yolo":
        points = [(int(l['x']), int(l['y'])) for l in keypoints]
        for connection in YOLO_CONNECTIONS:
            start_idx, end_idx = connection
            if start_idx < len(points) and end_idx < len(points):
                cv2.line(frame, points[start_idx], points[end_idx], (255, 0, 0), 2)
        for x, y in points:
            cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)

    else:
        raise ValueError(f"Unsupported model_type: {model_type}")

    return frame
