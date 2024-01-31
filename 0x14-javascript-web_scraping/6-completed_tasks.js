#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, 'utf-8', (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    return;
  }
  const dict = {};
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      dict[task.userId] = (dict[task.userId] || 0) + 1;
    }
  }
  console.log(dict);
});
