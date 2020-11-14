### Types of argument
#1 Positional Argument ---> Arguments passed in correct order
def add(a,b):
    return a + b
print(add(2 , 3))

#2 Keyword Arguments ---> Parameters identified by names
def grocery(item , price):
    print("Item is {0}".format(item))
    print("price is ${0}".format(price))

grocery(item = "Sugar" , price = "9999")

#3 Default Argument ---> 

def grocer1(item = "Sugar" , price = "$9999"):
    print("Item is {0}".format(item))
    print("price is ${0}".format(price))

#4 Variable Length Arguments
def add(farg , *args):
    print("Formal Arguments = ", farg)
    sum = 0
    for i in args:
        sum += i
    
    print("Sum of all numbers = ", (farg + sum))

add(60)

### Global And Local
## Global Scope and Local Scope
a = 1 # Global Variable
def modify():
    a = 2 # Local Variable
    print(a)
modify()
print(a) # Global a

## Global Keyword
def mod():
    global a
    a = 2 #Global a
    print(a)
mod()
print(a)

### Passing a group of elements

lst = [int(x) for x in input("Enter numbers seperated by space: ").split()]

def calculate(lst):
    sum = 0
    for n in range(0,len(lst)):
        sum += lst[n]
    return sum

print(calculate(lst))