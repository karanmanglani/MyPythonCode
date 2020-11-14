# while loop
a = int(input("Enter a number: "))
x = i = 1
while i <= a:
    x *= i
    i += 1
print("{0}! = {1} ".format(a,x))  

# for loop
x = 1
for i in range (1,a + 1,1):
    x *= i
print("{0}! = {1} ".format(a,x))  

list = [10,20,2.5]
for element in list:
    print(element)

for ch in "Karan":
    print(ch)


# star pattern
for i in range (1, a + 1):
    for j in range(1, i + 1):
        print('*',end='')
    print('')

# reverse star pattern

for i in range (a, 0,-1):
    for j in range(1, i + 1):
        print('*',end="")
    print("")

# Equilateral Triangle Pattern
space = 40
for i in range (1,a + 1):
    print(' ' * space, end='')
    print("* " * i)
    space -= 1
