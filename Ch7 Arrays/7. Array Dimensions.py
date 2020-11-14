import numpy as np

# 1d arrays
a = np.array([10,20,30])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.itemsize)

# 2d arrays ---> Combination of 1d arrays
b = np.array([[1,2,3],
[4,5,6]])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.itemsize)

# 3d arrays ---> Combination of 2d arrays
c = np.array([[[1,2,3] , [4,5,6]],
[[7,8,9] , [10,11,12]]])
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.itemsize)
print(c.dtype)
a = a.reshape(3,1,1)
print(a)
c = c.flatten()
print(c)