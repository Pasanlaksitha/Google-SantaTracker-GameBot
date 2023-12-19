#c1 177, 555 
#c2 296, 555
#c3 413, 555
#c4 530, 555

#grey rgb(51,51,51)
#black rgb(0,0,0)
#color change1 rgb(4,227,173)
#color change2 rgba(42,160,222)

from pyautogui import *
import pyautogui
import keyboard

def location_check():
    pyautogui.displayMousePosition()

def keypress():
    keyboard.press_and_release('up')
    keyboard.press_and_release('down')
    keyboard.press_and_release('left')
    keyboard.press_and_release('right')

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(217, 534)[0] == 51:
        keyboard.press_and_release('left')
        print("left")
    if pyautogui.pixel(328, 534)[0] == 51:
        print("up")
        keyboard.press_and_release('up')
    if pyautogui.pixel(439, 534)[0] == 51:
        print("down")
        keyboard.press_and_release('down')
    if pyautogui.pixel(550, 549)[0] == 51:
        print("right")
        keyboard.press_and_release('right')

#location_check()    