import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';
import ProfileCard from '../components/ProfileCard';
import TaskPanel from '../components/TaskPanel';
import { userApi } from '../api/user';
import { useAuth } from '../hooks/useAuth';

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [error, setError] = useState('');
  const { logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    fetchProfile();
  }, []);

  const fetchProfile = async () => {
    try {
      const data = await userApi.getProfile();
      setUser(data);
    } catch (err) {
      setError('Failed to load profile');
      if (err.response?.status === 401) {
        logout();
        navigate('/login');
      }
    }
  };

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar onLogout={logout} />
      
      <div className="container mx-auto px-4 py-8 max-w-6xl">
        {error && (
          <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            {error}
          </div>
        )}
        
        <ProfileCard user={user} />
        <TaskPanel />
      </div>
    </div>
  );
};

export default Dashboard;
