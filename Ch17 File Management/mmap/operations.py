import mmap , sys
print("press 1 for seeing phonebook 2 for displaying phone number and 3 for modifying a record and 4 to exit: ")
choice = int(input())
if(choice == 4):
    sys.exit()
with open('phonebook.dat','r+b') as f:
    mm = mmap.mmap(f.fileno(),0)
    if(choice == 1):
        print(mm.read().decode())
    elif(choice == 2):
        name = input('Enter name : ')
        n = mm.find(name.encode())
        n1 = n + len(name)
        print(mm[n1 : n1+10].decode())
    elif(choice == 3):
        name = input('Enter name : ')
        n = mm.find(name.encode())
        n1 = n + len(name)
        ph = input("Enter new phone number : ")
        mm[n1 : n1 + 10] = ph.encode()
    else:   
        print("No such option present!!!")

mm.close()