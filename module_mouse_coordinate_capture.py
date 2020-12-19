import pyscreenshot as ImageGrab
from pynput.mouse import Listener

xx, yy = 0, 0
def capture_coordinate():
    global xx, yy
    def on_click(x, y, button, pressed):
        global xx, yy
        xx, yy = x, y
        if not pressed:
            # Stop listener
            return False

    with Listener(on_click=on_click) as listener:
        listener.join()
        return xx, yy;


