#!/usr/bin/node

const argv = require('process').argv;

if (!argv[2]) {
  console.log('No argument');
} else {
  for (const arg of argv.slice(2)) {
    console.log(arg);
  }
}
