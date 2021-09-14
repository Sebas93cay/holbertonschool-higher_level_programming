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

  const names = [];
  for (const url of charactersUlrs) {
    const name = await new Promise((resolve, reject) => {
      request(url, (err, response, body) => {
        if (err) reject(err);
        else {
          const character = JSON.parse(body);
          resolve(character.name);
        }
      });
    });
    names.push(name);
  }
  names.forEach(name => {
    console.log(name);
  });
};

main();
