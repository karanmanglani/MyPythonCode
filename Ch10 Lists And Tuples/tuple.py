########## Tuples ##########

#! Tuples --> Immutable(can't be modified) form of list

tup = (10,25,12,54)
#* Sorting in reverse order
tup = sorted(tup,reverse = True)
print(tup)

###! Inserting elements
#* Insert 13 at position 3

y = tup[0:3-1]
y = y +[13]
tup = y + tup[3-1:]
tup = tuple(tup)
print(tup)
print(type(tup))

###! Modifying elements of tuple
#* Not possible so we will create new tuple

num = (10,20,30,40,50)
print(num)

# Accepting new element and position number

lst = [int(input('Enter a new element: '))]
new = tuple(lst)
pos = int(input("Enter position: "))

# Copy from 0 to pos - 1
num1 = num[0:pos-1]
num1 += new
num = num1+num[pos:]
print(num)
print(type(num))

###! Deleting elements of tuple
#* Not possible so we will create new tuple

num = (10,20,30,40,50)
print(num)

# Accepting  position number
pos = int(input("Enter position: "))

# Copy from 0 to pos - 1
num1 = num[0:pos-1]
num = num1+num[pos:]
print(num)
print(type(num))