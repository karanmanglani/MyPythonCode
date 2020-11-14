
#! Abstraction --> Hiding unnecesarry data from user

class myClass:
    def __init__(self):
        self.x = 2
        self.__y = 3 # Private variable
    
    def display(self):
        print(self.x)
        #* print(self.__y) will give error
        print(self._myClass__y) # This is name mangling 


m = myClass()
m.display()