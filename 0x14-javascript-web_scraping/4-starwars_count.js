#!/usr/bin/node
// A script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const FILMS_URL = process.argv[2];
const count = 0;
request(FILMS_URL, (error, body, response) => {
	if (error) {
		console.log(error);
	} else {
		const results = JSON.parse(body).results;
		results.map((item) => {
			for (let i = 0; i < item.characters.length; i++) {
				if (item.characters[i].endsWith('18/')) {
					count += 1;
				}
			}
		});
		console.log(count);
	}
});
