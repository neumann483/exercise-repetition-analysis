# 🤖 Pose Estimation Comparison: MediaPipe vs YOLOv8

## 🎯 Goal

Compare two pose estimation frameworks — MediaPipe and YOLOv8 — on short workout videos to evaluate:
- FPS performance
- Keypoint precision
- Stability under movement
- Behavior when limbs are occluded or in edge cases

---

## 🧪 Test Setup

- 3 workout videos: 1 with squats, 2 with push-ups
- Good lighting, full-body visibility, no visual noise
- Same hardware and processing pipeline for both models
- Keypoints were saved to CSV for comparison, annotated videos were generated for visual inspection

---

## 🧩 Test Results

### 1️⃣ **Video 1: Squats**

| Metric         | MediaPipe           | YOLOv8                |
|----------------|---------------------|------------------------|
| FPS            | **24.04**           | 15.39                  |
| Jitter         | ❌ None             | ⚠️ Present when going down |
| Precision      | ✅ All keypoints correctly mapped | ✅ All keypoints correct |
| Notes          | Very stable pose tracking throughout | Acceptable, but shaky during motion |

---

### 2️⃣ **Video 2: Push-ups**

| Metric         | MediaPipe           | YOLOv8                |
|----------------|---------------------|------------------------|
| FPS            | **24.04**           | 16.50                  |
| Jitter         | ❌ None             | ⚠️ Noticeable |
| Precision      | ⚠️ Slight confusion with crossed feet | ❌ Loses arm when occluded |
| Notes          | Smooth tracking even with occlusions | Struggles with occlusions and precision |

---

### 3️⃣ **Video 3: Push-ups**

| Metric         | MediaPipe           | YOLOv8                |
|----------------|---------------------|------------------------|
| FPS            | **23.45**           | **21.38**              |
| Jitter         | ❌ None             | ⚠️ Mild jitter |
| Precision      | ⚠️ Slight arm misalignment when hidden | ⚠️ Slight inaccuracies, similar to Video 2 |
| Notes          | Still tracks well | Jitter is reduced but keypoints remain off |

---

## ✅ Summary

| Aspect                     | MediaPipe         | YOLOv8            |
|----------------------------|-------------------|-------------------|
| FPS                        | **Higher** (~24)  | Lower (~15–21)    |
| Stability                  | **Very stable**   | ⚠️ Jittery, esp. during motion |
| Keypoint Accuracy          | ✅ Reliable       | ⚠️ Slightly off    |
| Occlusion Handling         | ✅ Resilient      | ❌ Loses limbs     |
| Number of Keypoints        | 33                | 17                |
| File Size (CSV)            | ⚠️ Larger         | ✅ Smaller         |

---

## 🏁 Conclusion

MediaPipe outperforms YOLOv8 in all critical areas for exercise repetition analysis:
- Delivers higher FPS and smoother keypoint tracking
- Maintains body part tracking even during occlusions or fast motion
- Produces richer keypoint data (x, y, z + confidence)

YOLOv8 may still be useful as a lighter alternative or for quick setups, but for this MVP, **MediaPipe is clearly the better choice** for accurate and stable pose estimation.

---

📝 Prepared by: Anhelina Ochakovska  
📆 Date: 16.07.2025