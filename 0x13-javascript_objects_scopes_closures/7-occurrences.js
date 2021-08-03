#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach(item => {
    if (item === searchElement) {
      counter++;
    }
  });
  return counter;
};
