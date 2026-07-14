import os
import PyPDF2

merger = PyPDF2.PdfMerger()
for file in sorted(os.listdir()):
    if file.endswith(".pdf"):
        merger.append(file)

merger.write("combined.pdf")
merger.close()
