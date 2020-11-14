### Function to search item in list
import math
from MultiplePointers import isSorted

lst = [int(x) for x in input("Enter numbers seperated by space: ").split(" ")]
n = int(input("Enter number to search: "))

def Search(lst , n):
    for i in range(0,len(lst)):
        if(lst[i] == n): return i
    return -1

print(Search(lst,n))
## Time Complexity = O(N)


def search(lst,n):
    if(isSorted(lst)):
        min = 0
        max = len(lst) - 1
        while min <= max:
            middle = math.floor(min + max / 2)

            if(lst[middle] < n):
                min = middle + 1
            
            elif(lst[middle] > n):
                max = middle - 1
            else:
                return middle
    return -1

print(search(lst,n))
## Time Complexity = O(log N)