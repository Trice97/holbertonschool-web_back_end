/**
 * Script that displays a welcome message,
 * reads user input from stdin,
 * prints the user's name,
 * and shows a closing message when input ends.
 */

//that first bloc incites the user to write his name
process.stdout.write(
   "Welcome to Holberton School, what is your name?\n")

//the second bloc listen to what is typed by the user and store it 
process.stdin.on("data",(data) => {
    const name =data.toString().trim();
    process.stdout.write(`Your name is: ${name}\n`);
    });

// this bloc display a message regarding the closure of the program
process.stdin.on("end", () => {
    process.stdout.write("This important software is now closing\n");
});