import numpy as np
import sys
arr = np.array([1,2,3,4,5])

print(arr)
arr = np.arange(1,25)
print(arr)

arr = np.random.randint(2,25,5)
print(arr)
print(arr[:3])
print(arr.shape)
print(arr.max())
print(arr.min())
print(arr.sum())
print(arr.argmax())
print(arr.argmin())

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr + 1)
print(arr * 2)
print(arr.shape)
print(arr[0:2,0:2])
print("on axis 0",arr.max(axis = 1))
li = [i for i in range(1,100)]
print(sys.getsizeof(li))

arr = np.array(li)
print(sys.getsizeof(arr))
