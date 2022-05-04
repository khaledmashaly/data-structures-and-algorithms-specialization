const readline = require('readline');

process.stdin.setEncoding('utf8');
let rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

rl.on('line', readLine);

function readLine(line) {
	if (line !== "\n") {
		let n = line.split(' ');
		n[0] = Number.parseFloat(n[0], 10);
		n[1] = Number.parseFloat(n[1], 10);

		let a, b;
		if (n[0] > n[1])
			a = n[0], b = n[1];
		else
			a = n[1], b = n[0];

		while (b !== 0) {
			let c = a;
			a = b;
			b = c % b;
		}

		let gcd = a;
		console.log(`n[0]= ${n[0]}, n[1]= ${n[1]}`);
		lcm = n[0] * n[1];
		console.log(lcm);
		lcm /= gcd;

		console.log(lcm);
		process.exit();
	}
}