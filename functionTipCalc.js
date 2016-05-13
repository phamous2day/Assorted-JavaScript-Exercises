function LevelofService (Total, rateofservice){

   if (rateofservice== "good") {
    Total= (Total* 1.20);
  }
   else if (rateofservice== "fail") {
    Total = (Total* 1.15);
  }

  else if (rateofservice== "bad") {
    Total= (Total* 1.10);
  }


  console.log("Your total price with tip is " + Total);
}


// var Total = 10;
// var rateofservice = "good"
var Total = prompt("Enter the Total price of your bill");
var rateofservice = prompt("Enter your rate of service: good, fail, or bad");
LevelofService (Total, rateofservice);
