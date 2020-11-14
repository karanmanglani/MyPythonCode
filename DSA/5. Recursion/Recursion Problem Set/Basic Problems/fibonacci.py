x = int(input("Enter a position of element to find it's fibonacci: "))

def fibonacci(x):
    if(x <= 2):
        return 1
    return fibonacci(x-1) + fibonacci(x - 2)

print(fibonacci(x)) 