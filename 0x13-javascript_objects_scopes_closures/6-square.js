#!/usr/bin/node
const FirstSquare = require('./5-square.js');
class Square extends FirstSquare {
	charPrint(c) {
		const char = c === undefined ? 'X' : c;
		let square = '';
		for (let i = 0; i < this.height; i++) {
			for (let j = 0; j < this.width; j++) {
				square += char;
			}
			square += '\n';
		}
		console.log(square);
	}
}

const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');

module.exports = Square;
