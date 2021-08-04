#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

for (const [k, v] of Object.entries(dict)) {
  if (v in newDict) {
    newDict[v].push(k);
  } else {
    newDict[v] = [k];
  }
}

console.log(newDict);
