#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = args[2];

request(url, (err, response) => {
  if (err) console.log(err);
  else console.log(`code: ${response.statusCode}`);
});
