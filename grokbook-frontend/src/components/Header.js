import React from 'react';
import { AppBar, Toolbar, Typography, Button, IconButton } from '@mui/material';
import { Book as BookIcon, Brightness4, Brightness7 } from '@mui/icons-material';
import { Link } from 'react-router-dom';
import { useTheme } from '@mui/material/styles';

const Header = ({ toggleColorMode }) => {
  const theme = useTheme();

  return (
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
        <IconButton onClick={toggleColorMode} color="inherit">
          {theme.palette.mode === 'dark' ? <Brightness7 /> : <Brightness4 />}
        </IconButton>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
