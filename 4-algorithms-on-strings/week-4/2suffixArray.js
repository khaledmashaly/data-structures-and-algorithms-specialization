const readline = require('readline');


const sortChars = s => {
	const map = { '$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4 };
	const count = [0, 0, 0, 0, 0];
	const order = [];
	for (let i = 0; i < s.length; i++) {
		const c = map[s[i]];
		count[c]++;
	}
	for (let i = 1; i < count.length; i++) {
		count[i] += count[i-1];
	}
	for (let i = s.length - 1; i >= 0; i--) {
		const c = map[s[i]];
		count[c]--;
		order[count[c]] = i;
	}
	return order;
};


const computeCharClass = (s, order) => {
	let classes = [];
	classes[order[0]] = 0;
	for (let i = 1; i < s.length; i++) {
		if (s[order[i]] === s[order[i-1]]) {
			classes[order[i]] = classes[order[i-1]];
		}
		else {
			classes[order[i]] = classes[order[i-1]] + 1;
		}
	}
	return classes;
};


const sortDoubled = (s, L, order, classes) => {
	let newOrder = [];
	let count = new Array(s.length).fill(0);
	for (let i = 0; i < s.length; i++) {
		count[classes[i]]++;
	}
	for (let i = 1; i < count.length; i++) {
		count[i] += count[i-1];
	}
	for (let i = s.length - 1; i >=0; i--) {
		const start = (order[i] - L + s.length) % s.length;
		const cl = classes[start];
		count[cl]--;
		newOrder[count[cl]] = start;
	}
	return newOrder;
};


const updateClasses = (newOrder, classes, L) => {
	const n = newOrder.length;  // sequence size
	let newClasses = [];
	newClasses[newOrder[0]] = 0;
	for (let i = 1; i < n; i++) {
		const cur = newOrder[i];
		const prev = newOrder[i-1];
		const mid = (cur + L) % n;
		const midPrev = (prev + L) % n;
		if ( classes[cur] !== classes[prev] || classes[mid] !== classes[midPrev] ) {
			newClasses[cur] = newClasses[prev] + 1;
		}
		else {
			newClasses[cur] = newClasses[prev];
		}
	}
	return newClasses;
};


const buildSuffixArray = (s) => {
	let order = sortChars(s);
	let classes = computeCharClass(s, order);
	let L = 1;

	while (L < s.length) {
		order = sortDoubled(s, L, order, classes);
		classes = updateClasses(order, classes, L);
		L *= 2;
	}

	console.log(...order);
	process.exit();
};


const readInput = function (line) {
	const sequence = line.trim();
	buildSuffixArray(sequence);
};


const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
	terminal: false
});


rl.on('line', readInput);