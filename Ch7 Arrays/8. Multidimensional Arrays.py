import numpy as np

a = np.ones((2,3),int)
print(a)
a = np.eye(3)
print(a)

## Reterive elements of 2d array
a = np.array([[1,2,3] , [4,5,6] , [7,8,9]])

for i in range(len(a)):
    for j in range(len(a)):
        print(a[i][j],end = " ")

## Retreive elements from 3d array
a = np.array([[[1,2,3] , [4,5,6]] , [[7,8,9] , [10 , 11, 12]]])
for i in range(len(a)):
    for j in range(len(a)):
        for k in range(len(a)):
            print(a[i][j][k], end = " ")

## Slicing MDA

a = np.array([[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20]])
a = a[2:4,3:5]
print(a)