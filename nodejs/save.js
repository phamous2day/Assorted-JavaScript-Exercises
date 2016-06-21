var fs = require('fs');
var inputText = process.argv[2];
for (var i = 2; i < process.argv.length; i++) {
  inputText+=String(process.argv[i]);

}



fs.writeFile('hello.txt', inputText, function (err) {
  if (err) return console.log(err);
  console.log('Hello World > hello.txt');
});
