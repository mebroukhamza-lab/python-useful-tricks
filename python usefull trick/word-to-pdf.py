# pip install docx2pdf
from docx2pdf import convert
convert("document.docx", "document.pdf")
print("Word document converted to PDF successfully")
