from pynput.mouse import Controller, Button

mouse = Controller()

def click(x, y, double_click=False):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)
    if double_click:
        mouse.click(Button.left, 1)
