#!/usr/bin/node

const argv = require('process').argv;


const factorial = a => {
  if (!a || isNaN(a) || a <= 0) {
    return 1;
  }
  return a * factorial(a - 1);
};

console.log(factorial(parseInt(argv[2])));
