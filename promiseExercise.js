// var express = require('express');
// var app = express();
// var session = require('express-session');
//
// var mongoose = require('mongoose');
// var User = require('./user');
//
// app.use(bodyParser.json());
//
// mongoose.connect('mongodb://localhost/students');
//
// // Ex.1
// Student.findOne({ name: 'Matt' })
//   .then(function(matt) {
//     console.log('We found matt:', matt);
//   });
//   if (err) return handleError(err);
//   console.log('%s %s is a %s.', person.name.first, person.name.last, person.occupation) // Space Ghost is a talk show host.
// })


//This is wiki in Promise style:

// var mongoose = require('mongoose');
// mongoose.connect('mongodb://localhost/wiki');
//
// var Page = mongoose.model('Page', {
//   _id: String,
//   content: String
// });
//
// Page.findById('HomePage') {
//   .then(function(page) {
//   page.content = 'Welcome to my grand wiki!';
//   return page.save();
//   })
//   .then(function(page) {
//         console.log('Success!');
//   })
//   .catch(function(err) {
//     console.error(err.message);
// });



//This is fs md.js exercise:

var fs = require('fs-promise');
var marked = require('marked-promise');
fs.readFile('exercises.md')
  .then(function(buffer){
    var contents = buffer.toString();
    var html = marked(contents);
    return html;
  })
  .then(function(html){
    console.log("Wrote README.html");
    return fs.writeFile('README.html', html);
  })
  .catch(function(err) {
    console.error(err.message);
  });
