import pyautogui
import time

script = open("beemovie.txt", "r")
time.sleep(10)
for typeword in script:
    pyautogui.typewrite(typeword)
    pyautogui.press("enter")

