#!/usr/bin/node

const args = process.argv;
const request = require('request');
const fs = require('fs');

const url = args[2];
const filePath = args[3];

const main = async () => {
  const content = await new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) reject(err);
      else resolve(body);
    });
  });
  fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) console.log(err);
  });
};

main();
