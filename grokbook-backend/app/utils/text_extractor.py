# app/utils/text_extractor.py
import os
import PyPDF2
import docx
import pandas as pd

class TextExtractor:
    @staticmethod
    def extract(file_path, filename):
        ext = os.path.splitext(filename)[1].lower()
        if ext == '.pdf':
            return TextExtractor.extract_pdf(file_path)
        elif ext in ['.doc', '.docx']:
            return TextExtractor.extract_docx(file_path)
        elif ext == '.txt':
            return TextExtractor.extract_txt(file_path)
        else:
            raise ValueError('Unsupported file type')

    @staticmethod
    def extract_pdf(file_path):
        text = ''
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfFileReader(f)
            for page_num in range(reader.numPages):
                text += reader.getPage(page_num).extractText()
        return text

    @staticmethod
    def extract_docx(file_path):
        doc = docx.Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])

    @staticmethod
    def extract_txt(file_path):
        with open(file_path, 'r') as f:
            return f.read()

    @staticmethod
    def extract_dataset(file_path, extension):
        if extension == '.csv':
            df = pd.read_csv(file_path)
        elif extension == '.xlsx':
            df = pd.read_excel(file_path)
        else:
            raise ValueError('Unsupported dataset type')
        return df
