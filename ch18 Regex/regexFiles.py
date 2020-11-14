import re
f = open('lol.txt','r')
str = f.read()
print(str)
for line in str.split('\n'):
    print(re.findall(r'\ba[\w]*\b',line))