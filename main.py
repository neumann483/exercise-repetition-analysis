"""
main.py

Entry point for running the exercise repetition pipeline.

This script handles argument parsing, model selection
(YOLO or Mediapipe), keypoint extraction,
optional skeleton drawing and result saving.

Run this script from the terminal using CLI flags.
"""
import argparse
import time
from detectors.yolo_pose import detect_yolo_pose
from detectors.mediapipe_pose import detect_mediapipe_pose
from utils.draw import draw_skeleton
from utils.video import save_video, get_video_info
from utils.keypoint_utils import save_keypoints_to_csv


def main():
    parser = argparse.ArgumentParser(description="Pose estimation and repetition counting")
    parser.add_argument('--model', type=str, choices=['yolo', 'mediapipe'], default='yolo', help='Model to use')
    parser.add_argument('--input', type=str, required=True, help='Path to input video')
    parser.add_argument('--output', type=str, help='Optional path to save annotated video')
    parser.add_argument('--save_csv', type=str, default='data/outputs/keypoints.csv', help='Path to save a keypoints CSV file')
    args = parser.parse_args()

    start_time = time.time()

    # Get the info of input video
    input_video_info = get_video_info(args.input)
    print(f"Input video info:\n{input_video_info}")

    # Choose between yolo and mediapipe and apply pose estimation
    if args.model == 'yolo':
        frames, keypoints = detect_yolo_pose(args.input)
    else:
        frames, keypoints = detect_mediapipe_pose(args.input)

    # Draw a skeleton on frames and save processed video
    if args.output:
        print("[INFO] Drawing skeletons and saving annotated video...")
        annotated_frames = []
        for frame, data in zip(frames, keypoints):
            frame_idx = data['frame_index']
            kps = data['keypoints']
            annotated = draw_skeleton(frame, kps, args.model)   # "mediapipe" or "yolo"
            annotated_frames.append(annotated)

        print(f"[INFO] Saving annotated video to: {args.output}")
        save_video(args.output, annotated_frames, 30)

    # Save keypoints to a CSV file
    if args.save_csv:
        save_keypoints_to_csv(keypoints, args.save_csv)

    end_time = time.time()

    print(f"Processing time: {end_time-start_time:.2f}s")


if __name__ == '__main__':
    main()
