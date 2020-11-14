import re
import urllib.request

# ooen the html file
f = urllib.request.urlopen(r'file:///D|Karan\Course\Python\All Resources\ch18 Regex\test.html')

# read data from the file object into text string
text = f.read()

# Convert the byte string to normal string
str = text.decode()
#apply regular expressions on string

result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d\d.\d\d)</td>',str)
print(result)
for item, price in result:
    print("Item = %-15s Price = %-10s"%(item,price))

f.close()