# pip install opencv-python
import cv2
img = cv2.imread("qrcode.png")
detector = cv2.QRCodeDetector()
data, points, _ = detector.detectAndDecode(img)
print("QR code content:", data)
