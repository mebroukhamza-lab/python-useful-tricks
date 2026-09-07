# pip install pillow
from PIL import Image
images = [Image.open(f).convert("RGB") for f in ["img1.jpg", "img2.jpg"]]
images[0].save("output.pdf", save_all=True, append_images=images[1:])
print("Images converted to PDF successfully")
