import argparse
from detectors.yolo_pose import detect_yolo_pose
from detectors.mediapipe_pose import detect_mediapipe_pose
from utils.draw import draw_skeleton
from utils.save import save_keypoints_to_csv


def main():
    parser = argparse.ArgumentParser(description="Pose estimation and repetition counting")
    parser.add_argument('--model', type=str, choices=['yolo', 'mediapipe'], default='yolo', help='Model to use')
    parser.add_argument('--input', type=str, required=True, help='Path to input video')
    parser.add_argument('--output', type=str, default='data/outputs/output.mp4', help='Path to output video')
    parser.add_argument('--save_csv', action='store_true', help='Whether to save keypoints to CSV')
    args = parser.parse_args()

    # Choose between yolo and mediapipe and apply pose estimation
    if args.model == 'yolo':
        frames, keypoints = detect_yolo_pose(args.input)
    else:
        frames, keypoints = detect_mediapipe_pose(args.input)

    # Draw a skeleton on frames
    #processed_frames = draw_skeleton(frames, keypoints)

    # Save keypoints to a CSV file
    if args.save_csv:
        save_keypoints_to_csv(keypoints, 'data/outputs/keypoints.csv')

    # Save processed video


if __name__ == '__main__':
    main()
