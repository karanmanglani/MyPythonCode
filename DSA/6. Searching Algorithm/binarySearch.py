import math
def isSorted(lst):
    for i in range(1,len(lst) - 1):
        if(lst[i] > lst[i+1]):
            return False
    
    return True

def binarySearch(lst,n):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = math.floor((left + right) / 2)

        if(n > lst[mid]):
            left = mid + 1
        
        elif(n < lst[mid]):
            right = mid - 1        
        elif(n == lst[mid]):
            return mid

lst = [int(n) for n in input("Enter numbers seperated by space: ").split(" ")]
n = int(input("Enter integer to search : "))

if(isSorted(lst)):
    x = binarySearch(lst,n)
    print("{0} found a the position {1}".format(n,x + 1))