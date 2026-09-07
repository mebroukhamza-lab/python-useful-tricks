# pip install pillow
from PIL import Image
from PIL.ExifTags import TAGS
img = Image.open("photo.jpg")
exif = img._getexif()
if exif:
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        print(tag, ":", value)
else:
    print("No EXIF data found")
