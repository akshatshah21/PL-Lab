mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
t = [[mat[j][i] for j in range(4)] for i in range(4)]
for i in t:
	print(i)
