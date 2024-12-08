import React, { useState, useEffect } from 'react';
import { Card, Button, ListGroup, Row, Col } from 'react-bootstrap';
import Cards from '../Components/Cards.jsx'
import '../Components/Profile.css'; // Make sure to import the updated CSS file

function ProfilePage() {
  const [profileData, setProfileData] = useState(null);

  // Simulating fetching profile data (replace with API call)
  useEffect(() => {
    const fetchProfileData = () => {
      const data = {
        username: 'TantoBoy',
        bio: 'A cutie and aggresive baby.',
        profilePicture: 'https://example.com/path-to-profile-picture.jpg', // Replace with your image URL
        posts: [
          { id: 1, content: 'Just adopted a new dog!' },
          { id: 2, content: 'Had an amazing time at the animal shelter.' },
          { id: 3, content: 'Looking for advice on pet care.' },
        ],
      };
      setProfileData(data);
    };

    fetchProfileData();
  }, []);

  // Loading state
  if (!profileData) {
    return <div>Loading...</div>;
  }

  return (
    <div className="profile-page">
      <Card className="profile-card">
        <Card.Header className="text-center">
          <img
            src={profileData.profilePicture}
            alt="Profile"
            className="profile-picture profile-paw-heart"
          />
          <h3 className="profile-petname">{profileData.username}</h3>
          <p className="profile-status">{profileData.bio}</p>
          {/* Edit Profile Button outside of posts section */}
      <div className="profile-edit-container">
        <Button variant="primary" className="profile-edit-button">Edit Profile</Button>
      </div>
        </Card.Header>
        <Card.Body>
          <h5>Posts</h5>
          <Cards/>
        </Card.Body>
      </Card>
      
    </div>
  );
}

export default ProfilePage;
