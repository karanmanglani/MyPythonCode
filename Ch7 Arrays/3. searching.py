from array import *

# Algorithm 1
arr = array('i',[])
n = int(input("Enter number of Elements : "))

for i in range(n):
    arr.append(int(input("Enter element number %d : " %(i + 1) )))

print(arr)
flag = False
i = 0 
s = int(input("Enter element to search : "))
for i in range(n):
    if(s == arr[i]):
        print("Element found in position %d" %(i + 1))
        flag = True
if(flag == False):
    print("Element not found")

# Algorithm 2
try:
    pos = arr.index(s)
    print("Element found in position %d" %(pos + 1))
except ValueError:
    print("not found in array")