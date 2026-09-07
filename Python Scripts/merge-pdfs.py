# pip install PyPDF2
import PyPDF2
merger = PyPDF2.PdfMerger()
for pdf in ["file1.pdf", "file2.pdf"]:
    merger.append(pdf)
merger.write("merged.pdf")
merger.close()
print("PDFs merged successfully")
