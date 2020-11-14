import re
str = 'an apple a day keeps doctor away'
# print(re.findall(r'a[\w]*',str)) #! also gives ay of day
print(re.findall(r'\ba[\w]*\b',str))

str = 'Nehi Chachi : 91889182'
print(re.search(r'\d{8}',str).group())
