### Compairing Arrays
import numpy as np

a = np.array([1,2,3,0])
b = np.array([0,3,9,11])

c = (a == b)
print(c)
c = (a > b)
print(c)
c = (a < b)
print(c)
if(np.any(c)):  # like ||
    print(c)


if(np.all(c)): # like &&
    print("All are true")

# np.logical_and() for more than 2 conditions
# np.logical_or() for more than 2 conditions

## Where() function
c = np.where(a > b, a,b) # Returns array of even element
print(c)
c = np.nonzero(a) # Array of index of non-zero elements
print(c)
## Aliasing arrays
a = np.array([1,2,3,4])
a = b
print(a)
print(b)

b[0] = 99
print(a) # value of b is changing with a or memory is allocated to elements -- > aliasing
print(b) 
## Viewing arrays
c = np.array([1,2,3,4])
d = c.view()
print(c)
print(d)

d[0] = 99
print(c) # value of d is  changing with a but memory is allocated to copy of element a -- >viewing
print(d) 

## copying arrays
e = np.array([1,2,3,4])
f = e.copy()
print(e)
print(f)

f[0] = 99
print(e) # value of f is not changing with a &  memory is allocated to a and b -- >viewing
print(f) 