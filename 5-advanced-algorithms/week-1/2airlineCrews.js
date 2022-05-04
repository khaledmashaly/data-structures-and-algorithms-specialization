const readline = require('readline');

process.stdin.setEncoding('utf8');
const rl = readline.createInterface({
	input: process.stdin
});

class Node {
	/**
	 * class representing a graph node
	 * @param {number} key - node id
	 */
	constructor(key) {
		this.key = key;
		this.edges = [];
		this.prevNode = null;
		this.prevEdge = null;
		this.visited = false;
	}

    /**
     * connect an edge from this node to another node
     * @param {Node} node - destination node to connect to
     * @param {number} capacity - maximum flow inside edge
	 * @param {Edge} [origin] - original edge in a residual network
	 * @param {boolean} [reverse] - indicates if edge is reversed
     */
	connect(node, capacity = 1, origin, reverse) {
		this.edges.push(new Edge(node, capacity, origin, reverse));
	}

	toString() {
		return `Node(${this.key})
	prevNode: ${this.prevNode ? this.prevNode.key : null}
	prevEdge: ${this.prevEdge ? this.prevEdge.capacity : null}
	visited: ${this.visited}`;
	}
}

class Edge {
    /**
     * class representing a weighted edge connecting two nodes in a graph
     * @param {Node} dest - destination of edge
     * @param {number} capacity - maximum flow possible
	 * @param {Edge} [origin=null] - original edge in a residual network
	 * @param {boolean} [reverse=false] - indicates if edge is reversed
     */
	constructor(dest, capacity, origin = null, reverse = false) {
		this.dest = dest;
		this.capacity = capacity;
		this.flow = 0;
		this.origin = origin;
		this.reverse = reverse;
	}

	toString() {
		return `\t----${this.capacity}----> (${this.dest.key})`;
	}
}


const printGraph = (g) => {
	console.log('\n\n\n');
	for (let i = 0; i < g.length; i++) {
		console.log(g[i].toString());
		for (let j = 0; j < g[i].edges.length; j++) {
			console.log(g[i].edges[j].toString());
		}
		console.log('\n');
	}
	console.log('\n\n\n');
};


/**
 * construct the residual network of a graph
 * @param {array<Node>} g - a graph to construct its residual network
 * @param {number} n - number of nodes in graph
 * @return {array<Node>}
 */
const residualNetwork = (g, n) => {
	let resNet = new Array(n);
	for (let i = 0; i < n; i++) {
		resNet[i] = new Node(i);
	}

	for (let i = 0; i < n; i++) {
		const edges = g[i].edges;
		for (let j = 0; j < edges.length; j++) {
			const currentEdge = edges[j];
			const destNode = currentEdge.dest.key;
			const resFlow = currentEdge.capacity - currentEdge.flow;
			if (resFlow) { // create normal edge
				resNet[i].connect(resNet[destNode], resFlow, currentEdge);
			}
			if (currentEdge.flow) { // create reverse edge
				resNet[destNode].connect(resNet[i], currentEdge.flow, currentEdge, true);
			}
		}
	}

	// printGraph(resNet);

	return resNet;
};


/**
 * breadth-first traversal of a graph using first node as origin
 * @param {array<Node>} g - graph to traverse
 * @return {array<Node>}
 */
const bfs = (g) => {
	for (let i = 0; i < g.length; i++) {
		g[i].prevNode = null;
		g[i].prevEdge = null;
		g[i].visited = false;
	}
	const s = g[0];
	s.visited = true;

	const queue = [s];
	while (queue.length > 0) {
		const v = queue.shift();
		for (let edge of v.edges) {
			const w = edge.dest;
			if (edge.capacity > 0 && !w.visited) {
				queue.push(w);
				w.visited = true;
				w.prevNode = v;
				w.prevEdge = edge;
			}
		}
	}

	return g;
};


/**
 * calculate minimum possible flow increase in the path from s to t
 * @param {Node} s - source node
 * @param {Node} t - destination node
 * @return {number}
 */
const minimumCapacity = (s, t) => {
	let x = Infinity;
	while (t !== s) {
		x = Math.min(x, t.prevEdge.capacity);
		t = t.prevNode;
	}
	return x;
};


/**
 * calculate new flow inside edges along path from s to t
 * @param {array<Node>} g - graph to calculate new flow
 * @param {array<Node>} rn - residual network of g
 * @param {number} x - minimum allowable flow increase from s to t
 */
const recaculateFlow = (g, rn, x) => {
	const s = rn[0];
	let t = rn[rn.length - 1];
	while (t !== s) {
		const edge = t.prevEdge;
		if (edge.reverse) {
			edge.origin.flow -= x;
		}
		else {
			edge.origin.flow += x;
		}
		t = t.prevNode;
	}
};


/**
 * calculate max flow in a graph
 * @param {array<Node>} g - graph to calculate max flow
 * @param {number} n - number of nodes in graph
 * @return {number}
 */
const match = (g, n) => {
	let f = 0;
	for (; ;) {
		let resNet = residualNetwork(g, n);
		// printGraph(resNet);
		resNet = bfs(resNet); // calculate shortest path
		// printGraph(resNet);
		const s = resNet[0]; // source city
		const t = resNet[resNet.length - 1]; // destination city
		if (!t.visited) return f;
		const x = minimumCapacity(s, t);
		recaculateFlow(g, resNet, x);
		f += x;
	}
};


const input = (function* () {
	const [n, m] = (yield).trim().split(' ').map(Number);
	const graph = new Array(n + m + 2);

	for (let i = 0; i < n + m + 2; i++) {
		graph[i] = new Node(i);
	}

	/* connect source to flights */
	for (let i = 1; i <= n; i++) {
		graph[0].connect(graph[i]);
	}

	/* connect crews to destination */
	for (let i = n + 1; i <= n + m; i++) {
		graph[i].connect(graph[n + m + 1]);
	}

	/* connect flights to crews */
	for (let i = 1; i <= n; i++) {
		const crews = (yield).trim().split(' ').map(Number);
		for (let j = 0; j < m; j++) {
			crews[j] && graph[i].connect(graph[n + 1 + j]);
		}
	}

	rl.close();
	const f = match(graph, n + m + 2);

	let result = new Array(n);
	for (let flight = 1; flight <= n; flight++) {
		const edges = graph[flight].edges;
		let crew = -1;
		for (let edge of edges) {
			if (edge.flow) {
				crew = edge.dest.key - n;
				break;
			}
		}
		result[flight - 1] = crew;
	}
	console.log(...result);
})();

input.next();

rl.on('line', (line) => {
	input.next(line);
});
