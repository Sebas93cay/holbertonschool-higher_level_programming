#!/usr/bin/node

exports.esrever = function (list) {
  const l = list.length;
  const listC = list.slice(0);
  for (let i = 0; i < Math.floor(l / 2); i++) {
    const tmp = listC[l - i - 1];
    listC[l - i - 1] = listC[i];
    listC[i] = tmp;
  }
  return listC;
};
