#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const URL = process.argv[2];
const file = process.argv[3];
let request = require('request');
let fs = require('fs');

request(URL, (error, body, response) => {
	if (error) {
		console.log(error);
	} else {
		const content = JSON.parse(body);
		fs.writeFile(file, content, 'utf8');
	}
});
