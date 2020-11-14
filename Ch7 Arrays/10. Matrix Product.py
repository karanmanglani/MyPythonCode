import sys
from numpy import *

r1 , c1 = [int(a) for a in input("First matrix rows, cols: ").split()]
r2 , c2 = [int(a) for a in input("Second Matrix rows , columns: ").split()]

if c1 != r2:
    print('Multiplication not possible')
    sys.exit()

str1 = input("Enter first matrix elements: ")
a = reshape(matrix(str1),  (r1 , c1))
str2 = input("Enter second matrix elements: ")
b = reshape(matrix(str2) , (r2 , c2))

print(a * b)