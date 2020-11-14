def swap(x,y):
    x = x + y
    y = x - y
    x = x - y

    yield x
    yield y

def pivot(lst, start , end):
    pivot = lst[start]
    swapIndex = start
    for i in range(start + 1,end + 1):
        if (pivot > lst[i]):
            swapIndex += 1
            lst[swapIndex] , lst[i] = swap(lst[swapIndex],lst[i])
    lst[start], lst[swapIndex] = swap(lst[start],lst[swapIndex])
    return swapIndex

def quickSort(lst = [],left = 0,right = 0):
    if(left < right):
        pivotIndex = pivot(lst,left,right)
        quickSort(lst,left,pivotIndex - 1)
        quickSort(lst,pivotIndex + 1,right)
    return lst

print(quickSort([0,-2,45,5,23,64],0,5))
