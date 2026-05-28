# Hand Gesture Controlled Hill Climb Racing

A real-time computer vision project that allows users to control Hill Climb Racing using hand gestures.

Built using Python, OpenCV, MediaPipe, and keyboard automation.

---

## Features

- Real-time webcam hand tracking
- Hand landmark detection using MediaPipe
- Gesture recognition using finger coordinates
- Accelerate and brake control using hand gestures
- Smooth gameplay using gesture stability logic
- Neutral state when no hand is detected

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- Keyboard Library

---

## How It Works

1. Webcam captures live video frames.
2. MediaPipe detects hand landmarks in real time.
3. Finger positions are analyzed using coordinate comparison logic.
4. Gestures are mapped to game controls:
   - Finger Up → Accelerate
   - Finger Down → Brake
   - No Hand → Neutral
5. Keyboard events are triggered to control gameplay.

---

## Gesture Recognition Logic

The project uses landmark coordinate comparison for gesture detection.

Example:
- Index fingertip → Landmark 8
- Index lower joint → Landmark 6

If:
```python
tip_y < joint_y
```

Then the finger is considered raised.

---

## Challenges Faced

- Stabilizing gesture detection
- Handling inconsistent hand detection
- Making game controls smoother
- Fixing compatibility issues with keyboard automation libraries

---

## Future Improvements

- Support for custom gestures
- GUI integration
- Multiple hand controls
- FPS optimization
- Deep learning based gesture classification

---

## Run the Project

Install dependencies:

```bash
pip install opencv-python mediapipe keyboard
```

Run:

```bash
python camera.py
```

---

## Demo

Control Hill Climb Racing in real time using hand gestures through webcam input.

---

## Project Motivation

This project was created to explore real-time computer vision through an interactive gaming application instead of a traditional CRUD-based project.

The main goal was to understand gesture recognition, webcam processing, and real-time automation systems using Python.

---

## Author

Bhumika Tiwari