// count lines of code
// count characters

// pseudo code
// 1. open the file
// 2. count the number of lines taken up by code (use split to ?? array of lines)
// 3. count the amount of characters
// 4. Print out the amount of lines, the amount of characters

var fs = require('fs');
var contents = fs.readFileSync('hello.txt').toString();

var lines = contents.split("\n").length;


console.log("Number of characters are " + contents.length);
console.log("Number of lines are " + lines);


// Extra thought-process
// function countChar() {
//   var sum = 0;
//   for (var i = 0; i < contents.length; i++) {
//     // sum+=Number(contents[i]);
//   }
//   return sum;
//   console.log(sum);
// }
// console.log();
// console.log("Number of character is ")



// Toby's way:
// var fs = require('fs');
// var filename = process.argv[2];
// fs.readFileSync(filename, function (err, buffer) {
//   var contents = buffer.toString();
//   var charCount = contents.length;
//   var lines = contents.split('\n');
//
//   console.log(lines)
// });
