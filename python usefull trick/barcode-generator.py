# pip install python-barcode
import barcode
from barcode.writer import ImageWriter
code = barcode.get("code128", "123456789", writer=ImageWriter())
code.save("barcode")
print("Barcode created successfully")
