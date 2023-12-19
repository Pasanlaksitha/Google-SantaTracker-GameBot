from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api
import win32con

down_path = 'd.png'
up_path = 'u.png'
left_path = 'l.png'
right_path = 'r.png'

down_region = (0,0,71,62)
left_region = (0,0,68,52)
right_region = (0,0,62,60)
up_region = (0,0,66,63)

search_region = (107,621, 512, 135)
tmp = (0, 0, 1920, 1080)
confidence_level = 0.8

def perform_keypress(action:str) -> None:
    action = action.lower().strip()
    if action in ['up', 'down', 'left', 'right']:
        keyboard.press_and_release(action)
    # if action == 'up':
    #     keyboard.press_and_release('up')
    # elif action == 'down':
    #     keyboard.press_and_release('down')
    # elif action == 'left':
    #     keyboard.press_and_release('left')
    # elif action == 'right':
    #     keyboard.press_and_release('right')

def find_image_on_screen(region, grayscale=False, confidence=0.8):
    try:
        up = pyautogui.locateOnScreen(up_path, region=region, grayscale=grayscale, confidence=confidence)
        down = pyautogui.locateOnScreen(down_path, region=region, grayscale=grayscale, confidence=confidence)
        left = pyautogui.locateOnScreen(left_path, region=region, grayscale=grayscale, confidence=confidence)
        right = pyautogui.locateOnScreen(right_path, region=region, grayscale=grayscale, confidence=confidence)

        if up is not None:
            print("Up arrow detected.")
            perform_keypress('up')
        elif down is not None:
            print("Down arrow detected.")
            perform_keypress('down')
        elif left is not None:
            print("Left arrow detected.")
            perform_keypress('left')
        elif right is not None:
            print("Right arrow detected.")
            perform_keypress('right')
        else:
            print("No arrow detected.")
        
    except pyautogui.ImageNotFoundException:
        print("Error: Image not found.")
        
while keyboard.is_pressed('q') == False:    
    find_image_on_screen(region=search_region, confidence=confidence_level)
    
