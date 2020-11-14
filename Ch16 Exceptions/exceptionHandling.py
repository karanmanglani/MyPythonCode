try:
    f = open("myfile","w")

    a,b = [int(x) for x in input("Enter 2 numbers : ").split()]
    c = a/b
    print(c)
    f.write("Writing {} in myfile".format(c))

except ZeroDivisionError:
    print("Can't divide by zero!!")
finally: # will run whtere exception is or not
    f.close()
    print("File Closed")

#! Assert returns assertion error if given condition is false
#* Use of assertion error
try:
    x = int(input('Enter a number between 5 and 10: '))
    assert x >= 5 and x <= 10
    print('The number entered is : ',x)
except AssertionError:
    print("Value does not lie between 5 and 10!!")