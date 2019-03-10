import os
import webbrowser
import keyboard
from PIL import ImageGrab,Image
import random

def creat_folders():               # if folder is not exist then create folder
    if not os.path.exists("Data_2"):
        os.mkdir("Data_2")
    for i in ["jump","nothing"]:
        if not os.path.exists("Data_2\\"+i):
            os.mkdir("Data_2\\"+i)

os.getcwd()                                                 # get current working directory
webbrowser.open("http://www.trex-game.skipser.com/")        # open game site
creat_folders()                 # creating folder

while True:
    rand = random.randint(0,100000000)
    img = ImageGrab.grab(bbox=(650,530,920,610))               #(left_x, top_y, right_x, bottom_y)
    if keyboard.is_pressed("up arrow"):
        img.save("Data_2\\jump\\j{}.jpeg".format(rand))
 #   if keyboard.is_pressed("down arrow"):
  #      img.save("Data_2\\duck\\d{}.jpeg".format(rand))
    if keyboard.is_pressed("a"):
        img.save("Data_2\\nothing\\n{}.jpeg".format(rand))
    if keyboard.is_pressed("q"):
        break
