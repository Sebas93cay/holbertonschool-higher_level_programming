#!/usr/bin/node

const { argv } = require('process');

const factorial = function (a) {
  if (!a || isNaN(a) || a <= 1) {
    return 1;
  }
  return a * factorial(a - 1);
};

console.log(factorial(parseInt(argv[2])));
