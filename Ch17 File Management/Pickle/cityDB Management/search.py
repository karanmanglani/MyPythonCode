import os

reclen = 30
size = os.path.getsize('cities.bin')
n = int(size/reclen)

with open('cities.bin', 'rb') as f:
    name = input("Enter name of the city : ").lower()
    position = 0
    found = False

    for i in range(n):
        f.seek(position)
        str = f.read(30).decode().lower()

        if name in str:
            print("Found at record number ", i+1)
            found = True
        position += reclen

    if not found:
        print("City not found!!!")

