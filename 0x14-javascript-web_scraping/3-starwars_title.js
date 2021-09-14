#!/usr/bin/node

const args = process.argv;
const request = require('request');

const episode = args[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + episode;

request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
