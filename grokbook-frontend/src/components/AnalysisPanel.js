import React from 'react';
import { Typography, List, ListItem, ListItemText } from '@mui/material';

const AnalysisPanel = ({ data }) => {
  if (!data) {
    return <Typography variant="h6">Analysis results will appear here</Typography>;
  }

  return (
    <div style={{ marginTop: '2rem' }}>
      <Typography variant="h6">Summary</Typography>
      <Typography variant="body1" paragraph>
        {data.summary}
      </Typography>
      <Typography variant="h6">Key Points</Typography>
      <List dense>
        {data.key_points.map((point, index) => (
          <ListItem key={index}>
            <ListItemText primary={point} />
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default AnalysisPanel;
