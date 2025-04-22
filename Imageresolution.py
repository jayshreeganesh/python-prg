# import PIL
# from PIL import Image
# print(PIL.__version__)

# import PIL could not be resolved
# pip3 install Pillow

import PIL
from PIL import Image

img = PIL.Image.open("C:\prg\python-prg\images\home.jpg")
width, height = img.size

print(width, "x", height)