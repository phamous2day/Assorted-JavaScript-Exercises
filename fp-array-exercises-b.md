# FP Array Exercise B

## Leetspeak

Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

```
A => 4
E => 3
G => 6
I => 1
O => 0
S => 5
T => 7
```

Example: LEET => l337

Hint: you can convert a string to an array of characters with .split('')



var str = "DO YOU SPEAK LEET?";

var mapping = {
  A: "4",
  E: "3",
  G: "6",
  I: "1",
  O: "0",
  S: "5",
  T: "7",
};

var letters = str.split('');
var changedLetters = letters.map(function(letter) {
if (mapping[letter]) {
  return mapping [letter];
}
else{
  return letter;
}
});

var result = changedLetters.join("");



## Basketball Players

Given an array of objects representing basketball players:

```
var players = [
  {
    name: 'Paul Millsap',
    position: 'PF',
    avgMinutesPlayed: 36,
    avgPoints: 16.4,
    avgRebounds: 9.4,
    starter: true
  },
  {
    name: 'Jeff Teague',
    position: 'PG',
    avgMinutesPlayed: 28.6,
    avgPoints: 15.6,
    avgRebounds: 1.9,
    starter: true
  },
  {
    name: 'Al Horford',
    position: 'C',
    avgMinutesPlayed: 32,
    avgPoints: 13.2,
    avgRebounds: 6.8,
    starter: true
  },
  {
    name: 'Kent Bazemore',
    position: 'SF',
    avgMinutesPlayed: 31.8,
    avgPoints: 12,
    avgRebounds: 6.6,
    starter: true
  },
  {
    name: 'Kyle Korver',
    position: 'SG',
    avgMinutesPlayed: 32.4,
    avgPoints: 11.2,
    avgRebounds: 4.9,
    starter: true
  },
  {
    name: 'Dennis Schroder',
    position: 'PG',
    avgMinutesPlayed: 18.3,
    avgPoints: 10.7,
    avgRebounds: 1.8,
    starter: false
  },
  {
    name: 'Kris Humphries',
    position: 'PF',
    avgMinutesPlayed: 14.7,
    avgPoints: 9.7,
    avgRebounds: 5.7,
    starter: false
  },
  {
    name: 'Mike Scott',
    position: 'PF',
    avgMinutesPlayed: 17.6,
    avgPoints: 7.0,
    avgRebounds: 3.6,
    starter: false
  },
  {
    name: 'Thabo Sefolosha',
    position: 'SF',
    avgMinutesPlayed: 18.9,
    avgPoints: 4.8,
    avgRebounds: 3.9,
    starter: false
  },
  {
    name: 'Mike Muscala',
    position: 'PF',
    avgMinutesPlayed: 7.4,
    avgPoints: 2.7,
    avgRebounds: 1.9,
    starter: false
  },
  {
    name: 'Tim Hardaway Jr.',
    position: 'SG',
    avgMinutesPlayed: 9.7,
    avgPoints: 2.2,
    avgRebounds: 1.0,
    starter: false
  },
  {
    name: 'Lamar Patterson',
    position: 'SG',
    avgMinutesPlayed: 5.0,
    avgPoints: 1.5,
    avgRebounds: 1.3,
    starter: false
  },
  {
    name: 'Kirk Hinrich',
    position: 'SG',
    avgMinutesPlayed: 4.5,
    avgPoints: 0.8,
    avgRebounds: 0.7,
    starter: false
  }
];
```

1. Write a function that takes the players array and returns a new array containing only the starters.

var starterStatus = players.filter(function (player) {
  return player.starter;
});
  console.log(starterStatus);



2. Write a function that takes the players array and returns only the point guards (position = 'PG').

var positionStatus = players.filter(function (player) {
  return player.position ==="SG";
});
  console.log(positionStatus);




3. Write a function that takes the players array and returns a new array containing the names of each player.

var playersName = players.map(function (player) {
  return player.name;

});

 console.log(playersName);


4. Write a function that takes the players array and returns a new array
containing the names of the starters.

var positionStatus = players.filter(function (player) {
  if(player.position ==="SG";)
  return player.name
});





5. Write a function that takes the players array and returns a new array containing the names of the point guards.


var positionStatus = players.filter(function (player) {
  if( player.position ==="PG") {
    return player.name;  
  }
});

 console.log(positionStatus);





6. Write a function that takes the players array and returns the sum of the avgPoints for each player.

var positionStatus = players.map(function (player) {
  if(player.position ==="SG";)
  return player.name
});



7. Write a function that takes the players array and returns the sum of the avgPoints of the starters.


var avgTeamPoints = players.reduce(function (sum, player) {
  return sum + player.avgPoints;
}, 0);
console.log('Average team points:  ' + avgTeamPoints)

8. Write a function that takes the players array and returns true if each player gets at leas 10 minutes of average playing time, and returns false otherwise


var starterPoints = players.filter(function(player) {
  return player.starter;
})
.reduce(function(sum, player){
  return sum + player.avgPoints;
  }0);





9. Write a function that takes the players array and returns true if each starter gets at least 30 minutes of average playing time, and returns false otherwise


var startersGet30Minutes = starters.every(function(player) {
  return player.avgMinutesPlayed > 30;
  })


10. Write a function that takes the players array and returns a tally object. The tally object should count the number of players in each position. It should look like:

        {
          PG: 2,
          SG: 4,
          PF: 3,
          SF: 3,
          C: 1
        }


        var positions = players.map(function(player){
return player.position;

          }).reduce(function(tally, position){
if (!tally[position]) {
  tally[position] = 1;
}
            else {
              tally[position] +=1;
            }
            return tally;
            }, {});

              console.log(positions);

## Bonus

* Write your own map implementation
* Write your own filter implementation
* Write your own reduce implementation
* Rewrite filter using reduce
* Write your own every implementation using reduce