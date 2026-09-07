# pip install pyperclip
import pyperclip
import time
last = ""
print("Watching clipboard... Ctrl+C to stop")
while True:
    current = pyperclip.paste()
    if current != last:
        print("Clipboard changed:", current)
        last = current
    time.sleep(1)
