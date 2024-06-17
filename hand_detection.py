import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def detect_hands(frame):
    frame_rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    result=hands.process(frame_rgb)
    return result


def draw_hands(frame,result):
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame ,hand_landmarks, mp_hands.HAND_CONNECTIONS)
