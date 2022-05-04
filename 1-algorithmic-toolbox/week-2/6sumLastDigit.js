let readline = require('readline');

process.stdin.setEncoding('utf8');
let rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

rl.on('line', readLine);

function readLine(line) {
	if (line !== "\n") {
		let n = parseInt(line, 10);
		let a = 0, b = 1;
		for (let i = 2; i <= n; i++) {
			let c = b;
			b = a + c;
			a = c;
			b = b < 10 ? b : b - 10;
			console.log(a);
			console.log(b);
			console.log(c);
		}
		console.log(b);
		process.exit();
	}
}