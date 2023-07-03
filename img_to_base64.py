import base64

def img_to_base64(filename):
    with open(filename, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode()