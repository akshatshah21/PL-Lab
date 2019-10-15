def recursiveSum(l):
	if len(l) == 0:
		return 0;
	if len(l) == 1:
		return l[0]
	else:
		return l[-1] + recursiveSum(l[:-1])
n = int(input('enter size: '))
l = []
if n!= 0:
	print('Enter elements one by one:')
	while n != 0:
		l.append(int(input()))
		n -= 1
print('Sum:', recursiveSum(l))