'use strict';
const readline = require('readline');
process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

let lineNo = -1;
let n = 0;
rl.on('line', readLine);

function readLine(line) {
	line.trim();
	if (line !== '') {
        lineNo++;
		if (lineNo === 0) {
            n = Number.parseInt(line, 10);
		}
		else {
            let a = line.split(' ');
            rl.close();
            // console.log(a);
            majorityElement(a, n);
            process.exit();
		}
	}
	else console.log('enter something silly!');
}

function majorityElement(elements, n) {
    // console.log(a);
    let sorter = {};
    for (let e of elements) {
        sorter[e] = sorter[e] ? sorter[e] + 1 : 1;
        if (sorter[e] > n/2) return console.log(1);
    }
    return console.log(0);
}