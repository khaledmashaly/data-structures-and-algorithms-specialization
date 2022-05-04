#python3
n, m = [int(i) for i in input().split(' ')]
g = [[] for i in range(n)]
for i in range(m):
	u, v = [int(i) for i in input().split(' ')]
	g[u - 1].append(v - 1)

print(n + 3 * m, n * 2)
for u in range(n):
	ux = 2 * u + 1
	uy = 2 * u + 2
	print(ux, uy, 0)
	for v in g[u]:
		vx = 2 * v + 1
		vy = 2 * v + 2
		print(-ux, -vx, -uy, -vy, 0)
		print(ux, vx, 0)
		print(uy, vy, 0)

# print(n * 3, 4 * n + 7 * m)
# for u in range(n):
# 	ux = 3 * u
# 	ur = ux + 1
# 	ug = ux + 2
# 	ub = ux + 3
# 	print(ur, ug, ub, 0)
# 	print(-ur, -ug, 0)
# 	print(-ur, -ub, 0)
# 	print(-ug, -ub, 0)
# 	for v in g[u]:
# 		vx = 3 * v
# 		vr = vx + 1
# 		vg = vx + 2
# 		vb = vx + 3
# 		print(-vr, -vg, -vb, 0)
# 		print(-vr, -vg, ub, 0)
# 		print(-vr, ug, ub, 0)
# 		print(ur, -vg, -vb, 0)
# 		print(ur, ug, -vb, 0)
# 		print(ur, -vg, ub, 0)
# 		print(-vr, ug, -vb, 0)
