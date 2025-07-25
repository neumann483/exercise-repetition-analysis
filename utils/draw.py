"""
Provides function to draw human pose skeletons on individual
video frames.

Supports:
- MediaPipe format (33 keypoits, including visibility/confidence)
- YOLOv8 format (117 keypoints, x/y only)

Main function:
- get_color(): retrieves color based on needed body side
- draw_skeleton(): applies lines between keypoints to visualize
the pose.
"""
import cv2
import mediapipe as mp

# YOLOv8 COCO keypoint skeleton (17 points)
YOLO_CONNECTIONS = [
    (5, 7), (7, 9), (6, 8), (8, 10),    # arms
    (11, 13), (13, 15), (12, 14), (14, 16),      # legs
    (5, 6), (11, 12), (5, 11), (6, 12)      # torso
]

# Define left, right and center keypoint indices for YOLO keypoints
YOLO_LEFT = {5, 7, 9, 11, 13, 15}
YOLO_RIGHT = {6, 8, 10, 12, 14, 16}
YOLO_CENTER = {0, 1, 2, 3, 4}

# MediaPipe has built-in connections
MP_DRAWING = mp.solutions.drawing_utils
MP_POSE_CONNECTIONS = mp.solutions.pose.POSE_CONNECTIONS

# Define left, right and center indices for MediaPipe keypoints
MP_LEFT = {11, 13, 15, 23, 25, 27, 29, 31}
MP_RIGHT = {12, 14, 16, 24, 26, 28, 30, 32}
MP_CENTER = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


def get_color(start, end, left_set, right_set):
    if start in left_set and end in left_set:
        color = (255, 0, 0)  # Blue
    elif start in right_set and end in right_set:
        color = (0, 0, 255)  # Red
    else:
        color = (0, 255, 0)  # Green
    return color


def draw_skeleton(frame, keypoints, model_type):
    if model_type == "mediapipe":
        # Convert normalized coords to pixel coords
        height, width, _ = frame.shape
        points = [(int(l['x'] * width), int(l['y'] * height)) for l in keypoints]
        for start_idx, end_idx in MP_POSE_CONNECTIONS:
            if start_idx < len(points) and end_idx < len(points):
                color = get_color(start_idx, end_idx, MP_LEFT, MP_RIGHT)
                cv2.line(frame, points[start_idx], points[end_idx], color, 2)
        for idx, (x, y) in enumerate(points):
            cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)

    elif model_type == "yolo":
        points = [(int(l['x']), int(l['y'])) for l in keypoints]
        for start_idx, end_idx in YOLO_CONNECTIONS:
            if start_idx < len(points) and end_idx < len(points):
                color = get_color(start_idx, end_idx, YOLO_LEFT, YOLO_RIGHT)
                cv2.line(frame, points[start_idx], points[end_idx], color, 2)
        for idx, (x, y) in enumerate(points):
            cv2.circle(frame, (x, y), 3, (255, 255, 0), -1)

    else:
        raise ValueError(f"Unsupported model_type: {model_type}")

    return frame
