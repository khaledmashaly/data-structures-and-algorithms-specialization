'use strict';
const readline = require('readline');
process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

let items = [];
let lineNo = -1;
let n = 0;
let w = 0;
rl.on('line', readLine);
rl.on('close', knapsack);

function readLine(line) {
	line.trim();
	if (line !== '') {
		if (lineNo >= 0) {
			const value = line.split(' '),
				v = Number.parseInt(value[0], 10),
				w = Number.parseInt(value[1], 10);
			items[lineNo] = {
				v,
				w,
				vw: (v/w).toFixed(5)
			};
			if (lineNo === n-1) {
				rl.close();
			}
		}
		else {
			let nW = line.split(' ');
			n = Number.parseInt(nW[0], 10);
			w = Number.parseInt(nW[1], 10);
		}
		lineNo++;
	}
	else console.log('enter something silly!');
}

function knapsack() {
	items.sort((a, b) => b.vw - a.vw);
	let v = 0;
	const bag = function() {
		let a;
		for (let i = 0; i < n; i++) {
			if (w === 0) {
				return v;
			}
			a = Math.min(items[i].w, w);
			v += a*(items[i].vw);
			items[i] -= a;
			w -= a;
		}
		return v;
	};

	const value = bag();
	console.log(value.toFixed(5));
	process.exit();
}