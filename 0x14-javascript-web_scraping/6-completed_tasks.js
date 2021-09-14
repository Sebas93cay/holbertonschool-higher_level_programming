#!/usr/bin/node

const args = process.argv;
const request = require('request');

const url = args[2];

const main = async () => {
  const content = await new Promise((resolve, reject) => {
    request(url, (err, response, body) => {
      if (err) reject(err);
      else resolve(body);
    });
  });
  const toDos = JSON.parse(content);
  const doneByUserId = toDos.reduce((prev, toDo) => {
    if (toDo.completed) {
      if (toDo.userId in prev) {
        prev[toDo.userId.toString()]++;
      } else {
        prev[toDo.userId.toString()] = 1;
      }
    }
    return prev;
  }, {});
  console.log(doneByUserId);
};

main();
