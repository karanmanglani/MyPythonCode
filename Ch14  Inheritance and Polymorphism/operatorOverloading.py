
#! Explicitly defining Operator Overloading

class BookX:
    def __init__(self,pages):
        self.pages = pages
    
    def __add__(self,other): #* + operator ke liye function
        return self.pages + other.pages
    
class BookY:
    def __init__(self,pages):
        self.pages = pages

b1 = BookX(100)
b2 = BookY(150)

print(b1 + b2)