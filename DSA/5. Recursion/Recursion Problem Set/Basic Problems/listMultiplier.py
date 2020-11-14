lst = [int(x) for x in input("Enter numbers seperated by space: ").split(" ")]

def listMultiplier(lst):
    if(len(lst) <= 1):
        return lst[len(lst) - 1]
    
    return lst[0] * listMultiplier(lst[1:])

print(listMultiplier(lst))