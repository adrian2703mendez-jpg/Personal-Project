const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const bcrypt = require('bcrypt');
const session = require('express-session');
const SQLiteStore = require('connect-sqlite3')(session);
const sqlite3 = require('sqlite3').verbose();

const app = express();
const PORT = process.env.PORT || 5000;
const dataDirectory = process.env.DATA_DIR || __dirname;
fs.mkdirSync(dataDirectory, { recursive: true });
const databaseFile = path.join(dataDirectory, 'course.sqlite');
const database = new sqlite3.Database(databaseFile);
const isProduction = process.env.NODE_ENV === 'production';
const trialDays = Number.parseInt(process.env.TRIAL_DAYS || '7', 10);

function run(sql, params = []) {
  return new Promise((resolve, reject) => {
    database.run(sql, params, function onRun(error) {
      if (error) reject(error);
      else resolve(this);
    });
  });
}

function get(sql, params = []) {
  return new Promise((resolve, reject) => {
    database.get(sql, params, (error, row) => {
      if (error) reject(error);
      else resolve(row);
    });
  });
}

function all(sql, params = []) {
  return new Promise((resolve, reject) => {
    database.all(sql, params, (error, rows) => {
      if (error) reject(error);
      else resolve(rows);
    });
  });
}

async function ensureColumn(column, definition) {
  const columns = await all('PRAGMA table_info(users)');
  if (!columns.some(existingColumn => existingColumn.name === column)) {
    await run(`ALTER TABLE users ADD COLUMN ${column} ${definition}`);
  }
}

function trialDates(startedAt = new Date()) {
  const start = new Date(startedAt);
  const end = new Date(start);
  end.setUTCDate(end.getUTCDate() + trialDays);
  return { trialStartedAt: start.toISOString(), trialEndsAt: end.toISOString() };
}

async function initializeDatabase() {
  await run(`CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    fullname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE COLLATE NOCASE,
    password TEXT NOT NULL,
    phone TEXT NOT NULL DEFAULT '',
    createdAt TEXT NOT NULL,
    progress TEXT NOT NULL,
    trialStartedAt TEXT,
    trialEndsAt TEXT,
    paidAccess INTEGER NOT NULL DEFAULT 0
  )`);

  await ensureColumn('trialStartedAt', 'TEXT');
  await ensureColumn('trialEndsAt', 'TEXT');
  await ensureColumn('paidAccess', 'INTEGER NOT NULL DEFAULT 0');

  const userCount = await get('SELECT COUNT(*) AS count FROM users');
  const legacyFile = path.join(__dirname, 'users.json');
  if (userCount.count === 0 && fs.existsSync(legacyFile)) {
    const legacyData = JSON.parse(fs.readFileSync(legacyFile, 'utf8'));
    for (const user of legacyData.users || []) {
      await run(
        'INSERT OR IGNORE INTO users (id, fullname, email, password, phone, createdAt, progress, trialStartedAt, trialEndsAt, paidAccess) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        [user.id, user.fullname, user.email, user.password, user.phone || '', user.createdAt, JSON.stringify(user.progress || defaultProgress()), trialDates(user.createdAt).trialStartedAt, trialDates(user.createdAt).trialEndsAt, 0]
      );
    }
  }

  const usersWithoutTrial = await all('SELECT id, createdAt FROM users WHERE trialStartedAt IS NULL OR trialEndsAt IS NULL');
  for (const user of usersWithoutTrial) {
    const dates = trialDates(user.createdAt);
    await run('UPDATE users SET trialStartedAt = ?, trialEndsAt = ? WHERE id = ?', [dates.trialStartedAt, dates.trialEndsAt, user.id]);
  }
}

function defaultProgress() {
  return {
    completedCourses: [],
    enrolledCourses: [],
    lessonsCompleted: 0,
    totalSpent: 0,
    badges: [],
    lastAccessed: new Date().toISOString()
  };
}

function publicUser(user) {
  return {
    id: user.id,
    fullname: user.fullname,
    email: user.email,
    phone: user.phone,
    createdAt: user.createdAt,
    progress: JSON.parse(user.progress || JSON.stringify(defaultProgress()))
  };
}

function accessForUser(user) {
  const paid = Number(user.paidAccess) === 1;
  const trialEndsAt = user.trialEndsAt;
  const trialActive = Boolean(trialEndsAt) && Date.now() < Date.parse(trialEndsAt);
  return {
    allowed: paid || trialActive,
    status: paid ? 'paid' : trialActive ? 'trial' : 'expired',
    trialStartedAt: user.trialStartedAt,
    trialEndsAt
  };
}

function requireAuth(req, res, next) {
  if (!req.session.userId) {
    return res.status(401).json({ success: false, message: 'Authentication required' });
  }
  next();
}

app.use(cors({ origin: process.env.FRONTEND_ORIGIN || true, credentials: true }));
app.use(bodyParser.json());
app.use(session({
  store: new SQLiteStore({ db: 'sessions.sqlite', dir: dataDirectory }),
  secret: process.env.SESSION_SECRET || 'development-only-change-me',
  resave: false,
  saveUninitialized: false,
  cookie: {
    httpOnly: true,
    sameSite: isProduction ? 'none' : 'lax',
    secure: isProduction,
    maxAge: 1000 * 60 * 60 * 24 * 7
  }
}));

// Registration endpoint
app.post('/api/register', async (req, res) => {
  try {
    const fullname = String(req.body.fullname || '').trim();
    const email = String(req.body.email || '').trim().toLowerCase();
    const password = String(req.body.password || '');
    const phone = String(req.body.phone || '').trim();

    if (!fullname || !email || password.length < 8) {
      return res.status(400).json({ success: false, message: 'Missing required fields' });
    }

    const existingUser = await get('SELECT id FROM users WHERE email = ?', [email]);
    if (existingUser) {
      return res.status(400).json({ success: false, message: 'Email already registered' });
    }

    const hashedPassword = await bcrypt.hash(password, 10);
    const newUser = {
      id: Date.now().toString(),
      fullname,
      email,
      password: hashedPassword,
      phone: phone || '',
      createdAt: new Date().toISOString(),
      progress: defaultProgress(),
      ...trialDates()
    };

    await run(
      'INSERT INTO users (id, fullname, email, password, phone, createdAt, progress, trialStartedAt, trialEndsAt, paidAccess) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
      [newUser.id, newUser.fullname, newUser.email, newUser.password, newUser.phone, newUser.createdAt, JSON.stringify(newUser.progress), newUser.trialStartedAt, newUser.trialEndsAt, 0]
    );

    res.status(201).json({ success: true, message: 'Account created successfully', userId: newUser.id });
  } catch (error) {
    console.error('Registration error:', error);
    res.status(500).json({ success: false, message: 'Server error during registration' });
  }
});

// Login endpoint
app.post('/api/login', async (req, res) => {
  try {
    const email = String(req.body.email || '').trim().toLowerCase();
    const password = String(req.body.password || '');

    if (!email || !password) {
      return res.status(400).json({ success: false, message: 'Email and password required' });
    }

    const user = await get('SELECT * FROM users WHERE email = ?', [email]);
    if (!user) {
      return res.status(401).json({ success: false, message: 'Invalid email or password' });
    }

    const passwordMatch = await bcrypt.compare(password, user.password);
    if (!passwordMatch) {
      return res.status(401).json({ success: false, message: 'Invalid email or password' });
    }

    req.session.userId = user.id;
    res.json({ success: true, message: 'Logged in successfully', user: publicUser(user) });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ success: false, message: 'Server error during login' });
  }
});

app.post('/api/logout', (req, res) => {
  req.session.destroy(() => {
    res.clearCookie('connect.sid');
    res.json({ success: true, message: 'Logged out successfully' });
  });
});

app.get('/api/session', requireAuth, async (req, res) => {
  try {
    const user = await get('SELECT * FROM users WHERE id = ?', [req.session.userId]);
    if (!user) {
      return res.status(401).json({ success: false, message: 'Session user not found' });
    }
    res.json({ success: true, user: publicUser(user) });
  } catch (error) {
    console.error('Session lookup error:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

app.get('/api/access', requireAuth, async (req, res) => {
  try {
    const user = await get('SELECT trialStartedAt, trialEndsAt, paidAccess FROM users WHERE id = ?', [req.session.userId]);
    if (!user) {
      return res.status(401).json({ success: false, message: 'Session user not found' });
    }
    res.json({ success: true, access: accessForUser(user) });
  } catch (error) {
    console.error('Access lookup error:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

app.get('/api/progress/:userId', requireAuth, async (req, res) => {
  try {
    if (req.params.userId !== req.session.userId) {
      return res.status(403).json({ success: false, message: 'Forbidden' });
    }
    const user = await get('SELECT progress FROM users WHERE id = ?', [req.session.userId]);

    if (!user) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }

    res.json({ success: true, progress: JSON.parse(user.progress) });
  } catch (error) {
    console.error('Error fetching progress:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// Save user progress
app.post('/api/progress/:userId', requireAuth, async (req, res) => {
  try {
    if (req.params.userId !== req.session.userId) {
      return res.status(403).json({ success: false, message: 'Forbidden' });
    }
    const { lessonsCompleted, completedCourses, enrolledCourses, totalSpent, badges } = req.body;
    const user = await get('SELECT progress FROM users WHERE id = ?', [req.session.userId]);
    if (!user) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }

    const progress = JSON.parse(user.progress);
    if (lessonsCompleted !== undefined) progress.lessonsCompleted = lessonsCompleted;
    if (completedCourses !== undefined) progress.completedCourses = completedCourses;
    if (enrolledCourses !== undefined) progress.enrolledCourses = enrolledCourses;
    if (totalSpent !== undefined) progress.totalSpent = totalSpent;
    if (badges !== undefined) progress.badges = badges;
    progress.lastAccessed = new Date().toISOString();

    await run('UPDATE users SET progress = ? WHERE id = ?', [JSON.stringify(progress), req.session.userId]);
    res.json({ success: true, message: 'Progress updated successfully' });
  } catch (error) {
    console.error('Error saving progress:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// Reset user progress
app.post('/api/progress/:userId/reset', requireAuth, async (req, res) => {
  try {
    if (req.params.userId !== req.session.userId) {
      return res.status(403).json({ success: false, message: 'Forbidden' });
    }
    const user = await get('SELECT id FROM users WHERE id = ?', [req.session.userId]);
    if (!user) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }

    await run('UPDATE users SET progress = ? WHERE id = ?', [JSON.stringify(defaultProgress()), req.session.userId]);
    res.json({ success: true, message: 'User progress reset successfully' });
  } catch (error) {
    console.error('Error resetting progress:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// Get user profile with all stats
app.get('/api/user/:userId', requireAuth, async (req, res) => {
  try {
    if (req.params.userId !== req.session.userId) {
      return res.status(403).json({ success: false, message: 'Forbidden' });
    }
    const user = await get('SELECT * FROM users WHERE id = ?', [req.session.userId]);

    if (!user) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }

    res.json({ success: true, user: publicUser(user) });
  } catch (error) {
    console.error('Error fetching user profile:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

initializeDatabase()
  .then(() => {
    app.listen(PORT, () => {
      console.log(`Seeds of Wealth backend running on http://localhost:${PORT}`);
      console.log(`SQLite database stored in ${databaseFile}`);
    });
  })
  .catch(error => {
    console.error('Database initialization error:', error);
    process.exit(1);
  });
