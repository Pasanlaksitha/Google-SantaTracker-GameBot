# Google Santa Tracker Bot Documentation
👇 Game you need to beat Highscore <br>
https://santatracker.google.com/intl/en/wrapbattle.html
## Introduction
This documentation provides information on how to use and understand the Google Santa Tracker Bot. The bot is designed to play the Google Santa Tracker game by automatically navigating through the game's interface using pixel colour detection and simulated keyboard inputs.

## Dependencies

* Python 3.x
* PyAutoGUI library
* Keyboard Library

Install the required dependencies using the following commands:

```
pip install pyautogui
pip install keyboard
```

## Getting started

### 1. Clone the Repository

Clone the Google Santa Tracker Bot repository to your local machine:

```
git clone https://github.com/your-username/google-santa-tracker-bot.git
cd google-santa-tracker-bot
```

### 2. Adjust Screen Coordinates

Open the `santa_tracker_bot.py` file in a text editor and update the screen coordinates to match your screen configuration. Modify the values of `c1`, `c2`, `c3`, and `c4` based on the cells or circles in the Google Santa Tracker game on your screen.

### 3. Run the Bot

```
python color-identify.py
```

### 4.  Quit the Bot
Press the `q` key on your keyboard to stop the bot.


## Understanding the Code

### Screen Coordinates

The screen coordinates (`c1`, `c2`, `c3`, `c4`) represent the positions of the cells or circles in the Google Santa Tracker game. These values need to be adjusted to match the layout on your screen.

### Color Codes

* Grey: RGB(51, 51, 51)
* Black: RGB(0, 0, 0)

### Pixel Color Detection 

The line `pyautogui.pixel(217, 534)[0] == 51` in the code is responsible for detecting the colour of a specific pixel on the screen. This is achieved using the pyautogui.pixel() function, which returns the RGB color values of the pixel at the specified coordinates.

217 and 534 are the X and Y coordinates, respectively, of the pixel being checked.
`[0]` indicates that we are retrieving the red component of the RGB colour values, other arguments in this function are `[1] `and `[2]` which are Green and Blue respectively.
The expression `== 51` checks if the red component of the pixel colour is equal to 51. 



The bot uses pixel colour detection to identify the game's current state based on the colour of specific pixels.

### Main Loop

The main loop continuously checks the pixel colour at predefined locations. Depending on the colour detected, the bot sends corresponding keyboard inputs to navigate the Santa Tracker game.

## Customization
Feel free to customize the bot according to your preferences or specific game variations. You can modify the pixel colours, screen coordinates, and keypress actions as needed.

## Troubleshooting
If the bot is not working as expected, consider the following:

* Ensure that the screen coordinates are correctly set for your display.
* Check for any updates or changes in the Google Santa Tracker game that may affect pixel colour detection.

## Note 

### BUG
When I was testing this game, I noticed that there was a problem with the game
that is, when a key circle closes to the pressing zone the game doesn't concern if a wrong arrow key is pushed. If we push with the correct key, that means once we press all 4 keys at once each time a circle passes, we score a point. 

___so i coded a shorter program for this if you need you can configure it to initiate when color code is detected like `color-identify.py` below one is  only a concept its works without coordination___

```python
import keyboard
while not keyboard.is_pressed('q'):
    for i in ['left','up','down','right']:
        keyboard.press_and_release(i)

```
