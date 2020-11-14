from zipfile import *

z = ZipFile('test.zip','r')

names = z.namelist()
for fname in names:
    print('\nContents of %s\n' % fname)
    f = z.open(fname)
    contents = f.read()
    print(contents.decode())