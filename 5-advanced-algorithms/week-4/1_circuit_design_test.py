from random import randint, randrange
from itertools import combinations
from os import system
from subprocess import run, PIPE
from math import factorial as f

while True:
	v = randint(1, 10)
	possible_clausses_no = f(2 * v) / f(2 * v - 2) / f(2)
	c = randint(1, possible_clausses_no)

	var = []
	for i in range(1, v + 1):
		var.extend([i, -i])

	possible_clausses = list(combinations(var, 2))

	clausses = []
	indices = [-1]
	for _ in range(c):
		i = -1
		while i in indices:
			i = randrange(len(possible_clausses))
		clausses.append(possible_clausses[i])

	with open('1.cnf', 'w') as cnf:
		cnf.write('p cnf {} {}\n'.format(v, c))
		for clauss in clausses:
			cnf.write('{} {} 0\n'.format(*clauss))

	minisat = run(['minisat', './1.cnf', './1.sat'])

	circuit_in = '{} {}\n'.format(v, c)
	for clauss in clausses:
		circuit_in += '{} {}\n'.format(*clauss)


	circuit = run(
		['python3', './1_circuit_design.py'],
		input=circuit_in.encode('ascii'),
		stdout=PIPE
	)

	minisat_sol = ''
	with open('1.sat') as sat:
		minisat_sol = sat.readline()

	if minisat_sol[:3] != circuit.stdout.decode('ascii')[:3]:
		break
