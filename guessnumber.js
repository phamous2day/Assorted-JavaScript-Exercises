// debugger;
var mynumber = 10;
var turns = 0;


while (turns <2)
{var guess = Number(prompt("Guess the number I'm thinking"));
  if (guess == mynumber) {
      alert('You guessed my number!');
      break;
  } else if (guess < mynumber) {
      alert('Your guess is too low. Try again.');
      turns++
  } else if (guess > mynumber) {
      alert('Your guess is too high. Try again.');
      turns++
  }
}
