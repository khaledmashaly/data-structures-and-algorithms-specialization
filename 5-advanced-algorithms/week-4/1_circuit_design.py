# python3
import sys
import threading
from collections import defaultdict

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

def main():
	v, c = [int(i) for i in input().split(' ')]
	g = [[] for _ in range(2 * v)]
	gr = [[] for _ in range(2 * v)]
	visited = [False for _ in range(2 * v)]
	scc = [0] * (2 * v)
	scc_dict = defaultdict(list)
	stack = []
	value = [0] * (2 * v)

	def node(var):
		if var < 0:
			return - var - 1
		elif var > 0:
			return var + v - 1

	def dfs(start: int):
		if not visited[start]:
			visited[start] = True
			for u in g[start]:
				dfs(u)
			stack.append(start)

	def dfs(start: int):
		if not visited[start]:
			visited[start] = True
			for u in g[start]:
				dfs(u)
			stack.append(start)


	def dfsr(start: int, sccn: int):
		if not visited[start]:
			visited[start] = True
			scc[start] = sccn
			scc_dict[sccn].append(start)
			for u in gr[start]:
				dfsr(u, sccn)

	for _ in range(c):
		i, j = [int(x) for x in input().split(' ')]
		g[node(-i)].append(node(j))
		g[node(-j)].append(node(i))
		gr[node(j)].append(node(-i))
		gr[node(i)].append(node(-j))

	for x in range(2 * v):
		if not visited[x]:
			dfs(x)

	visited = [False] * (2 * v)

	sccn = 0
	while len(stack) > 0:
		x = stack.pop()
		if not visited[x]:
			sccn += 1
			dfsr(x, sccn)

	for x in range(1, v + 1):
		if scc[node(x)] == scc[node(-x)]:
			print('UNSATISFIABLE')
			exit()
	else:
		print('SATISFIABLE')

	for x in reversed(range(1, sccn + 1)):
		for y in scc_dict[x]:
			if value[y] == 0:
				value[y] = 1
				value[(y + v) % (2 * v)] = -1

	print(*[x * y for x, y in zip(range(1, v + 1), value[v:])])

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
