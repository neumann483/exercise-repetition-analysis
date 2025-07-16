"""
video.py

Handles saving a list of frames (with or without skeleton overlays)
into a video file at a specifies output path.

Main function:
- save_video(): takes a list of processed frames amd writes
them to .mp4 using OpenCV.

Used after keyppint detection and skeleton drawing is complete.
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
