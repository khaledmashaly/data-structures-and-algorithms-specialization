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
		line = line.split(' ');
		let n = Number.parseInt(line[0], 10);
		console.log(Number.isSafeInteger(99999999999999999));
		let m = Number.parseInt(line[1], 10);
		let period = [0,1];
		let i = 1;

		do {
			i++;
			let newPeriod = period[i-1] + period[i-2];
			period[i] = newPeriod < m ? newPeriod : newPeriod - m;
			console.log(period);
		} while(!(period[i] === 1 && period[i-1] === 0));

		period.splice(-2, 2);
		console.log(period);
		console.log('length = ' + period.length);
		console.log(n);
		n = n % period.length;
		console.log(n);
		let mod = period[n];

		console.log(mod);
		process.exit();
	}
}