######################## Multiple Pointers Pattern #########################
## Basic Idea
# 1. Creating pointers or values that correspond to an index or position and move towards the beginning
#    ,end or middle based on a certain conditon 
# 2. Very efficient for solving problems with minimal space complexity as well

########## Without multiple pointers #######
def sumZero(lst):
    lstLength = len(lst)
    for i in range(lstLength):
        for j in range(lstLength):
            if not(i == j):
                if lst[i] + lst[j] == 0:
                    return [lst[i],lst[j]]
    return None

print(sumZero([1,2,3]))    

### Time Complexity O(n^2)
def sumToZero(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        sum = lst[left] + lst[right]
        if sum == 0:
            return [lst[left], lst[right]]
        elif sum > 0:
            right -= 1
        else:
            left += 1
    return None

print(sumToZero([-4,-3,-2,-1,0,1,2,3,10]))

###################### Multiple Pointers Challenge ###############

def countUniqueValues(lst):
    pointer1 = 0
    pointer2 = 1
    while pointer2 < len(lst):
        if not(lst[pointer1] == lst[pointer2]):
            lst[pointer1 + 1] = lst[pointer2]
            pointer1 += 1
            pointer2 += 1
        else:
            pointer2 += 1
    if pointer1 > 0:
        return pointer1 + 1
    else:
        return 0

print(countUniqueValues([-2,-1,-1,0,1]))
         
