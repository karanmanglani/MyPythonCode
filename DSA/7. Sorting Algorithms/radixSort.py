import math
#! Helper Methods
#! get digit in a given position in a number
#* Way 1 
#*def getDigit(num,pos):
#*    n = str(num)
#*    return int(n[len(n) - 1 - pos])

#* Way 2
def getDigit(num,pos):
    return math.floor(abs(num)/pow(10,pos)) % 10 #* Used abs as -32,0 without abs will give -2

#! get number of digits in number
#* Way 1
#* def digitCount(num):
    #* return len(str(num))
#* Way 2
def digitCount(num):
    if(num == 0) : return 1
    return math.floor(math.log10(abs(num))) + 1

def mostDigits(lst):
    maxDigit = 0
    for i in lst:
        digit = digitCount(i)
        if(digit > maxDigit):
            maxDigit = digit
    return maxDigit

def radixSort(nums):
    
    maxDigits = mostDigits(nums)
    for k in range(maxDigits):
        digitBucket = [[],[],[],[],[],[],[],[],[],[]] 
        for i in range(len(nums)):
            digitBucket[getDigit(nums[i] , k)].append(nums[i])
        newLst = []
        for i in range(len(digitBucket)):
            for element in digitBucket[i]:
                newLst.append(element)
        nums = newLst
    
    return newLst
print(radixSort([12,23,11,24,7,54]))