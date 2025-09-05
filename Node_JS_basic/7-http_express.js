const express = require('express');
const fs = require('fs').promises;

// Function to count students (same logic as before)
function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split(/\r?\n/).filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const fields = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (firstname && field) {
          const cleanField = field.trim();
          const cleanFirstname = firstname.trim();
          if (!fields[cleanField]) fields[cleanField] = [];
          fields[cleanField].push(cleanFirstname);
        }
      });

      let result = `Number of students: ${students.length}\n`;
      Object.keys(fields).sort().forEach((field) => {
        result += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      });

      return result.trim();
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

// Create Express application
const app = express();

// Route for homepage
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Route for students
app.get('/students', (req, res) => {
  const databaseFile = process.argv[2];

  countStudents(databaseFile)
    .then((studentData) => {
      res.send(`This is the list of our students\n${studentData}`);
    })
    .catch(() => {
      res.send('This is the list of our students\nCannot load the database');
    });
});

// Start server on port 1245
app.listen(1245);

module.exports = app;
