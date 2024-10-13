import React, { useState } from 'react';
import { Container, Grid } from '@mui/material';
import DocumentUpload from '../components/DocumentUpload';
import DocumentViewer from '../components/DocumentViewer';
import AnalysisPanel from '../components/AnalysisPanel';
import XInsightsPanel from '../components/XInsightsPanel';

const Home = () => {
  const [analysisData, setAnalysisData] = useState(null);
  const [documentFile, setDocumentFile] = useState(null);

  return (
    <Container maxWidth="xl" style={{ marginTop: '2rem' }}>
      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <DocumentUpload setAnalysisData={setAnalysisData} setDocumentFile={setDocumentFile} />
          <AnalysisPanel data={analysisData} />
        </Grid>
        <Grid item xs={12} md={5}>
          <DocumentViewer file={documentFile} />
        </Grid>
        <Grid item xs={12} md={3}>
          <XInsightsPanel posts={analysisData?.relevant_posts} />
        </Grid>
      </Grid>
    </Container>
  );
};

export default Home;
