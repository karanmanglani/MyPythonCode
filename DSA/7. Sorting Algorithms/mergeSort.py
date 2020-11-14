import math
import random
#! It's Divide and Conqueor Algorithm
def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0

    while (i < len(lst1) and j < len(lst2)):
        if(lst2[j] > lst1[i]):
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    
    while (i < len(lst1)):
        lst.append(lst1[i])
        i += 1
    
    while (j < len(lst2)):
        lst.append(lst2[j])
        j += 1
    return lst

def mergeSort(lst):
    if(len(lst) <= 1): return lst

    midPoint = math.floor(len(lst) / 2)
    left = mergeSort(lst[0:midPoint])
    right = mergeSort(lst[midPoint:])

    return merge(left, right)

lst = []
def randomList(n,start,stop,lst):
    if ( n < 1):
        return None
    lst.append(random.randint(start,stop))
    randomList(n - 1,start,stop,lst)

randomList(500,0,100000,lst)
print(mergeSort(lst))
