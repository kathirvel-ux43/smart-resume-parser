# File reader module - handles PDF and DOCX files

import fitz
from docx import Document
import re

class FileTextReader:
    def get_pdf_content(self, file_path):
        pdf_text = ""
        pdf_doc = fitz.open(file_path)
        for page_num in pdf_doc:
            pdf_text += page_num.get_text()
        pdf_doc.close()
        return pdf_text
    
    def get_docx_content(self, file_path):
        docx_text = ""
        doc_doc = Document(file_path)
        for para in doc_doc.paragraphs:
            docx_text += para.text + "\n"
        return docx_text
    
    def prepare_text(self, raw_text):
        cleaned_text = re.sub(r'\n+', ' ', raw_text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
        return cleaned_text.strip()