import pyautogui
import time

script = open("beemovie.txt", "r")
#É um bot simples que escreve onde quer que esteja
time.sleep(10)
for typeword in script:
    pyautogui.typewrite(typeword)
    pyautogui.press("enter")

