count = 0
started = False
running = True
from pynput import keyboard
from PIL import Image, ImageGrab, ImageOps
import glob
import os
import re
list_of_files = glob.glob('E:/GeneralDev/chronicon-ai/data/*jpg')
if(len(list_of_files) != 0):
    count
    last = max(list_of_files, key=os.path.getctime)
    count = int(re.findall(r'\d+',last)[0])
    print("ID # of the last file: {0}".format(count))
print("Script running")

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.alt_gr:
        # Stop listener
        return False

def on_press(key):
    global started
    try:
        if(key == keyboard.Key.alt_gr):
            return False
        if(key == keyboard.Key.backspace):
            started = True
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    if started == True:
        #global count
        count += 1
        image = ImageGrab.grab()
        image = ImageOps.grayscale(image)
        image = ImageOps.contain(image, (128,128))
        image.save("data/"+str(count)+str(key)+".jpg")
while(running):
    with keyboard.Events() as events:
        # Block at most one second
        event = events.get(1.0)
        if event != None:
            #global started
            try:
                if(event.key == keyboard.Key.alt_gr):
                    running = False
                    exit()
                if(event.key == keyboard.Key.backspace):
                    started = True
                print('alphanumeric key {0} pressed'.format(
                    event.key.char))
            except AttributeError:
                print('special key {0} pressed'.format(
                    event.key))
            if started == True:
                #   global count
                count += 1
                image = ImageGrab.grab()
                image = ImageOps.grayscale(image)
                image = image.resize((128,128))
                image.save("data/"+str(count)+str(event.key)+".jpg")
