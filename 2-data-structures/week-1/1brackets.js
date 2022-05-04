'use strict';
let readline = require('readline');

process.stdin.setEncoding('utf8');
let rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

rl.on('line', readLine);

function readLine(line) {
	if (line !== "\n") {
		const code = line;
		const stack = [];
		const indeces = [];

		for (let i = 0; i < code.length; i++) {
				const char = code[i];
				if ( isOpeningBracket(char) ) {
					stack.push(char);
					indeces.push(i+1);
				}
				else if ( isClosingBracket(char) ) {
					if ( stack.length !== 0 ) {
						const test = stack.pop();
						switch (char) {
							case ']':
								if (test === '[') {
									break;
								}
								else {
									return console.log(i+1) || process.exit();
								}
							case '}':
								if (test === '{') {
									break;
								}
								else {
									return console.log(i+1) || process.exit();
								}
							case ')':
								if (test === '(') {
									break;
								}
								else {
									return console.log(i+1) || process.exit();
								}
						}
						indeces.pop();
					}
					else {
						return console.log(i+1) || process.exit();
					}
			}
		}



		function isOpeningBracket(char) {
			if (['[', '(', '{'].indexOf(char) !== -1) return true;
			return false;
		}

		function isClosingBracket(char) {
			if ([']', ')', '}'].indexOf(char) !== -1) return true;
			return false;
		}

		if ( stack.length !== 0) {
			return console.log(indeces[indeces.length-1]) || process.exit();
		}
		else {
			return console.log('Success') || process.exit();
		}
	}
}