import React from 'react';
import { Typography, Container } from '@mui/material';

const Footer = () => (
  <footer style={{ marginTop: 'auto', padding: '1rem 0', backgroundColor: '#f5f5f5' }}>
    <Container maxWidth="lg">
      <Typography variant="body2" color="textSecondary" align="center">
        © {new Date().getFullYear()} GrokBook
      </Typography>
    </Container>
  </footer>
);

export default Footer;
