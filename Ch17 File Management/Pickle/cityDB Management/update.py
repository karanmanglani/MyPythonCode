import os 
reclen = 30
size = os.path.getsize('cities.bin')
n = int(size/reclen)

with open("cities.bin",'r+b') as f:
    name = input("Enter name of city : ")
    name.lower()
    newName = input("Enter new name for the city : ")
    newName += (reclen - len(newName))* " "
    newName = newName.encode()
    position = 0
    
    for i in range(n):
        f.seek(position)
        str = f.read(30).decode().lower()

        if name in str :
            found = True
            f.seek(-30,1)
            f.write(newName)
        position += 30
    if not found:
        print("City not found!!")