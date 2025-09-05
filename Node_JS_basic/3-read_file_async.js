const fs = require('fs').promises;

function countStudents(path) {
  // Return a Promise using fs.readFile (asynchronous)
  return fs.readFile(path, 'utf8')
    .then((data) => {
      // Same parsing logic as exercise 2
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

      // Display results (same as exercise 2)
      console.log(`Number of students: ${students.length}`);
      Object.keys(fields).sort().forEach((field) => {
        console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
      });
    })
    .catch(() => {
      // If file cannot be read, throw error
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
