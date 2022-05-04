#python3
from decimal import Decimal
from fractions import Fraction

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
	n = int(input())
	m = [[Fraction(i) for i in input().split(' ')] for _ in range(n)]
	gauss(m)
	for i in m:
		print(i[n], end=' ')
