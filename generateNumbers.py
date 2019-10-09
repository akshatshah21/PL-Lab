import random; print(list(filter(lambda x : round(x - int(x),1) in [0.7, 0.8, 0.9], [random.uniform(0, 1000) for i in range(100)])))
