import React, { useEffect, useState } from 'react';
import { AppBar, Toolbar, IconButton, Typography, Box } from '@mui/material';
import LogoutIcon from '@mui/icons-material/Logout';
import { useAuth } from '../context/AuthContext';
import UploadArea from '../components/UploadArea';
import LoadingScreen from '../components/LoadingScreen';
import { uploadFile } from '../api/file';
import { DataGrid } from '@mui/x-data-grid';
import { CartesianGrid, XAxis, YAxis, Bar, BarChart, Tooltip} from 'recharts'
// import { BarChart, Bar } from '@mui/x-charts/BarChart';
// import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip } from "@material-ui/x-charts";

const initialRows = [
  { id: 1, name: 'Category A', value: 15 },
  { id: 2, name: 'Category B', value: 25 },
  { id: 3, name: 'Category C', value: 35 }
];

const columns = [
  { field: 'id', headerName: 'ID', width: 70 },
  { field: 'name', headerName: 'Category', width: 150 },
  { field: 'value', headerName: 'Value', width: 150 }
];

export default function Home() {
  const { logout } = useAuth();
  const [loading, setLoading] = useState(false);
  const [rows, setRows] = useState([]);
  const [cols, setCols] = useState([]);
  const [chartData,setChartdata] = useState([]);
  const [chartLabels, setChartLabels] = useState([]);
  useEffect(() => {
    setChartdata(rows.map((row) => row.value)) 
    setChartLabels(rows.map((row) => row.name))
  } ,[rows, cols])
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
      <div style={{ height: 400, width: 400 }}>
      {!loading && rows.length > 0 && (
        <BarChart width={600} height={400} data={rows}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="Date" />
        <YAxis />
        <Tooltip />
        <Bar dataKey="Temp Min" fill="#8884d8" />
      
        <Bar dataKey="Temp Max" fill="#82ca9d" />
      </BarChart>
      )}
      </div>
    </Box>
  );
}
