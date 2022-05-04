'use strict';
const readline = require('readline');
process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

let lineNo = 1;
let n,a;
rl.on('line', readLine);

function readLine(line) {
	line.trim();
	if (line !== '') {
		if (lineNo === 1) {
			n = Number.parseInt(line, 10);
			lineNo++;
		}
		else {
			a = line.split(' ');
			for (let i = 0; i < a.length; i++) {
				a[i] = Number.parseInt(a[i], 10);
			}
			maxProduct(n, a);
		}
	}
	else console.log('enter something silly!');
}

function maxProduct(n, a) {
	let i = -1, j = -1;

	for (let k = 0; k < a.length; k++) {
		if (i === -1 || a[k] > a[i]) i = k;
	}

	for (let k = 0; k < a.length; k++) {
		if (k !== i && (j === -1 || a[k] > a[j])) j = k;
	}

	console.log(a[i] * a[j]);
	process.exit();
}