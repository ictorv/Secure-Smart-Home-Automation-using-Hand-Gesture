import base64
from PIL import Image
from io import BytesIO

def save_base64_image(base64_string, filename):
    image_data = base64.b64decode(base64_string.split(',')[1])
    image = Image.open(BytesIO(image_data))
    image.save(filename, 'JPEG')
