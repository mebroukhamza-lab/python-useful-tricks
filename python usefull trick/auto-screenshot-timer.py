# pip install pyautogui
import pyautogui
import time
for i in range(5):
    pyautogui.screenshot(f"screenshot_{i}.png")
    print(f"Screenshot {i} taken")
    time.sleep(60)
print("All screenshots taken successfully")
