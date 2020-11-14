### Lambdas or Anonymous Functions i.e a function without name
from functools import reduce

f = lambda x: x * x
print(f(5))

a , b = [int(n) for n in input("Enter two numbers seperated by space : ").split(" ")]
max = lambda x , y: x if x > y else y
print(max(a,b))

### Using filters without lambdas
def is_even(x):
    if x%2 ==0:
        return True
    else:
        return False

lst = [10,21,35,40]
lst1 = list(filter(is_even,lst))
print(lst1)

### Using filter with lambdas

lst1 = list(filter(lambda x: (x%2 == 0) , lst))
print(lst1)

### Map

lst = [1 , 2 , 3]
lst1 = list(map(lambda x: x*x,lst))
print(lst1)

### Using Lambda with reduce()
## Need to import reduce from functools
lst1 = reduce(lambda x,y : x * y , lst)
print(lst1)