# pip install PyPDF2
import PyPDF2
reader = PyPDF2.PdfReader("document.pdf")
watermark = PyPDF2.PdfReader("watermark.pdf").pages[0]
writer = PyPDF2.PdfWriter()
for page in reader.pages:
    page.merge_page(watermark)
    writer.add_page(page)
with open("watermarked.pdf", "wb") as f:
    writer.write(f)
print("Watermark added successfully")
