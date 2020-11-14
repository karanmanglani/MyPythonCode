### Challenge --->
### Funtion Accepting sorted list and giving number of unique values using Multiple Pointers
### [1,1,1,1,1,2] ---> 2
### [1,2,3,4,4,7,7,12,12,13] --> 7
### [] --> 0
### [-2, -1 , -1 ,0,1] ---> 4

# Accepting List
lst = [int(x) for x in input("Enter Numbers seperated by space: ").split(" ")]
# length of list
n = len(lst)
# Check for sort
def isSorted(lst):
    for x in range(0,n - 1):
        if(lst[x] > lst[x + 1]):
            return False
    
    return True

def uniqueValues(lst):
    if(n == 0): return 0
    i = 0
    j = 1
    for j in range(1,n):
        if(lst[j] != lst[i]):
            i += 1
            lst[i] = lst[j]
    return i + 1

print(uniqueValues(lst))