import React from 'react';
import { Typography } from '@mui/material';
import { Document, Page } from 'react-pdf';
import 'react-pdf/dist/esm/Page/AnnotationLayer.css';

const DocumentViewer = ({ file }) => {
  if (!file) {
    return <Typography variant="h6">No document selected</Typography>;
  }

  return (
    <div>
      <Typography variant="h6">Document Viewer</Typography>
      <Document file={file}>
        <Page pageNumber={1} />
      </Document>
      {/* Add pagination or navigation as needed */}
    </div>
  );
};

export default DocumentViewer;
