var fs = require('fs');
var contents = fs.readFileSync('hello.txt').toString();
console.log(contents);


// Another way to write it
// var contents = require("fs").readFileSync('hello.txt').toString();
//
// console.log(contents);
