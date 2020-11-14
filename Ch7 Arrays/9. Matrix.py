import numpy as np;
### Methods of creating matrix
## Method 1 array method
a = np.matrix([[1,2,3] , [4,5,6]])
print(a)

## Method 2 --> String method
str = "9 4 3; 6 5 7; 2 1 8"
a = np.matrix(str)
print(a)

### Getting diagonal of matrix
print(np.diagonal(a))

### Matrix methods
big = a.max()
print(big)

small = a.min()
print(small)

print(a.sum())

print(a.mean())

print(a.prod(0)) # Product of column
print(a.prod(1)) # Product of rows

### Sortig Matrix
print(np.sort(a))
a = np.array([[3,2,1] , [2 , 4 , 6]])
print(np.sort(a,axis = 0))

### Transposing Matrix ---> Rows to column and column to rows
print(a.transpose())

### Matrix arithmetic
a = np.matrix('1 2 3; 4 5 6')
b = np.matrix('2 2 2; 1 -1 2')
print(a + b)
print(a - b)
print(a / b)
