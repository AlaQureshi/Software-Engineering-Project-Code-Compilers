const express = require('express');
const path = require('path');
const app = express();
const PORT = 3000;

// Serve static files from the project directory
app.use(express.static(path.join(__dirname)));

// Route to serve index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'pages/index.html'));
});

// Route to serve signup.html
app.get('/signup.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'pages/signup.html'));
});

// Route to serve login.html
app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'pages/login.html'));
});

// Route to serve dashboard.html
app.get('/dashboard.html', (req, res) => {
    res.sendFile(path.join(__dirname, 'pages/dashboard.html'));
});
// Route to serve profile.html
app.get('/profile', (req, res) => {
    console.log("Profile route hit");
    res.sendFile(path.join(__dirname, 'pages/profile.html'));
});


app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
