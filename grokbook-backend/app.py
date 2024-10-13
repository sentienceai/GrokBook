# app.py
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app)

# Import resources
from app.resources.document_upload_resource import DocumentUploadResource

# Add resource routes
api.add_resource(DocumentUploadResource, '/api/upload')

if __name__ == '__main__':
    app.run(debug=True)
