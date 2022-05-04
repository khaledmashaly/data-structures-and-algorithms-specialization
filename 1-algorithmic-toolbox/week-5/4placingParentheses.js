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
        rl.close();
        let s = line.split('');
        let d = s.filter(x => !isNaN(x))
                 .map(x => Number.parseInt(x, 10));
        let op = s.filter(x => isNaN(x));
        parentheses(d, op);
        process.exit();
	}
	else console.log('enter something silly!');
}

function parentheses(d, op) {
    const n = d.length;
    let m = [];
    let M = [];
    for (let i = 0; i < n; i++) {
        m[i] = [];
        m[i][i] = d[i];
        M[i] = [];
        M[i][i] = d[i];
    }
    for (let s = 0; s <= n-1; s++) {
        for (let i = 0; i < n-s; i++) {
            let j = i + s;
            [ m[i][j], M[i][j] ] = minAndMax(i, j, m, M, op);
            /* console.log('m',m);
            console.log('M',M); */
        }
    }
    return console.log(M[0][n-1]);
}

function minAndMax(i, j, m, M, op) {
    let min = Infinity;
    let max = -Infinity;
    for (let k = i; k <= j-1; k++) {
        /* console.log('M[i][k]='+M[i][k]);
        console.log('m[i][k]='+m[i][k]);
        console.log('M[k+1][j]='+M[k+1][j]);
        console.log('m[k+1][j]='+M[k+1][j]); */
        let a = calc(op[k], M[i][k], M[k+1][j]);
        let b = calc(op[k], M[i][k], m[k+1][j]);
        let c = calc(op[k], m[i][k], M[k+1][j]);
        let d = calc(op[k], m[i][k], m[k+1][j]);
        min = Math.min(min, a, b, c, d);
        max = Math.max(max, a, b, c, d);
    }
    return min === Infinity ? [ m[i][j], M[i][j] ] : [ min, max ];
}

function calc(op, x, y) {
    switch (op) {
        case '*':
            return x * y;
        case '+':
            return x + y;
        case '-':
            return x - y;
        default:
            throw 'wrong operator';
    }
}