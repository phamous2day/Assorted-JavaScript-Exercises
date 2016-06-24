var fs = require('fs');
var express = require('express');
var app = express();

// Parser is for my form, it turns form input into JSON
var bodyParser = require('body-parser');



app.use(bodyParser.urlencoded({ extended: false }));
app.set('view engine', 'hbs');
app.use(express.static('public'));

app.get('/', function(req, res){
res.render('about.hbs', {
  title: "Aloha, e komo mai",
  content: "Welcome to my portfolio site"
});
});

app.get('/about2', function (request, response) {
  response.render('about2.hbs');
});
app.get('/projects', function (request, response) {
  response.render('projects.hbs');
});
app.get('/contact', function (request, response) {
  response.render('contact.hbs');
});
app.get('/thankyou', function (request, response) {
  response.render('thankyou.hbs');
});
app.post('/thankyou', function(request, response) {
  var data = request.body;
  console.log("Data is ",data);
  fs.appendFile('messages.txt', JSON.stringify(data), function (err) {
    if (err) throw err;
      console.log('Contact form has been saved');
});
  response.render("thankyou.hbs");
});



app.listen(3000, function(){
  console.log("This is my portfolio site listening on port 3000!");
});
