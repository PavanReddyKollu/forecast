import React, { useState } from 'react';
import { AppBar, Toolbar, IconButton, Typography, Box } from '@mui/material';
import LogoutIcon from '@mui/icons-material/Logout';
import { useAuth } from '../context/AuthContext';
import UploadArea from '../components/UploadArea';
import LoadingScreen from '../components/LoadingScreen';
import { uploadFile } from '../api/file';
import { DataGrid } from '@mui/x-data-grid';

export default function Home() {
  const { logout } = useAuth();
  const [loading, setLoading] = useState(false);
  const [rows, setRows] = useState([]);
  const [cols, setCols] = useState([]);

  const handleFile = async file => {
    setLoading(true);
    try {
      const res = await uploadFile(file);
      const data = res.data;
      setCols(Object.keys(data[0]).map(key => ({ field: key, headerName: key, width: 150 })));
      setRows(data.map((row, i) => ({ id: i, ...row })));
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ height: '100vh', width: '100%' }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" sx={{ flexGrow: 1 }}>Forecast Dashboard</Typography>
          <IconButton color="inherit" onClick={logout}><LogoutIcon /></IconButton>
        </Toolbar>
      </AppBar>
      <Box sx={{ p: 4, display: 'flex', justifyContent: 'center', alignItems: 'center', height: 'calc(100% - 64px)' }}>
        {loading && <LoadingScreen />}
        {!loading && rows.length === 0 && <UploadArea onFile={handleFile} />}
        {!loading && rows.length > 0 && (
          <DataGrid rows={rows} columns={cols} pageSize={10} rowsPerPageOptions={[10]} />
        )}
      </Box>
    </Box>
  );
}
