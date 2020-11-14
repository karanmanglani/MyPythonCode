#### This pattern uses Dictionaries or sets to collect Values/Frequencies of values
#### This can often avoid the use of nested loops or O(N ^ 2)Time complexity operations with strings/arrays
#### Time complexity ---> O(n)

#### Challenge 1
####  Function to check if all elements of 2nd LIST are square of element in first array
#### Without Frequency Counter
### [1,2,3, 3,2] & [1,4,9,4,16] should also give false

arr1 = [1,2,3]
arr2 = [1,4,9]

def isSquare(a , b):
    result = False
    if(len(a) == len(b)):
        for i in range(0,len(a)):
            try:
                b.remove(a[i] ** 2)
                print(b)
            except ValueError:
                result = False
        if(len(b) == 0):
            result = True
    else:
        print("Number of values in both arrays is not same")
        result = False
    
    return result

print(isSquare(arr1 , arr2))   
print("Frequency Counter Starts")
## Time Complexity ---> O(N ^ 2)

#### Frequency Counter Pattern Way
arr1 = [1,2,3]
arr2 = [1,4,9]
def arrayToDictionary(a):
    dict = {}
    print(dict)
    ## Creating Dictionary of a
    for x in a:
       if(x in dict.keys()): 
            dict[x] += 1
       else:
            dict[x] = 1
    return dict
    
def isSquared(a , b):
    
    frequencyCounter2 = arrayToDictionary(b)
    frequencyCounter1 = arrayToDictionary(a)
    
    print(frequencyCounter1)
    print(frequencyCounter2) 
    for key in frequencyCounter1:
        if ((key ** 2) not in frequencyCounter2.keys()):
            print(key**2 in frequencyCounter2.keys())
            return False
        if(frequencyCounter2[key ** 2] != frequencyCounter1[key]):
            return False
    return True

print(isSquared(arr1, arr2))

# Time Complexity ---> O(N)


