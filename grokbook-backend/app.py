# app.py
from quart import Quart
from quart_cors import cors
from app.resources.document_upload_resource import DocumentUploadResource

app = Quart(__name__)
app = cors(app)

@app.route('/api/upload', methods=['POST'])
async def upload_document():
    return await DocumentUploadResource.post()

# Explicitly create the application instance
application = app

if __name__ == '__main__':
    application.run(debug=True, port=5001)