
U = [[0 if row > col else 1 for col in range(3)] for row in range(3)]

print("Upper Triangular Matrix")
for i in U:
	print(i)

L = [[0 if row<col else 1 for col in range(3)] for row in range(3)]
print("lower triangular matrix")
for i in L:
	print(i)
