import sys,os

fname = input("Enter filename : ")

if os.path.isfile(fname):
    f = open(fname,'r')
else:
    print("file does not exists!!")
    sys.exit()
cl = cw = cc = 0
for line in f:
    words = line.split()
    cl += 1
    cw += len(words)
    cc += len(line)

print("Number of lines : ", cl)
print("Number of words : ", cw)
print("Number of characters : ", cc)

f.close()