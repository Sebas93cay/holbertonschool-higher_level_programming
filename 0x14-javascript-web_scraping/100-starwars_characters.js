#!/usr/bin/node

const args = process.argv;
const request = require('request');

const movieId = args[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

const main = async () => {
  const charactersUlrs = await new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) reject(err);
      else {
        const movie = JSON.parse(body);
        resolve(movie.characters);
      }
    });
  });
  charactersUlrs.forEach(url => {
    request(url, (err, response, body) => {
      if (err) console.log(err);
      else {
        console.log(JSON.parse(body).name);
      }
    });
  });
};

main();
