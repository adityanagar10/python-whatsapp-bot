import pyautogui as pt
from time import sleep
import pyperclip
import random


sleep(6)

position1 = pt.locateOnScreen("model1.png", confidence=.6)
x=position1[0]
y=position1[1]

#Gets message

def get_message():
    global x,y

    position = pt.locateOnScreen("model1.png", confidence=.6)
    x=position[0]
    y=position[1]
    pt.moveTo(x,y, duration = .5)
    pt.moveTo(x + 50 , y-35, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(20,15)
    pt.click()


get_message()


