# Exercise Repetition Analysis — Pose Estimation

This project is a lightweight prototype for analyzing exercise performance using computer vision.  
It includes **pose detection**, **keypoint tracking**, and **visualization** for workout videos.

 The current focus is on comparing **MediaPipe** and **YOLOv8** for pose estimation tasks.

---

## Project Structure

```exercise-repetition-analysis/
├── main.py     # Entry point script (CLI)
├── models/
│ ├── mediapipe_pose.py     # Pose detection using MediaPipe
│ └── yolo_pose.py  # Pose detection using YOLOv8
├── utils/
│ ├── keypoint_utils.py     # Saving/loading keypoints
│ ├── draw.py     # Drawing skeletons on frames
│ └── video.py    # Saving annotated videos
├── compare_pose.md     # Report comparing the two models
├── inputs/     # Folder for input videos
├── outputs/    # Folder for output videos and CSVs
└── requirements.txt #  Dependencies
```


---

## Quickstart

1. **Clone the repo**

```bash
git clone git@github.com:yourusername/exercise-repetition-analysis.git
cd exercise-repetition-analysis
```

2. **Create a virtual environment and install dependencies**

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. **Run pose detection**

```bash
python main.py --model mediapipe --input data/inputs/squats.mp4 --output data/outputs/squats_annotated.mp4 --save_csv data/outputs/squats_keypoints.csv
```
Optional flags:

--model: mediapipe or yolo

--output: path to save annotated video

--save_csv: path to save keypoints as CSV


## Current Features
- Pose detection using MediaPipe and YOLOv8

- Keypoint extraction and saving to CSV

- Skeleton overlay drawing on video frames

- Saving output video with pose annotations

- CLI for running on different videos

- Model comparison report (compare_pose.md)


## Technologies
- Python 3.10+

- OpenCV

- Ultralytics YOLOv8

- MediaPipe

- NumPy, Matplotlib