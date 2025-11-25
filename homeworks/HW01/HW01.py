import numpy as np

a = np.array([1, 2, 3])
b = np.zeros((2, 3))
c = np.ones((2, 2, 3))
d = np.arange(1, 10, 2)
print(a)
print(b)
print(c, c.shape, c.dtype)
print(d)

array = np.array([[1, 2, 3], [4, 5, 6]])
print(array[1,2])
print(array[0, ::]) 

arr1 = np.array([[4, 5, 6], [1, 2, 3]])
print(arr1 * array)
print(arr1.mean())