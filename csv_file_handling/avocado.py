from functools import reduce
dataset = []
f = open("avocado.csv", "r")
rows = f.readlines()
for l in rows:
	entries = l.split(",")
	entries[-1] = entries[-1][:-1]
	dataset.append(entries)

# Print dataset
for i in dataset:
	print(i)

# Mean AveragePrice
avg = reduce(lambda x,y: x+y, map(lambda x: eval(x[2]), dataset[1:])) / (len(dataset)-1)
print("Mean AveragePrice: ", avg)

# Find mean AveragePrice of records whose region is Albany

# albany = [i for i in dataset[1:] if i[13] == 'Albany']
albany = list(filter(lambda x: x[13] == 'Albany',dataset[1:]))
# albany_avg = reduce(lambda x,y: x+y, [eval(i[2]) for i in albany])
albany_avg = reduce(lambda x,y: x+y, map(lambda x: eval(x), [i[2] for i in albany]))/len(albany)
print("Mean of AveragePrice of Albany records:", albany_avg)

f.close()