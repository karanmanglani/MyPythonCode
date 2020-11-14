class Student(object):
    totalStrength = 50 #* This is a class variable
    def __init__(self,name = "",rno = 0):
        self.name = name #* This is instance variable
        self.rno = rno
    
    def info(self): #* This is instance method
        print(self.name)
        print(self.rno)
    @classmethod
    def strengthTotal(cls): #* This is a class method
        print("Total strength = ",cls.totalStrength)

s1 = Student(name = "Karan Manglani", rno=12)
s1.info()
s1.strengthTotal()
"""
************************************************************************************************************************
* Instance Methods/variables            | Class Methods / Variables                                                     *
*-> They change only instace if changed | -> These change method/ variables values for all instances if changed         *
************************************************************************************************************************
"""

