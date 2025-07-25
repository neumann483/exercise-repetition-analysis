"""
video.py

Handles saving a list of frames (with or without skeleton overlays)
into a video file at a specifies output path.

Main function:
- save_video(): takes a list of processed frames amd writes
them to .mp4 using OpenCV.
- get_video_info(): retrieves information from video:
 resolution, fps, amount of frames.
- resize_video_frame(): resizes video frame to a needed resolution.

Used after keypoint detection and skeleton drawing is complete.
"""
import cv2


def save_video(output_path: str, frames: list, fps: float):
    if not frames:
        raise ValueError("No frames to save.")

    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')    # or 'XVID' for .avi
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    for frame in frames:
        out.write(frame)

    out.release()
    print(f"[INFO] Saved video to {output_path}")


def get_video_info(input_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise ValueError("Cannot open video file")
    info = {
        "width": int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        "height": int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        "fps": cap.get(cv2.CAP_PROP_FPS),
        "frame_count": int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
        "duration_sec": round(cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS), 2)
    }
    cap.release()
    return info


def resize_video_frame(frame, max_dim=720):
    h, w = frame.shape[:2]
    if max(h, w) <= max_dim:
        return frame    # No need to resize

    scale = max_dim / max(h, w)
    new_w = int(w * scale)
    new_h = int(h * scale)
    return cv2.resize(frame, (new_w, new_h), interpolation=cv2.INTER_AREA)
