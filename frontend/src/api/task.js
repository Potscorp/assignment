import apiClient from './client';

export const taskApi = {
  getTasks: async (searchQuery = '', statusFilter = '') => {
    const params = {};
    if (searchQuery) params.q = searchQuery;
    if (statusFilter && statusFilter !== 'all') params.status = statusFilter;
    const response = await apiClient.get('/tasks/', { params });
    return response.data;
  },
  createTask: async (title, description) => {
    const response = await apiClient.post('/tasks/', { title, description, status: 'pending' });
    return response.data;
  },
  updateTask: async (id, data) => {
    const response = await apiClient.put(`/tasks/${id}/`, data);
    return response.data;
  },
  deleteTask: async (id) => {
    await apiClient.delete(`/tasks/${id}/`);
  },
};
