var express = require('express');
var mongoose = require('mongoose');
var bcrypt = require('bcrypt-as-promised');
var bodyParser = require('body-parser');
mongoose.connect('mongodb://localhost/coffee-store');

var User = mongoose.model('User', {
  _id: String,
  encryptedPassword: String
});

var app = express();
app.use(bodyParser.json());

function formatMongooseError(err) {
  var message = err.message + '. ';
  if (err.errors) {
    message +=
    Object.keys(err.errors).map(function(key) {
      return err.errors[key].message;
    }).join(' ');
  }
  return message;
}

app.post('/register', function(request, response) {
  var info = request.body;

  bcrypt.hash(info.password, 10)
  .then(function(encryptedPassword) {
    // 2. Create a user in the DB
    return User.create({
      _id: info.username,
      encryptedPassword: encryptedPassword
    },
    .then(function(user) {
      response.json({
        status: 'ok'
      });
      .catch(function(err) {
        var message = formatMongooseError(err);
        response.json){
          status: 'fail',
        error: message
      });
      });
    }
  );
});
