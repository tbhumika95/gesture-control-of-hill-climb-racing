import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

up_count = 0
down_count = 0

while True:

    success, frame = cap.read()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb_frame)

    finger_points = []

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            for id, landmark in enumerate(hand_landmarks.landmark):

                h, w, c = frame.shape

                cx = int(landmark.x * w)
                cy = int(landmark.y * h)

                finger_points.append((id, cx, cy))

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            if len(finger_points) >= 9:

                index_tip_y = finger_points[8][2]

                index_joint_y = finger_points[6][2]

                if index_tip_y < index_joint_y:

                    up_count += 1
                    down_count = 0

                else:

                    down_count += 1
                    up_count = 0

                if up_count > 5:

                    cv2.putText(
                        frame,
                        "ACCELERATE",
                        (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        3
                    )

                if down_count > 5:

                    cv2.putText(
                        frame,
                        "BRAKE",
                        (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        3
                    )

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()