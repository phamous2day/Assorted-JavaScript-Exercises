
var button = document.getElementById('button');
// var button = $('#button');
console.log(button);

console.log('Button said: ' + button.textContent);
// button.text();
button.textContent = 'Click please!';
// button.text('Click please!');

button = document.querySelector('button');
// $('button')
console.log('Found button', button);

var buttons = document.querySelectorAll('button');
// querySelectorAll returns a NodeList, which
// works like an array, but has additional
// methods.
// $('button')

console.log('Found buttons', buttons);

for (var i = 0; i < buttons.length; i++) {
  console.log('Button ' + i + ': ', buttons[i]);
}

/*
jQuery saves you from having to write a loop
over multiple elements on a page.
$('button').click(function () {
  console.log('you clicked');
});
*/

buttons = document.getElementsByTagName('button');
buttons = document.getElementsByClassName('btn');

console.log('buttons with class btn: ', buttons);

/*
Manipulation
*/

var list = document.getElementById('list');
var li = document.createElement('li');
// var li = $('<li>')
li.textContent = 'Three';
list.appendChild(li);
// $(list).append(li);

var image = document.getElementById('image');
image.setAttribute('src', 'dom-exercises/img1.jpg');
// $('#image').attr('src', 'dom-exercises/img1.jpg');

var imageUrl = image.getAttribute('src');
// var imageUrl = $(image).attr('src');
console.log('Image url is: ', imageUrl);


var content = document.getElementById('content');
content.innerHTML = '<a href="http://google.com">Google</a>';
// $('#content').html('<a href="http://google.com">Google</a>');

console.log('HTML in #content is ' + content.innerHTML);

var bodyTag = document.body;
bodyTag.style.backgroundColor = 'yellow';
bodyTag.style['background-color'] = 'yellow';
// $('body').css({ backgroundColor: 'yellow' });
// $('body').css('backgroundColor', 'yellow');
// $('body').css('background-color', 'yellow');

content.style.border = '2px solid green';
// $(content).css({ border: '2px solid green' });

var li = document.querySelector('li');
li.classList.add('selected');
// $('li').addClass('selected');

if (li.classList.contains('selected')) {
  // $(li).hasClass('selected')
  console.log('Yes it is selected.');
} else {
  console.log('No it isn\'t selected.');
}
li.classList.remove('selected');
// $(li).removeClass('selected')

if (li.classList.contains('selected')) {
  console.log('Yes it is selected.');
} else {
  console.log('No it isn\'t selected.');
}

var input = document.getElementById('text-field');

input.value = 'Hello';
// $(input).val('Hello');
console.log('Input value is ' + input.value);
// $(input).val()

var googleLink = document.querySelector('#content a');

googleLink.addEventListener('click', function(event) {
  event.preventDefault();
  alert('You tried to go to google');
});
/*
$('#content a').click(function(event) {
  event.preventDefault();
  alert('You tried to go to google');
})
*/

var removeButtons = document.querySelectorAll('#todo button');

for (var i = 0; i < removeButtons.length; i++) {
  removeButtons[i].addEventListener('click', function(event) {
    var button = event.target;
    // event.target is the element the event happened to
    // In jQuery that is `this`
    var li = button.parentNode;
    // var li = button.parent();
    var list = li.parentNode;
    list.removeChild(li);
    // li.remove();
  });
}
/*
$('#todo button').click(function() {
  var li = $(this).parent();
  li.remove();
});
*/
var todoList = document.getElementById('todo');
var taskLi = document.createElement('li');
taskLi.textContent = 'Watch TV';
var removeButton = document.createElement('button');
removeButton.textContent = 'remove';
taskLi.appendChild(removeButton);

todoList.appendChild(taskLi);

/*
$('#todo').on('click', 'button', function() {

});
*/

todoList.addEventListener('click', function(event) {
  var target = event.target;
  var li = button.parentNode;
  var list = li.parentNode;
  list.removeChild(li);
});
/*
$('#todo').on('click', 'button', function(event) {
  $(this).parent().remove();
});
*/


window.addEventListener('load', function() {
  console.log('Page has loaded');
});
// or
window.onload = function() {
  console.log('Page has loaded');
};

/*
$(document).ready(function () {
  console.log('Page has loaded');
});

or

$(function() {
  console.log('Page has loaded');
});
*/






// Exercise: implement recoginition for Konami code
