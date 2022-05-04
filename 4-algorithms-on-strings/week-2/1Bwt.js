const readline = require('readline');


const bwt = function (text) {
	const chars = text.length;
	const cyclicRotations = [];
	for (let i = 0; i < chars; i++) {
		text = text[chars - 1] + text.slice(0, chars - 1);
		cyclicRotations.push(text);
	}
	cyclicRotations.sort();
	const bwt = cyclicRotations.reduce((acc, rotation) => acc + rotation[chars - 1], '');
	console.log(bwt);
	process.exit();
};


const readInput = function (line) {
	const text = line.trim();
	bwt(text);
};


const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
	terminal: false
});


rl.on('line', readInput);
