import numpy as np
'''
Difference between import numpy as np & from numpy import *

1 ---> np.array() ---> manually import required function 
2 ---> array() ---> import all the functions
'''

### Using numpy
## Creating arrays
#1 array() function
arr = np.array([10 , 20 , 30 , 40 , 50])
print(arr)

#2 linespace()
a = np.linspace(0,10,5) # 0 - 10 is divided in 5 equal parts 
print(a)

#3 logspace()
a = np.logspace(1,4,5) # values 1 ^ 10 to 4 ^ 10 is divided in 5 equal parts
print(a)

#4 arrange()
a = np.arange(0,10,2) #similar to range 
print(a)

#5 zeros() & ones()

a= np.zeros(5,int)
print(a)
a = np.ones(5,float)
print(a)