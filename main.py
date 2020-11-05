import pyautogui
from tkinter import *
from time import sleep
import keyboard as key
import webbrowser as wb
import tkinter.font as font
import datetime
import random
import requests
import os
import System
import Screen

now = datetime.datetime.now()
minute = now.minute
hour = now.hour - 12 if now.hour >= 12 else now.hour

url = "https://www.edulive.edu-smart.info/isc/login.php"
url2 = "edulive.edu-smart.info/isc/login.php"
data = requests.request("GET", url)
curr_url = data.url

global ID
global DOF

def start():
    if Connect["state"] == "normal":
        Connect["state"] = "disabled"
    Connect["text"] = "Connected"
    label1.destroy()
    label2.destroy()
    root.geometry("500x300")
    text.set("Server Connected!")
    wb.open(url)
    sleep(7)
    if curr_url is not url or curr_url is not url2:
        pyautogui.moveTo(1184, 184, 0.4)
        pyautogui.click()
        sleep(3)
        pyautogui.moveTo(1194, 132, 0.4)
        pyautogui.click()

    sleep(5)
    pyautogui.moveTo(764, 319, 0.2)
    pyautogui.click()
    pyautogui.write(ID)
    pyautogui.moveTo(800, 400, 0.01)
    pyautogui.click()
    pyautogui.moveTo(722, 396)
    pyautogui.click()
    pyautogui.write(DOF)
    pyautogui.moveTo(807, 453)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    sleep(6)
    pyautogui.hotkey("space")
    pyautogui.hotkey("space")
    pyautogui.hotkey("up")
    pyautogui.hotkey("up")
    pyautogui.hotkey("up")

    getTime()
    
def stop():
    if Stop["state"] == "normal":
        Stop["state"] = "disabled"
        Connect["state"] == "enabled"
    text.set("Server failed!")
    
def getTime():
    hour=8
    minute=35
    if hour == 8 and minute >= 30 or hour == 9 and minute <= 5:
        pyautogui.moveTo(980, 248, 0.5)
        pyautogui.click()
        sleep(4)
        pyautogui.moveTo(643, 479, 0.2)
        pyautogui.click()
        text.set("Activation Finished!!!")

    if hour == 9 and minute >= 10 or hour == 9 and minute <= 46:
        pyautogui.moveTo(852, 328, 0.5)
        pyautogui.click()
        sleep(4)
        pyautogui.moveTo(643, 479, 0.2)
        pyautogui.click()
        text.set("Activation Finished!!!")


    if hour == 2 and minute >= 40 or hour == 3 and minute <= 15:
        pyautogui.moveTo(890, 446, 0.5)
        pyautogui.click()
        sleep(4)
        pyautogui.moveTo(643, 479, 0.2)
        pyautogui.click()
        text.set("Activation Finished!!!")

    if hour == 3 and minute >= 10 or hour == 3 and minute <= 55:
        pyautogui.moveTo(969, 531, 0.5)
        pyautogui.click()
        sleep(4)
        pyautogui.moveTo(643, 479, 0.2)
        pyautogui.click()
        text.set("Activation Finished!!!")

    else:
        while True:
            pyautogui.moveTo(random.randint(29, 1313), random.randint(123, 661), 0.5)
            reload()
            getTime()

if __name__ == "__main__":
    ID = "BDSMAKV836"
    DOF = "05-01-2007"
    root = Tk()
    root.geometry("500x400+300+200")
    root.minsize(500, 400)
    root.maxsize(500, 400)
    root.resizable(0, 0)
    root.title("Ideal School & College")
     
    ISC = StringVar()
    ISC.set("  Online Classes Automator  ")
           
    name = StringVar()
    name.set("Created by Tahcin Ul Karim")
                
    text = StringVar()
    text.set("Press 'Connect' and wait....")

    label1 = Label(root, textvariable=ISC, relief=RAISED, font = "lucida 20 bold", fg = 'green')
    label1.pack()

    label2 = Label(root, textvariable=name, relief=RAISED, font=("lucida 23 italic"), fg = 'green')
    label2.pack()

    label3 = Label(root, textvariable=text, relief=RAISED, font = "lucida 25", fg = 'green')
    label3.pack()
                
    Connect = Button(root, text ="Connect", command = start, bg='#0052cc', fg='#ffffff')
    Connect['font'] = font.Font(size=30)
    Connect.pack(fill=BOTH, expand=1)

    Stop = Button(root, text ="Stop", command = stop)
    Stop['font'] = font.Font(size=30)
    Stop.pack(fill=BOTH, expand=1)

    Exit = Button(root, text ="Exit", command = exit, bg='#8B0000', fg='#ffffff')
    Exit['font'] = font.Font(size=30)
    Exit.pack(fill=BOTH, expand=1)
        
    root.mainloop()