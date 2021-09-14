#!/usr/bin/node

const fs = require('fs');

const args = process.argv;

const filePath = args[2];
const content = args[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) console.log(err);
});
