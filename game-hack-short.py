import keyboard
while not keyboard.is_pressed('q'):
    for i in ['left','up','down','right']:
        keyboard.press_and_release(i)
#https://santatracker.google.com/intl/en/wrapbattle.html