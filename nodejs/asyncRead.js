var fs = require('fs');
var contents = fs.readFile('hello.txt', function(err, buffer) {
  if (err) {
    console.log("Error:", err);
    return;
  }
console.log("Got Data: ", buffer);
});

console.log("This happened first");
