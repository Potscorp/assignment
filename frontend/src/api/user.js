import apiClient from './client';

export const userApi = {
  getProfile: async () => {
    const response = await apiClient.get('/users/me/');
    return response.data;
  },
  updateProfile: async (data) => {
    const response = await apiClient.put('/users/me/', data);
    return response.data;
  },
};
