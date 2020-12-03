####################### Pattern Theory ##################
# 1. This pattern uses dictionaries to collect values or frequencies of values.
# 2. This can often avoid the need to use nested loops or o(n^2) operations with arrays/strings

## Example Problem
# write a function called same, which accepts two arrays. The function should return true if every value in the array has the corresponding value squared in second array.
# The frequency of values must be same
## Sample input and Output
# same([1,2,3] , [4,1,9]) ==> true
# same([1,2,3] , [1,9]) ==> false
# same([1,2,1] , [4,1,4]) ==> false

######## Naive approach without frequency counter design pattern with O(n^2) complexity because of nested Loops
arr1 = [1,2,3]
arr2 = [4,1,9]

def same(arr1, arr2):
    if not(len(arr1) == len(arr2)):
        return False
    
    for i in arr1:
        squareFound = False
        for j in arr2:
            if (j == i*i):
                squareFound = True
                arr2.remove(j)
        if squareFound:
            squareFound = False
            break
        else:
            return False
        
    return True

print(same(arr1,arr2))

############# Using Frequency counter pattern with time complexity O(n)
arr1 = [1,2,3]
arr2 = [4,1,9]
def sameRefactored(arr1,arr2):
    if not(len(arr2) == len(arr1)):
        return False
    
    frequencyCounter1 = {}
    frequencyCounter2 = {}

    for i in arr1:
        if (i in frequencyCounter1.keys()):
            frequencyCounter1[i] += 1
        else:
            frequencyCounter1[i] = 1

    for j in arr2:
        if (j in frequencyCounter2.keys()):
            frequencyCounter2[j] += 1
        else:
            frequencyCounter2[j] = 1
    
    for i in frequencyCounter1.keys():
        if not(i*i in frequencyCounter2.keys()):
            return False
        if not(frequencyCounter1[i] == frequencyCounter2[i*i]):
            return False
    
    return True

print(sameRefactored(arr1,arr2))

#################### Frequency Counter Challenge #############
str1 = ''
str2 = ''
def isAnagram(str1,str2):
    frequencyCounter1 = {}
    frequencyCounter2 = {}

    for i in str1:
        if i in frequencyCounter1.keys():
            frequencyCounter1[i] += 1
        else:
            frequencyCounter1[i] = 1

    for i in str2:
        if i in frequencyCounter2.keys():
            frequencyCounter2[i] += 1
        else:
            frequencyCounter2[i] = 1

    for i in frequencyCounter1.keys():
        if i not in frequencyCounter2.keys():
            return False
        
        if not frequencyCounter1[i] == frequencyCounter2[i]:
            return False
    
    return True

print(isAnagram(str1,str2))