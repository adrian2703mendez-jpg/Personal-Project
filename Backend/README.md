# Backend Setup Guide

## Overview
This backend API handles user registration and login for the Seeds of Wealth course platform. User data is securely stored with hashed passwords.

## Prerequisites
- Node.js (v14 or higher)
- npm (comes with Node.js)

## Installation

1. **Navigate to the Backend folder:**
```bash
cd Backend
```

2. **Install dependencies:**
```bash
npm install
```

## Running the Server

**Start the backend server:**
```bash
npm start
```

You should see:
```
🌱 Seeds of Wealth backend running on http://localhost:5000
📝 User data stored in /path/to/users.json
```

## API Endpoints

### Register User
**POST** `http://localhost:5000/api/register`

Request body:
```json
{
  "fullname": "Jane Doe",
  "email": "jane@example.com",
  "password": "securePassword123",
  "phone": "+1 555-555-5555"
}
```

Response (success):
```json
{
  "success": true,
  "message": "Account created successfully",
  "userId": "1703077200000"
}
```

### Login User
**POST** `http://localhost:5000/api/login`

Request body:
```json
{
  "email": "jane@example.com",
  "password": "securePassword123"
}
```

Response (success):
```json
{
  "success": true,
  "message": "Logged in successfully",
  "user": {
    "id": "1703077200000",
    "fullname": "Jane Doe",
    "email": "jane@example.com",
    "phone": "+1 555-555-5555",
    "createdAt": "2024-12-26T..."
  }
}
```

### Get All Users (Testing Only)
**GET** `http://localhost:5000/api/users`

## Data Storage

User data is stored in `Backend/users.json`:
```json
{
  "users": [
    {
      "id": "1703077200000",
      "fullname": "Jane Doe",
      "email": "jane@example.com",
      "password": "$2b$10$hashed_password_here",
      "phone": "+1 555-555-5555",
      "createdAt": "2024-12-26T12:00:00.000Z"
    }
  ]
}
```

## Testing the Flow

1. **Start the backend:**
```bash
npm start
```

2. **Open Registration.html** in your browser
3. **Fill out the form** and click "Create account"
4. **You'll be redirected to Login.html**
5. **Use the same email/password** to log in
6. **You'll be redirected to Lobby.html** with your user data stored in localStorage

## Important Notes

⚠️ **Security Reminders:**
- Passwords are hashed with bcrypt (10 salt rounds)
- Never commit passwords to version control
- For production, use a real database (MongoDB, PostgreSQL, etc.)
- Add HTTPS in production
- Add rate limiting to prevent brute force attacks
- Implement token-based authentication (JWT) for stateless sessions

## Troubleshooting

**Error: "Connection error. Make sure the backend is running..."**
- Ensure the backend server is running (`npm start`)
- Check that it's listening on `http://localhost:5000`

**Error: "Email already registered"**
- The email is already in the system. Use a different email or clear `users.json` to reset.

**Clear User Data:**
To reset and remove all users, delete the `users.json` file (it will be recreated on next server start).

## File Structure
```
Backend/
├── server.js          # Express server with API endpoints
├── package.json       # Node.js dependencies
└── users.json         # User data (auto-created)
```

## Next Steps
- Add database integration (MongoDB, PostgreSQL)
- Add email verification
- Implement JWT authentication
- Add password reset functionality
- Add user profile management endpoints
