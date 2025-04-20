import React from 'react';
import { Box, CircularProgress, Typography } from '@mui/material';

const quotes = [
  'Forecasting the future, one degree at a time.',
  'Machine learning: where data meets destiny.',
  'Predicting tomorrow’s temperature with today’s data.',
];
export default function LoadingScreen() {
  const quote = quotes[Math.floor(Math.random() * quotes.length)];
  return (
    <Box
      sx={{
        position: 'fixed', top: 0, left: 0, width: '100%', height: '100%',
        display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center',
        bgcolor: 'rgba(255,255,255,0.8)', zIndex: 9999
      }}
    >
      <CircularProgress />
      <Typography sx={{ mt: 2, fontStyle: 'italic' }}>{quote}</Typography>
    </Box>
  );
}