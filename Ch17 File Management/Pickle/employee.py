class Emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
    def display(self):
        print("Id = {}\tName = {}\tSalary = {}".format(self.id,self.name,self.sal))
    