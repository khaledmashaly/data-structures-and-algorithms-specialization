'use strict';
const readline = require('readline');
process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
	input: process.stdin,
	terminal: false
});

let lineNo = -1;
let n = 0;
rl.on('line', readLine);

function readLine(line) {
	line.trim();
	if (line !== '') {
		lineNo++;
		if (lineNo === 1) {
			let tree = line.split(' ');
			rl.close();
			tree = tree.map(function (parent, index) {
				return new Node(parent, index);
			});
			let parent = -1;
			while (tree.length !== sorted.length) {
				tree.reduce(function);
			}
			console.log(tree);
			process.exit();
		}
	}
	else console.log('enter something silly!');
}

function Node(parent, index) {
	this.parent = parent;
	this.index = index;
}

function calcHeight(tree) {

}