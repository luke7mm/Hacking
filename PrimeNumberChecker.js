//Javascript program mostly copied from
//https://www.programiz.com/javascript/examples/prime-number
//Most of this work is not my own
//Program is accurate under one million

//Game to check if number inputted is prime.

//Number inputted
const number = parseInt(prompt("Please input your number to check if it is prime."));
let isPrime = true;


if (number === 1) {
  console.log("1 is neither prime nor composite number.")
}

else if (number > 1) {

  for (let i = 2; i < number; i++) {
    if (number % i == 0) {
      isPrime = false;
      break;
    }
  }

  if (isPrime) {
    console.log(`${number} is a prime number`);
  } else {
    console.log(`${number} is not a prime number`);
  }
}

//check if number is less than 1
else {
  console.log("The number is not a prime number.");
}




