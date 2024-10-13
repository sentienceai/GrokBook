# app/resources/document_upload_resource.py
from flask_restful import Resource
from flask import request
import tempfile
import os

from app.utils.text_extractor import TextExtractor
from app.services.grok_service import GrokService
from app.services.x_service import XService
from flask import jsonify
from flask_restful import Resource

class DocumentUploadResource(Resource):
    def post(self):
        try:
            # Add your file upload logic here
            # For now, let's just return a simple message
            return jsonify({"message": "File upload endpoint reached"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
        file = request.files['file']
        filename = file.filename

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            file.save(tmp.name)
            ext = os.path.splitext(filename)[1].lower()

            if ext in ['.pdf', '.doc', '.docx', '.txt']:
                text_content = TextExtractor.extract(tmp.name, filename)
                os.unlink(tmp.name)
                analysis_result = GrokService.analyze_text(text_content)
            elif ext in ['.csv', '.xlsx']:
                df = TextExtractor.extract_dataset(tmp.name, ext)
                os.unlink(tmp.name)
                data_csv = df.to_csv(index=False)
                analysis_result = GrokService.analyze_dataset(data_csv)
            else:
                os.unlink(tmp.name)
                return {'message': 'Unsupported file type'}, 400

            key_points = analysis_result.get('key_points', [])
            relevant_posts = XService.get_relevant_posts(key_points)

            return {
                'analysis_result': analysis_result,
                'relevant_posts': relevant_posts
            }, 200
