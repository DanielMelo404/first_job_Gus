import pyautogui
import time

print("Move your mouse to the region corners. Press Ctrl+C to stop.")
# 347 156
try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse position: ({x}, {y})", end='\r')
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nDone.")
