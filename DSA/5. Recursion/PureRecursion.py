lst = [int(x) for x in input("Enter numbers seperated by space: ").split(" ")]

def collectOddValue(lst):
    newLst = []
    print(type(newLst))

    if(len(lst) == 0):
        return newLst
    
    if(lst[0] % 2 != 0):
        newLst.append(lst[0])
    
    lst.remove(lst[0])    
    newLst.extend(collectOddValue(lst))
    return newLst

print(collectOddValue(lst))