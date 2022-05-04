#python3
from math import factorial
from itertools import combinations

def c(n, r):
	return factorial(n) / factorial(n - r) / factorial(r)

n, m = [int(i) for i in input().split(' ')]
g = [[] for i in range(n)]
for i in range(m):
	u, v = [int(i) for i in input().split(' ')]
	g[u - 1].append(v - 1)
	g[v - 1].append(u - 1)

clausses = []

# 1) each vertex belongs to a path
for i in range(n):
	clausses.append([])
	for j in range(1, n + 1):
		xij = n * i + j
		clausses[-1].append(xij)
	clausses[-1].append(0)

# 2) each vertex appears just once in a path
for i in range(n):
	for j in combinations(range(1, n + 1), 2):
		xij = n * i + j[0]
		yij = n * i + j[1]
		clausses.append([-xij, -yij, 0])

# 3) each position in a path is occupied by some vertex
for j in range(1, n + 1):
	clausses.append([])
	for i in range(n):
		xij = n * i + j
		clausses[-1].append(xij)
	clausses[-1].append(0)

# 4) no two vertices occupy the same position of a path
for j in range(1, n + 1):
	for i in combinations(range(n), 2):
		xij = n * i[0] + j
		yij = n * i[1] + j
		clausses.append([-xij, -yij, 0])

# 5) two successive vertices on a path must be connected by an edge
for i in range(n):
	u = g[i]
	for j in range(n):
		if j != i and j not in u:
			for k in range(n - 1):
				xij = n * k + i + 1
				yij = n * (k + 1) + j + 1
				clausses.append([-xij, -yij, 0])

print(len(clausses), n ** 2)
for clauss in clausses:
	print(*clauss)
