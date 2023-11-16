#!/usr/bin/node

const args = process.argv.slice(2);

const fs = require('fs');

fs.readFile(args[0], 'utf8', (err1, data1) => {
  if (err1) {
    return;
  }

  fs.readFile(args[1], 'utf8', (err2, data2) => {
    if (err2) {
      return;
    }

    const content = data1 + data2;
    fs.writeFile(args[2], content, 'utf8', (err3) => {
    });
  });
});
