#### It's a Design Pattern Bois
## Outer function contains a function inside it which is recursive funtion 
from array import array as a

lst = a('i',[int(x) for x in input("Enter numbers seperated by space: ").split(" ")])

def collectOddValues(lst):
    result = a('i',[])
    
    def helper(helperInput):
        if(len(helperInput) < 1):
            return result
        
        if(helperInput[0] % 2 != 0):
            result.append(helperInput[0])

        if(len(helperInput) > 1):
            helperInput.remove(helperInput[0])
            helper(helperInput)
    
    helper(lst)

    return result

print(collectOddValues(lst))
