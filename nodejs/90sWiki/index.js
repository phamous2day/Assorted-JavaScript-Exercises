var express = require('express');
var bodyParser = require('body-parser');
var fs = require('fs');
var session = require('express-session');
var wikiLinkify = require('wiki-linkify');
var app = express();
var marked = require('marked');

app.use(session({
  secret: 'magiczebra',
  cookie: {
    maxAge: 24 * 60 * 60000
  }
}));
app.set('view engine', 'hbs');
app.use(bodyParser.urlencoded({ extended: false }));

app.get('/', function(request, response) {
  response.redirect('/HomePage');
});

app.get('/login', function(request, response) {
  response.render('login.hbs', {
    title: 'Login'
  });
});

app.get('/logout', function(request, response) {
  request.session.user = null;
  response.redirect('/');
});

app.post('/login-submit', function(request, response) {
  var credentials = request.body;
  if (credentials.username === 'Toby' &&
      credentials.password === 'abc') {
    request.session.user = credentials.username;
    response.redirect(request.session.requestUrl);
  } else {

    response.redirect('/');
  }
});

app.get('/:pageName', function(request, response) {
  var pageName = request.params.pageName;
  var filename = 'pages/' + pageName + '.txt';
  var user = request.session.user;
  fs.access(filename, fs.R_OK, function(err) {
    if (err) {
      // cannot read, rendering place holder page
      response.render('placeholder.hbs', {
        title: pageName
      });
    } else {
      fs.readFile(filename, function(err, buffer) {
        if (err) {
          response.statusCode = 500;
          response.send('Sorry, problem reading file.');
          return;
        }
        var content = buffer.toString();
        var wikiContent = wikiLinkify(content);
        response.render('page.hbs', {
          title: pageName,
          content: marked(wikiContent),
          pageName: pageName,
          user: user
        });
      });
    }
  });

});

function authRequired(request, response, next) {
  if (!request.session.user) {
    request.session.requestUrl = request.url;
    response.redirect('/login');
  } else {
    next();
  }
}

app.get('/:pageName/edit', authRequired, function(request, response) {
  var pageName = request.params.pageName;
  var filename = 'pages/' + pageName + '.txt';
  fs.readFile(filename, function(err, buffer) {
    var content;
    if (err) {
      content = '';
    } else {
      content = buffer.toString();
    }

    response.render('edit.hbs', {
      title: 'Edit ' + pageName,
      pageName: pageName,
      content: content
    });
  });

});

app.post('/:pageName/save', authRequired, function(request, response) {
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
