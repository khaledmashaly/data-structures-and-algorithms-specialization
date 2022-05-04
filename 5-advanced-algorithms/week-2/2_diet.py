#python3
from itertools import combinations
from math import fsum, isfinite, isclose

def gauss(m):
	lead = 0
	row_count = len(m)
	column_count = len(m[0])
	for r in range(row_count):
		if lead >= column_count:
			return
		i = r
		while m[i][lead] == 0:
			i += 1
			if i == row_count:
				i = r
				lead += 1
				if lead == column_count:
					return
		m[i], m[r] = m[r], m[i]
		el = m[r][lead]
		m[r] = [x / float(el) for x in m[r]]
		for i in range(row_count):
			if i != r:
				el = m[i][lead]
				m[i] = [mi - el * mr for mi, mr in zip(m[i], m[r])]
		lead += 1

if __name__ == "__main__":
	n, m = [int(i) for i in input().split(' ')]
	a = [[float(i) for i in input().split(' ')] for _ in range(n)]
	b = [float(i) for i in input().split(' ')]
	p = [float(i) for i in input().split(' ')]

	a.append([1.0] * m)
	b.append(1e9)

	# add amount_i >= 0 inequalities
	for i in range(m):
		a.append([1.0 if j == i else 0.0 for j in range(m)])
		b.append(0.0)

	for i in range(len(a)):
		a[i].append(b[i])

	p_max = float('-inf')
	v_max = []
	a_max = []
	for v in combinations(range(len(a)), m):
		v_dash = []
		for i in v:
			v_dash.append(a[i])

		gauss(v_dash)
		a_dash = [i[-1] for i in v_dash]
		sol = False
		if not any(i < 0 for i in a_dash):
			for i in range(n + 1):
				x = fsum([ax * ay for ax, ay in zip(a[i][:-1], a_dash)])
				y = a[i][-1]
				if x > y and not isclose(x, y, rel_tol=1e-04):
					break
			else:
				sol = True

		if sol:
			p_dash = fsum([px * ax for px, ax in zip(p, a_dash)])
			if p_dash > p_max:
				p_max, v_max, a_max = p_dash, v, a_dash

	if isfinite(p_max):
		if v_max.count(n) == 0:
			print('Bounded solution')
			print(*(format(i, '.18f') for i in a_max))
		else:
			print('Infinity')
	else:
		print('No solution')
