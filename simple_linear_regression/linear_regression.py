l = open('train.csv').readlines() 
training_ds = [i.split(',') for i in l[1:]]
for i in training_ds:
	i[1] = i[1][:-1]

training_x = [eval(i[0]) for i in training_ds]
training_y = [eval(i[1]) for i in training_ds]

mean_x = sum(training_x) / 700
mean_y = sum(training_y) / 700

ss_xy = 0.0
ss_xx = 0.0
for i in range(700):
	ss_xy += training_x[i] * training_y[i] - 700 * mean_x * mean_y
	ss_xx += (training_x[i] ** 2) - (700 * (mean_x ** 2))

m = ss_xy / ss_xx
c = mean_y - (m * mean_x)


l = open('test.csv').readlines()
test_x = [eval(i.split(',')[0]) for i in l[1:]]
test_y = [eval(i.split(',')[1]) for i in l[1:]]

for i in range(0,len(test_x)):
	predicted = m * test_x[i] + c
	error = test_y[i] - predicted
	print("{}\t{}\t{}".format(test_y[i], predicted, error))