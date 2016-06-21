// Adding 2 input values
// var input1 = Number(process.argv[2]);
// var input2 = Number(process.argv[3]);
// console.log(input1+input2);



// Adding all input values
var sum = 0;
for (var i = 2; i < process.argv.length; i++) {
  sum+=Number(process.argv[i]);

}
console.log (sum);
