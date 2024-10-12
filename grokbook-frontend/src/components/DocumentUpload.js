import React, { useState } from 'react';
import { Typography, Button } from '@mui/material';
import { CloudUpload as CloudUploadIcon } from '@mui/icons-material';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const DocumentUpload = ({ setAnalysisData }) => {
  const [documentFile, setDocumentFile] = useState(null);

  const { getRootProps, getInputProps } = useDropzone({
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'text/plain': ['.txt']
    },
    onDrop: (acceptedFiles) => {
      if (acceptedFiles.length > 0) {
        setDocumentFile(acceptedFiles[0]);
      }
    }
  });

  const handleUpload = async () => {
    if (!documentFile) return;

    const formData = new FormData();
    formData.append('file', documentFile);

    try {
      const response = await axios.post('/api/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      setAnalysisData(response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div>
      <Typography variant="h6">Upload Document</Typography>
      <div {...getRootProps()} style={{ border: '2px dashed #ccc', padding: '20px', marginBottom: '20px' }}>
        <input {...getInputProps()} />
        <p>Drag and drop a document here, or click to select files</p>
      </div>
      <Button
        variant="contained"
        color="primary"
        startIcon={<CloudUploadIcon />}
        onClick={handleUpload}
        disabled={!documentFile}
      >
        Analyze Document
      </Button>
    </div>
  );
};

export default DocumentUpload;
