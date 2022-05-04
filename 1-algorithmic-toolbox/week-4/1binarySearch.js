'use strict';
/* const readline = require('readline');
process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

let lineNo = -1;
let a = [];
rl.on('line', readLine);

function readLine(line) {
	line.trim();
	if (line !== '') {
        lineNo++;
        line = line.split(' ').map(x => Number.parseInt(x, 10));
		if (lineNo === 0) {
            let n = line[0];
            a = line.slice(1, n+1);
		}
		else {
            let k = line[0];
            let b = line.slice(1, k+1);
            rl.close();
            binarySearch(a, 0, a.length - 1, b);
            process.exit();
		}
	}
	else console.log('enter something silly!');
} */

stressTest();
process.exit();

function linearSearch(a, keys) {
    let ans = [];
    for (let key of keys) {
        ans.push(a.indexOf(key));
    }
    // return console.log(ans);
    return ans;
}

function binarySearch(a, low, high, key) {
    let match = [];
    let mid = 0, Bk = 0, An = 0;
    const globalLow = low, globalHigh = high;
    let matchFound = false;
    for (let i = 0; i < key.length; i++) {
        matchFound = false;
        low = globalLow, high = globalHigh;
        while (low <= high) {
            mid = Math.floor(low + (high-low)/2);
            Bk = key[i];
            An = a[mid];
           /* {
                console.log('low= ' + low);
                console.log('high= ' + high);
                console.log('mid= ' + mid);
                console.log('Bk= ' + Bk);
                console.log('An= ' + An);
                console.log('a= ' + a);
                console.log('key= ' + key);
            } */
            if (key[i] === a[mid]) {
                match.push(mid);
                matchFound = true;
                break;
            }
            else if (key[i] < a[mid]) {
                high = mid - 1;
            }
            else {
                low = mid + 1;
            }
            /* for (var j = 0; j < 1000000000; j++); */
        }
        if (!matchFound) {
            match.push(-1);
        }
    }
    // return console.log(match.join(' '));
    return match;
}

function rand(l, h) {
    return Math.floor(( Math.random() * (h-l) ) + l);
}

function stressTest(a, b) {
    while(true) {
        const n = rand(3, 100000);
        console.log(`n = ${n}`);

        let a = [];
        for (let i = 0; i < n; i++) {
            let r = -1;
            do {
                r = rand(0, 1000000000);
            }
            while (a.indexOf(r) !== -1);
            a.push(r);
        }
        a = a.sort((a,b) => a-b);
        let aJoined = a.join(' ');
        console.log(`a = ${aJoined}`);

        const k = rand(3, 100000);
        console.log(`k = ${k}`);

        let b = [];
        for (let i = 0; i < k; i++) {
            b.push(rand(0, 1000000000));
        }
        let bJoined = b.join(' ');
        console.log(`b = ${bJoined}`);

        let linearResult = linearSearch(a, b);
        let binaryResult = binarySearch(a, 0, a.length - 1, b);

        linearResult = linearResult.join(' ');
        binaryResult = binaryResult.join(' ');

        if (linearResult !== binaryResult) {
            console.log(`linearResult = ${linearResult}`);
            console.log(`binaryResult = ${binaryResult}`);
            break;
        }
        else {
            console.log('correct');
        }
    }
}