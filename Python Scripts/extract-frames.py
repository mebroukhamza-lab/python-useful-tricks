# pip install opencv-python
import cv2
video = cv2.VideoCapture("video.mp4")
count = 0
while True:
    success, frame = video.read()
    if not success:
        break
    cv2.imwrite(f"frame_{count}.jpg", frame)
    count += 1
print(f"{count} frames extracted successfully")
