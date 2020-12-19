from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

def type_string(text):
    keyboard.type(text)
    #time.sleep(4)

def enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
