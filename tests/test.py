import time
import os
from utils.video import get_video_info, save_video
from detectors.mediapipe_pose import detect_mediapipe_pose
from detectors.yolo_pose import detect_yolo_pose
from utils.keypoint_utils import save_keypoints_to_csv
from utils.draw import draw_skeleton
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
INPUT_PATH = ROOT_DIR / "data" / "inputs" / "tricep_dips_18.mp4"
OUTPUT_PATH = ROOT_DIR / "data" / "outputs" / "18.mp4"
CSV_PATH = ROOT_DIR / "data" / "outputs" / "18.csv"

info = get_video_info(INPUT_PATH)
print(info)

start_time = time.time()

frames, keypoints = detect_yolo_pose(str(INPUT_PATH))
#frames, keypoints = detect_mediapipe_pose(str(INPUT_PATH))

annotated_frames = []
for frame, data in zip(frames, keypoints):
    frame_idx = data['frame_index']
    kps = data['keypoints']
    annotated = draw_skeleton(frame, kps, "yolo")   # "mediapipe" or "yolo"
    annotated_frames.append(annotated)

print(f"[INFO] Saving annotated video to: {OUTPUT_PATH}")
save_video(str(OUTPUT_PATH), annotated_frames, info["fps"])

save_keypoints_to_csv(keypoints, str(CSV_PATH))

end_time = time.time()
print(f"Processing time:{end_time-start_time:.2f} s")
print(f"Frames processed: {info['frame_count']}")
print(f"Video resolution: {info['width']} x {info['height']}")
