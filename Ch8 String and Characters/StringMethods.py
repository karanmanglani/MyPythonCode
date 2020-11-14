str = 'Karan Manglani'
n = len(str)
i = -n

for i in range(-1 , -n - 1 , -1):
    print(str[i])

## Searching string
# Method 1
string = 'Karan Manglani'
sub = 'Karan'

print(sub in string)

# Method 2
print(string.find(sub , 0 , len(string))) # ---> Returns index of searched string


## Finding Index of searched string 
print(string.index(sub,0,len(string))) # rindex() gives index from right

# Removing Spaces
str = '   a   '
print(str.lstrip())
print(str.rstrip())
print(str.strip())

### Program to find all positions of string
str = input("Enter main string: ")
sub = input("Enter string to find: ")
i = 0
pos = -1
flag = False
n = len(str)
while True:
    pos = str.find(sub , pos + 1 , n)  # rfind() search from right
    if pos == -1 :
        break
    print('Found at position: ', pos + 1)
    flag = True
    

if flag == False:
    print("String not found")


# Count number of substring in string
print(str.count(sub,0,n))

# Replacing a string
str1 = str.replace(sub, "Replaced")
print(str1)

### Inserting substring into string
str = input("Enter a string : ")
sub = input("Enter a sub-string: ")
n = int(input("Enter position no. : "))
n -= 1
l1  = len(str)
l2 = len(sub)

str1 = []

for i in range(n):
    str1.append(str[i])

for i in range(l2):
    str1.append(sub[i])

for i in range(n,l1):
    str1.append(str[i])

str1 = ''.join(str1)

print(str1)
