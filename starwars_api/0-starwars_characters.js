#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

function printCharacters (characters, index) {
  if (index >= characters.length) return;
  request(characters[index], (err, res, body) => {
    if (err) return console.error(err);
    console.log(JSON.parse(body).name);
    printCharacters(characters, index + 1);
  });
}

request(url, (err, res, body) => {
  if (err) return console.error(err);
  printCharacters(JSON.parse(body).characters, 0);
});
