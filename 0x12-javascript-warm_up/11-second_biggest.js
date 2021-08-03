#!/usr/bin/node

const { argv } = require('process');

let biggest = NaN;
let secondBiggest = NaN;

for (const n of argv.slice(2)) {
  if (n > biggest || isNaN(biggest)) {
    secondBiggest = biggest;
    biggest = n;
  } else if (isNaN(secondBiggest) || n > secondBiggest) {
    secondBiggest = n;
  }
}

console.log(secondBiggest);
