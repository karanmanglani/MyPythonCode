##############################################################################################################################################
#! Types of methods :-                                                                         
#*      * Instance methods -->Methods acting upon instance variables of class                                                                 
#*          a) Access methods --> Simply access or read data of variable. generally written in form getxx(). Also called getter methods                                                             
#*          b) Mutator methods --> They also change the value of variable. generally written in form setXX(). Also called setter methods                                                             
#*      * Class methods --> Methods acting on class / static variables                                                                    
#*      * Static methods --> Methods which do not require action of class or instances                                                                   
##############################################################################################################################################

class Student:
    totalStrength = 0
    def __init__(self,n = "" , m = 0): #! This is a constructor
        Student.totalStrength += 1
        self.name = n
        self.marks = m
    
    def info(self): # This is a instance method
        print("Your name is ",self.name," and your marks are ",self.marks)
    
    ## Getter methods
    def getName(self):
        return self.name

    ## Setter methods
    def setName(self,name):
        self.name = name
    ## class methods
    @classmethod
    def getStrength(cls):
        return cls.totalStrength
    
    ## Static Methods
    @staticmethod
    def getTotalStudents():
        print("No. of students = ",Student.totalStrength)

