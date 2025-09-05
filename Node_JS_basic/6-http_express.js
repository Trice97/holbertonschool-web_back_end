const express = require('express');

// Create Express application
const app = express();

// Define route for homepage
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Start server on port 1245
app.listen(1245);

module.exports = app;
