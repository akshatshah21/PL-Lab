#n = int(input('Enter an integer: '))
import sys

n = int(sys.argv[1])	#Commannd Line Arg
flag = False
if n == 1:
	print('1 is a square')
else:
	for i in range(1,n//2 + 1):
		if n / i == i:
			flag = True
			break
#	print(i)
	if flag == True:
		print(n, 'is a square')
	else:
		print(n, 'is not a square')

