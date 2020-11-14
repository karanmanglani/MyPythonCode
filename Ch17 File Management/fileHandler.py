############################### File Handling #############################
#! Opening a file
fileHandler = open("log.txt","a+")
str1 = input("Enter a text: ")
fileHandler.write(str1 + '\n')
fileHandler.close()

fileHandler = open("log.txt","r")
str2 = fileHandler.read()
print(str2)
fileHandler.close()

f = open("notepad.txt",'a+')
print('Enter text (@ at the end) : ')
str = ''
while str != '@':
    str = input()
    if(str != '@'):
        f.write(str + '\n')
f.close()

#! checking existance of a file 
import os , sys

fname = input("Enter filename : ")

if os.path.isfile(fname):
    f = open(fname,'r')
else:
    print("file does not exists!!")
    sys.exit()

print('The file contents are : ')
str = f.read()
print(str)

#! To get number of lines , word and characters
cl = cw = cc = 0
for line in f:
    words = line.split()
    cl += 1
    cw = len(words)
    cc += len(line)

print("Number of lines : ", cl)
print("Number of words : ", cw)
print("Number of characters : ", cc)

f.close()
#* With statement will take care of closing file
with open("notepad.txt", 'r') as f:
    print(f.read())
