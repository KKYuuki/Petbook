import express from 'express';
import mysql from 'mysql2';
import bodyParser from 'body-parser';
import cors from 'cors';

const app = express();
const port = 5000; // You can choose any available port

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MySQL Database connection
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: 'kenneth', // Your MySQL password
  database: 'Petbook',  // Your database name
});

// Test MySQL connection
db.connect((err) => {
  if (err) {
    console.error('Database connection failed: ' + err.stack);
    return;
  }
  console.log('Connected to MySQL as id ' + db.threadId);
});

// POST endpoint for user signup
app.post('/signup', (req, res) => {
  const { username, email, password, name, bio, profilePicture } = req.body;

  // Check if the required fields are provided
  if (!username || !email || !password) {
    return res.status(400).json({ message: 'Username, Email, and Password are required!' });
  }

  const sql = 'INSERT INTO Users (Username, Email, Password, Name, Bio, ProfilePicture) VALUES (?, ?, ?, ?, ?, ?)';
  db.query(sql, [username, email, password, name, bio, profilePicture], (err, result) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ message: 'Database error' });
    }
    res.status(200).json({ message: 'User created successfully', userId: result.insertId });
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
