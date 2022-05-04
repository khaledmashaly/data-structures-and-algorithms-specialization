#python3
from itertools import combinations
from decimal import Decimal, getcontext, FloatOperation, InvalidOperation
from fractions import Fraction
from math import isfinite

getcontext().prec = 25
getcontext().traps[FloatOperation] = True


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
		m[r] = [x / el for x in m[r]]
		for i in range(row_count):
			if i != r:
				el = m[i][lead]
				m[i] = [mi - el * mr for mi, mr in zip(m[i], m[r])]
		lead += 1

if __name__ == "__main__":
	n, m = [int(i) for i in input().split(' ')]
	a = [[Decimal(i) for i in input().split(' ')] for _ in range(n)]
	b = [Decimal(i) for i in input().split(' ')]
	p = [Decimal(i) for i in input().split(' ')]

	# add amount_i >= 0 inequalities
	for i in range(m):
		a.append([Decimal('-1') if j == i else Decimal('0') for j in range(m)])
		b.append(Decimal('0'))

	a.append([Decimal('1')] * m)
	b.append(Decimal('1000000000'))

	for i in range(len(a)):
		a[i].append(b[i])

	p_max = Decimal('-Infinity')
	v_max = []
	a_max = []
	for v in combinations(range(len(a)), m):
		v_dash = []
		for i in v:
			v_dash.append(a[i])

		gauss(v_dash)
		a_dash = [i[-1] for i in v_dash]
		sol = True
		for i in range(len(a)):
			if i < n or i == n + m:
				sm = sum([ax * ay for ax, ay in zip(a[i][:-1], a_dash)])
				try:
					sm = round(sm, 6)
				except InvalidOperation:
					pass
				if sm > a[i][-1]:
					sol = False
					break
			else:
				if round(a_dash[i - n], 6) < 0:
					sol = False
					break
				# if sum([ax * ay for ax, ay in zip(a[i][:-1], a_dash)]) < a[i][-1]:
				# 	sol = False
				# 	break

		if sol:
			p_dash = sum([px * ax for px, ax in zip(p, a_dash)])
			if p_dash > p_max:
				p_max = p_dash
				v_max = v
				a_max = a_dash

	if isfinite(p_max):
		if v_max.count(n + m) == 0:
			print('Bounded solution')
			print(*(format(float(i), '.18f') for i in a_max))
		else:
			print('Infinity')
	else:
		print('No solution')
