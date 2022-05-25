import cv2
import mediapipe as mp

webcam =  cv2.VideoCapture(0)
face = mp.solutions.face_detection
faces = face.FaceDetection()
screen = mp.solutions.drawing_utils

while True:

    check, frame = webcam.read()
    if not check:
        break

    list = faces.process(frame)
    if list.detections:
        for fac in list.detections:
            screen.draw_detection(frame, fac)
            cv2.imshow("DETECTOR DE ROSTOS", frame)
            if cv2.waitKey(5) == 27:
                break
                webcam.release()
                cv2.destroyAllWindows()