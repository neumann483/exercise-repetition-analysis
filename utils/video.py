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
