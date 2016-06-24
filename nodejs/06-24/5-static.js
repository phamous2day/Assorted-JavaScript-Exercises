var express = require('express');
var app = express();

app.set('view engine', 'hbs');
app.use(express.static('public'));

app.get('/', function (req, res) {
  res.render('hello.hbs', {
    title: 'This is my Awesome Title!',
    content: 'Hello, world!',
    name: "DigitalCrafts"
  });
});


app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
