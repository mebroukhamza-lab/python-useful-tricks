# pip install pdf2image
from pdf2image import convert_from_path
pages = convert_from_path("document.pdf", dpi=200)
for i, page in enumerate(pages):
    page.save(f"page_{i}.jpg", "JPEG")
print("PDF converted to images successfully")
