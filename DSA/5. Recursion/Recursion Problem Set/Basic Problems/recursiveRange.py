x = int(input("Enter a number: "))

def recursiveRange(x):
    if(x == 0):
        return 0
    return x + recursiveRange(x - 1)

print(recursiveRange(x))