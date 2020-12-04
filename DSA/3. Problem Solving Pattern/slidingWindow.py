###### Sliding Window Pattern ########
## Theory 
# 1. This pattern creates a window which can either be an array or number from one position to another 
# 2. Depending on a certain conditon , the window either increases or closes (and a new window is created)
# 3. Very useful for keeping track of a subset of data in an array/string etc

def maxSubarraySum(lst,n):
    max = 0
    for i in range(len(lst)):
        sum = lst[i]
        for j in range(1,n):
            if i+j < len(lst):
                sum += lst[i+j]
        if sum > max:
            max = sum
    return max

print(maxSubarraySum([],4))

## Time complexity ---> O(n^2)
## Same problem using sliding window pattern

def maxSubarraySumRefactored(lst,n):
    maxSum = 0
    sum = 0
    if(len(lst) < n):
        return None
    for i in range(n):
        maxSum += lst[i]
    sum = maxSum
    for i in range(n, len(lst)):
        sum = sum - lst[i-n] +lst[i]
        maxSum = max(maxSum,sum)
    return maxSum
print(maxSubarraySumRefactored([1,2,3,4,5,6,2,3],3))

## Explanation 
# [1,2,3,4],2
#  1 + 2 = 3 next 3 - 1 +3 