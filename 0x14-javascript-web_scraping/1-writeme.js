#!/usr/bin/node
// A script that writes a string to a file.

const file = process.argv[2];
const content = process.argv[3];

const fs = require('fs');

fs.writeFile(file, content, 'utf8', (error) => {
	if (error) {
		console.log(error);
	}
});
