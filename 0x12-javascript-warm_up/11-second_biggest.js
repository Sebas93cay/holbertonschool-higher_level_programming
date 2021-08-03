#!/usr/bin/node

const { argv } = require('process');

let biggest = NaN;
let secondBiggest = NaN;

for (let n of argv.slice(2)) {
  n = parseInt(n);
  if (n > biggest || isNaN(biggest)) {
    secondBiggest = biggest;
    biggest = n;
  } else if (isNaN(secondBiggest) || (n > secondBiggest && n != biggest)) {
    secondBiggest = n;
  }
}

console.log(secondBiggest);
