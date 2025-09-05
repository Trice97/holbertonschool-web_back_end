const http = require('http');
const fs = require('fs').promises;

// Function to count students (same logic as exercise 3)
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

// Create HTTP server with routing
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const databaseFile = process.argv[2];

    countStudents(databaseFile)
      .then((studentData) => {
        res.end(`This is the list of our students\n${studentData}`);
      })
      .catch(() => {
        res.end('This is the list of our students\nCannot load the database');
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
