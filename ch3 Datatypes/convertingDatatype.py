# Converting Datatype Explicitly

#int conversion
x = 15.56
int(x) # will display 15

# float conversion
num = 15
float(num)# will display 15.0

# complex num conversion
n = 10
complex(n) #will display 10+0j

a= 10
b = -5
complex(a,b) #will display 10 - 5j

# Program to convert any datatype in int

def convertToNum(n1):
    n = int(n1)
    print( n)

convertToNum(0xA180)
convertToNum(0b00010011)
convertToNum(0o774)