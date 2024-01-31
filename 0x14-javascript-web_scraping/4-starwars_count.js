#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error.message);
  } else if (response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;
    const wedgeMovies = filmsData.filter(film =>
      film.characters.some(character => character.endsWith(`/${characterId}`))
    );
    console.log(wedgeMovies.length);
  } else {
    console.error(`Error: Unexpected status code - ${response.statusCode}`);
  }
});
