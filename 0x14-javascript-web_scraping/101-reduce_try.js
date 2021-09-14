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

  const characters = await charactersUlrs.reduce(async (prev, url) => {
    const name = await new Promise((resolve, reject) => {
      request(url, (err, response, body) => {
        if (err) reject(err);
        else {
          resolve(JSON.parse(body).name);
        }
      });
    });

    console.log('the prev is ', prev);
    return prev.concat([name]);
    // return [1, 2];
  }, []);

  console.log('los charaters son');
  console.log(characters);
  // characters.forEach(c => {
  // console.log(c);
  // })
};

main();
