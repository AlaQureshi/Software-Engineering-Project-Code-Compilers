# Job Search Portal by Software-Engineering-Project-Compiler-Crew

## How to Run <br>

1. Install Node & NPM following https://nodejs.org/en/download/package-manager

2. Run `npm i` to install dependencies in package.json from NPM on the root folder

3. Run `npm run start` to start the web server in your local on the root folder

4. Access http://localhost:3000/ on your browser

## Pages
- localhost:3000/ (Job Board Page)

- localhost:3000/login (Login Page)

- localhost:3000/dashboard (Job Board Page - temporary)

## Datastore
- All data are stored in Sqlite3 which exists in database.db in the root folder 
```
TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    user_type ENUM('JOB_SEEKER', 'EMPLOYER') NOT NULL
)
```

## User Authentication
Once user is logged in successfully, the user's JWT is stored in the user's browser Cookies with key name "token"