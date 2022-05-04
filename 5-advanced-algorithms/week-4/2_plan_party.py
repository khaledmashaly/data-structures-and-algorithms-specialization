#python3
import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

def main():
	n = int(input())
	g = [[] for _ in range(n)]
	f = [int(i) for i in input().split(' ')]
	children = [0] * n
	for i in range(n - 1):
		u, v = [int(i) for i in input().split(' ')]
		g[u - 1].append(v - 1)
		children[u - 1] = children[u - 1] + 1

	d = [float('inf') for _ in range(n)]
	def fun_party(v, parent):
		if d[v] == float('inf'):
			if children[v] == 0:
				d[v] = f[v]
			else:
				x = f[v]
				for u in g[v]:
					for w in g[u]:
						x += fun_party[w]
				y = 0
				for w in g[v]:
					y += fun_party[w]
				d[v] = max(x, y)
		return d[v]

	root = None
	for i in range(n):
		if children[i] == 0:
			root = i
			break

	print(fun_party(root))

# This is to avoid stack overflow issues
threading.Thread(target=main).start()
