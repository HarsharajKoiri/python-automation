import cv2
import numpy as np
import mediapipe as mp

# Initialize webcam
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# White canvas
canvas = np.ones((480, 640, 3), dtype=np.uint8) * 255
prev_x, prev_y = 0, 0

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Mirror the frame
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            # Get index fingertip position (landmark 8)
            lm = handLms.landmark[8]
            h, w, _ = frame.shape
            cx, cy = int(lm.x * 640), int(lm.y * 480)

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = cx, cy

            # Draw line on white canvas
            cv2.line(canvas, (prev_x, prev_y), (cx, cy), (0, 0, 255), 4)
            prev_x, prev_y = cx, cy

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
    else:
        prev_x, prev_y = 0, 0  # Reset when hand is not visible

    # Show both webcam and canvas
    cv2.imshow("Webcam Feed", frame)
    cv2.imshow("Draw Canvas", canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
