
#!####################################################################################################
#! Types of Inheritance :-                                                                           #
#!      a) Single Inheritance ----> 1 super class , >1 subclass                                      #
#!      b) Multiple Inheritance --> >1 super class , 1 subclass                                      #
#!####################################################################################################

#* Single Inheritance

class A(object):
    def __init__(self,x):
        self.x = x

class B(A):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y
    
    def display(self):
        print(self.x + self.y)


class C(A):
    def __init__(self,x,z):
        super().__init__(x)
        self.z = z
    
    def display(self):
        print(self.x + self.z)

b = B(2,3)
c = C(3,4)

b.display()
c.display()


#* Multiple Inheritance 
class A:
    def height(self):
        print("Height is 5")

class B:
    def color(self):
        print("Color is Brown")

class C(A,B):
    pass

c = C()

c.height()
c.color()

#! Accesing constructors from all base classes in multiple inheritance

class D(object):
    def __init__(self):
        self.d = 'd'
        print(self.d)
        super().__init__()

class E(object):
    def __init__(self):
        self.e = 'e'
        print(self.e)
        super().__init__()

class F(D,E):
    def __init__(self):
        self.f = 'f'
        print(self.f)
        super().__init__()

f = F()

