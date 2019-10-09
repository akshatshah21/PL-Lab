import random
''' Database Generation'''
database = [[y+1 if x == 0 else None for x in range(5)] for y in range(10)] # IDs set
for i in range(10):
	name = chr(random.randint(65, 90))	# First letter
	name += random.choice(['a', 'e', 'i', 'o', 'u'])	#Second letter, vowel
	for j in range(9):	#Rest of the letters
		name += chr(random.randint(97,122))
	database[i][1] = name
	email = name.lower()	#Email
	database[i][2] = email + random.choice(['@ymail.in', '@inlook.com', '@tediffmail.co.in']) #Concat the domain
	database[i][3] = random.randint(18,60)	#Age
	database[i][4] = random.choice([j*10000 for j in range(1,35)])	#Salary

for i in database:
	print(i)

'''Query 1: Average salary'''
avg = reduce(lambda x, y : x+y, [d[4] for d in database])
avg /= len(database)
print"Average Salary:" + str(avg)


'''Query 2: First character of name:'''

c = raw_input("Enter first character of name to search:")
query2 = list(filter(lambda x : c == x[1][0], database))
print 'Results found:' + str(len(query2))

for i in query2:
	print(i)
'''Query 3: Updating salaries of those aging 18-25'''

#query3 = filter(lambda x : x[3] >=18 and x[3] <= 25, database)
print("Updated salaries:")

database = map(lambda x : x[:4] + [int(1.1*x[4]) if x[3] >=18 and x[3] <=25 else x[4]], database)
for i in database:
	print(i)
	
	
''' Query 4: Min and Max Salary, after updating the database '''
maxSal = reduce(lambda x,y : x if x>y else y, [d[4] for d in database])
print "Max salary:" + str(maxSal)
minSal = reduce(lambda x,y : x if x<y else y, [d[4] for d in database])
print "Min salary:" + str(minSal)


'''Query 5: Domain is inlook.com'''
query5 = filter(lambda x : "@inlook.com" in x[2], database)
print "People having inlook emails:" + str(len(query5))
for i in query5:
	print(i)
