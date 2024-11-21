import re
from pdfminer.high_level import extract_text
from PyPDF2 import PdfReader

def extract_text_from_pdf(resume):
    #return extract_text(resume.stream)
     reader = PdfReader(resume)
     text = ''
     for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
     return text


