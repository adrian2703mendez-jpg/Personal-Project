const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const bcrypt = require('bcrypt');

const app = express();
const PORT = 5000;
const usersFile = path.join(__dirname, 'users.json');

// Middleware
app.use(cors());
app.use(bodyParser.json());

// Initialize users.json if it doesn't exist
if (!fs.existsSync(usersFile)) {
  fs.writeFileSync(usersFile, JSON.stringify({ users: [] }, null, 2));
}

// Helper function to read users
function readUsers() {
  const data = fs.readFileSync(usersFile, 'utf8');
  return JSON.parse(data);
}

// Helper function to write users
function writeUsers(data) {
  fs.writeFileSync(usersFile, JSON.stringify(data, null, 2));
}

// Registration endpoint
app.post('/api/register', async (req, res) => {
  try {
    const { fullname, email, password, phone } = req.body;

    // Validate input
    if (!fullname || !email || !password) {
      return res.status(400).json({ success: false, message: 'Missing required fields' });
    }

    const data = readUsers();

    // Check if email already exists
    const emailExists = data.users.some(u => u.email === email);
    if (emailExists) {
      return res.status(400).json({ success: false, message: 'Email already registered' });
    }

    // Hash password
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create new user
    const newUser = {
      id: Date.now().toString(),
      fullname,
      email,
      password: hashedPassword,
      phone: phone || '',
      createdAt: new Date().toISOString(),
      progress: {
        completedCourses: [],
        enrolledCourses: [],
        lessonsCompleted: 0,
        totalSpent: 0,
        badges: [],
        lastAccessed: new Date().toISOString()
      }
    };

    data.users.push(newUser);
    writeUsers(data);

    res.status(201).json({ success: true, message: 'Account created successfully', userId: newUser.id });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).json({ success: false, message: 'Server error during registration' });
  }
});

// Login endpoint
app.post('/api/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    // Validate input
    if (!email || !password) {
      return res.status(400).json({ success: false, message: 'Email and password required' });
    }

    const data = readUsers();

    // Find user by email
    const user = data.users.find(u => u.email === email);
    if (!user) {
      return res.status(401).json({ success: false, message: 'Invalid email or password' });
    }

    // Compare passwords
    const passwordMatch = await bcrypt.compare(password, user.password);
    if (!passwordMatch) {
      return res.status(401).json({ success: false, message: 'Invalid email or password' });
    }

    // Return user info (without password)
    const { password: _, ...userWithoutPassword } = user;
    res.json({ success: true, message: 'Logged in successfully', user: userWithoutPassword });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ success: false, message: 'Server error during login' });
  }
});

// Get all users (for testing only - remove in production)
app.get('/api/users', (req, res) => {
  const data = readUsers();
  const usersWithoutPasswords = data.users.map(u => {
    const { password, ...userWithoutPassword } = u;
    return userWithoutPassword;
  });
  res.json({ users: usersWithoutPasswords });
});

// Get user progress
app.get('/api/progress/:userId', (req, res) => {
  try {
    const { userId } = req.params;
    const data = readUsers();
    const user = data.users.find(u => u.id === userId);

    if (!user) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }

    res.json({
      success: true,
      progress: user.progress || {
        completedCourses: [],
        enrolledCourses: [],
        lessonsCompleted: 0,
        totalSpent: 0,
        badges: [],
        lastAccessed: new Date().toISOString()
      }
    });
  } catch (error) {
    console.error('Error fetching progress:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// Save user progress
app.post('/api/progress/:userId', (req, res) => {
  try {
    const { userId } = req.params;
    const { lessonsCompleted, completedCourses, enrolledCourses, totalSpent, badges } = req.body;
    const data = readUsers();

    const userIndex = data.users.findIndex(u => u.id === userId);
    if (userIndex === -1) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }

    // Update progress
    if (!data.users[userIndex].progress) {
      data.users[userIndex].progress = {
        completedCourses: [],
        enrolledCourses: [],
        lessonsCompleted: 0,
        totalSpent: 0,
        badges: [],
        lastAccessed: new Date().toISOString()
      };
    }

    if (lessonsCompleted !== undefined) data.users[userIndex].progress.lessonsCompleted = lessonsCompleted;
    if (completedCourses !== undefined) data.users[userIndex].progress.completedCourses = completedCourses;
    if (enrolledCourses !== undefined) data.users[userIndex].progress.enrolledCourses = enrolledCourses;
    if (totalSpent !== undefined) data.users[userIndex].progress.totalSpent = totalSpent;
    if (badges !== undefined) data.users[userIndex].progress.badges = badges;
    data.users[userIndex].progress.lastAccessed = new Date().toISOString();

    writeUsers(data);
    res.json({ success: true, message: 'Progress updated successfully' });
  } catch (error) {
    console.error('Error saving progress:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// Reset user progress
app.post('/api/progress/:userId/reset', (req, res) => {
  try {
    const { userId } = req.params;
    const data = readUsers();

    const userIndex = data.users.findIndex(u => u.id === userId);
    if (userIndex === -1) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }

    // Reset progress to initial state
    data.users[userIndex].progress = {
      completedCourses: [],
      enrolledCourses: [],
      lessonsCompleted: 0,
      totalSpent: 0,
      badges: [],
      lastAccessed: new Date().toISOString()
    };

    writeUsers(data);
    res.json({ success: true, message: 'User progress reset successfully' });
  } catch (error) {
    console.error('Error resetting progress:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// Get user profile with all stats
app.get('/api/user/:userId', (req, res) => {
  try {
    const { userId } = req.params;
    const data = readUsers();
    const user = data.users.find(u => u.id === userId);

    if (!user) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }

    const { password, ...userWithoutPassword } = user;
    res.json({ success: true, user: userWithoutPassword });
  } catch (error) {
    console.error('Error fetching user profile:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

app.listen(PORT, () => {
  console.log(`🌱 Seeds of Wealth backend running on http://localhost:${PORT}`);
  console.log(`📝 User data stored in ${usersFile}`);
});
