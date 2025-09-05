/**
 * Script that displays a welcome message,
 * reads user input from stdin,
 * prints the user's name,
 * and shows a closing message when input ends.
 */

// Print the initial question when the program starts
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Event listener: triggered whenever the user provides input
process.stdin.on('data', (data) => {
  // Convert the input buffer to string and remove extra spaces/newlines
  const name = data.toString().trim();

  // Print the formatted message with the user's name
  process.stdout.write(`Your name is: ${name}\n`);
});

// Event listener: triggered when the input stream ends (Ctrl+D or pipe finished)
process.stdin.on('end', () => {
  // Print the closing message before the program exits
  process.stdout.write('This important software is now closing\n');
});
