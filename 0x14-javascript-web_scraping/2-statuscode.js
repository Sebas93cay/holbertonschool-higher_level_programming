#!/usr/bin/node
// This script prints the status code of a GET request

const args = process.argv;
const request = require('request');

const url = args[2];

request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
