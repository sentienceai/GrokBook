import React, { useState } from 'react';
import { Typography, Button } from '@mui/material';
import { CloudUpload as CloudUploadIcon } from '@mui/icons-material';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const DocumentUpload = ({ setAnalysisData }) => {
  const [documentFile, setDocumentFile] = useState(null);
  const navigate = useNavigate();
  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:5000'; 

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
      const response = await axios.post(
        `${process.env.REACT_APP_API_BASE_URL}/api/upload`,
        formData,
        {
          headers: { 'Content-Type': 'multipart/form-data' },
        }
      );

      const data = response.data;

      // Determine the file type and navigate accordingly
      const ext = documentFile.name.split('.').pop().toLowerCase();
      if (['csv', 'xlsx'].includes(ext)) {
        // Navigate to dataset analysis view
        navigate('/dataset-analysis', { state: { data } });
      } else {
        // Navigate to document analysis view
        navigate('/document-analysis', { state: { data } });
      }
    } catch (error) {
      console.error('Error uploading file:', error);
      alert('An error occurred while uploading the file.');
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
