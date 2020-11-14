with open('phonebook.dat','wb') as f:
    n = int(input("Enter number of entries : "))

    for i in range(n):
        name = input("Enter name : ").encode()
        number = input("Enter phone number : ").encode()
        f.write(name+number)

