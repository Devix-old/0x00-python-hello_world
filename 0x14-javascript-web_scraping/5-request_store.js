#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, 'utf-8', (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    return;
  }
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
