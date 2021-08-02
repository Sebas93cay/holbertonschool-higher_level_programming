#!/usr/bin/node

const argv = require('process').argv;

const numArg = argv.length;

if (numArg === 2) {
  console.log('No argument');
} else if (numArg === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
