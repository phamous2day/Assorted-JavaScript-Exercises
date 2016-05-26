var string = "Hi good morning"
var letterCounts = {};



for (var i = 0; i < string.length; i++) {
var char = string.charAt(i).toLowerCase();
if (!(char in letterCounts)){
letterCounts[char] = 0;
}
letterCounts[char] = letterCounts[char] +1;

}
for (var char in letterCounts) {
  var count = letterCounts[char];
  console.log(char + ": " + count);
}
