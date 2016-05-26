function hello () {
console.log('Hello');
}

function callTheFunction3times (fun) {
  fun();
  fun();
  fun();

}
callTheFunction3times (hello);
