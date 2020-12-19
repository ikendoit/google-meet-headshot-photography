try:
    from PIL import Image
except ImportError:
    import Image


def crop_and_save(input_path, output_path, x_tl, y_tl, x_br, y_br):

    cropped_image = Image.open(input_path).crop((x_tl, y_tl, x_br, y_br))

    cropped_image.save(output_path)
