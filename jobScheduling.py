'''
	Question:
		Job scheduling
'''
import random
import pprint
#emp = [[y+1 if x==0 else None for y in range]]
products = [chr(i) for i in range(65,70)]
cost = [i*100 for i in range(1,6)]
#emp = 
#l = [i[0]for i in  emp]
print(products)
print(cost)

def SortbyCost(val):
	return val[2]


database = [[y+1 if x == 0 else None for x in range(5)] for y in range(100)] # IDs set
for i in range(100):
	name = chr(random.randint(65, 90))	# First letter
	name += random.choice(['a', 'e', 'i', 'o', 'u'])	#Second letter, vowel
	for j in range(9):	#Rest of the letters
		name += chr(random.randint(97,122))
	database[i][1] = name
	email = name.lower()	#Email
	database[i][2] = email + random.choice(['@ymail.in', '@inlook.com', '@tediffmail.co.in']) #Concat the domain
	database[i][3] = random.randint(18,60)	#Age
	database[i][4] = random.choice([j*10000 for j in range(1,35)])	#Salary

for i in  database:
	print(i)

print("IDs:")
randIDs=[(database.pop(random.randint(1, len(database)-1)))[0] for i in range(10)]
print(randIDs)

jobList=[[y,random.randint(1,9),random.choice(cost)]for y in randIDs]
print("JOBS:\nID|Deadline|Cost")
pprint.pprint(jobList)
print("Sorted JobList by cost:")
jobList.sort(key=SortbyCost, reverse=False)

pprint.pprint(jobList)




'''
Job Sequencing
'''

seq = [[0 for i in range(3)] for x in range(24)]
#print(seq)

print("JOBLIST:")
for i in jobList:
	print(i)

print("Deadline list:")
for i in jobList:
	print(i[1])

for i in jobList:
	for j in seq[i[1]]:
		print("j=", j)
		print(seq[i[1]].index(j))
		if j == 0:
			print("cond")
			print(i[2])
			j = i[2]
			print("changed=",j)
			break;

			
for i in seq:		
	print(i)





