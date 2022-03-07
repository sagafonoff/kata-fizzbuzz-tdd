function shoutNumber(numberShouted) {
  if (numberShouted % 15 === 0) {
    return "FizzBuzz";
  } else if (numberShouted % 3 === 0) {
    return "Fizz";
  } else if (numberShouted % 5 === 0) {
    return "Buzz";
  }
  return numberShouted;
}

for (let counter = 0; counter < 100; counter++) {
  shoutNumber(counter);
}

export { shoutNumber };
