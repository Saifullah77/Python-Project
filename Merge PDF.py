from PyPDF2 import PdfMerger

ALLPDF = [" ", " "]

OurMerger = PdfMerger()

for newPDF in ALLPDF:
    OurMerger.append(newPDF)
    
OurMerger.write("saifullah.pdf")

OurMerger.close()
    
