# pip install opencv-python
import cv2
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
if ret:
    cv2.imwrite("webcam_photo.jpg", frame)
cam.release()
print("Photo captured successfully")
