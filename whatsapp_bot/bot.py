#these are the important packages

import pyautogui as pt
from time import sleep
import pyperclip
import random


sleep(3)#it is the time when the execution starts 


#this locates the smile button
position1 = pt.locateOnScreen("whatsapp_bot/smille.png", confidence = .6)
x = position1[0]
y = position1[1]




#for checking the messages or collecting/copying 
def get_message():
    global x , y
    position = pt.locateOnScreen("whatsapp_bot/smille.png", confidence = .6)#confidence is the estimation
    x = position[0]
    y = position[1]
    pt.moveTo(x,y,duration=.5)
    pt.moveTo(x + 110,y - 70,duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,20)

    #for copying the text or the message
    pt.click()
    whtap = pyperclip.paste()
    print("message is " + whtap)
    return whtap





#for sending the reply or the message 
def send_rply(message):
    global x,y
    position = pt.locateOnScreen("whatsapp_bot/smille.png", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 300,y -5,duration=.5)
    pt.click()
    pt.typewrite(message, interval=.05)
    pt.typewrite("\n",interval=.05)




#for sending a random message 
def rply(message):
    randomno = random.randrange(4)
    if "?" in str(message).lower():
        return "dont ask me anything so just go"
    else:
        if "!" in str(message).lower():
            return "dont get too excited"
        elif randomno == 1:
            return "very noicee"
        elif randomno == 2:
            return "excellent"
        elif randomno == 3:
            return "perfect"
        else:
            return "bad"




#for finding the new unread messages 

def new_msg():
    pt.moveTo(x+110,y-60,duration=.5)
    while True:
        try:
            position = pt.locateOnScreen("whatsapp_bot/green1.png", confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0 )
                pt.click()
                sleep(.5)
        except(Exception):
            print("no new messages")
        if pt.pixelMatchesColor(int(x+110),int(y-60),(32,44,51),tolerance=10):
            print("white")
            new_message = rply(get_message())
            send_rply(new_message)
        else:
            print("no new messages")
        sleep(5)


#calling the final function
new_msg()