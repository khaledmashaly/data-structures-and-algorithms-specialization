const readline = require('readline');


let lineNo = 0;
let text = '';
let n = 0;
const patterns = [];


class Node {
	constructor(key) {
		this.key = key;
		this.edges = [];
		this.prefix = false;
	}
}


class Edge {
	constructor(label, next_node) {
		this.label = label;
		this.next = next_node;
	}
}


const constructTrie = function () {
	let trie = [new Node(0)];
	let node;
	for (let pattern of patterns) {
		node = trie[0];
		for (let char of pattern) {
			const match = node.edges.find(edge => edge.label === char);
			if (match === undefined) {
				const new_node = new Node(trie.length);
				trie.push(new_node);
				const new_edge = new Edge(char, new_node);
				node.edges.push(new_edge);
				node = new_edge.next;
			}
			else {
				node = match.next;
			}
		}
		node.prefix = true;
	}
	trieMatching(trie);
};


const prefixTrieMatching = function (string, trie) {
	const string_match = string;
	let symbol = string_match.shift();
	let v = trie[0];
	while (v.edges.length > 0 && !v.prefix) {
		const match = v.edges.find(edge => edge.label === symbol);
		if (match !== undefined) {
			symbol = string_match.shift();
			v = match.next;
		}
		else
			return false;
	}
	return true;
};


const trieMatching = function (trie) {
	const string = text.split('');
	const runs = string.length;
	const matches = [];
	for (let i = 0; i < runs; i++) {
		const match = prefixTrieMatching(string.slice(i), trie);
		if (match)
			matches.push(i);
	}
	console.log(...matches);
	process.exit();
};


const readInput = function (line) {
	lineNo++;
	if (lineNo === 1) {
		text = line.trim();
	}
	else if (lineNo === 2) {
		n = Number.parseInt(line.trim(), 10);
	}
	else {
		const pattern = line.trim();
		patterns.push(pattern);
		if (patterns.length === n) {
			constructTrie();
		}
	}
};


const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
	terminal: false
});


rl.on('line', readInput);
