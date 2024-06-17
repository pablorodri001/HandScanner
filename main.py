import cv2
from camera import open_camera , read_frame
from hand_detection import detect_hands, draw_hands
from number_recognition import count_fingers
from interfaz import show_frame,wait_key

def main():
    cap=open_camera()
    if cap is None:
        return
    
    while True:
        frame = read_frame(cap)
        if frame is None:
            break

        result = detect_hands(frame)
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                fingers_count = count_fingers(hand_landmarks)
                cv2.putText(frame, f'Dedos: {fingers_count}' ,(10,30) , cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2, cv2.LINE_AA)
                draw_hands(frame,result)
        
        show_frame(frame)
        if wait_key() == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()