from functools import reduce
V = {1,2,3,4,5,6,7}
E = {(1,2), (2,3), (3,4), (4,5), (5,6), (6,3), (3,7), (7,1)}
S = []
cycles = 0
print('Graph:\nVertices:', V, '\nEdges:', E)
for e in E:
	# Case 1: Both in V
	if e[0] in V and e[1] in V:
		V.remove(e[0])
		V.remove(e[1])
		S.append(set(e))
	# Case 2: e[0] in V, e[1] not in V
	elif e[0] in V and e[1] not in V:
		V.remove(e[0])
		for s in S:
			if e[1] in s:
				s.add(e[0])
	# Case 3: e[0] not in V, e[1] in V
	elif e[0] not in V and e[1] in V:
		V.remove(e[1])
		for s in S:
			if e[0] in s:
				s.add(e[1])
	# Case 4: Both not in V
	else:
		setsToUnion = []
		for s in S:
			if e[0] in s and e[1] in s:
				cycles += 1
			else:
				if e[0] in s:
					setsToUnion.append(s)
					S.remove(s)
					for s2 in S:	# S changed during its own traversal, so maybe that's why for loop is nested here
						if e[1] in s2:
							setsToUnion.append(s2)
						S.remove(s2)
		if len(setsToUnion) != 0:
			S.append(reduce(lambda x,y:x.union(y), setsToUnion))
print(cycles)