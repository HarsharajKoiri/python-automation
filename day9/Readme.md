# Day 9 - HandDraw ✋ 

**HandDraw** is a simple Python program that lets you **draw in the air using your index finger**!  
It detects hand movement through your webcam and maps finger motion to a clean **white canvas** — like a virtual drawing board.

---

## Features

- Tracks hand and index finger in real-time
- Draws on a separate white canvas window
- Live webcam feed for reference
- Automatically resets drawing if hand is not visible
- Press **`q`** to quit anytime

---

## Requirements

- Python 3.x  
- OpenCV  
- MediaPipe  
- NumPy

Install with:

```bash
pip install opencv-python mediapipe numpy
```
## How to Use
```bash
python HandDraw.py
```
- Use your index finger to draw.
- A white canvas window opens for sketching.
- Press q to close both windows.

## Flowchart
```pgsql
Start
  |
  v
Initialize Libraries (OpenCV, MediaPipe, NumPy)
  |
  v
Open Webcam Feed
  |
  v
Detect Hand Using MediaPipe
  |
  v
Is Hand Detected? --------------------- No --------------------> Go back to "Detect Hand Using MediaPipe"
  |
  Yes
  v
Track Position of Index Finger
  |
  v
Map Finger Movement to Canvas (Drawing on White Canvas)
  |
  v
Is Hand Lost (for a certain time)? ------------- No ----------------> Continue Drawing on Canvas
  |
  Yes
  v
Clear Canvas (if hand is lost)
  |
  v
Press 'q' to Quit? ---------------------------- No ------------------> Continue Drawing on Canvas
  |
  Yes
  v
Exit Program
  |
  v
End
```
