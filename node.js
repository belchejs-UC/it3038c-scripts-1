var path = require("path");

console.log("directory name: " + __dirname);
console.log("directory and file name: " + __filename);

console.log("Using PATH module:");
console.log(`Hello from file ${path.basename(__filename)}`);

console.log(`Process args: ${process.argv}`);
