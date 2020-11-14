######## Sliding Window Pattern ######

### This pattern involves creating a window which can either be an array or number from one position
### to another. 

### Depending on a certain condition a new window either increase or closes(hence creating a new window)

### Very useful to keep track of a subset of data in array/string/list ,etc

### Example ---> Function accepting list counting maximum sum of n consecutive number in list

lst = [int(x) for x in input("Enter numbers seperated by space: ").split(" ")]
n = int(input("Enter number of consecutives: "))

def maxSubList(lst , n):
    sum = 0
    max = 0
    if n > len(lst):
        print("Not Possible!!")
        return 0
    
    for i in range(len(lst)):
        for j in range(i , i + n):
            if(j > len(lst) - 1) : break
            sum += lst[j]
        if(sum > max): max = sum
        sum = 0

    return max

print(maxSubList(lst , n))
### Time Complexity ---> O(N ^ 2)
### Space Complexity ---> O(N)  

def maxSubListSum(lst , n):
    if n > len(lst):
        print("Not Possible!!")
        return 0
    maxSum = 0
    tempSum = 0

    for i in range(0,n):
        tempSum += lst[i]
    print(tempSum)

    maxSum = tempSum

    for i in range(n , len(lst)):
        tempSum = tempSum - lst[i - n] + lst[i]
        if(tempSum > maxSum):
            maxSum = tempSum

    return maxSum

print(maxSubListSum(lst,n)) 

### Time Complexity ---> O(N)
### Space Complexity ---> O(N) 
