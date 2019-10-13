I = [[int(x==y) for y in range(5)] for x in range(5)]
print("Identity matrix:")
for i in I:
	print(i)

M1 = [[0 if x==0 or x ==4 or y==0 or y==4 else 1 for y in range(5)] for x in range(5)]
print("\nM1:")
for i in M1:
	print(i)

M2 = [[0 if (x+y)%2==0 else 1 for y in range(5)] for x in range(5)]
print("\nM2:")
for i in M2:
	print(i)
