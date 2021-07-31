from pynput import mouse, keyboard
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
import time,threading,sys

# These variables can be changed by any user
LEFT_CLICK_MODE_KEY = 'r'
RIGHT_LATENCY = 0.03
LEFT_LATENCY = 0.05

mouseContr = MouseController()

rightClickMode = False
leftClickMode = False

def clickbtn(btn,latency):
    mouseContr.click(btn)
    time.sleep(latency)

def on_click(x,y,button,pressed):
    global rightClickMode
    if button == button.middle:
        rightClickMode = pressed

def on_press(key): # On key press
    global leftClickMode
    try:
        if key.char.lower() == LEFT_CLICK_MODE_KEY: leftClickMode = True
    except: pass

def on_release(key): # On key release
    global leftClickMode
    try:
        if key.char.lower() == LEFT_CLICK_MODE_KEY: leftClickMode = False
    except: pass

keyBoardListner = keyboard.Listener(on_press=on_press,on_release=on_release)
mouseListner = mouse.Listener(on_click=on_click)

keyBoardListner.start()
mouseListner.start()

while True:
    if leftClickMode:
        clickbtn(Button.left,LEFT_LATENCY)
    elif rightClickMode:
        clickbtn(Button.right,RIGHT_LATENCY)

