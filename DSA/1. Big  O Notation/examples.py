def countUpAndDown(n):
    print("Going up!!")
    for i in range(1,n + 1):
        print(i)
    
    print("Going down !!")
    for i in range(n , 0,-1):
        print(i)

countUpAndDown(10)

def printAllPairs(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

printAllPairs(5)