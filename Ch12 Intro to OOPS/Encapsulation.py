
#! Encapsulation ---> Mechanism where the data(variable) and the code(Methods) that acts on data will bind togather
#! It's nothing but writting variables and methods in the class itself

class Student:
    def __init__(self):
        self.id = 10
        self.name = "Karan"
    
    def display(self):
        print(self.id)
        print(self.name)

karan = Student()
karan.display()
