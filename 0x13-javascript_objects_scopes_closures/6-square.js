#!/usr/bin/node

const sq = require('./5-square');

const Square = class extends sq {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};

module.exports = Square;
