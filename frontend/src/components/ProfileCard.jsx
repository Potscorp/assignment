const ProfileCard = ({ user }) => {
  if (!user) return null;

  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-6">
      <h2 className="text-xl font-semibold mb-4 text-gray-800">Profile</h2>
      <div className="space-y-2">
        <p className="text-gray-600">
          <span className="font-medium">Username:</span> {user.username}
        </p>
        <p className="text-gray-600">
          <span className="font-medium">Email:</span> {user.email}
        </p>
      </div>
    </div>
  );
};

export default ProfileCard;
