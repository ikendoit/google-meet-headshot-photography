try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(file_path, x, y):

    cropped_image = Image.open(file_path).crop((x, y - 40, x + 200, y + 40))

    text = pytesseract.image_to_string(cropped_image)

    return text
