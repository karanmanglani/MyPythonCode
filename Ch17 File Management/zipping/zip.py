from zipfile import *

f = ZipFile('test.zip','w',ZIP_DEFLATED)
f.write('log.txt')
f.write('notepad.txt')

print('test.zip file created!!!')