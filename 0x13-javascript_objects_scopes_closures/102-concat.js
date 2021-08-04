#!/usr/bin/node

const argv = require('process').argv;
const fs = require('fs');

main(argv);
function main (argv) {
  if (argv.length === 5) {
    let dataA, dataB;
    try {
      dataA = fs.readFileSync(argv[2], 'utf8');
    } catch (err) {
      console.log(err);
    }
    try {
      dataB = fs.readFileSync(argv[3], 'utf8');
    } catch (err) {
      console.log(err);
    }
    const dataC = dataA + dataB;
    fs.writeFileSync('./' + argv[4], dataC);
  }
}
