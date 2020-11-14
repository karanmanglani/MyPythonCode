lst = [int(n) for n in input("Enter numbers seperatted by space: ").split(" ")]
n = int(input("Entter nuber you ant to search: "))

def linearSearch(lst,n):
    for i in range(0,len(lst)):
        if(n == lst[i]):
            return i
    
    return None

if(linearSearch(lst,n) != None):
    print("{0} found at position {1}".format(n,linearSearch(lst,n) + 1))
else:
    print("Not found!!!")
            