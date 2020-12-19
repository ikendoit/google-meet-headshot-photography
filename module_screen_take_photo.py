import pyscreenshot as ImageGrab

def save_screen_shot(file_path):
    # grab fullscreen, save to file
    im = ImageGrab.grab()
    im.save(file_path)
