def recursiveSum(l, length):
	sum = 0
	if length == 1:
		return l
	if length == 2:
		#print('Case len = 2')
		return l[0] + l[1]
	elif length != 0:
		#print('Case len = ', length)
		sum = l[-1] + recursiveSum(l[:-1], length - 1)
		return sum
	return sum
		









n = int(input('enter size: '))
#l = [1] * 1000
l = []
#n = len(l)

print('Enter elements one by one:')
while n != 0:
	l.append(int(input()))
	n -= 1

#print(l)
print('Sum:', recursiveSum(l, n))
