#!/usr/bin/node

const {
  argv
} = require('process');

if (argv[2] === undefined) {
  console.log('No argument');
} else {
  for (const arg of argv.slice(2)) {
    console.log(arg);
  }
}
