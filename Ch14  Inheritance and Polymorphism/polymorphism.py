
#!###########################################################################################################
#! Examples of Polymorphism in Python :- 
#!      A) Duck Typing Philosophy -> A method is run according to type of object
#!      B) Operator Overloading -> When an operator can exhibit polymorphism like '+' operator
#!      C) Method Overloading -> Method performing more than one task. Not availaible in python
#!      (but there is jugaad). Like sum(10 , 20) gives 30 , sum(10,20,30) gives 60 
#!      D) Method Overriding -> wriing method in sub class replacing method in superclass
#!###########################################################################################################

#* Duck Typing Philosophy example

class Duck:
    def talk(self):
        print("'Quack Quack ")
    
class Human(object):
    def talk(self):
        print('Hello hi!')

class Dog(object):
    def Bark(self):
        print("Bow!Bow")

def duckTypingTalk(object):
    object.talk()

def strongTypingTalk(obj):    
    if hasattr(obj,'Bark'):
        obj.Bark()
    elif hasattr(obj,'talk'):
        obj.talk()

d = Duck()
h = Human()
dog = Dog();

duckTypingTalk(d)
duckTypingTalk(d)
strongTypingTalk(dog)

#* Operator Overloading Example
print(1 + 3)
a = 'a'
c = 'c'
b = a + c
print(b)