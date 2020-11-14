
#! Creating a method and not giving it a body (Abstract Method).Then giving it body in sub class
from abc import ABC , abstractclassmethod

class MyClass(ABC): #* ABC - Abstract base class a meta class(class that defines behaviour of another class)
    @abstractclassmethod
    def calculate(self,x):
        pass

class sub1(MyClass):
    def calculate(self,x):
        print('Square of',x,' is =',x*x)
    
import math
class Sub2(MyClass):
    def calculate(self , x):
        print('Sqrt of ',x,' is ',math.sqrt(x))

class Sub3(MyClass):
    def calculate(self,x):
        print('Cube of ',x,' is ',x*x*x)

sqr = sub1()
sqrt = Sub2()
cube = Sub3()
sqr.calculate(5)
sqrt.calculate(25)
cube.calculate(5)