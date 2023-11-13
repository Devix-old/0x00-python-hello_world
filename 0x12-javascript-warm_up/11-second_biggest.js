#!/usr/bin/node
let numbers = (process.argv.slice(2)).map(Number);

max = Math.max(...numbers);
let second_max = -Infinity;

for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] > second_max && numbers[i] < max) {
        second_max = numbers[i];
  }
}    
console.log(second_max);
