#!/usr/bin/node
// A script that display the status code of a GET request.

const URL = process.argv[2];

let request = require('request');
request(URL, (error, response, body) => {
	if (error) {
		console.log('error:', error);
	} else {
		console.log('code:', response && response.statusCode);
	}
});
