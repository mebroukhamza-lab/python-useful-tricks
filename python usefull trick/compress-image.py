# pip install pillow
from PIL import Image
img = Image.open("image.jpg")
img.save("compressed.jpg", optimize=True, quality=40)
print("Image compressed successfully")
