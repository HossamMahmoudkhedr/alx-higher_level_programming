#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const FILMS_URL = process.argv[2];
const PEOPLE_URL = '';
request(FILMS_URL, (error, body, response) => {
	if (error) {
		console.log(error);
	} else {
		PEOPLE_URL = JSON.parse(body).characters[17];
	}
});

if (PEOPLE_URL) {
	request(PEOPLE_URL, (error, body, response) => {
		if (error) {
			console.log(error);
		} else {
			console.log(JSON.parse(body).films.length);
		}
	});
}
