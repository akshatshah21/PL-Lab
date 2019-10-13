mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
ans = [[0 for i in range(4)] for j in range(4)]
rows = len(mat)
cols = len(mat[0])
print(rows, cols)
for i in range(rows):
	for j in range(cols):
		if i != j:
			ans[j][i] = mat[i][j]
for i in mat:
	print(i)

