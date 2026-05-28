import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
while True :
    success , frame = cap.read()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            for id, landmark in enumerate(hand_landmarks.landmark):

                h, w, c = frame.shape

                cx = int(landmark.x * w)
                cy = int(landmark.y * h)

                print(id, cx, cy)


            
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )


    cv2.imshow("Camera" , frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()