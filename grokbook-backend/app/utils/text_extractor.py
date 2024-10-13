# app/utils/text_extractor.py
import os
import PyPDF2
import docx
import pandas as pd
import asyncio

class TextExtractor:
    @staticmethod
    async def extract(file_path, filename):
        loop = asyncio.get_running_loop()
        if filename.lower().endswith('.pdf'):
            return await loop.run_in_executor(None, TextExtractor._extract_from_pdf, file_path)
        elif filename.lower().endswith('.docx'):
            return await loop.run_in_executor(None, TextExtractor._extract_from_docx, file_path)
        else:
            raise ValueError("Unsupported file format")

    @staticmethod
    def _extract_from_pdf(file_path):
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return ' '.join(page.extract_text() for page in reader.pages)

    @staticmethod
    def _extract_from_docx(file_path):
        doc = docx.Document(file_path)
        return ' '.join(paragraph.text for paragraph in doc.paragraphs)

    @staticmethod
    def extract_dataset(file_path, extension):
        if extension == '.csv':
            df = pd.read_csv(file_path)
        elif extension == '.xlsx':
            df = pd.read_excel(file_path)
        else:
            raise ValueError('Unsupported dataset type')
        return df
