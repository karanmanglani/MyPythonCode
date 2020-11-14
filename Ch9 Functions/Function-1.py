# Returning Multiple values from arrays

def fun(a,b):
    return a + b , a - b , a * b

sum , sub , mul  = fun(4, 5)
print(sum)
print(sub)
print(mul)

# Defining function inside function

def display(str):
    def message():
        return "Hi "
    return (message() + str)

print(display("Karan"))

# taking function as argument

def new(fun):
    return "Hi " + fun

def no(str):
    return str + " How are you"

print(new(no("karan")))

