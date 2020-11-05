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

now = datetime.datetime.now()
minute = now.minute
hour = now.hour - 12 if now.hour >= 12 else now.hour

url = "https://www.edulive.edu-smart.info/isc/login.php"
url2 = "edulive.edu-smart.info/isc/login.php"
data = requests.request("GET", url)
curr_url = data.url

def install_packages(name):
    name = str(name)
    with open("module.txt", "w") as md:
        md.write(name)
    with open("module.txt", "r") as md:
        line = md.read()
        if not name in line:
            os.system("pip install " + name)

def reload():
    now = datetime.datetime.now()
    minute = now.minute
    hour = now.hour - 12 if now.hour >= 12 else now.hour
    sleep(5)
    pyautogui.hotkey('f5')
    
def image():
    if not os.path.isfile("icon.png"):
        img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTskzeDhx2QdK2zHYTAhwTHpZwbRcVA1bqbUQ&usqp=CAU"
    with open("icon.png", "wb") as img:
        img.write(img_url.content)