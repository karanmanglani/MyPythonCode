
def swap(x,y):
    x = x + y
    y = x - y
    x = x - y

    yield x
    yield y

def bubbleSort(lst):
    noSwaps = True 
    for i in range(0,len(lst) - 1):
        noSwaps = True 
        for j in range(0,len(lst) - i - 1):
            if(lst[j] > lst[j + 1]):
                lst[j] , lst[j+1] = swap(lst[j] , lst[j+1])
                noSwaps = False
        if(noSwaps):
            break
    return lst


lst = [10,2,25,32,13,24]
print(bubbleSort(lst))
