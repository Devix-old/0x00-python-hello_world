#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request(url, 'utf-8', (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    return;
  }

  let i = 0;
  body = JSON.parse(body);

  for (const film of body.results) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        i++;
      }
    }
  }

  console.log(i);
});
