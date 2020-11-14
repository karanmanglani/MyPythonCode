import random
def insertionSort(lst):
    for i in range(1,len(lst)):
        currentElement = lst[i]
        j = i - 1
        while( j>= 0 and lst[j] > currentElement):
            if(lst[j] > currentElement):
                lst[j+1] = lst[j]
            j -= 1;
        lst[j+1] = currentElement
    return lst  

def randomList(n,start,stop,lst):
    if ( n < 1):
        return None
    lst.append(random.randint(start,stop))
    randomList(n - 1,start,stop,lst)
lst = []
randomList(500,0,100000,lst)
print(insertionSort(lst))

#!################################
#! [3,5,4]
#* i             j
#* 1             0   3 > 5  no
#* lst[0 + 1]    current element [3,5,4]
#* 2             2 5 > 4 yup lst[2] = 5 [3,5,5]
#* 2             1 5 > 5 no  [3,5,5]
#* 2             0 3 > 5 no 
#* lst[0 + 1] = currentElement [3,4,5] 