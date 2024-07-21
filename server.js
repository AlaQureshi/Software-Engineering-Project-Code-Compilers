const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const sqlite3 = require('sqlite3').verbose();
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const path = require('path');

const app = express();
const PORT = 3000;
const secretKey = 'job_search_portal_secret_key';

// Middleware
app.use(bodyParser.json());
app.use(cookieParser());

// Create a DB connection
const db = new sqlite3.Database('./database.db');

// Create users table if it doesn't exist
db.run(`CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL,
  user_type TEXT NOT NULL CHECK(user_type IN('JOB_SEEKER', 'EMPLOYER'))
)`);

// Signup route
app.post('/signup', (req, res) => {
    const { username, password, userType } = req.body;
    const hashedPassword = bcrypt.hashSync(password, 10);

    db.run(`INSERT INTO users (username, password, user_type) VALUES (?, ?, ?)`, [username, hashedPassword, userType], function (err) {
        if (err) {
            return res.status(500).json({ message: `Error occurred: ${err}` });
        }
        res.status(200).json({ message: 'User registered successfully.' });
    });
});

// Login route
app.post('/login', (req, res) => {
    const { username, password } = req.body;

    db.get(`SELECT * FROM users WHERE username = ?`, [username], (err, user) => {
        if (err || !user) {
            return res.status(401).json({ message: 'Invalid username' });
        }

        const isPasswordValid = bcrypt.compareSync(password, user.password);
        if (!isPasswordValid) {
            return res.status(401).json({ message: 'Invalid password' });
        }

        const token = jwt.sign({ id: user.id }, secretKey, { expiresIn: '1h' });
        res.status(200).json({ token });
    });
});

// Middleware to protect routes
const authenticateJWT = (req, res, next) => {
    const token = req.cookies.token;
    if (!token) {
        return res.sendStatus(403);
    }

    jwt.verify(token, secretKey, (err, user) => {
        if (err) {
            return res.sendStatus(403);
        }

        req.user = user;
        next();
    });
};

// Serve static files from the project directory
app.use(express.static(path.join(__dirname)));

// Route to welcome page
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'pages/index.html'));
});

// Route to serve signup.html
app.get('/signup', (req, res) => {
    res.sendFile(path.join(__dirname, 'pages/signup.html'));
});

// Route to serve login.html
app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'pages/login.html'));
});

// Route to serve dashboard.html
app.get('/dashboard', authenticateJWT, (req, res) => {
    res.sendFile(path.join(__dirname, 'pages/dashboard.html'));
});

// Route to serve profile.html
app.get('/profile', (req, res) => {
    console.log("Profile route hit");
    res.sendFile(path.join(__dirname, 'pages/profile.html'));
});

// Start express app
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
