import numpy as np
arr1 = np.array([210 , 220 , 130 , 540 , 750])
arr2 = np.array([15 , 125 , 125,  435, 645])

arr = arr1 - arr2
print("Array 1 - Array 2 = ",arr)

### useful mathematical function in numpy
print(np.prod(arr)) # Product of all the elements in array
print(np.median(arr)) #Returns median / average value
print(np.var(arr)) # Returns variance of array
print(np.cov(arr)) # Covariance of array
print(np.std(arr)) # Standard deviaton 
print(np.argmax(arr)) # index of biggest element
print(np.argmin(arr)) # index of smallest element
print(np.unique(arr)) # array of unique elements
print(np.sort(arr)) # Sorted in ascending order