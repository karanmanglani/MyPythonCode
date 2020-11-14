from os import *
from zipfile import *


def createZip():
    name = input("Enter the name for zip file : ")
    f = ZipFile("{0}.zip".format(name),'w',ZIP_DEFLATED)


# Creating a function to zip a file
#   -Selecting a file
#   -Zipping it 
# Creating a function to unzip a file
#   -Selecting a zip file
#   -Unzipping it