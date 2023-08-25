import numpy as np
from matplotlib import pyplot as plt

bogusdata = [(9, 55), (11, 67), (13, 19), (15, 3), (17, 14), (19, 82), (21, 69), (23, 51), (25, 32), (27, 17)]

plt.scatter(list(map(list, zip(*bogusdata)))[0],list(map(list, zip(*bogusdata)))[1])

plt.xlabel("x")
plt.ylabel("y")
plt.title("bogusdata")

linear_model=np.polyfit(list(map(list, zip(*bogusdata)))[0],list(map(list, zip(*bogusdata)))[1],1)
linear_model_fn=np.poly1d(linear_model)
x_s=np.arange(min(list(map(list, zip(*bogusdata)))[0]),max(list(map(list, zip(*bogusdata)))[0]))
plt.plot(x_s,linear_model_fn(x_s),color="green")

plt.show()
