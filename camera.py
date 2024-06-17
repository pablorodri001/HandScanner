import cv2

def open_camera():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error no se pudo abrir la camara")
        return None
    return cap

def read_frame(cap):
    ret,frame = cap.read()
    if not ret:
        print("Error no se pudo leer el ret")
        return None
    return frame