
import math
class Square:
    def area(self,x):
        print('Area = ', x*x)

class Circle(Square):
    def area(self,x):
        print("Area = ",math.pi * x * x)

c = Circle()
c.area(7)