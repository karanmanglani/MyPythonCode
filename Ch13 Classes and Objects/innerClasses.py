class Person(object):
    def __init__(self,name,dd,mm,yy):
        self.name = name
        self.db = self.Dob(dd,mm,yy)

    def display(self):
        print("Name = ",self.name,' Dob = {}/{}/{}'.format(self.db.dd,self.db.mm,self.db.yyyy))
    
    class Dob:
        def __init__(self,dd,mm,yyyy):
            self.dd = dd
            self.mm = mm
            self.yyyy = yyyy

p = Person("Karan Manglani",12,8,2004)
print(p.display())