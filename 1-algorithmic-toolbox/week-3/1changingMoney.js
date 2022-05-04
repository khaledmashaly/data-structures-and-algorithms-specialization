'use strict';
let readline = require('readline');

process.stdin.setEncoding('utf8');
let rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

rl.on('line', readLine);

function readLine(line) {
	if (line !== "\n") {
		let m = Number.parseInt(line, 10);
		let change = [10, 5, 1];
		let n = 0;

		for (let i = 0; i < change.length; i++) {
			let changed = Math.floor(m / change[i]);
			m %= change[i];
			n += changed;
			if (m != 0) continue;
			else break;
		}

		console.log(n);
		process.exit();
	}
}