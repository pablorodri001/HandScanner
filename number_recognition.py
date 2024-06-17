import numpy as np 

def count_fingers(hand_landmarks):
    finger_tips=[4,8,12,16,20]
    count=0

    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    return count