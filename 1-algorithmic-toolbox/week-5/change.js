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
		line = line.map(x => Number.parseInt(x, 10));
		const money = line[0];
		const coins = line.slice(1, money)
        DpChange(n);
        process.exit();
	}
	else console.log('enter something silly!');
}

function DpChange(money, coins) {

}