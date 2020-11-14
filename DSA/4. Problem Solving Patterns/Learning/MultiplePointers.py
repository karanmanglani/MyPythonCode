#################################### Multiple Pointers #################################
### In this Pattern we create pointers or values that correspond to an index or position and 
### move towards the beginning , end or middle based on certain condition
### Very Efficient for solving problems with minimal space complexity as well

### Challenge 1 --> 
### write a function accepting sorted list of integers finding first pair where sum is zero or undefined

# Create list for user input
lst = [int(x) for x in input("Enter numbers seperated by space : ").split(" ")]
n = len(lst)

# Creating Function
def isSorted(lst):
    for x in range(0,len(lst) - 1):
        if(lst[x] > lst[x + 1]):
            return False
    
    return True

def zeroPair(lst):
    if(isSorted(lst)):
        for x in range(0,n):
            for j in range(x + 1, n):
                if(lst[x] + lst[j] == 0):
                    return [lst[x] , lst[j]]
        return False
    else:
        print("List not sorted!!")
        return False

ans = zeroPair(lst)
if(ans == False):
    print("Undefined")
else:
    print(ans)

### Time Complexity ---> O(N ^ 2)
### Space Complexity ---> O(1)

###Using Multiple Pointers --->

def sumZero(lst):
    if(isSorted(lst)):
        left = 0
        right = n - 1
        while(left < right):
            sum = lst[left] + lst[right]
            if(sum == 0):
                return [lst[left] , lst[right]]
            elif(sum > 0):
                right -= 1
            else:
                left += 1
        return False
    else:
        print("List not Sorted!!")
        return False

ans = sumZero(lst)
if(ans == False):
    print("Undefined")
else:
    print(ans)

### Time Complexity ---> O(N)
### Space Complexity ---> O(1)