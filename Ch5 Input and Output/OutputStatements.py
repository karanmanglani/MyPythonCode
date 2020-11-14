######### PRINT STATEMENT #########

### print("string") statement
print('Use \\n \nfor moving to next line')
print("Use \\t \t for tab")

print(2 * " use n * \' string \' to print n times| ")
print("+ join without space"+"like this but , join with space",'like this')

### print(variable list)
a,b = 2,4
# sep used to seperate numbers
print(a,b,sep=" ----- ")

### print(object)
lst = [10,'A','Hai']
print(lst)

d={'Karan':99, 'Akshat':90, 'Mohit':20}
print(d)

### print('string' , variable list)
print("you typed",a,"as input")

### print(formatted string)
print("Value %i" % a)
print("The value of {0} + {1} is {2}".format(a,b,a + b))
