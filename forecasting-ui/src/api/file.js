import axios from 'axios';

const client = axios.create({ baseURL: import.meta.env.VITE_API_URL });
client.interceptors.request.use(config => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export function uploadFile(file) {
  const formData = new FormData();
  formData.append('file', file);
  return client.post('/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
}