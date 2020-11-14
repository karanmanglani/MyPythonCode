import re
str = 'man sun mop run'
res = re.search(r'm\w\w',str)

if res is not None:
    print(res)
else:
    print('Not found')

#! re.match() checks if first word satisfies regular expression 
#! re.split() splits on satisfying re 
#! re.sub() replaces a string