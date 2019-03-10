from PIL import ImageGrab
from keras.models import load_model
import pyautogui
import keyboard
import webbrowser
import time
import numpy as np
from keras.preprocessing import image



model = load_model("model\\trex_6.h5")
webbrowser.open("http://www.trex-game.skipser.com/")
time.sleep(5)


while True:
    img = ImageGrab.grab(bbox=(650,530,920,610))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img/255
    pred = model.predict_classes(img)[0]
    print(pred)
    if pred == 0:
        pyautogui.press("space")

    if keyboard.is_pressed("q"):
        break
