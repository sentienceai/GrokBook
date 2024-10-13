# app.py
from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from dotenv import load_dotenv
import logging

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/hello', methods=['GET'])
def hello():
    logger.info("GET request received at /hello")
    return jsonify({"message": "Hello, World!"}), 200

class DocumentUploadResource(Resource):
    def post(self):
        logger.info("POST request received at /api/upload")
        try:
            # Add your file upload logic here
            # For now, let's just return a simple message
            return {"message": "File upload endpoint reached"}, 200
        except Exception as e:
            logger.error(f"Error in DocumentUploadResource: {str(e)}")
            return {"error": str(e)}, 500

# Add resource routes
api.add_resource(DocumentUploadResource, '/api/upload')

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(debug=True, host='0.0.0.0', port=5001)
