import matplotlib.pyplot as plt
import numpy as np
np.random.seed(5)
x = np.random.randint(10,100,15)
y = np.random.randint(5,50,15)
print(x)
print(y)
plt.plot(x,y)
plt.show()

