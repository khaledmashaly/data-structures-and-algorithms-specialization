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
        const n = Number.parseInt(line, 10);
        primitiveCalculator(n);
        process.exit();
	}
	else console.log('enter something silly!');
}

function primitiveCalculator(n) {
    if (n === 1) {
        return console.log(0) || console.log(1);
    }
    else if (n) {
        
    }
    let primitives = {
        addOne(n) {
            return n + 1;
        },
        multiplyTwo(n) {
            return 2 * n;
        },
        multiplyThree(n) {
            return 3 * n;
        }
    };
    return console.log(primitives.multiplyThree(n));
}