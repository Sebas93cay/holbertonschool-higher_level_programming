#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = args[2];

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const json = JSON.parse(body);
    const movieCounter = json.results.reduce((prev, movie) => {
      if (movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        return prev + 1;
      } else {
        return prev;
      }
    }, 0);
    console.log(movieCounter);
  }
});
