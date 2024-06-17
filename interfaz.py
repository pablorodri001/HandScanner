import cv2

def show_frame(frame):
    cv2.imshow('Reconocimiento de manos',frame)



def wait_key():
    return cv2.waitKey(1) & 0xFF