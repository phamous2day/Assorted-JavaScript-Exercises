const cows = require('cows');

cows();


var fs = require('fs');
var contents = fs.readFileSync('cows.txt').toString();
console.log(contents);
