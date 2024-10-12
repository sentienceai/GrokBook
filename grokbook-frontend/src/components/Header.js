import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { Book as BookIcon } from '@mui/icons-material';
import { Link } from 'react-router-dom';

const Header = () => (
  <AppBar position="sticky">
    <Toolbar>
      <BookIcon style={{ marginRight: '10px' }} />
      <Typography variant="h6" style={{ flexGrow: 1 }}>
        <Link to="/" style={{ textDecoration: 'none', color: 'inherit' }}>
          GrokBook
        </Link>
      </Typography>
      <Button color="inherit" component={Link} to="/library">
        Library
      </Button>
      <Button color="inherit" component={Link} to="/settings">
        Settings
      </Button>
    </Toolbar>
  </AppBar>
);

export default Header;
