import apiClient from './client';

export const authApi = {
  register: async (username, email, password) => {
    const response = await apiClient.post('/auth/register/', { username, email, password });
    return response.data;
  },
  login: async (email, password) => {
    const response = await apiClient.post('/auth/login/', { email, password });
    return response.data;
  },
};
