# pip install rembg pillow
from rembg import remove
from PIL import Image
img = Image.open("input.png")
output = remove(img)
output.save("output.png")
print("Background removed successfully")
