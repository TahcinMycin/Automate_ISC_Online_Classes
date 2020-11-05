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

now = datetime.datetime.now()
minute = now.minute
hour = now.hour - 12 if now.hour >= 12 else now.hour

url = "https://www.edulive.edu-smart.info/isc/login.php"
url2 = "edulive.edu-smart.info/isc/login.php"
data = requests.request("GET", url)
curr_url = data.url

class Window:

    global label1
    global label2
    global label3
    global root
    global ISC
    global Connect
    global Stop
    global Exit
    
    def start(self):
        label1.destroy()
        label2.destroy()
        root.geometry("500x300")
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
        pyautogui.write("BDSMAKV836")
        pyautogui.moveTo(800, 400, 0.01)
        pyautogui.click()
        pyautogui.moveTo(722, 396)
        pyautogui.click()
        pyautogui.write("05-01-2007")
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

        Window.getTime()
    
    def stop(self):
        label1.config(fg = 'red')
        text.set("Loading finished!!!") 
    
    def getTime(self):
        if hour >= 8 and minute >= 30 or hour <= 9 and minute <= 5:
            pyautogui.moveTo(980, 248, 0.5)
            pyautogui.click()
            sleep(4)
            pyautogui.moveTo(643, 479, 0.2)
            pyautogui.click()
            text.set("Activation Finished!!!")

        elif hour == 9 and minute >= 10 or hour == 9 and minute <= 46:
            pyautogui.moveTo(852, 328, 0.5)
            pyautogui.click()
            sleep(4)
            pyautogui.moveTo(643, 479, 0.2)
            pyautogui.click()
            text.set("Activation Finished!!!")


        elif hour <= 2 and minute >= 40 or hour >= 3 and minute <= 15:
            pyautogui.moveTo(890, 446, 0.5)
            pyautogui.click()
            sleep(4)
            pyautogui.moveTo(643, 479, 0.2)
            pyautogui.click()
            text.set("Activation Finished!!!")

        elif hour == 3 and minute >= 10 or hour == 3 and minute <= 55:
            pyautogui.moveTo(969, 531, 0.5)
            pyautogui.click()
            sleep(4)
            pyautogui.moveTo(643, 479, 0.2)
            pyautogui.click()
            text.set("Activation Finished!!!")

        else:
            while True:
                pyautogui.moveTo(random.randint(29, 1313), random.randint(123, 661), 0.5)
                System.reload()
                Window.getTime()
    
    def create(self):
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
                
        Connect = Button(root, text ="Connect", command = Window.start, bg='#0052cc', fg='#ffffff')
        Connect['font'] = font.Font(size=30)
        Connect.pack(fill=BOTH, expand=1)

        Stop = Button(root, text ="Stop", command = Window.stop)
        Stop['font'] = font.Font(size=30)
        Stop.pack(fill=BOTH, expand=1)

        Exit = Button(root, text ="Exit", command = exit)
        Exit['font'] = font.Font(size=30)
        Exit.pack(fill=BOTH, expand=1)
        
        root.mainloop()
            
        