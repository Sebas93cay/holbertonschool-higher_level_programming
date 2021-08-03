#!/usr/bin/node

exports.esrever = function (list) {
  const l = list.length;
  for (let i = 0; i < l; i++) {
    const tmp = list[l - i - 1];
    list[l - i] = list[i];
    list[i] = tmp;
  }
  return list;
};
