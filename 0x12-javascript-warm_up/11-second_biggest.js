#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

if (numbers.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...numbers);
  const secondMax = Math.max(...numbers.filter(num => num !== max));
  console.log(secondMax);
}
