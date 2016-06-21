var fs = require('fs');
var contents = fs.readFileSync('hello.txt').toString();

var contentString  = contents.toString();
var contentUP = contentString.toUpperCase();
console.log(contentUP);
