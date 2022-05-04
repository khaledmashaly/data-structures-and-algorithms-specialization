const readline = require('readline');


const bwtInverse = function (bwt) {
	const chars = bwt.length;
	bwt = bwt.split('');
	let originalWord = [bwt[0]];
	bwt = bwt.map((char, i) => [char, i]);
	const firstColumn = bwt.slice().sort((a, b) => {
		if (a[0] < b[0]) {
			return -1;
		}
		if (a[0] > b[0]) {
			return 1;
		}
		else {
			if (a[1] < b[1]) {
				return -1;
			}
			if (a[1] > b[1]) {
				return 1;
			}
		}
		return 0;
	});
	let currentChar = bwt[0];
	for (let i = 0; i < chars - 2; i++) {
	//while (currentChar[0] !== '$') {
		const nextCharIndex = firstColumn.indexOf(currentChar);
		const nextChar = bwt[nextCharIndex];
		originalWord.unshift(nextChar[0]);
		currentChar = nextChar;
	}
	console.log(originalWord.join('') + '$');
	process.exit();
};


const readInput = function (line) {
	const bwt = line.trim();
	bwtInverse(bwt);
};


const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
	terminal: false
});


rl.on('line', readInput);
