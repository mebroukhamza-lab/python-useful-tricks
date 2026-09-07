# pip install PyPDF2
import PyPDF2
with open("document.pdf", "rb") as f:
    reader = PyPDF2.PdfReader(f)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
print(text)
