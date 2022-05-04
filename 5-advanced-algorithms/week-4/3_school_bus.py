n, m = [int(i) for i in input.split()]
d = [[0] * n for i in range(n)]

for i in range(m):
	u, v, t = [int(i) for i in input.split()]
	d[u - 1][v - 1] = d[v - 1][u - 1] = t

c = [[[0] * n] for i in range(2 ** n)]

c[1][0] = 0
