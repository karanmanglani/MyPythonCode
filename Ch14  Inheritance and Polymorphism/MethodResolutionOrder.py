
#*############################################################################################################
#* Method Resolution Order(MRO) --> Method to search in multiple inheritance.Includes 3 steps :-             #                                                              
#* 1) Search in sub class before base class                                                                  #
#* 2) Search in left base class if not found then in right base class (therefore search from left to right)  #
#* 3) Do not search in a class more than once                                                                #
#*############################################################################################################

#! Understanding MRo
class A(object):
    def method(self):
        print('A class method')
        super().method()

class B(object):
    def method(self):
        print('B class method')
        super().method()

class C(object):
    def method(self):
        print('C class method')
        super().method()

class X(A,B):
    def method(self):
        print('X class method')
        super().method()

class Y(B,C):
    def method(self):
        print('Y class method')
        super().method()

class P(X,Y,C):
    def method(self):
        print('P class method')
        super().method()

p = P()
print(P.mro()) #! To find Method Resolution Order of the P class 
try:
    p.method()
except AttributeError:
    pass