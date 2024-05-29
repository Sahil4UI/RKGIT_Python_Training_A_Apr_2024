import matplotlib.pyplot as plt
import numpy as np

np.random.seed(5)
x = np.random.randint(10,100,15)
y = np.random.randint(5,50,15)
plt.title("Scatter graph")
plt.xlabel('House Number')
plt.ylabel('street number')
plt.scatter(x,y)
plt.show()
