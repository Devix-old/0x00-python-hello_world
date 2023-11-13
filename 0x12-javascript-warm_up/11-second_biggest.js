#!/usr/bin/node
const numbers = (process.argv.slice(2)).map(Number);

const max = Math.max(...numbers);
let secondMax = -Infinity;

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] > secondMax && numbers[i] < max) {
    secondMax = numbers[i];
  }
}
console.log(secondMax);
