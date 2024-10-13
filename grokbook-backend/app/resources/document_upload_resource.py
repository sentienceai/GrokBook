# app/resources/document_upload_resource.py
from quart import request, current_app
from quart.views import MethodView
import tempfile
import os
import logging
import traceback
import asyncio
from werkzeug.utils import secure_filename

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from app.utils.text_extractor import TextExtractor
from app.services.grok_service import GrokService
from app.services.x_service import XService

class DocumentUploadResource(MethodView):
    @staticmethod
    async def post():
        async with current_app.app_context():    
            current_app.logger.debug("DocumentUploadResource.post method called")
            form = await request.form
            files = await request.files
            if 'file' not in files:
                return {'error': 'No file part in the request'}, 400
            file = files['file']
            if file.filename == '':
                return {'error': 'No file selected for uploading'}, 400
            
            filename = secure_filename(file.filename)
            current_app.logger.info(f"Processing file: {filename}")
            
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                await file.save(temp_file.name)
                current_app.logger.debug(f"File saved temporarily at {temp_file.name}")
                
                try:
                    file_extension = os.path.splitext(filename)[1].lower()
                    current_app.logger.debug(f"File extension: {file_extension}")
                    
                    current_app.logger.debug("Extracting text from document")
                    text = await TextExtractor.extract(temp_file.name, filename)
                    
                    current_app.logger.debug("Analyzing text with GrokService")
                    grok_service = GrokService()
                    analysis_result = await grok_service.analyze_text(text)
                    
                    return analysis_result, 200
                except Exception as e:
                    current_app.logger.error(f"An error occurred during file processing: {str(e)}")
                    return {'error': str(e)}, 500
                finally:
                    current_app.logger.debug(f"Removing temporary file: {temp_file.name}")
                    os.unlink(temp_file.name)
