import pyautogui
import keyboard
import time

scroll_amount = 300  # Amount per scroll (positive = up, negative = down)
scroll_total = 0

print("Press UP or DOWN arrow keys to scroll. Press ESC to stop.\n")

try:
    while True:
        if keyboard.is_pressed('down'):
            pyautogui.scroll(-scroll_amount)
            scroll_total -= scroll_amount
            print(f"Scrolled Down: Total = {scroll_total}")
            time.sleep(0.2)

        elif keyboard.is_pressed('up'):
            pyautogui.scroll(scroll_amount)
            scroll_total += scroll_amount
            print(f"Scrolled Up: Total = {scroll_total}")
            time.sleep(0.2)

        elif keyboard.is_pressed('esc'):
            print("\nStopped.")
            break

except KeyboardInterrupt:
    print("\nInterrupted.")

