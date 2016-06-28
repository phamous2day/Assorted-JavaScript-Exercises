var express = require('express');
var bodyParser = require('body-parser');
var fs = require('fs');
var app = express();

app.set('view engine', 'hbs');
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', function(request, response) {
  response.redirect('/HomePage');
});

app.get('/:pageName', function(request, response) {
  var pageName = request.params.pageName;
  var filename = 'pages/' + pageName + '.txt';
  fs.access(filename, fs.R_OK, function (err) {
    if (err) {
      response.render('placeholder.hbs', {
        title:pageName
      });
    } else {
      fs.readFile(filename, function (err, buffer){
        if (err) {
          response.statusCode = 500;
          response.send("sorry, problem reading file");
          return;
        }
        var content = buffer.toString();
        response.render(page.hbs {
          title: pageName,
          content: content
        }) ;
      });
    }
  });
  response.render('placeholder.hbs', {
    title: pageName
  });
});

app.get('/:pageName/edit', function(request, response) {
  var pageName = request.params.pageName;
  response.render('edit.hbs', {
    title: 'Edit ' + pageName,
    pageName: pageName
  });
});

app.post('/:pageName/save', function(request, response) {
  var pageName = request.params.pageName;
  var content = request.body.content;
  var filename = 'pages/' + pageName + '.txt';
  fs.writeFile(filename, content, function(err) {
    response.redirect('/' + pageName);
  });
});

app.listen(3000, function() {
  console.log('Listening on port 3000.');
});
