
from math import sin
from math import pi
def factorial(n):
	f = 1
	for i in range(1,n+1):
		f *= i
	return f

x = float(eval((input("Enter x:")))) * pi / 180
mySin = sum([((-1)**i) * (x**(2*i + 1))/factorial(2*i + 1) for i in range(50)])
print("My sinx=",mySin)
print("math.sinx() =", sin(x)) 

'''

f = lambda x : True if (x % 4 == 0 and x % 100 != 0 or x % 400 == 0) else False

print(f(2000)) 

#map, filter, reduce

x = map(lambda x : 2*x+1, [x for x in range(10)])

print(x)

#filter

x = filter(lambda x : x % 5 == 0, [x for x in range(100)])

print(x)

#reduce

x = reduce(lambda x, y : x+y, [x for x in range(10)])

print(x)


#chr(97-122)(65-90)(48-57
#ord('A') 


#exp3
#1. generate 10000 random real numbers list, find out those which contains 7 or 8 or 9 as a digit after decimal point
#2. Create a Database
Database1 = [['ID', 'Name', 'Email', 'Age', 'Salary']] 


#name 1. 1st chars should any alphabate with capital
	#2. Second should be vowels 

#Email: 1. It should not start with digit 25, append anything from ['gamil.com', 'yahoo.com', 'facebook.com']

#Age 18-60

#Salary
'''
 


















