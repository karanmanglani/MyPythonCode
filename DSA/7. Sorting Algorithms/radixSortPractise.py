import math

def getDigit(num,pos):
    return math.floor(abs(num)/pow(10,pos)) % 10

def digitCount(num):
    if num == 0: return 1
    return math.floor(math.log10(abs(num))) + 1

def maxDigits(nums):
    maxDigit = 0
    for i in nums:
        if digitCount(i) > maxDigit:
            maxDigit = digitCount(i)
    return maxDigit


def radixSort(nums):
    maxDigit = maxDigits(nums)
    for k in range(maxDigit):
        digitBucket = [[],[],[],[],[],[],[],[],[],[]]
        for i in range(len(nums)):
            digitBucket[getDigit(nums[i],k)].append(nums[i])
        
        newLst = []
        for i in range(len(digitBucket)):
            for element in digitBucket[i]:
                newLst.append(element)
        nums = newLst

    return newLst

print(radixSort([12,23,234,432,41,20,102,43,63454,123,1234214]))

