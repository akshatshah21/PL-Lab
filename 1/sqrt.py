import sys

n = int(sys.argv[1])	#Command Line Arg
flag = False
if n == 1:
	print('Root: 1')
else:
	low = 1
	high = n
	while high != low + 1:
		mid = (high + low) // 2
		if mid*mid == n:
			flag = 1
			break
		elif mid * mid < n:
			low = mid
		else:
			high = mid
	if flag == 1:
		print('Root:', mid)
	else:
		print('Not a perfect square, root between', low, 'and', high)