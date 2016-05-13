var phoneBook = {
  Dorothy: '913-438-3234',
  TinMan: '12344-438485938',
  CowardlyLion: '12345-28385'
};

var bookByPhoneNumber = {
  '913-438-3234': 'Dorothy',
  '12344-438485938': 'TinMan',
  '12345-28385': 'CowardlyLion'
};

var someonesName = "Dorothy";
var dorothysNumber = phoneBook[someonesName];
var alsoDorothysNumber = phoneBook.someonesName;
var someonesPhoneNumber = '12344-438485938';

var key;
for (key in phoneBook) {
  var phoneNumber = phoneBook[key];
  if (phoneNumber === someonesPhoneNumber) {
    console.log("Ah! That's " + key + "'s phone number!");
  }
}

phoneBook.ScareCrow = '12367-383831';
phoneBook.Dorothy = '12345-282384';
delete phoneBook.Dorothy;

console.log('something');

if ('Dorothy' in phoneBook) {
  
}
