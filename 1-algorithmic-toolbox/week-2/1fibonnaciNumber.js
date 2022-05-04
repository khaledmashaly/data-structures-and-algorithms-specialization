'use strict';
const readline = require('readline');
process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

rl.on('line', readLine);

function readLine(line) {
	line.trim();
	if (line !== '') {
		let n = Number.parseInt(line, 10);
		let a = 0, b = 1;
		if (n === 0) {
			console.log(a);
			process.exit();
		}
		else if (n === 1) {
			console.log(b);
			process.exit();
		}
		let i = 1, c;
		while (i < n) {
			i++;
			c = b;
			b += a;
			a = c;
		}
		console.log(b);
		process.exit();
	}
}