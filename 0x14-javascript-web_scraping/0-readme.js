#!/usr/bin/node
// A script that reads and prints the content of a file

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf8', (error, contnet) => {
	if (error) {
		console.log(error);
	} else {
		console.log(contnet);
	}
});
