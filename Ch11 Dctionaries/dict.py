from collections import OrderedDict
d = {'Name': "Karan" , 'Id' : 92}
print(d)

## Creating from sequence
s = ["Name","Id"]

d = d.fromkeys(s , 1)
print(d)

## Getting value from key
print(d.get("Name",0))

## Getting value pairs
print(d.items())

## Getting keys and value
print(d.keys())
print(d.values())

## Using loops with dictionaries
for k in d:
    print("Key : ",k,"\tValue : ",d[k],end="\n")

## Converting lists to dictionaries
keys = ["Name","Id","Pass"]
values = ["Karan", 92, 69]

d = dict(zip(keys,values))

for k in d:
    print("Key : ",k,"\tValue : ",d[k],end="\n")

## OrderedDictonaries(Collections module)

d = OrderedDict()
d[10] = 'A'
d[11] = 'B'
d[12] = 'C'

print(d)