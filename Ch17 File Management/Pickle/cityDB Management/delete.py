import os

reclen = 30
size = os.path.getsize('cities.bin')
n = int(size/reclen)
f1 = open('f1.bin','wb')
with open('cities.bin', 'rb') as f:
    name = input("Enter name of the city : ").lower()
    position = 0
    found = False

    for i in range(n):
        f.seek(position)
        str = f.read(30).decode()

        if name not in str.lower():
            f1.write(str.encode())
            found = True
        position += reclen

    if not found:
        print("City not found!!!")
f1.close()

os.remove('cities.bin')
os.rename('f1.bin','cities.bin')