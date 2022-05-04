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
		let F = [0, 1];
		for (let i = 2; i <= n; i++) {
			F[i] = (F[i-1] + F[i-2]) % 10;
		}
		console.log(F[n]);
		process.exit();
	}
}