'use strict';
const readline = require('readline');
process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

let lineNo = -1;
let a = '';
rl.on('line', readLine);

function readLine(line) {
	line.trim();
	if (line !== '') {
	  lineNo++;
		if (lineNo === 0) {
		a = line;
		}
		else {
		let b = line;
		rl.close();
		// console.log(a);
		editDistance(a, b);
		process.exit();
		}
	}
	else console.log('enter something silly!');
}

function editDistance(a, b) {
    const n = a.length;
    const m = b.length;
    let d = [];
    for (let i = 0; i <= n; i++) {
	    if (i === 0) {
		    d[i] = [];
		    for (let j = 0; j <= m; j++) {
                d[0][j] = j;
		    }
        }
        else {
            d[i] = [i];
        }
    }
    // console.log(d);
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= m; j++) {
            let insertion = d[i][j-1] + 1;
            let deletion = d[i-1][j] + 1;
            let match = d[i-1][j-1];
            let mismatch = d[i-1][j-1] + 1;
            /* if (i === 2 && j === 2) {
                console.log('insertion='+insertion);
                console.log('deletion='+deletion);
                console.log('match='+match);
                console.log('mismatch='+mismatch);
                console.log(a[i]);
            } */
            if (a[i-1] === b[j-1]) {
                d[i][j] = Math.min(insertion, deletion, match);
            }
            else {
                d[i][j] = Math.min(insertion, deletion, mismatch);
            }
        }
    }
    // console.log(d);
    return console.log(d[n][m]);
}