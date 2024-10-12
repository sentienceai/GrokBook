import React from 'react';
import { Typography, List, ListItem, ListItemText, Avatar, ListItemAvatar } from '@mui/material';

const XInsightsPanel = ({ posts }) => {
  if (!posts) {
    return <Typography variant="h6">Relevant X posts will appear here</Typography>;
  }

  return (
    <div>
      <Typography variant="h6">Relevant Posts from X</Typography>
      <List dense>
        {posts.map((post, index) => (
          <ListItem key={index} alignItems="flex-start">
            <ListItemAvatar>
              <Avatar alt={post.user} src={post.user_image_url} />
            </ListItemAvatar>
            <ListItemText
              primary={`@${post.user}`}
              secondary={post.text}
            />
          </ListItem>
        ))}
      </List>
    </div>
  );
};

export default XInsightsPanel;
