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

arr1 = [1,2,3]
arr2 = [4,1,9]

def same(arr1, arr2):
    

print(same(arr1,arr2))