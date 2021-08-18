import pyautogui as pt
from time import sleep
import pyperclip
import random


sleep(2)

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
    pt.moveRel(30,-145)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message Received: "+whatsapp_message)

    return whatsapp_message

#Post response

def post_message(message):
    global x,y

    position = pt.locateOnScreen("model1.png", confidence=.6)
    x=position[0]
    y=position[1]
    pt.moveTo(x + 200, y+20, duration=.5)
    pt.click()
    pt.typewrite("Hello this is AASUR, Aditya's personal bot. Aditya is busy RN and so I am replying to the message. If the message is really important please call him else Aditya will get back to you", interval = .01)
    pt.typewrite("\n", interval = .01)




post_message(get_message())


