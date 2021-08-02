#!/usr/bin/node

const {
  argv
} = require('process');
argv[2] = argv[2].trim();
if (/^-?\d*\.?\d*$/.test(argv[2])) {
  console.log(`My number: ${argv[2].match(/^-?\d+/)[0]}`);
} else {
  console.log('Not a number');
}
