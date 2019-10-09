n = int(input("Enter n:"))
l = [True] * n
for i in range(0, n):
	if i+1 == 1:
#		print("case 1")
		l[i] = False
		continue
	if l[i] is True:
		for j in range(i + 1, n):
			if (j + 1) % (i + 1) == 0:
				#print(j+1, "is multiple of",i+1)
				#print(l[j])	
				l[j] = False
#print("List:",l)
for i in range(0,n):
	if l[i] == True:
		print(i + 1)	
