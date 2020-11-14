# Break statement
group1 = [1,2,3,4,5]
search = int(input("Enter a number to search in Group 1: "))

for element in group1:
    if search == element:
        print("Element found in group 1")
        break # come out of loop
else: # else can be used with for and while loop
    print("Element not found in Group 1")

# Continue Statement

x = 0
while x < 10:
    x += 1
    if x > 5:
        continue # does not allow statements below it to execute and start loop from first line
    print(" x = " , x)
print("out of loop")

# pass statement

num = [ 1 , 2, -3,-4]
for element in num:
    if(element > 0):
        pass # do nothing
    else:
        print(element)

# assert statement
x = int(input("Enter a number greater than 0 : "))

assert x > 0, "Entered number is less than zero"

# assert with try and except

try: 
    assert (x > 0) # If x < 0 try will break due to error
    print("U entered: " , x)
except AssertionError: # not break if error is assertion error
    print("Entered number is less than zero")

# return statement
def sum(a , b):
    return a + b

x = sum(2,3)
print(x)