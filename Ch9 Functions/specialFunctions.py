
#! DECORATOR ---> A function accepting function and returning function
#* 1 Decorator
def decorator(fun):
    def inner():
        return fun() + 2
    return inner

@decorator ### Apply decorator function to the function below
def num():
    return 10

print(num()) 
#* 2 Decoratars

def decor(fun):
    def inner():
        return fun() + 2
    return inner

def decor1(fun):
    def inner():
        return fun() * 2
    return inner

@decor
@decor1
def num():
    return 10

print(num())

#! Generators ---> Functions returning qa sequence of values

def mygen(x , y):
    while x <= y:
        yield x
        x += 1

for i in mygen(1,10):
    print(i,end=" ")

def gen():
    yield 'A'
    yield 'B'
    yield 'C'
g = gen()
print(next(g)) # "A"
print(next(g)) # "B"
print(next(g)) # "C"
#print(next(g)) # Error

#! Special Variable __name__ ---> == '__main__' if program is executed directly else return module name if run as module

def display():
    if __name__ == '__main__':
        print('This program is run directly!!')
    else:
        print("Program is running as module ",__name__)

display()