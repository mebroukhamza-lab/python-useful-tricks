# pip install PyPDF2
import PyPDF2
reader = PyPDF2.PdfReader("document.pdf")
writer = PyPDF2.PdfWriter()
for page in reader.pages:
    writer.add_page(page)
writer.encrypt("mypassword")
with open("protected.pdf", "wb") as f:
    writer.write(f)
print("PDF protected with password successfully")
