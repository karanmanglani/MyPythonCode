
class A :
    a = 1
    b = 2

    def method1(cls):
        print(cls.a)
        print(cls.b)

class B(A):
    c = 3
    def method2(cls):
        print(cls.c)

b = B()
b.method1()
b.method2()