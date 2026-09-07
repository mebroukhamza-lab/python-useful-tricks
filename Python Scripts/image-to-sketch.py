# pip install opencv-python
import cv2
img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
sketch = cv2.divide(gray, cv2.bitwise_not(blur), scale=256.0)
cv2.imwrite("sketch.png", sketch)
print("Sketch created successfully")
