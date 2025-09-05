const fs = require('fs');

function countStudents(path) {
  try {
    // Read file synchronously and split into lines
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split(/\r?\n/).filter((line) => line.trim() !== '');

    // Remove header and process student data
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

    // Display results
    console.log(`Number of students: ${students.length}`);
    Object.keys(fields).sort().forEach((field) => {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    });
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
