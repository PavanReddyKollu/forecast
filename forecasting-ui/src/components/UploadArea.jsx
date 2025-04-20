import React from 'react';
import { useDropzone } from 'react-dropzone';
import { Box, Typography } from '@mui/material';

export default function UploadArea({ onFile }) {
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    accept: {
      'text/csv': ['.csv'],
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx', '.xls'],
    },
    multiple: false,
    onDrop: files => onFile(files[0]),
  });

  return (
    <Box
      {...getRootProps()}
      sx={{
        border: '2px dashed #90caf9',
        borderRadius: 2,
        p: 4,
        textAlign: 'center',
        cursor: 'pointer',
        '&:hover': { backgroundColor: '#e3f2fd' },
      }}
    >
      <input {...getInputProps()} />
      {isDragActive ? (
        <Typography>Drop the file here...</Typography>
      ) : (
        <Typography>Drag & drop a CSV/Excel file here, or click to select</Typography>
      )}
    </Box>
  );
}