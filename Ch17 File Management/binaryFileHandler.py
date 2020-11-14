f1 = open('new.jpg', 'rb')
f2 = open('new2.jpg', 'ab')

bytes = f1.read()
f2.write(bytes)

f1.close()
f2.close()