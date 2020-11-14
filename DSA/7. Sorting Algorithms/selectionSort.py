import random
def swap(x,y):
    x = x + y
    y = x - y
    x = x - y

    yield x
    yield y

def selectionSort(lst):
    for i in range(0,len(lst)):
        lowest = i
        for j in range(i+1,len(lst)):
            if(lst[j] < lst[lowest]):
                lowest = j;
        if(i != lowest):
            lst[i] , lst[lowest] = swap(lst[i],lst[lowest])

    return lst

def randomList(n,start,stop,lst):
    if ( n < 1):
        return None
    lst.append(random.randint(start,stop))
    randomList(n - 1,start,stop,lst)
lst = []
randomList(500,0,100000,lst)  
print(selectionSort(lst))                