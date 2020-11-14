### Recursion ---> Function repeating itself

# Program to return factorial
def factorial(n):
    try:
        if(n == 0):
            return 1
        else:
            return n * factorial(n - 1)
    except RecursionError:
        print("Number Too long")
        return 0

n = int(input("Enter number to find factorial: "))
print(factorial(n))

# Tower of Hanoi

def towers(n , a , c, b):
    try:
        if n == 1:
            print("Move disk %i from pole %s to %s"%(n,a,c))
        else:
            # Move first n-1 disk from A to B using C as intermidiate pole
            towers(n - 1, a , b , c)

            # Move remaining 1 disk from A to c
            print("Move disk %i from pole %s to %s"%(n,a,c))

            # Move n-1 disk from b to c using A as an intermidiate pole
            towers(n - 1 , b ,c ,a)
    except RecursionError:
        print("Can't Solve for these much of Discs")

n = int(input('Enter number of disk: '))
towers(n, 'A' , 'C' , 'B')