from array import *
x = array('i',[])

print("How many elements? ", end='')
n = int(input())
for i in range(n):
    print('Enter element : ',end = '')
    x.append(int(input()))
print("Orignal Array : ",x)

# Bubble Sort --->
i = j =0
flag = False # after swapping flag becomes true
for i in range(n - 1): # i is from 0  to n - 1
    for j in range(n - 1 - i): # j is from 0 to one element lesser than i
        if(x[j] > x[j + 1]):
            t = x[j]
            x[j] = x[j + 1]
            x[j + 1] = t
            flag = True
    if(flag == False):
        break
    else:
        flag = False

print("Sorted Array : ",x)