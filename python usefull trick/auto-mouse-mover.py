# pip install pyautogui
import pyautogui
import time
while True:
    pyautogui.moveTo(500, 500, duration=1)
    pyautogui.moveTo(600, 600, duration=1)
    time.sleep(30)
