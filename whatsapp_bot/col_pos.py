import pyautogui as pt
from time import sleep

while True:
    posxy = pt.position()
    print(posxy, pt.pixel(posxy[0],posxy[1]))
    sleep(1)
    if posxy[0] == 0:
        break