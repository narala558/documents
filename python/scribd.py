import os.path
import time

import pyautogui
import pyscreenshot as ImageGrab


def save_page(name):
    ImageGrab.grab()
    ImageGrab.grab_to_file(name)


output_dir = 'book'
try:
    os.rmdir(output_dir)
except:
    pass

try:
    os.mkdir(output_dir)
except:
    pass


start_time = 5

print('Starts in {} seconds'.format(start_time))
time.sleep(start_time)

for i in range(1000):
    time.sleep(1)
    name = os.path.join(output_dir, '{}.png'.format(i))
    save_page(name)
    pyautogui.typewrite(['right'])
