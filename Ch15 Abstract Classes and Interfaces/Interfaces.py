
#! Abstract Class with abstract methods having no Concrete body(Body with code in them) except method headers
#* A program to connect to a database
from abc import *

class MyClass(ABC):
    def connect(self):
        pass
    def disConnect(self):
        pass

class Oracle(MyClass):
    def connect(self):
        print('Connecting to Oracle ')
    def disConnect(self):
        print('Disconecting to oracle ')


class Sybase(MyClass):
    def connect(self):
        print('Connecting to Sybase ')
    def disConnect(self):
        print('Disconecting to Sybase ')

class Database:
    str = input('Enter Database Name: ')

    # convert string into classname
    classname = globals()[str]

    x = classname()

    x.connect()
    x.disConnect()