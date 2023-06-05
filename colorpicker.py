import pyautogui
import time
from pynput import mouse
import os
from PIL import Image
def on_click(x, y, button, pressed):
    if pressed:
        color = pyautogui.pixel(x, y)
        print(f"Clicked at ({x}, {y}) with color {color}")

        r, g, b = color
        img = Image.new('RGB', (300, 300), color=color)
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        filename = f"color {r} {g} {b}.jpg"
        img.save(os.path.join(desktop_path, filename), "JPEG", quality=90)

listener = mouse.Listener(on_click=on_click)

listener.start()


while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break
listener.stop()